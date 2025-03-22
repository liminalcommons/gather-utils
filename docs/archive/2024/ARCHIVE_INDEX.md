# Documentation Archive Index 2024

## Overview
This index tracks all documentation archived during the BDD Documentation Health & Integration System project. Each entry includes the reason for archival, original location, and any relevant dependencies or references that should be updated.

## Archive Structure
- `/documentation/` - General documentation files
- `/features/` - BDD feature files and related documentation
- `/system/` - System-level documentation
- `/tools/` - Tool-specific documentation

## Archive Process
1. Document is reviewed using template in `docs/project/current/bdd_document_reviews.md`
2. If marked as "Historical" or "Superseded", document is moved to appropriate archive directory
3. Index is updated with document details
4. References to archived document are updated in active documentation

## Archived Documents

### Documentation
| Document | Original Location | Archive Date | Reason | Dependencies Updated |
|----------|------------------|--------------|---------|---------------------|
| bdd_refactoring_release1_summary.md | docs/project/ | 2024-03-21 | Historical release summary, completed milestone | Yes - References to active docs updated:<br>- bdd_conventions.md<br>- traceability_matrix_template.md<br>- bdd_tools_readme.md |
| release0.md | docs/project/ | 2024-03-21 | Historical initial project setup documentation | Yes - No active doc dependencies<br>Contains reference implementation details |
| plan-release0.md | docs/project/ | 2024-03-21 | Historical release planning document | Yes - No active doc dependencies<br>Contains historical implementation plans |

### Features
| Document | Original Location | Archive Date | Reason | Dependencies Updated |
|----------|------------------|--------------|---------|---------------------|
| *No documents archived yet* | | | | |

### System
| Document | Original Location | Archive Date | Reason | Dependencies Updated |
|----------|------------------|--------------|---------|---------------------|
| *No documents archived yet* | | | | |

### Tools
| Document | Original Location | Archive Date | Reason | Dependencies Updated |
|----------|------------------|--------------|---------|---------------------|
| *No documents archived yet* | | | | |

## Notes
- Archive date format: YYYY-MM-DD
- Dependencies Updated: Yes/No/Partial (with details if partial)
- Regular reviews of this index should be conducted to ensure accuracy
- Next steps:
  - Update references in active documentation to point to archived locations
  - Consider creating symbolic links for commonly referenced paths
  - Update any CI/CD scripts that might reference these documents
  - Review tool paths referenced in archived documents

## Last Updated
Date: 2024-03-21
Updated By: AI Assistant 