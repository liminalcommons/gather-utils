#!/usr/bin/env python3
import sys, os
import json
import time
from pathlib import Path
from dotenv import load_dotenv

# Add the project root to PYTHONPATH so that the 'gather_manager' package can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
load_dotenv()

from gather_manager.api.client import GatherClient

class Release0Tester:
    def __init__(self):
        self.api_key = os.getenv("GATHER_API_KEY", "9HoXr7Xr4OpIA8o7")
        self.raw_space_id = os.getenv("GATHER_SPACE_ID", "ELoGghDX4v3HEwI0\\Liminal Commons")
        if '\\' in self.raw_space_id:
            self.space_id, self.space_name = self.raw_space_id.split('\\')
        else:
            self.space_id, self.space_name = self.raw_space_id, "Liminal Commons"
        
        self.code_space_id = f"{self.space_id}\\{self.space_name}"
        self.output_dir = os.getenv("OUTPUT_DIR", ".")
        self.client = None
        self.maps = []
        self.results = {}
        
    def run_tests(self):
        """Run all tests sequentially and report results"""
        print(f"🔍 Testing Release0 Scope for Space: {self.space_name}")
        print("=" * 80)
        
        tests = [
            self.test_api_connection,
            self.test_get_space_info,
            self.test_get_maps,
            self.test_download_maps,
            self.test_map_files_exist
        ]
        
        for test in tests:
            test_name = test.__name__.replace('test_', '')
            print(f"\n📋 Testing: {test_name}")
            try:
                result = test()
                self.results[test_name] = result
                if result:
                    print(f"✅ PASS: {test_name}")
                else:
                    print(f"❌ FAIL: {test_name}")
            except Exception as e:
                print(f"❌ ERROR: {test_name} - {str(e)}")
                self.results[test_name] = False
        
        self.print_summary()
        
    def test_api_connection(self):
        """Test API connection by initializing client"""
        try:
            self.client = GatherClient(api_key=self.api_key)
            return True
        except Exception as e:
            print(f"  Error connecting to API: {e}")
            return False
    
    def test_get_space_info(self):
        """Test fetching space information"""
        try:
            space = self.client.get_space(self.code_space_id)
            print(f"  Space ID: {space.id}")
            print(f"  Space Name: {space.name}")
            return space.id is not None and space.name == self.space_name
        except Exception as e:
            print(f"  Error fetching space info: {e}")
            return False
    
    def test_get_maps(self):
        """Test fetching maps list"""
        try:
            self.maps = self.client.get_maps(self.code_space_id)
            print(f"  Found {len(self.maps)} maps")
            if len(self.maps) > 0:
                print(f"  First map: {self.maps[0].name} (ID: {self.maps[0].id})")
            return len(self.maps) > 0
        except Exception as e:
            print(f"  Error fetching maps: {e}")
            return False
    
    def test_download_maps(self):
        """Test downloading map data"""
        if not self.maps:
            print("  No maps to download")
            return False
            
        try:
            # Test with just the first map to save time
            test_map = self.maps[0]
            map_id = test_map.id
            formatted_space_id = self.client._format_space_id(self.code_space_id)
            
            # Get raw map data
            detailed_map = self.client._request("GET", f"api/v2/spaces/{formatted_space_id}/maps/{map_id}")
            print(f"  Successfully downloaded map data for: {test_map.name}")
            return True
        except Exception as e:
            print(f"  Error downloading map data: {e}")
            return False
    
    def test_map_files_exist(self):
        """Test that map files exist in the output directory"""
        output_path = Path(os.path.join(self.output_dir, self.space_name))
        if not output_path.exists():
            print(f"  Output directory does not exist: {output_path}")
            return False
            
        files = list(output_path.glob("map_*.json"))
        print(f"  Found {len(files)} map files in {output_path}")
        
        if len(files) > 0:
            # Check that at least one file has valid JSON content
            try:
                with open(files[0], 'r') as f:
                    data = json.load(f)
                print(f"  Verified JSON content in {files[0].name}")
                return True
            except Exception as e:
                print(f"  Error reading map file: {e}")
                return False
        else:
            return False
    
    def print_summary(self):
        """Print a summary of all test results"""
        print("\n" + "=" * 80)
        print("📊 RELEASE0 TEST SUMMARY")
        print("=" * 80)
        
        all_passed = all(self.results.values())
        
        for test_name, result in self.results.items():
            status = "✅ PASS" if result else "❌ FAIL"
            print(f"{status}: {test_name}")
        
        print("\n🏁 OVERALL RESULT: ", end="")
        if all_passed:
            print("✅ ALL TESTS PASSED - Release0 requirements met!")
        else:
            print("❌ SOME TESTS FAILED - Release0 requirements not fully met")
        
        return all_passed

if __name__ == "__main__":
    tester = Release0Tester()
    tester.run_tests() 