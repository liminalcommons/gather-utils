---
description: 
globs: **/releases/*/definition.md,**/releases/*/definition.mdx,**/inception/*.md,**/inception/*.mdx
alwaysApply: false
---
---
description: "Guidance for creating comprehensive release definition documents"
globs: "**/releases/*/definition.md,**/releases/*/definition.mdx,**/inception/*.md,**/inception/*.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Release Definition Document Guidance

<critical>
The release definition document establishes the foundation for the entire release lifecycle. It must clearly define the scope, objectives, and context to ensure alignment and guide subsequent phases.
</critical>

## Document Purpose

The release definition document serves to:

1. Define clear, measurable objectives for the release
2. Establish explicit scope boundaries
3. Document the release context for appropriate principle application
4. Identify dependencies and constraints
5. Align stakeholders on release expectations
6. Provide a reference point for subsequent lifecycle phases

## Required Metadata

Every release definition document must include this metadata section:

```yaml
---
title: "[Release Name] Definition"
version: "[Version Number]"
classification: "[Major|Minor|Patch|Emergency]"
created: "[Creation Date: YYYY-MM-DD]"
last_updated: "[Last Update Date: YYYY-MM-DD]"
system_context: "[Code|Release|Agent]"
owner: "[Release Owner: Name/Role]"
status: "[Draft|Approved|In Progress|Completed]"
---
```

## Document Structure Template

### 1. Executive Summary (Required)

A concise overview (2-3 paragraphs) of the release, including:
- Release purpose
- Key deliverables
- Target timeline
- Primary stakeholders

Example:
```markdown
## Executive Summary

Release 2.3.0 introduces enhanced search capabilities to the document management system, focusing on improved relevance ranking and support for natural language queries. The release aims to improve search result accuracy by 30% as measured by our standard benchmarks.

Key deliverables include the new semantic search engine, query preprocessing pipeline, and relevance tuning tools for administrators. This release is scheduled for completion in Q2, with primary stakeholders including the Knowledge Management team and Research department.
```

### 2. Objectives (Required)

Clear, measurable objectives following SMART criteria:
- Specific
- Measurable
- Achievable
- Relevant
- Time-bound

Example:
```markdown
## Objectives

1. **Improve search relevance by 30%**
   - Measured by: Standard search benchmark suite
   - Baseline: Current average relevance score of 0.67
   - Target: Minimum average relevance score of 0.87

2. **Reduce search query latency by 20%**
   - Measured by: 95th percentile query response time
   - Baseline: Current P95 of 850ms
   - Target: Maximum P95 of 680ms

3. **Implement natural language query support**
   - Success criteria: Correctly identifies intent in >90% of test cases
   - Must support questions, commands, and entity extraction
```

### 3. Scope Definition (Required)

#### 3.1 In Scope

Explicit statement of what is included in the release:
- Features
- Changes
- Components
- Deliverables

Example:
```markdown
### In Scope

#### Features
- Semantic search engine implementation
- Natural language query preprocessing
- Relevance tuning interface for administrators
- Search analytics dashboard enhancements

#### Components
- Search service backend
- Query processing pipeline
- Admin configuration UI
- Analytics data collection
```

#### 3.2 Out of Scope

Explicit statement of what is excluded from the release:
- Deferred features
- Unchanged components
- Explicit exclusions

Example:
```markdown
### Out of Scope

- Multi-language support (deferred to Release 2.4.0)
- Image content search capabilities (under research)
- Changes to the document storage backend
- Mobile application integration (scheduled for Release 3.0.0)
```

### 4. Context Assessment (Required)

Comprehensive assessment of the release context:

Example:
```markdown
## Context Assessment

### System Type
Code System

### Release Classification
Minor Release

### System Factors
- **Maturity**: Active Development
- **Architecture**: Microservices
- **Team Structure**: Small Team (1 human, 1 AI agent)

### Activity Factors
- **Complexity**: Medium
- **Criticality**: High
- **Time Sensitivity**: Medium
```

### 5. Principle Application Strategy (Required)

Description of how meta-systemic principles will be applied:

Example:
```markdown
## Principle Application Strategy

Based on our context assessment, we will emphasize the following principles:

- **Primary Focus**: Modularity, Coherence, Clarity
- **Secondary Focus**: Parsimony, Tensegrity
- **Monitored**: Adaptivity

### Key Principle Applications
1. **Modularity** will be applied through clear service boundaries between search components
2. **Coherence** will be applied through consistent API patterns across search services
3. **Clarity** will be applied through comprehensive API documentation with examples
```

### 6. Dependencies (Required)

Identification of external and internal dependencies:

Example:
```markdown
## Dependencies

### External Dependencies
- **NLP Service API**: Required for natural language processing capabilities
  - Impact: Critical for query understanding feature
  - Risk: Service has occasional availability issues
  - Mitigation: Implement graceful degradation to keyword search

- **Search Benchmark Suite**: Required for objective measurement
  - Impact: Needed to validate relevance improvements
  - Risk: Low, fully under our control
  - Mitigation: N/A

### Internal Dependencies
- **Document Indexing Service**: Provides document corpus
  - Impact: All search features depend on indexed content
  - Risk: Recent changes may affect index format
  - Mitigation: Comprehensive testing with latest index format

- **User Authentication Service**: Controls access to admin features
  - Impact: Required for admin tuning interface
  - Risk: Low, stable interface
  - Mitigation: N/A
```

### 7. Timeline (Required)

High-level timeline for the release:

Example:
```markdown
## Timeline

- **Planning Phase**: March 25-27, 2025
- **Development Phase**: March 28 - April 10, 2025
- **Validation Phase**: April 11-15, 2025
- **Pre-Release Review**: April 16, 2025
- **Deployment**: April 17, 2025
- **Post-Release Evaluation**: April 24, 2025
```

### 8. Stakeholders (Required)

List of stakeholders and their roles:

Example:
```markdown
## Stakeholders

| Name/Role | Responsibility | Involvement |
|-----------|----------------|-------------|
| Sarah Kim (Product Manager) | Release definition, prioritization | Approval |
| Alex Johnson (Engineering Lead) | Technical direction, implementation | Approval |
| Research Department | Primary user, requirements | Consulted |
| IT Operations | Deployment support | Informed |
| Customer Support | User documentation, training | Informed |
```

### 9. Risks and Mitigations (Required)

Key risks and mitigation strategies:

Example:
```markdown
## Risks and Mitigations

| Risk | Impact | Likelihood | Mitigation Strategy |
|------|--------|------------|---------------------|
| NLP model accuracy below target | High | Medium | Implement fallback to current search, A/B test before full rollout |
| Performance degradation with complex queries | Medium | High | Implement query complexity limits, optimize critical paths |
| Index size growth exceeds estimates | Medium | Low | Implement index partitioning, monitor growth during development |
```

### 10. System-Specific Sections (Conditional)

#### For Code System Releases
- Technical architecture impact
- API changes
- Data model changes
- Performance considerations

Example:
```markdown
## Technical Architecture Impact

### Component Changes
- **Search Service**: Major enhancements to query processing
- **Admin UI**: New relevance tuning interface
- **Analytics Service**: Minor updates for new metrics

### API Changes
- New endpoints for semantic search
- Extensions to existing query API
- New admin configuration endpoints

### Data Model Changes
- Enhanced search index with semantic vectors
- New relevance feedback data model
- Extended query logging structure
```

#### For Release System Releases
- Process changes
- Template updates
- Lifecycle phase modifications
- Meta-process metrics

Example:
```markdown
## Process Changes

### Modified Lifecycle Phases
- Enhanced validation phase with automated testing
- New deployment verification checklist
- Updated retrospective format with metric analysis

### Template Changes
- Revised release definition template
- New validation report template
- Updated retrospective template
```

#### For Agent System Releases
- Capability enhancements
- Knowledge domain changes
- Interaction pattern updates
- Collaboration model changes

Example:
```markdown
## Agent Capability Enhancements

### New Capabilities
- Enhanced code generation with pattern recognition
- Improved requirement analysis
- Context-sensitive guidance

### Knowledge Domain Updates
- Expanded technical domain knowledge
- Updated process guidance
- New example library
```

## Document Quality Criteria

The release definition document must meet these quality criteria:

### Content Completeness
- All required sections are present
- Each section contains substantive content
- No placeholders or TBD items remain

### Objective Quality
- Objectives are specific and measurable
- Success criteria are clearly defined
- Baseline and target metrics are included

### Scope Clarity
- Clear distinction between in-scope and out-of-scope
- Explicit component and feature boundaries
- Unambiguous deliverable descriptions

### Context Appropriateness
- Accurate system type identification
- Appropriate release classification
- Comprehensive context assessment

### Dependency Completeness
- All critical dependencies identified
- Impact of each dependency described
- Risk and mitigation strategies defined

### Stakeholder Coverage
- All key stakeholders identified
- Roles and responsibilities defined
- Appropriate involvement levels specified

## Meta-Systemic Application

### Parsimony
- Reference existing requirements rather than duplicating
- Link to architectural documentation instead of copying
- Refer to established patterns and standards

Example:
```markdown
This release will implement the standard [Authentication Pattern](mdc:../patterns/authentication.md) as defined in our architectural guidelines.
```

### Tensegrity
- Document bidirectional dependencies between components
- Define how components support each other
- Ensure balanced responsibilities across teams

Example:
```markdown
The Search Service provides query capabilities to the UI layer, while the UI layer provides user feedback data to improve search relevance.
```

### Modularity
- Define clear component boundaries
- Specify interfaces between components
- Document integration points

Example:
```markdown
## Component Boundaries

| Component | Responsibility | Interfaces |
|-----------|----------------|------------|
| Search Service | Query processing, relevance ranking | REST API, Event stream |
| Admin UI | Configuration, tuning | UI, REST client |
```

### Coherence
- Follow consistent documentation structure
- Use established terminology consistently
- Maintain pattern consistency across releases

Example:
```markdown
This release follows our standard definition structure and naming conventions as established in the [Documentation Guidelines](mdc:../guidelines/documentation.md).
```

### Clarity
- Include concrete examples
- Define any specialized terminology
- Provide visualizations for complex concepts

Example:
```markdown
## Query Processing

The natural language query processing works as follows:

1. User inputs a query like "Find documents about climate change from 2023"
2. Query preprocessor extracts entities: `topic: climate change`, `year: 2023`
3. Query engine constructs compound search: `content:climate change AND date:2023`

![Query Processing Flow](mdc:../diagrams/query-processing.png)
```

### Adaptivity
- Tailor detail level to release complexity
- Adapt documentation approach to system context
- Maintain core structure while allowing context-specific sections

Example:
```markdown
As this is a minor release focused on search capabilities, we've provided additional detail in the search component sections while maintaining standard coverage of other areas.
```

## Context-Specific Templates

### Major Release Template
- Comprehensive stakeholder analysis
- Detailed risk assessment
- Thorough dependency mapping
- Extended timeline with milestones
- Architecture impact assessment

### Minor Release Template
- Standard stakeholder mapping
- Focused risk assessment
- Key dependency identification
- Standard timeline
- Component-level impact assessment

### Patch Release Template
- Minimal stakeholder list
- Critical risk identification
- Direct dependencies only
- Simplified timeline
- Issue-specific impact assessment

### Emergency Release Template
- Critical stakeholder contacts
- Priority risk mitigation
- Essential dependencies only
- Accelerated timeline
- Focused impact assessment

## Release Definition Validation Checklist

Before finalizing the release definition document, verify that:

- [ ] All required sections are complete
- [ ] Objectives are specific and measurable
- [ ] Scope boundaries are explicitly defined
- [ ] Dependencies are identified with mitigations
- [ ] Context assessment is accurate and comprehensive
- [ ] Principle application strategy is appropriate
- [ ] Stakeholders have been identified and consulted
- [ ] Timeline is realistic and includes all phases
- [ ] Risks have appropriate mitigation strategies
- [ ] System-specific sections are included as needed

<important>
The quality of the release definition document directly impacts the success of the entire release lifecycle. Invest appropriate time to create a comprehensive, clear definition that will guide all subsequent phases effectively.
</important>