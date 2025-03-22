# Project Reorganization Plan

## Documentation Files

### Move to `docs/project/`
- `PROJECT_STATUS.md` → `docs/project/PROJECT_STATUS.md`
- `TECHNICAL_REQUIREMENTS.md` → `docs/project/TECHNICAL_REQUIREMENTS.md`
- `BDD_TEST_STATUS.md` → `docs/project/BDD_TEST_STATUS.md`

### Move to `.cursor/`
- `CURSOR_DEVELOPMENT_CONTEXT.md` → `.cursor/development_context.md`
- `RESUMPTION_PROMPT.md` → `.cursor/resumption_prompt.md`

### Move to `docs/`
- `findings.md` → `docs/api_troubleshooting.md` (rename to avoid conflict with existing findings.md)

## Potentially Obsolete Files to Review

### Scripts to Evaluate
- `test_release0.py` - Consider removing if BDD tests cover this functionality
- `test_api_connection.py` - Consider removing if BDD tests cover this functionality
- `debug_env.py` - Consider moving to `tools/` if still needed
- `check_env.py` - Consider moving to `tools/` if still needed
- `download_maps.py` - Consider moving to `tools/` if still needed

## Implementation Steps

1. Create backup copies of all files before moving or deleting
2. Move documentation files to their appropriate directories
3. Review potentially obsolete files and decide whether to:
   - Keep in current location
   - Move to a more appropriate directory
   - Remove if no longer needed
4. Update any references to moved files in other documents
5. Update `.cursor/project_structure.md` to reflect the new organization

## Post-Reorganization Verification

1. Ensure all documentation is accessible in its new location
2. Verify that Cursor agent can still find all necessary context
3. Run BDD tests to ensure functionality is not affected
4. Update any documentation that references the moved files 