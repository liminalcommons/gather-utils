---
description: 
globs: **/agent/development/*.md,**/agent/development/*.mdx,**/releases/*/agent_development.md,**/releases/*/agent_development.mdx,**/prompts/**/*.md,**/agent_guidelines/**/*.md
alwaysApply: false
---
---
description: "Agent-specific guidance for the development phase of the release lifecycle"
globs: "**/agent/development/*.md,**/agent/development/*.mdx,**/releases/*/agent_development.md,**/releases/*/agent_development.mdx,**/prompts/**/*.md,**/agent_guidelines/**/*.md"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Agent System Development Guidance

<critical>
This rule provides specialized guidance for the development phase when enhancing agent capabilities. Apply these principles and techniques to ensure effective agent capabilities that embody meta-systemic principles while delivering maximum value through human-AI collaboration.
</critical>

## Agent Development Context

Agent system development focuses on five key dimensions:

1. **Capability Enhancement**: Implementing new or improved agent capabilities
2. **Knowledge Domain Development**: Creating and refining agent knowledge structures
3. **Interaction Pattern Implementation**: Developing effective human-AI collaboration patterns
4. **Prompt Engineering**: Creating effective prompts and templates for agent guidance
5. **Validation Integration**: Building validation mechanisms into agent capabilities

## Development Approach

Structure your agent development activities as follows:

### 1. Capability Enhancement

Develop agent capabilities systematically:

```markdown
## Capability Development

### Capability Implementation Matrix
| Capability | Requirements | Development Approach | Success Criteria | Status |
|------------|--------------|---------------------|------------------|--------|
| Meta-systemic analysis | Identify principle application in code/documentation | Pattern-based analysis with examples | Accurate identification in >90% of cases | In Progress |
| Architecture guidance | Provide implementation guidance for patterns | Template-based guidance with context adaptation | Appropriate guidance for specific contexts | Planned |
| Documentation generation | Create structured documentation from requirements | Template-based generation with knowledge integration | Complete, clear documentation artifacts | Completed |

### Incremental Development Approach
1. **Core Functionality Implementation**:
   - Develop minimum viable capability implementation
   - Focus on fundamental accuracy and correctness
   - Implement basic knowledge application
   - Verify against simple test cases

2. **Context-Sensitive Enhancement**:
   - Add context detection and adaptation
   - Implement variation handling
   - Enhance example-based reasoning
   - Validate against diverse scenarios

3. **Integration and Refinement**:
   - Integrate with other agent capabilities
   - Implement cross-domain knowledge application
   - Enhance error handling and edge cases
   - Validate against complex real-world scenarios

4. **Performance Optimization**:
   - Improve response quality and precision
   - Enhance efficiency and conciseness
   - Optimize knowledge retrieval
   - Fine-tune guidance for specific contexts
```

### 2. Knowledge Domain Development

Build robust, well-structured knowledge domains:

```markdown
## Knowledge Domain Development

### Knowledge Architecture
- Organize knowledge into well-defined domains
- Create clear boundaries between knowledge areas
- Establish relationships between domains
- Define cross-domain integration points

### Knowledge Representation
- Develop canonical descriptions for key concepts
- Create example-based knowledge representations
- Implement hierarchical knowledge structures
- Define clear terminology and nomenclature

### Knowledge Application
- Create context-triggered knowledge retrieval
- Implement cross-domain knowledge synthesis
- Develop pattern-based knowledge application
- Build adaptive knowledge selection mechanisms

### Implementation Example

#### Meta-Systemic Principles Knowledge Domain

```yaml
knowledge_domain:
  name: "Meta-Systemic Principles"
  purpose: "Core principles that guide system design and evolution"
  
  concepts:
    - name: "Parsimony"
      definition: "Each concept is defined once and referenced elsewhere"
      key_aspects:
        - "Information density optimization"
        - "Duplication minimization"
        - "Reference-based knowledge management"
        - "Canonical source definition"
      examples:
        - "Shared utility functions instead of duplicated code"
        - "Type definitions in central location"
        - "Documentation that references canonical sources"
      application_patterns:
        - "Extract common functionality to shared locations"
        - "Reference rather than duplicate information"
        - "Create canonical sources for concepts"
      related_concepts:
        - "DRY principle"
        - "Information architecture"
        - "Knowledge management"
      
    - name: "Tensegrity"
      definition: "Elements both support and are supported by others"
      key_aspects:
        - "Balanced component relationships"
        - "Mutual support mechanisms"
        - "Resilient connections"
        - "Distributed responsibility"
      examples:
        - "Services that provide bidirectional value"
        - "Components with balanced dependencies"
        - "Error handling with graceful degradation"
      application_patterns:
        - "Design components with bidirectional value"
        - "Balance dependencies across the system"
        - "Implement resilient connection points"
      related_concepts:
        - "Resilient systems"
        - "Balanced architecture"
        - "Interdependent components"
  
  # Additional principles follow the same structure
  
  relationships:
    - type: "tension"
      concepts: ["Parsimony", "Clarity"]
      description: "Balance between consolidated information and clear explanation"
      resolution: "Include essential details directly while referencing additional information"
    
    - type: "tension"
      concepts: ["Modularity", "Tensegrity"]
      description: "Balance between independence and interconnection"
      resolution: "Create clear boundaries with explicit, resilient connection points"
    
    # Additional relationships defined similarly
  
  application_contexts:
    - context: "Code System"
      adaptations:
        - "Focus on code organization and architecture"
        - "Apply to implementation patterns and structures"
        - "Emphasize code and documentation relationships"
    
    - context: "Release System"
      adaptations:
        - "Focus on process and artifact organization"
        - "Apply to workflow and responsibility distribution"
        - "Emphasize process and artifact relationships"
    
    - context: "Agent System"
      adaptations:
        - "Focus on capability and knowledge organization"
        - "Apply to interaction patterns and guidance"
        - "Emphasize human-AI collaboration relationships"
```
```

### 3. Interaction Pattern Implementation

Develop effective interaction patterns:

```markdown
## Interaction Pattern Development

### Interaction Pattern Design
- Define clear interaction flows for specific contexts
- Create balanced responsibility models
- Develop appropriate information exchange mechanisms
- Implement context adaptation capabilities

### Collaboration Models
- Define roles and responsibilities for human and AI
- Create clear handoff procedures
- Implement feedback integration mechanisms
- Develop progressive enhancement patterns

### Dialogue Structures
- Create effective question and clarification patterns
- Implement structured information presentation
- Develop context-sensitive response formats
- Build appropriate abstraction management

### Implementation Example

#### Collaborative Development Interaction Pattern

```yaml
interaction_pattern:
  name: "Collaborative Development Pattern"
  purpose: "Enable effective human-AI collaboration for implementation tasks"
  
  workflow:
    - phase: "Requirement Analysis"
      human_role: "Provide high-level requirements and context"
      agent_role: "Analyze requirements, identify tasks, suggest approach"
      interaction_flow:
        - agent: "Request clear problem statement and context"
        - human: "Provide problem description and constraints"
        - agent: "Analyze requirements and suggest implementation approach"
        - human: "Refine approach and confirm direction"
      success_criteria:
        - "Shared understanding of requirements"
        - "Clear implementation approach established"
        - "Key considerations identified"
    
    - phase: "Initial Implementation"
      human_role: "Guide overall direction, make key design decisions"
      agent_role: "Generate implementation, apply patterns, explain approach"
      interaction_flow:
        - agent: "Generate initial implementation based on approach"
        - human: "Review implementation and provide feedback"
        - agent: "Refine based on feedback, explain decisions"
        - human: "Approve or request further changes"
      success_criteria:
        - "Working initial implementation"
        - "Implementation follows established patterns"
        - "Clear explanation of implementation decisions"
    
    - phase: "Refinement"
      human_role: "Provide specific feedback, identify edge cases"
      agent_role: "Implement refinements, enhance error handling, optimize"
      interaction_flow:
        - human: "Provide specific feedback and enhancement requests"
        - agent: "Implement requested changes with appropriate adaptations"
        - human: "Validate changes and identify any remaining issues"
        - agent: "Address remaining issues and finalize implementation"
      success_criteria:
        - "Implementation addresses all requirements"
        - "Edge cases and error handling implemented"
        - "Code quality and performance optimized"
    
    - phase: "Documentation"
      human_role: "Specify documentation requirements, review clarity"
      agent_role: "Generate comprehensive documentation, explain complexity"
      interaction_flow:
        - human: "Specify documentation requirements"
        - agent: "Generate documentation with examples"
        - human: "Review and request clarifications if needed"
        - agent: "Enhance documentation based on feedback"
      success_criteria:
        - "Complete documentation with examples"
        - "Clear explanation of complex aspects"
        - "Documentation follows established standards"
  
  adaptations:
    - context: "Simple Task"
      modifications:
        - "Combine initial implementation and refinement phases"
        - "Streamline documentation requirements"
        - "Focus on rapid implementation over optimization"
    
    - context: "Complex Architecture"
      modifications:
        - "Add design phase before implementation"
        - "Increase emphasis on pattern application"
        - "Enhance documentation with architectural explanation"
    
    - context: "Maintenance Task"
      modifications:
        - "Add impact analysis phase"
        - "Focus on consistency with existing patterns"
        - "Emphasize regression prevention"
  
  anti_patterns:
    - name: "One-way Development"
      description: "Agent simply implements without human input on key decisions"
      prevention: "Explicitly identify decision points and request human input"
    
    - name: "Over-explanation"
      description: "Agent provides excessive detail that obscures key points"
      prevention: "Use structured explanations with progressive disclosure"
    
    - name: "Under-contextualization"
      description: "Agent implements without sufficient context awareness"
      prevention: "Explicitly confirm context understanding before implementation"
```
```

### 4. Prompt Engineering

Develop effective prompts and templates:

```markdown
## Prompt Development

### Prompt Architecture
- Create clear, structured prompt templates
- Define context-specific prompt variations
- Develop reusable prompt components
- Implement prompt chaining and composition

### Content Structuring
- Organize prompts with clear sections
- Create appropriate knowledge references
- Develop consistent terminology usage
- Implement information hierarchy

### Context Adaptation
- Design prompts for different system contexts
- Create role-specific prompt variations
- Implement task-specific adaptations
- Develop domain-specific variations

### Implementation Example

#### Meta-Systemic Analysis Prompt Template

```yaml
prompt_template:
  name: "Meta-Systemic Analysis Prompt"
  purpose: "Guide agent in analyzing artifacts for meta-systemic principle application"
  
  structure:
    - section: "Task Definition"
      content: |
        Perform a meta-systemic analysis of the {{artifact_type}} to evaluate application of meta-systemic principles, identify strengths and weaknesses, and provide improvement recommendations.
    
    - section: "Context Information"
      content: |
        System Context: {{system_context}}
        Artifact Type: {{artifact_type}}
        System Maturity: {{system_maturity}}
        Team Structure: {{team_structure}}
    
    - section: "Analysis Instructions"
      content: |
        1. First, review the artifact to understand its overall purpose and structure.
        2. Analyze the application of each meta-systemic principle:
           - Parsimony: Evaluate information density and reference usage
           - Tensegrity: Assess relationship balance and mutual support
           - Modularity: Evaluate boundary clarity and interface definitions
           - Coherence: Assess pattern consistency and alignment
           - Clarity: Evaluate explanation quality and example usage
           - Adaptivity: Assess context sensitivity and adaptation
        3. For each principle, identify specific strengths and improvement opportunities.
        4. Provide an overall assessment with key recommendations.
    
    - section: "Output Structure"
      content: |
        1. Executive Summary: Overall assessment and key findings
        2. Principle-by-Principle Analysis:
           - [Principle Name]: Assessment, strengths, weaknesses, examples
           - [Repeat for each principle]
        3. Key Recommendations: Prioritized list of improvements
        4. Implementation Guidance: Specific suggestions for enhancement
    
    - section: "Principle Reference"
      content: |
        Here are the key aspects of each principle to evaluate:
        
        Parsimony:
        - Single sources of truth for concepts
        - Appropriate reference mechanisms
        - Minimal duplication of information
        - Effective information organization
        
        [Similar reference for each principle]
  
  variations:
    - context: "Code System"
      replacements:
        - section: "Analysis Instructions"
          modifications:
            - "Focus on code organization and architecture"
            - "Emphasize implementation pattern consistency"
            - "Evaluate documentation and code alignment"
    
    - context: "Release System"
      replacements:
        - section: "Analysis Instructions"
          modifications:
            - "Focus on process structure and artifact organization"
            - "Emphasize workflow and responsibility clarity"
            - "Evaluate artifact consistency and relationships"
    
    - context: "Agent System"
      replacements:
        - section: "Analysis Instructions"
          modifications:
            - "Focus on capability organization and knowledge structure"
            - "Emphasize interaction pattern effectiveness"
            - "Evaluate guidance clarity and adaptation"
  
  examples:
    - example_name: "Code Architecture Analysis"
      variables:
        artifact_type: "Architecture Document"
        system_context: "Code System"
        system_maturity: "Active Development"
        team_structure: "Small Team"
      expected_output: |
        [Sample analysis output focusing on code architecture]
    
    - example_name: "Process Documentation Analysis"
      variables:
        artifact_type: "Process Documentation"
        system_context: "Release System"
        system_maturity: "Maintenance"
        team_structure: "Multiple Teams"
      expected_output: |
        [Sample analysis output focusing on process documentation]
```
```

### 5. Testing and Validation Integration

Incorporate validation into development:

```markdown
## Testing and Validation Integration

### Test-Driven Development
- Define validation criteria before implementation
- Create comprehensive test cases
- Implement capability verification mechanisms
- Develop regression prevention approaches

### Integrated Validation
- Build validation directly into capabilities
- Implement self-assessment mechanisms
- Create quality check patterns
- Develop continuous validation approaches

### Scenario-Based Testing
- Create diverse test scenarios
- Develop domain-specific test cases
- Implement edge case validation
- Build performance testing capabilities

### Implementation Example

#### Capability Validation Framework

```yaml
validation_framework:
  name: "Agent Capability Validation Framework"
  purpose: "Provide integrated validation for agent capabilities"
  
  validation_dimensions:
    - dimension: "Functional Correctness"
      test_approaches:
        - name: "Golden Set Testing"
          description: "Validate against known correct examples"
          implementation: |
            Create a set of representative examples with known correct outputs.
            Compare agent outputs to expected results and calculate accuracy.
            Establish minimum accuracy thresholds for acceptance.
          metrics:
            - "Accuracy Percentage"
            - "Error Rate by Category"
        
        - name: "Edge Case Testing"
          description: "Validate handling of boundary conditions"
          implementation: |
            Identify edge cases and unusual inputs.
            Validate appropriate handling and graceful degradation.
            Ensure consistent behavior across edge cases.
          metrics:
            - "Edge Case Coverage"
            - "Edge Case Success Rate"
    
    - dimension: "Principle Application"
      test_approaches:
        - name: "Principle Audit"
          description: "Assess application of meta-systemic principles"
          implementation: |
            Review capability implementation against principle criteria.
            Identify areas of strong and weak principle application.
            Ensure balanced application across all principles.
          metrics:
            - "Principle Coverage Score"
            - "Principle Balance Index"
        
        - name: "Pattern Consistency Check"
          description: "Verify consistent pattern application"
          implementation: |
            Compare implementation to established patterns.
            Identify pattern violations or inconsistencies.
            Ensure appropriate pattern adaptation for context.
          metrics:
            - "Pattern Consistency Score"
            - "Pattern Adaptation Appropriateness"
    
    - dimension: "Context Adaptation"
      test_approaches:
        - name: "Context Variation Testing"
          description: "Validate adaptation to different contexts"
          implementation: |
            Test capability across different system contexts.
            Verify appropriate variation based on context.
            Ensure core functionality remains consistent.
          metrics:
            - "Context Adaptation Score"
            - "Context Coverage Percentage"
        
        - name: "Contextual Appropriateness"
          description: "Assess appropriateness of responses for context"
          implementation: |
            Evaluate response appropriateness for specific contexts.
            Verify detail level, terminology, and format adaptation.
            Ensure balanced adaptation without losing core functionality.
          metrics:
            - "Contextual Appropriateness Score"
            - "Adaptation Consistency Index"
  
  implementation:
    - phase: "Test Definition"
      activities:
        - "Define specific test cases for each dimension"
        - "Create expected outputs for test cases"
        - "Establish acceptance criteria and thresholds"
    
    - phase: "Validation Integration"
      activities:
        - "Implement validation checks within capability"
        - "Create self-assessment mechanisms"
        - "Develop performance monitoring"
    
    - phase: "Continuous Validation"
      activities:
        - "Establish regression testing approach"
        - "Implement automated validation pipeline"
        - "Create validation reporting mechanisms"
  
  examples:
    - capability: "Architecture Pattern Recognition"
      test_cases:
        - name: "Identify Factory Pattern"
          input: |
            [Code example implementing factory pattern]
          expected_output: |
            [Expected analysis identifying factory pattern]
          validation_criteria:
            - "Correctly identifies factory pattern"
            - "Explains key components of the pattern"
            - "Identifies any implementation issues"
        
        - name: "Pattern Variation Recognition"
          input: |
            [Code example with pattern variation]
          expected_output: |
            [Expected analysis identifying pattern with variation]
          validation_criteria:
            - "Identifies core pattern despite variation"
            - "Explains adaptations and their purpose"
            - "Assesses appropriateness of adaptation"
```
```

## Meta-Systemic Principle Application

### Parsimony
- Create reusable knowledge structures
- Define concepts once and reference elsewhere
- Establish canonical pattern definitions
- Minimize duplication across capabilities

Example:
```markdown
### Knowledge Reference Architecture

Instead of duplicating knowledge across agent capabilities, implement a centralized knowledge architecture:

```
knowledge/
├── principles/
│   ├── parsimony.md
│   ├── tensegrity.md
│   ├── modularity.md
│   ├── coherence.md
│   ├── clarity.md
│   └── adaptivity.md
├── patterns/
│   ├── code/
│   │   └── architecture_patterns.md
│   ├── release/
│   │   └── process_patterns.md
│   └── agent/
│       └── interaction_patterns.md
└── domains/
    ├── code_system.md
    ├── release_system.md
    └── agent_system.md
```

Each capability references these canonical knowledge sources rather than duplicating descriptions, ensuring consistency and maintainability.
```

### Tensegrity
- Design capabilities that support each other
- Create balanced human-AI collaboration models
- Implement bidirectional knowledge exchange
- Build resilient interaction patterns

Example:
```markdown
### Balanced Capability Design

Design agent capabilities that provide mutual support:

| Capability | Provides To Other Capabilities | Receives From Other Capabilities |
|------------|--------------------------------|----------------------------------|
| Pattern Recognition | Identifies patterns for documentation and implementation | Receives context from knowledge management, requirements from analysis |
| Documentation | Creates clear explanations for implementation and validation | Receives patterns from recognition, structures from knowledge management |
| Implementation | Generates code following patterns, fulfilling requirements | Receives patterns from recognition, documentation from documentation |
| Validation | Verifies implementation and documentation quality | Receives implementation from implementation, documentation from documentation |

This balanced design ensures capabilities support each other rather than operating in isolation.
```

### Modularity
- Create clear boundaries between agent capabilities
- Define explicit interfaces between knowledge domains
- Encapsulate implementation details
- Design for independent evolution

Example:
```markdown
### Modular Capability Architecture

Design agent capabilities with clear boundaries and interfaces:

```
┌─────────────────────┐      ┌─────────────────────┐
│  Pattern Recognition│◄─────┤  Knowledge Management│
└─────────┬───────────┘      └─────────────────────┘
          │                               ▲
          ▼                               │
┌─────────────────────┐      ┌─────────────────────┐
│  Implementation     │─────►│  Documentation      │
└─────────┬───────────┘      └─────────┬───────────┘
          │                            │
          ▼                            ▼
┌─────────────────────┐      ┌─────────────────────┐
│  Validation         │◄─────┤  Feedback Analysis  │
└─────────────────────┘      └─────────────────────┘
```

Each capability has:
- Well-defined inputs and outputs
- Clear responsibility boundaries
- Explicit interfaces for interaction
- Independent implementation details
```

### Coherence
- Apply consistent patterns across capabilities
- Maintain uniform interaction styles
- Use consistent terminology throughout
- Ensure aligned knowledge representation

Example:
```markdown
### Interaction Pattern Consistency

Maintain consistent interaction patterns across agent capabilities:

1. **Pattern Recognition**
   - First step: Context understanding and requirement clarification
   - Core interaction: Analysis and explanation with examples
   - Resolution: Clear identification with rationale and alternatives

2. **Implementation Guidance**
   - First step: Context understanding and requirement clarification
   - Core interaction: Development with explanations and examples
   - Resolution: Complete implementation with rationale and alternatives

3. **Documentation Generation**
   - First step: Context understanding and requirement clarification
   - Core interaction: Creation with structure and examples
   - Resolution: Complete documentation with rationale and alternatives

This consistent flow creates a predictable interaction pattern regardless of the specific capability being used.
```

### Clarity
- Provide explicit explanation of agent reasoning
- Include concrete examples for complex concepts
- Design clear, structured responses
- Create progressive disclosure of information

Example:
```markdown
### Progressive Disclosure Pattern

Implement clarity through progressive disclosure in responses:

**Level 1: Executive Summary**
```
The code implements a Repository pattern with appropriate separation of concerns.
Key strengths include clean interface definition and error handling.
Improvement opportunities exist in transaction management and query optimization.
```

**Level 2: Principle Analysis**
```
Modularity: Strong (9/10)
- Clear interface definition with repository pattern
- Good separation of concerns
- Explicit dependency injection

Parsimony: Moderate (7/10)
- Some duplication in query methods
- Opportunity to extract common query patterns
...
```

**Level 3: Detailed Implementation**
```
Detailed explanation of each component with code examples...
Specific implementation suggestions...
Comparative pattern examples...
```

This structure allows users to access the level of detail they need without overwhelming them with information.
```

### Adaptivity
- Create context-sensitive capabilities
- Develop adaptive interaction patterns
- Build flexible knowledge application
- Implement variable detail levels

Example:
```markdown
### Context Adaptation Framework

Implement multi-dimensional context adaptation:

```yaml
context_dimensions:
  - dimension: "System Context"
    values:
      - "Code System"
      - "Release System"
      - "Agent System"
    adaptation: "Affects domain knowledge, terminology, and examples"
  
  - dimension: "User Role"
    values:
      - "Developer"
      - "Architect"
      - "Project Manager"
    adaptation: "Affects technical depth, focus areas, and terminology"
  
  - dimension: "Task Type"
    values:
      - "Implementation"
      - "Review"
      - "Documentation"
    adaptation: "Affects level of detail, guidance style, and validation focus"
  
  - dimension: "System Maturity"
    values:
      - "Early Exploration"
      - "Active Development"
      - "Maintenance"
    adaptation: "Affects recommendation style, principle emphasis, and constraint focus"
```

Each capability adapts along these dimensions while maintaining core functionality.
```

## Release Scope-Specific Development

### Major Release Development
- Comprehensive capability development
- In-depth knowledge domain creation
- Extensive pattern implementation
- Thorough testing and validation
- Complete documentation and examples

### Minor Release Development
- Focused capability enhancements
- Targeted knowledge domain updates
- Specific pattern improvements
- Standard testing and validation
- Focused documentation updates

### Patch Release Development
- Specific capability fixes
- Limited knowledge corrections
- Pattern consistency improvements
- Focused issue validation
- Issue-specific documentation updates

### Emergency Release Development
- Critical issue resolution
- Essential knowledge corrections
- Core pattern preservation
- Issue-specific validation
- Minimal documentation updates

## Development Phase Quality Checklist

Before concluding the development phase, verify that:

- [ ] All planned capabilities are implemented with appropriate quality
- [ ] Knowledge domains are well-structured and accurate
- [ ] Interaction patterns are effective and context-sensitive
- [ ] Prompts and templates follow best practices
- [ ] Testing and validation are integrated into capabilities
- [ ] Documentation is comprehensive and clear
- [ ] Meta-systemic principles are appropriately applied
- [ ] Context adaptation is implemented for relevant variations
- [ ] Implementation follows consistent patterns
- [ ] Final validation confirms requirement fulfillment

## Human-AI Collaboration in Development

In our two-person team:

### Human Team Member Focus
- Setting capability requirements and priorities
- Making key design decisions
- Providing domain expertise
- Evaluating subjective quality aspects
- Approving final implementations

### AI Agent Focus
- Generating capability implementations
- Creating structured knowledge representations
- Developing consistent interaction patterns
- Ensuring principle application
- Producing comprehensive documentation

<important>
Agent system development requires balancing technical capability implementation with effective human-AI collaboration design. Focus on both functional correctness and interaction quality to create agent capabilities that deliver maximum value through complementary strengths.
</important>