---
description: 
globs: /evaluation/*.md,**/evaluation/*.mdx,**/releases/*/evaluation.md,**/releases/*/evaluation.mdx
alwaysApply: false
---
---
description: "Core guidance for the post-release evaluation phase of the release lifecycle"
globs: "**/evaluation/*.md,**/evaluation/*.mdx,**/releases/*/evaluation.md,**/releases/*/evaluation.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Post-Release Evaluation Phase Guidance

<critical>
The post-release evaluation phase is essential for continuous improvement. During this phase, analyze outcomes, capture learnings, and identify improvements to enhance both the product and the release process itself.
</critical>

## Core Evaluation Activities

The post-release evaluation phase consists of these essential activities:

1. **Success Assessment**: Evaluate achievement of release objectives and business outcomes
2. **Process Reflection**: Analyze effectiveness of the release process and meta-systemic principles
3. **Learning Capture**: Document insights and knowledge gained during the release
4. **Metric Analysis**: Collect and analyze performance and quality metrics
5. **Improvement Planning**: Identify specific improvements for future releases

## Evaluation Approach

Structure your post-release evaluation as follows:

### 1. Scheduling and Preparation

Plan the evaluation after sufficient operational experience:

```markdown
## Evaluation Planning

### Timing
- Schedule evaluation 1-4 weeks after deployment (based on release scope)
- Allow sufficient time for operational metrics to accumulate
- Complete before planning for next release begins

### Preparation
- Gather metrics from monitoring systems
- Collect feedback from users and stakeholders
- Compile development and release process data
- Review original release objectives and requirements
- Prepare validation results for reference

### Participants
- Release owner/manager
- Key developers and technical contributors
- QA and validation representatives
- Operations/support representatives
- Key stakeholders and user representatives
```

### 2. Success Assessment

Evaluate achievement of release objectives:

```markdown
## Success Assessment

### Objective Achievement
- Evaluate each defined objective against measurable criteria
- Determine if targets were met, exceeded, or missed
- Identify factors contributing to success or shortfall
- Document evidence supporting the assessment

### Business Impact
- Measure actual business impact against expectations
- Evaluate user adoption and satisfaction
- Assess operational impact (efficiency, reliability, etc.)
- Identify unexpected outcomes (positive or negative)

### Stakeholder Feedback
- Gather feedback from key stakeholders
- Compare perception of success with metric-based assessment
- Identify perception gaps for further analysis
- Document qualitative feedback on value delivered
```

### 3. Process Reflection

Analyze the effectiveness of the release process:

```markdown
## Process Reflection

### Phase Analysis
- Evaluate effectiveness of each lifecycle phase
- Identify phases that worked particularly well
- Highlight phases with challenges or inefficiencies
- Analyze phase transitions and handoffs

### Meta-Systemic Principle Application
- Assess application of each principle throughout the release
- Identify principle tensions and resolution effectiveness
- Evaluate principle balance for the specific context
- Determine which principles provided the most value

### Timeline and Resource Analysis
- Compare actual timeline with planned timeline
- Assess resource utilization efficiency
- Identify bottlenecks and constraints
- Evaluate estimation accuracy
```

### 4. Success Factors and Challenges

Document what worked well and what didn't:

```markdown
## Success Factors and Challenges

### Key Success Factors
- Identify specific practices that contributed to success
- Document effective approaches for replication
- Analyze why these practices were effective
- Highlight innovations and improvements from previous releases

### Key Challenges
- Document significant challenges encountered
- Analyze root causes of issues
- Evaluate effectiveness of mitigations
- Identify systemic issues versus one-time problems

### Risk Management Review
- Assess accuracy of risk identification
- Evaluate effectiveness of mitigation strategies
- Identify unpredicted risks that emerged
- Document risk management learnings
```

### 5. Metric Analysis

Compile and analyze key metrics:

```markdown
## Metric Analysis

### Performance Metrics
- Compile technical performance data
- Compare with baseline and targets
- Analyze trends and patterns
- Identify areas for optimization

### Quality Metrics
- Analyze defect rates and types
- Evaluate testing effectiveness
- Assess stability and reliability
- Document quality trends compared to previous releases

### Process Metrics
- Measure development velocity and efficiency
- Assess documentation completeness
- Evaluate validation coverage and effectiveness
- Compare with process targets and previous releases

### User Impact Metrics
- Analyze user adoption and engagement
- Measure user-reported issues
- Evaluate user satisfaction
- Document operational impact
```

### 6. Learning Capture

Document key insights and knowledge gained:

```markdown
## Learning Capture

### Technical Learnings
- Document key technical insights
- Capture architectural and design learnings
- Record implementation challenges and solutions
- Identify knowledge gaps and areas for research

### Process Learnings
- Document effective process adaptations
- Capture planning and coordination insights
- Record validation approach effectiveness
- Identify process inefficiencies and bottlenecks

### Team Learnings
- Document collaboration effectiveness
- Capture communication insights
- Record workload and resource allocation learnings
- Identify team dynamics observations
```

### 7. Improvement Planning

Identify specific actions for future improvement:

```markdown
## Improvement Planning

### Process Improvements
- Identify specific process changes needed
- Prioritize improvements based on impact
- Assign ownership for implementation
- Establish timeline for adoption

### Technical Improvements
- Identify architectural or design improvements
- Document technical debt to be addressed
- Prioritize based on impact and urgency
- Create action plan for implementation

### Knowledge and Capability Improvements
- Identify training or knowledge sharing needs
- Document tooling or infrastructure improvements
- Specify documentation enhancements
- Establish plan for capability development
```

### 8. Final Assessment and Recommendations

Summarize evaluation and provide recommendations:

```markdown
## Final Assessment and Recommendations

### Overall Assessment
- Provide holistic evaluation of release success
- Highlight key strengths and weaknesses
- Summarize principle application effectiveness
- Document overall progress compared to previous releases

### Key Recommendations
- Identify 3-5 highest priority improvements
- Provide clear, actionable next steps
- Highlight recommendations for next release
- Define success criteria for improvements

### Knowledge Sharing Plan
- Define approach for sharing learnings
- Identify key insights for broader distribution
- Specify documentation updates needed
- Establish knowledge integration timeline
```

## Meta-Systemic Principle Application

### Parsimony
- Reference existing documents rather than duplicating content
- Maintain single source of truth for metrics and findings
- Link to detailed data rather than including it all
- Focus on unique insights rather than repeating known information

Example:
```markdown
## Performance Metric Analysis

The complete performance metrics are available in the @Performance Monitoring Dashboard. This evaluation focuses on the key insights derived from those metrics rather than reproducing all the data.

Key metrics referenced:
- Search latency (P95): 187ms vs. 250ms baseline
- Query throughput: 250 qps vs. 200 qps baseline
- Error rate: 0.05% vs. 0.25% baseline
```

### Tensegrity
- Connect evaluation findings to release objectives
- Link process observations to specific implementation decisions
- Establish clear relationships between findings and action items
- Create balanced assessment across all release aspects

Example:
```markdown
## Finding-to-Action Mapping

| Finding | Source Data | Resulting Action |
|---------|-------------|------------------|
| Query parser performance exceeded expectations | Performance metrics, code review | Document the optimization techniques for future reference |
| Validation process had excessive manual steps | Process metrics, team feedback | Enhance test automation for admin interfaces (AP-002) |
| Error handling inconsistency affected quality | Code review, incident reports | Standardize error handling patterns (AP-003) |
```

### Modularity
- Organize evaluation by distinct sections
- Separate objective assessment from process evaluation
- Create clear boundaries between different types of reflection
- Enable independent consumption of different evaluation components

Example:
```markdown
## Evaluation Structure

This evaluation is organized into modules that can be reviewed independently:

1. **Success Assessment**: Focuses on business outcomes and goal achievement
2. **Process Evaluation**: Examines the effectiveness of the release process
3. **Metric Analysis**: Reviews quantitative performance and quality data
4. **Improvement Planning**: Provides specific recommendations for future releases

Each section can be consumed independently while the final assessment brings all insights together.
```

### Coherence
- Follow consistent evaluation patterns
- Use standard metrics and evaluation approaches
- Apply consistent reflection structure
- Maintain coherent format across evaluation documents

Example:
```markdown
This evaluation follows our standard reflection structure and applies consistent evaluation criteria across all aspects of the release. We use the same metrics and evaluation approaches as previous releases to enable trend analysis and comparison.
```

### Clarity
- Provide explicit assessment of success and challenges
- Include concrete examples of learnings
- Use visual elements to highlight key metrics and trends
- Explain action items with clear responsibilities

Example:
```markdown
### Success Example: Semantic Search Implementation

The semantic search implementation demonstrates a clear success:

**Approach:**
- Started with focused prototype to validate approach
- Used incremental implementation with weekly review
- Applied pair programming for complex algorithms
- Conducted progressive performance optimization

**Results:**
- 35% relevance improvement (exceeding 30% target)
- 25% latency reduction (exceeding 20% target)
- Clean integration with existing components
- Positive user feedback (88% satisfaction)

**Key Learning:**
Prototyping complex features before full implementation significantly reduces risk and improves quality.
```

### Adaptivity
- Scale evaluation depth to release complexity
- Adapt reflection focus to release type
- Apply appropriate analysis detail based on release scope
- Adjust action item scope based on findings

Example:
```markdown
## Adaptive Evaluation Approach

This evaluation applies our adaptive reflection framework based on:
- Release classification (Minor)
- Component significance (Search is business-critical)
- Process maturity (Established)
- Team experience (Mixed experience with search technology)

Based on these factors, we focused on:
- Deep technical reflection for search components
- Standard process evaluation
- Targeted action items for specific improvement areas
- Knowledge capture for search implementation
```

## Context-Specific Evaluation Approaches

### For Code System Evaluation
- Focus on technical implementation and architecture
- Evaluate code quality and technical debt
- Assess performance and stability metrics
- Analyze user-facing features and user experience
- Review technical documentation quality

Example approaches:
- Technical retrospectives with development team
- Architecture review sessions
- Performance analysis against baselines
- User experience reviews
- Code quality metric analysis

### For Release System Evaluation
- Focus on process effectiveness and efficiency
- Evaluate artifact quality and completeness
- Assess phase transitions and handoffs
- Analyze meta-process metrics
- Review guidance and rule effectiveness

Example approaches:
- Process retrospectives with all stakeholders
- Artifact quality reviews
- Phase effectiveness analysis
- Rule application assessment
- Template effectiveness evaluation

### For Agent System Evaluation
- Focus on agent capability effectiveness
- Evaluate interaction pattern quality
- Assess knowledge application accuracy
- Analyze collaboration effectiveness
- Review guidance quality and adaptivity

Example approaches:
- Capability effectiveness reviews
- Interaction pattern analysis
- Knowledge domain evaluations
- Collaboration model assessment
- Example-based capability validation

## Release Scope-Specific Considerations

### Major Release Evaluation
- Comprehensive evaluation of all release aspects
- In-depth analysis of principle application
- Broad stakeholder involvement
- Extensive metric collection and analysis
- Comprehensive improvement planning
- Formal knowledge capture and distribution

### Minor Release Evaluation
- Focused evaluation on key release aspects
- Standard analysis of principle application
- Key stakeholder involvement
- Core metric collection and analysis
- Targeted improvement planning
- Streamlined knowledge capture

### Patch Release Evaluation
- Limited evaluation of specific fixes/changes
- Abbreviated principle application assessment
- Minimal stakeholder involvement
- Basic metric collection
- Issue-specific improvement planning
- Focused knowledge capture for affected areas

### Emergency Release Evaluation
- Rapid post-incident analysis
- Focus on response effectiveness
- Response team involvement
- Critical path metrics only
- Prevention-focused improvement planning
- Incident-specific knowledge capture

## Evaluation Phase Quality Checklist

Before concluding the evaluation phase, verify that:

- [ ] All release objectives have been assessed
- [ ] Process effectiveness has been evaluated for all phases
- [ ] Meta-systemic principle application has been analyzed
- [ ] Key success factors and challenges have been documented
- [ ] Relevant metrics have been collected and analyzed
- [ ] Key learnings have been captured
- [ ] Specific improvement actions have been identified
- [ ] Responsibilities have been assigned for improvements
- [ ] Final assessment and recommendations are clear
- [ ] Knowledge sharing plan has been established

## Human-AI Collaboration in Evaluation

In our two-person team:

### Human Team Member Focus
- Making value judgments about success
- Providing experiential insights about process
- Evaluating stakeholder satisfaction
- Prioritizing improvement areas
- Making context-sensitive assessments

### AI Agent Focus
- Analyzing metrics and identifying patterns
- Ensuring comprehensive coverage of all aspects
- Maintaining consistent evaluation structure
- Documenting findings systematically
- Connecting findings to meta-systemic principles

<important>
The post-release evaluation phase closes the feedback loop and enables continuous improvement. Focus on honest assessment, actionable insights, and specific recommendations to ensure that each release builds upon the learnings of previous ones.
</important>