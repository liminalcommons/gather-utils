---
description: 
globs: **/agent/planning/*.md,**/agent/planning/*.mdx,**/releases/*/agent_plan.md,**/releases/*/agent_plan.mdx
alwaysApply: false
---
---
description: "Agent system-specific guidance for the planning phase of the release lifecycle"
globs: "**/agent/planning/*.md,**/agent/planning/*.mdx,**/releases/*/agent_plan.md,**/releases/*/agent_plan.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Agent System Planning Guidance

<critical>
This rule provides specialized guidance for the planning phase when the primary system context is agent system enhancement. Apply these guidelines in conjunction with the core planning phase rules.
</critical>

## Agent System Planning Approach

When planning agent system changes, focus on these specialized aspects:

### 1. Capability Enhancement Planning

Break down capability enhancements into implementable tasks:

```markdown
## Capability Enhancement Breakdown

### Capability-Based Decomposition
- **Capability**: [Capability Name]
  - **Enhancement 1.1**: [Specific enhancement]
    - **Description**: [Detailed description of what needs to be implemented]
    - **Implementation Approach**: [Brief description of implementation approach]
    - **Success Criteria**: [Specific, measurable criteria for completion]
    - **Dependencies**: [Internal and external dependencies]
    - **Effort Estimate**: [Estimate in story points or hours]
    - **Complexity**: [High/Medium/Low]
    - **Priority**: [High/Medium/Low]
  
  - **Enhancement 1.2**: [Specific enhancement]
    - [Additional enhancement details...]

- **Capability**: [Next Capability Name]
  - **Enhancement 2.1**: [Specific enhancement]
    - [Enhancement details...]

### Common Enhancement Patterns
- **Knowledge Enhancement Pattern**: [Standard approach for knowledge expansion]
- **Reasoning Enhancement Pattern**: [Standard approach for improving reasoning]
- **Output Quality Enhancement Pattern**: [Standard approach for improving outputs]
- **Interaction Enhancement Pattern**: [Standard approach for improving interactions]
```

### 2. Knowledge Domain Planning

Plan knowledge domain enhancements and organization:

```markdown
## Knowledge Domain Planning

### Knowledge Structure
- **Domain Organization**:
  - [How knowledge will be structured]
  - [Domain hierarchy and relationships]
  - [Knowledge boundaries and interfaces]
  - [Cross-domain references]

- **Knowledge Representation**:
  - [How knowledge will be stored and accessed]
  - [Representation formats and structures]
  - [Knowledge granularity considerations]
  - [Versioning and evolution approach]

### Knowledge Content
- **Domain**: [Knowledge Domain Name]
  - **Current State**: [Assessment of current knowledge]
  - **Target State**: [Desired knowledge enhancements]
  - **Knowledge Gaps**: [Specific gaps to address]
  - **Sources**: [Where new knowledge will come from]
  - **Validation Approach**: [How knowledge will be validated]
  
- **Domain**: [Next Knowledge Domain Name]
  - [Domain details...]

### Knowledge Integration
- **Cross-Domain References**: [How domains will reference each other]
- **Knowledge Consistency**: [How consistency will be maintained]
- **Knowledge Hierarchy**: [How knowledge hierarchies will work]
- **Knowledge Evolution**: [How knowledge will evolve over time]
```

### 3. Interaction Pattern Planning

Plan improvements to interaction patterns:

```markdown
## Interaction Pattern Planning

### Pattern Enhancements
- **Pattern**: [Interaction Pattern Name]
  - **Current Limitations**: [Issues with current pattern]
  - **Enhancements**: [Specific improvements to make]
  - **Use Cases**: [When this pattern should be used]
  - **Components**: [Elements of the interaction pattern]
  - **Expected Outcomes**: [What the pattern should achieve]
  
- **Pattern**: [Next Interaction Pattern Name]
  - [Pattern details...]

### Prompt Engineering
- **Prompt Templates**:
  - [Template structures and formats]
  - [Reusable components]
  - [Adaptation mechanisms]
  - [Context sensitivity approaches]

- **Prompt Optimization**:
  - [Strategies for improving prompt effectiveness]
  - [Testing and validation approaches]
  - [Performance considerations]
  - [Consistency mechanisms]

### Response Design
- **Response Formats**:
  - [Standard response structures]
  - [Format variations by context]
  - [Adaptation mechanisms]
  - [Quality standards]

- **Output Optimization**:
  - [Strategies for improving response quality]
  - [Consistency mechanisms]
  - [Style and tone guidelines]
  - [Validation approaches]
```

### 4. Collaboration Model Planning

Plan enhancements to human-AI collaboration:

```markdown
## Collaboration Model Planning

### Role Refinements
- **AI Agent Role**:
  - **Current Responsibilities**: [Current role definition]
  - **Enhanced Responsibilities**: [New/modified responsibilities]
  - **Decision Authority**: [What decisions the agent can make]
  - **Escalation Criteria**: [When to defer to human judgment]
  - **Performance Expectations**: [Quality and efficiency targets]

- **Human Team Member Role**:
  - **Current Responsibilities**: [Current role definition]
  - **Enhanced Responsibilities**: [New/modified responsibilities]
  - **Decision Authority**: [Decisions reserved for humans]
  - **Direction Setting**: [How humans guide the agent]
  - **Performance Expectations**: [Quality and efficiency targets]

### Workflow Enhancements
- **Workflow**: [Collaboration Workflow Name]
  - **Current Limitations**: [Issues with current workflow]
  - **Enhancements**: [Specific improvements to make]
  - **Interaction Flow**: [Step-by-step process]
  - **Artifact Exchanges**: [What artifacts are shared]
  - **Success Criteria**: [What makes this workflow successful]
  
- **Workflow**: [Next Collaboration Workflow Name]
  - [Workflow details...]

### Feedback Mechanisms
- **Agent Improvement Feedback**:
  - [How feedback will be collected]
  - [How feedback will be processed]
  - [How improvements will be implemented]
  - [How effectiveness will be measured]

- **Human Guidance Feedback**:
  - [How humans will receive feedback]
  - [How guidance effectiveness will be measured]
  - [How guidance will be improved]
  - [How feedback loops will work]
```

### 5. Evaluation Scenario Planning

Plan scenarios for capability evaluation:

```markdown
## Evaluation Scenario Planning

### Test Scenarios
- **Scenario**: [Scenario Name]
  - **Description**: [What the scenario tests]
  - **Capability Focus**: [Which capabilities are being tested]
  - **Input Conditions**: [Starting context and inputs]
  - **Expected Behaviors**: [What the agent should do]
  - **Success Criteria**: [How success will be measured]
  - **Evaluation Approach**: [How the scenario will be evaluated]
  
- **Scenario**: [Next Scenario Name]
  - [Scenario details...]

### Evaluation Methods
- **Quantitative Evaluation**:
  - [Metrics to be captured]
  - [Measurement approaches]
  - [Benchmark targets]
  - [Analysis methods]

- **Qualitative Evaluation**:
  - [Subjective assessment approaches]
  - [Review processes]
  - [Feedback collection]
  - [Expert evaluation]

### Capability Metrics
| Capability | Metric | Current Baseline | Target | Measurement Method |
|------------|--------|------------------|--------|-------------------|
| [Capability 1] | [Metric 1] | [Current value] | [Target value] | [How it will be measured] |
| [Capability 1] | [Metric 2] | [Current value] | [Target value] | [How it will be measured] |
| [Capability 2] | [Metric 1] | [Current value] | [Target value] | [How it will be measured] |
```

### 6. Risk and Limitation Assessment

Identify risks and plan for agent limitations:

```markdown
## Risk and Limitation Assessment

### Risk Identification
| Risk | Description | Impact | Likelihood | Risk Level |
|------|-------------|--------|------------|------------|
| [Risk 1] | [Detailed description] | High/Medium/Low | High/Medium/Low | High/Medium/Low |
| [Risk 2] | [Detailed description] | High/Medium/Low | High/Medium/Low | High/Medium/Low |

### Risk Mitigation Strategies
- **Risk 1**:
  - **Mitigation Approach**: [Specific mitigation strategy]
  - **Monitoring Approach**: [How to monitor for this risk]
  - **Contingency Plan**: [What to do if risk materializes]
  - **Owner**: [Risk owner]

- **Risk 2**:
  - [Risk mitigation details...]

### Capability Limitations
- **Limitation**: [Specific capability limitation]
  - **Description**: [Detailed explanation of the limitation]
  - **Impact**: [How this affects usage]
  - **Communication Strategy**: [How to communicate this to users]
  - **Workaround**: [Alternative approaches when hitting this limitation]
  
- **Limitation**: [Next limitation]
  - [Limitation details...]
```

## Meta-Systemic Principle Application

### Parsimony in Agent System Planning

1. **Design efficient knowledge structures**:
   - Plan for canonical knowledge sources
   - Design effective reference mechanisms
   - Avoid knowledge duplication across domains
   - Create shared knowledge libraries

2. **Develop reusable components**:
   - Plan modular prompt components
   - Design reusable response patterns
   - Create standardized interaction templates
   - Establish shared capability building blocks

3. **Optimize information organization**:
   - Plan coherent knowledge taxonomies
   - Design consistent reference systems
   - Create efficient metadata schemas
   - Establish hierarchical organization structures

Example:
```markdown
## Knowledge Efficiency Strategy

Our knowledge architecture will implement these parsimony improvements:

1. **Canonical Knowledge Sources**: The revised knowledge architecture will establish canonical sources for each domain, reducing current duplication by approximately 60%.

2. **Knowledge Reference System**: We'll implement a hierarchical reference system allowing efficient access to knowledge across domains without duplication:

   ```yaml
   reference_pattern:
     domain: "domain_name"        # Knowledge domain
     concept: "concept_name"      # Specific concept
     aspect: "aspect_name"        # Optional specific aspect
     version: "version_id"        # Optional version specifier
   ```

3. **Modular Knowledge Components**: Knowledge will be structured as composable units that can be referenced and reused across different contexts:

   ```yaml
   knowledge_component:
     identifier: "unique_id"
     type: "concept|procedure|rule|example"
     content: "Knowledge content"
     related_concepts: ["concept1", "concept2"]
     usage_contexts: ["context1", "context2"]
   ```

This approach reduces knowledge maintenance overhead by 40% while improving consistency and enabling more efficient knowledge retrieval.
```

### Tensegrity in Agent System Planning

1. **Balance human and AI responsibilities**:
   - Plan complementary capability distribution
   - Design balanced workload allocation
   - Create mutual value exchange mechanisms
   - Establish clear support relationships

2. **Design resilient collaboration models**:
   - Plan for graceful degradation in capabilities
   - Design fault tolerance in interactions
   - Create appropriate escalation paths
   - Establish fallback mechanisms

3. **Establish bidirectional feedback**:
   - Plan systematic feedback collection
   - Design improvement mechanisms for both roles
   - Create learning feedback loops
   - Establish balanced performance assessment

Example:
```markdown
## Human-AI Collaboration Balance

The enhanced collaboration model balances responsibilities between human and AI team members:

```yaml
balanced_responsibilities:
  code_generation:
    ai_agent:
      - Pattern-based code implementation
      - Documentation generation
      - Test case creation
      - Style consistency enforcement
    human:
      - Architecture decisions
      - Algorithm selection
      - Edge case identification
      - Performance optimization decisions
  
  documentation:
    ai_agent:
      - Comprehensive documentation drafting
      - Consistency checking
      - Format standardization
      - Reference management
    human:
      - Audience needs assessment
      - Critical information prioritization
      - Clarity and effectiveness evaluation
      - Final approval
```

The model creates these bidirectional support mechanisms:

1. **Capability Augmentation**: Each role enhances the other's effectiveness:
   - AI amplifies human productivity through automation and consistency
   - Human enhances AI effectiveness through direction and judgment

2. **Resilience Design**: The collaboration model includes:
   - Graceful degradation when either party has limitations
   - Clear escalation paths for complex decisions
   - Capability confidence signaling
   - Explicit knowledge gap identification

3. **Mutual Improvement**: Systematic feedback loops improve both parties:
   - Human feedback improves AI capabilities
   - AI pattern detection improves human consistency
   - Joint retrospectives enhance collaboration
```

### Modularity in Agent System Planning

1. **Create clear capability boundaries**:
   - Plan explicit interfaces for capabilities
   - Design independent but integrated capabilities
   - Establish clear knowledge domain boundaries
   - Create modular interaction patterns

2. **Design for independent evolution**:
   - Plan capability versioning approaches
   - Design backward compatibility mechanisms
   - Create extensible capability frameworks
   - Establish clear extension points

3. **Establish capability contracts**:
   - Define input and output specifications
   - Document capability limitations
   - Specify expected behaviors
   - Create capability composition mechanisms

Example:
```markdown
## Modular Capability Design

The agent capabilities will follow a modular design with:

1. **Capability Interfaces**:
   ```typescript
   interface AnalysisCapability {
     analyze(content: string, context: AnalysisContext): AnalysisResult;
     supportedContentTypes: string[];
     confidenceLevel(content: string, context: AnalysisContext): number;
     limitationCheck(content: string, context: AnalysisContext): LimitationResult;
   }
   
   interface GenerationCapability {
     generate(parameters: GenerationParameters, context: GenerationContext): GenerationResult;
     supportedOutputTypes: string[];
     iterativeRefine(previous: GenerationResult, feedback: string): GenerationResult;
     validateOutput(result: GenerationResult, criteria: ValidationCriteria): ValidationResult;
   }
   ```

2. **Capability Composition**:
   - Capabilities can be combined through standardized interfaces
   - Specialized capabilities extend base capabilities
   - Capabilities can be conditionally applied based on context
   - Complex workflows combine multiple capabilities

3. **Evolution Strategy**:
   - Each capability has independent versioning
   - Interfaces maintain backward compatibility
   - New capabilities can be added without modifying existing ones
   - Deprecation follows a defined lifecycle
```

### Coherence in Agent System Planning

1. **Maintain consistent interaction patterns**:
   - Plan standardized conversation flows
   - Design consistent response structures
   - Create uniform prompt templates
   - Establish common interaction models

2. **Apply consistent knowledge representation**:
   - Plan uniform knowledge structures across domains
   - Design consistent reference mechanisms
   - Create standardized knowledge formats
   - Establish coherent terminology

3. **Create pattern libraries**:
   - Plan comprehensive pattern documentation
   - Design pattern selection guidance
   - Create pattern variation guidelines
   - Establish pattern governance approaches

Example:
```markdown
## Interaction Pattern Consistency

To ensure coherent interactions, we'll standardize these patterns:

1. **Standard Conversation Flow**:
   ```yaml
   interaction_pattern:
     - phase: "initiation"
       purpose: "Establish context and intent"
       agent_responsibility: "Acknowledge and clarify request"
       human_responsibility: "Provide initial request"
     
     - phase: "exploration"
       purpose: "Gather necessary information"
       agent_responsibility: "Ask clarifying questions, organize information"
       human_responsibility: "Provide details and clarifications"
     
     - phase: "execution"
       purpose: "Complete the requested task"
       agent_responsibility: "Apply relevant capabilities, provide progress updates"
       human_responsibility: "Provide feedback and guidance"
     
     - phase: "verification"
       purpose: "Ensure quality and completeness"
       agent_responsibility: "Self-validate output, highlight assumptions"
       human_responsibility: "Review and provide feedback"
     
     - phase: "refinement"
       purpose: "Improve and finalize output"
       agent_responsibility: "Apply revisions, maintain quality"
       human_responsibility: "Direct revisions, approve final output"
   ```

2. **Response Structure Standards**:
   - All explanations follow the "concept-example-application" pattern
   - Error responses include cause, impact, and resolution suggestions
   - Complex outputs include both summary and detailed sections
   - Uncertainty is explicitly indicated with confidence levels

3. **Pattern Library**:
   - Each pattern documented with purpose, structure, and examples
   - Pattern selection guidance based on context
   - Approved variations for different contexts
   - Pattern effectiveness metrics for continuous improvement
```

### Clarity in Agent System Planning

1. **Create explicit capability documentation**:
   - Plan clear capability descriptions
   - Design concrete usage examples
   - Create detailed limitation documentation
   - Establish explicit usage guidance

2. **Define interaction protocols precisely**:
   - Plan detailed interaction expectations
   - Design clear communication guidelines
   - Create explicit feedback mechanisms
   - Establish unambiguous error handling

3. **Explain agent reasoning**:
   - Plan appropriate transparency levels
   - Design explanation mechanisms
   - Create rationale documentation approaches
   - Establish confidence indication methods

Example:
```markdown
## Capability Documentation Strategy

For each capability, we'll create comprehensive documentation:

1. **Capability Specification**:
   ```yaml
   capability:
     name: "Code Generation Capability"
     purpose: "Generate code based on requirements and context"
     
     inputs:
       - name: "requirements"
         description: "Description of what the code should accomplish"
         type: "string"
         required: true
       
       - name: "language"
         description: "Programming language for generation"
         type: "string"
         required: true
         allowed_values: ["python", "javascript", "typescript", "java"]
       
       - name: "context"
         description: "Additional context about the codebase"
         type: "string"
         required: false
     
     outputs:
       - name: "code"
         description: "Generated code meeting requirements"
         type: "string"
       
       - name: "explanation"
         description: "Explanation of the code implementation"
         type: "string"
       
       - name: "tests"
         description: "Tests for the generated code"
         type: "string"
         optional: true
     
     limitations:
       - "May struggle with complex algorithmic problems"
       - "Cannot access external systems during generation"
       - "Limited to languages in allowed_values"
       - "May need additional context for large projects"
     
     examples:
       - input: |
           requirements: "Create a function that calculates the Fibonacci sequence up to n terms"
           language: "python"
         output: |
           ```python
           def fibonacci(n):
               """
               Generate Fibonacci sequence up to n terms.
               
               Args:
                   n: Number of terms to generate
                   
               Returns:
                   List of Fibonacci numbers
               """
               result = [0, 1]
               for i in range(2, n):
                   result.append(result[i-1] + result[i-2])
               return result[:n]
           ```
   ```

2. **Usage Guidelines**:
   - Clear examples of when to use each capability
   - Step-by-step instructions for common scenarios
   - Troubleshooting guide for common issues
   - Best practices for optimal results

3. **Transparency Mechanisms**:
   - Confidence indicators for generated outputs
   - Explicit reasoning narratives for complex logic
   - Alternative suggestions for uncertain recommendations
   - Source attribution for knowledge-based outputs
```

### Adaptivity in Agent System Planning

1. **Design for context sensitivity**:
   - Plan context detection mechanisms
   - Design contextual response adaptation
   - Create appropriate style variations
   - Establish context-specific interaction models

2. **Prepare for different usage patterns**:
   - Plan adaptations for different user needs
   - Design for varying expertise levels
   - Create domain-specific adaptations
   - Establish task-appropriate behaviors

3. **Enable capability evolution**:
   - Plan incremental improvement mechanisms
   - Design capability experimentation framework
   - Create learning feedback systems
   - Establish capability assessment approaches

Example:
```markdown
## Adaptive Capability Framework

Our capabilities will adapt to different contexts through:

1. **Context Detection**:
   ```yaml
   context_factors:
     user_expertise:
       - beginner: Limited domain knowledge, needs guidance
       - intermediate: Working knowledge, occasional assistance
       - expert: Deep expertise, wants efficiency
     
     task_complexity:
       - simple: Straightforward with clear parameters
       - moderate: Multiple considerations but well-defined
       - complex: Many variables and decision points
     
     interaction_history:
       - new: First-time interaction on topic
       - continuing: Continuation of previous context
       - reference: Referencing established context
     
     domain:
       - technical: Programming, system design, technical documentation
       - process: Workflows, procedures, methodologies
       - creative: Content creation, design, ideation
   ```

2. **Adaptive Responses**:
   - Adjust detail level based on user expertise
   - Modify guidance style for task complexity
   - Maintain appropriate context continuity
   - Adapt terminology to domain context

3. **Learning Mechanisms**:
   - Capture effective adaptations
   - Track adaptation effectiveness
   - Refine context detection rules
   - Improve adaptation selection criteria
```

## Agent System-Specific Planning Artifacts

### Capability Implementation Plan

Detail how capabilities will be implemented:

```markdown
## Capability Implementation Plan

### Implementation Strategy
- **Approach**: [Overall implementation approach]
- **Principles**: [Guiding implementation principles]
- **Success Criteria**: [How implementation success will be measured]
- **Key Challenges**: [Anticipated implementation challenges]

### Capability Roadmap
- **Phase 1: [Phase Name]**
  - **Duration**: [Estimated duration]
  - **Focus**: [Primary focus of this phase]
  - **Capabilities**: [Capabilities to be implemented]
  - **Dependencies**: [Critical dependencies]
  - **Success Metrics**: [How success will be measured]
  - **Risks**: [Phase-specific risks]

- **Phase 2: [Phase Name]**
  - [Phase details...]

### Knowledge Integration
- **Knowledge Sources**: [Where knowledge will come from]
- **Integration Approach**: [How knowledge will be integrated]
- **Verification Method**: [How knowledge will be verified]
- **Maintenance Strategy**: [How knowledge will be maintained]

### Evaluation Framework
- **Testing Approach**: [How capabilities will be tested]
- **Scenario Coverage**: [Key scenarios for validation]
- **Performance Metrics**: [How performance will be measured]
- **Quality Standards**: [Quality requirements]
```

### Capability Specifications

Provide detailed capability specifications:

```markdown
## Capability Specifications

### [Capability Name]

#### Purpose and Scope
- **Primary Purpose**: [The main function of this capability]
- **Key Features**: [Important aspects of this capability]
- **Use Cases**: [When this capability should be used]
- **Success Criteria**: [How effectiveness will be measured]

#### Implementation Details
- **Approach**: [How the capability will be implemented]
- **Components**:
  - **Component 1**: [Purpose and function]
  - **Component 2**: [Purpose and function]
  - **Component 3**: [Purpose and function]

- **Knowledge Requirements**:
  - **Domain 1**: [Required knowledge]
  - **Domain 2**: [Required knowledge]
  - **Domain 3**: [Required knowledge]

#### Interface Specification
- **Inputs**:
  - **Input 1**: [Description, type, constraints]
  - **Input 2**: [Description, type, constraints]
  - **Input 3**: [Description, type, constraints]

- **Outputs**:
  - **Output 1**: [Description, type, format]
  - **Output 2**: [Description, type, format]
  - **Output 3**: [Description, type, format]

- **Behavior**:
  - **Normal Operation**: [Expected behavior]
  - **Edge Cases**: [Behavior in edge cases]
  - **Error Handling**: [How errors are handled]
  - **Performance Characteristics**: [Expected performance]

#### Implementation Guidelines
- **Best Practices**: [Recommendations for implementation]
- **Common Pitfalls**: [Issues to avoid]
- **Quality Considerations**: [Quality factors to address]
- **Testing Approach**: [How to test this capability]
```

### Interaction Pattern Specifications

Detail interaction pattern designs:

```markdown
## Interaction Pattern Specifications

### [Pattern Name]

#### Purpose and Context
- **Primary Purpose**: [The main function of this pattern]
- **Usage Context**: [When this pattern should be used]
- **User Needs Addressed**: [What user needs it satisfies]
- **Alternatives**: [Alternative patterns for comparison]

#### Pattern Structure
- **Initiation**: [How the interaction begins]
  - **Trigger**: [What initiates this pattern]
  - **Initial Response**: [How the agent responds]
  - **Context Establishment**: [How context is established]

- **Core Interaction**:
  - **Phase 1**: [Description of first interaction phase]
  - **Phase 2**: [Description of second interaction phase]
  - **Phase 3**: [Description of third interaction phase]

- **Conclusion**:
  - **Resolution**: [How the interaction concludes]
  - **Follow-up**: [Any follow-up actions]
  - **Transition**: [Potential transitions to other patterns]

#### Prompt Templates
- **Initial Prompt Template**:
  ```
  [Template for initiating this interaction pattern]
  ```

- **Intermediate Prompt Templates**:
  ```
  [Templates for middle stages of interaction]
  ```

- **Conclusion Prompt Template**:
  ```
  [Template for concluding the interaction]
  ```

#### Response Guidelines
- **Style and Tone**: [Appropriate style for this pattern]
- **Level of Detail**: [How detailed responses should be]
- **Structure Requirements**: [How responses should be structured]
- **Adaptations**: [How responses adapt to context]

#### Example Dialog
- **Example 1**:
  - Human: "[Example user input]"
  - AI: "[Example agent response]"
  - Human: "[Follow-up input]"
  - AI: "[Follow-up response]"

- **Example 2**:
  - [Additional dialog example]
```

### Evaluation Scenario Specifications

Detail evaluation scenarios:

```markdown
## Evaluation Scenario Specifications

### [Scenario Name]

#### Scenario Overview
- **Purpose**: [What this scenario evaluates]
- **Capabilities Tested**: [Capabilities being assessed]
- **Context**: [Relevant context for the scenario]
- **Difficulty Level**: [Easy/Medium/Hard]

#### Scenario Setup
- **Initial State**: [Starting conditions]
- **User Profile**: [Characteristics of the user]
- **Task Description**: [What the user is trying to accomplish]
- **Available Information**: [What information is available]
- **Constraints**: [Any limitations or constraints]

#### Expected Behavior
- **Key Steps**:
  - **Step 1**: [Expected agent behavior]
  - **Step 2**: [Expected agent behavior]
  - **Step 3**: [Expected agent behavior]

- **Decision Points**:
  - **Decision 1**: [Decision to be made and criteria]
  - **Decision 2**: [Decision to be made and criteria]
  - **Decision 3**: [Decision to be made and criteria]

#### Success Criteria
- **Must Have**:
  - [Essential criteria that must be met]
  - [Essential criteria that must be met]
  - [Essential criteria that must be met]

- **Should Have**:
  - [Important but not essential criteria]
  - [Important but not essential criteria]
  - [Important but not essential criteria]

- **Could Have**:
  - [Desirable but optional criteria]
  - [Desirable but optional criteria]
  - [Desirable but optional criteria]

#### Evaluation Method
- **Testing Approach**: [How the scenario will be tested]
- **Metrics**: [Specific measurements to capture]
- **Scoring System**: [How performance will be scored]
- **Benchmark Comparison**: [What the results will be compared to]
```

## Release Scope-Specific Planning

### Major Agent System Planning
- Comprehensive capability enhancement planning
- Detailed knowledge domain development
- Thorough interaction pattern design
- Extensive collaboration model refinement
- Comprehensive evaluation framework
- Detailed risk and limitation assessment
- Extensive training and documentation

### Minor Agent System Planning
- Focused capability enhancements
- Targeted knowledge domain extensions
- Specific interaction pattern improvements
- Moderate collaboration model adjustments
- Standard evaluation approach
- Focused risk assessment
- Appropriate training updates

### Patch Agent System Planning
- Specific capability improvements
- Limited knowledge domain updates
- Minimal interaction pattern refinements
- Minor collaboration model adjustments
- Basic evaluation approach
- Targeted risk assessment
- Notification-based guidance updates

### Emergency Agent System Planning
- Critical capability fixes only
- Essential knowledge corrections
- Necessary interaction adjustments
- Minimal collaboration changes
- Focused evaluation on critical paths
- Risk assessment for critical areas
- Just-in-time guidance updates

## Agent System Planning Checklist

Before concluding the planning phase, verify that:

- [ ] All capability enhancements are clearly defined
- [ ] Knowledge domain planning is comprehensive
- [ ] Interaction patterns are well-specified
- [ ] Collaboration model is clearly defined
- [ ] Evaluation scenarios cover all capabilities
- [ ] Risks and limitations are identified with mitigations
- [ ] Implementation approach is appropriate and realistic
- [ ] Success criteria are specific and measurable
- [ ] Dependencies are identified and managed
- [ ] Meta-systemic principles have been applied appropriately

## Human-AI Collaboration in Planning

In our two-person team:

### Human Team Member Focus
- Defining capability requirements and priorities
- Evaluating knowledge domain boundaries
- Setting interaction pattern principles
- Establishing collaboration model framework
- Assessing risks and limitations
- Setting implementation priorities
- Making key design decisions

### AI Agent Focus
- Developing detailed capability specifications
- Creating comprehensive knowledge domain maps
- Designing detailed interaction patterns
- Documenting collaboration workflows
- Generating evaluation scenarios
- Ensuring consistent pattern application
- Maintaining planning document integrity

<important>
The agent system planning phase establishes the foundation for effective capability enhancements. Be thorough in defining capabilities, knowledge domains, and interaction patterns to ensure successful implementation and adoption.
</important>