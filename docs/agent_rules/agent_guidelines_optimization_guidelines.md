# Enhanced Framework for Effective Cursor Rule Application

This framework is designed to help you (or an LLM agent) craft and maintain Cursor rule files (.mdc) so that they are consistently applied, maintainable, and tailored to your project’s needs. This revision incorporates extra guidance that encourages the LLM to produce rules that are modular, self-contained, and performance‑aware.

---

## 1. Metadata and File Recognition

### YAML Front Matter
- **Mandatory Fields:**  
  Every rule file must begin with a YAML front matter block. At minimum, include:
  - **description:** A brief, agent‑friendly summary of the rule’s purpose.
  - **globs:** A glob pattern (e.g., `"*"` for global application or a more specific pattern) that determines when the rule should be injected.
  - **alwaysApply:** A boolean flag that, if true, enforces unconditional injection.
  
  **Example:**
  ```yaml
  ---
  description: "Agent guidelines for using Tailwind CSS styling"
  globs: "src/**/*.css"
  alwaysApply: false
  ---
  ```

### File Extension
- **Use `.mdc` Extension:**  
  Rename your rule files to have a `.mdc` extension (instead of `.md`) and store them in the `.cursor/rules` directory. This ensures Cursor recognizes and loads them automatically.

---

## 2. Rule Type Setting

The “rule type” setting refines how and when a rule is injected. In the Cursor rule editor, you’ll see a dropdown with four options:

- **Manual:**  
  - **Definition:** The rule is not attached automatically.
  - **Usage:** It must be explicitly referenced (e.g., via an `@` mention) in the conversation.
  - **When to Use:** For guidelines that should be considered only upon direct request.

- **Agent Requested:**  
  - **Definition:** The agent sees a brief description of the rule and may choose to fetch and include the full rule if it deems the rule relevant.
  - **Usage:** Typically leave the globs field empty so that the decision is driven solely by the description.
  - **When to Use:** For rules that are potentially useful in certain contexts but should not be auto‑attached.
  - **Example Descriptions:**  
    - *"USE WHEN processing database queries: Ensure all SQL statements are parameterized to mitigate injection risks."*  
    - *"USE WHEN handling API requests: Validate that API keys are loaded securely from environment variables rather than hard-coded."*  
    - *"USE WHEN compiling frontend code: Confirm that React components are using hooks (not class components) for state management."*

- **Auto Attached:**  
  - **Definition:** The rule is automatically added to the context when a file mentioned in the conversation matches the rule’s glob pattern.
  - **Usage:** Requires specifying concrete file patterns in the **globs** field.
  - **When to Use:** For file‑ or directory‑specific guidelines.
  - **Example Patterns:**  
    - **TypeScript Files:**  
      `**/*.ts,**/*.tsx` – Applies when any TypeScript file in the project is active.
    - **HTML Files:**  
      `public/**/*.html` – Applies to HTML files in the public folder.
    - **CSS Files:**  
      `src/**/*.css` – Attaches styling guidelines when a CSS file in `src` is edited.
    - **Documentation Files:**  
      `docs/**/*.md` – Applies to markdown documentation.

- **Always:**  
  - **Definition:** The rule is attached to every chat and every Command+K session without exception.
  - **Usage:** Its content is always available regardless of the current context.
  - **When to Use:** For essential, high‑priority guidelines that must consistently influence the AI’s behavior.

---

## 3. Glob Patterns and Scope

- **Define the Context:**  
  Use the **globs** field to specify exactly which files or directories the rule should apply to. For a global rule, use `"*"` and consider setting `alwaysApply: true`.

- **Avoid Unintended Matches:**  
  For rules targeting specific file types, make your glob patterns as specific as possible. For example, use `"src/**/*.ts"` instead of a broader pattern.

- **Combine with Rule Type:**  
  Note that the **Auto Attached** rule type uses these glob patterns to trigger automatic inclusion, whereas **Agent Requested** or **Manual** rules typically have empty globs.

---

## 4. Content Clarity and Formatting

- **Structured Layout:**  
  Organize rule content with clear headings and bullet lists. Divide the content into sections such as **Context**, **Requirements**, and **Examples**.

- **Actionable Directives:**  
  Write in clear, imperative language (e.g., “ALWAYS use…”, “DO NOT…”). This minimizes ambiguity and ensures both the AI and human maintainers understand the rule.

- **Self-Contained Explanations:**  
  Each rule should include a short summary that explains the intended effect, potential edge cases, and when it should be triggered.  
  *Enhancement for LLM Agents:*  
  Encourage the agent to include a brief "Trigger Condition" in the description (e.g., "USE WHEN file changes involve backend queries").

- **Minimal Overhead:**  
  Keep rules concise to reduce token usage, yet ensure they are detailed enough to be actionable.

- **Optional Inline Tags:**  
  You may include inline labels (e.g., `[AGENT]`, `[STYLE]`) to further indicate the rule’s purpose, though the rule type setting should be the primary indicator.

---

## 5. Prioritization and Conflict Resolution

- **Assign Priorities:**  
  If supported, assign numerical priorities to ensure that critical rules take precedence over advisory ones.  
  *Enhancement for LLM Agents:*  
  Instruct the agent to suggest a priority level based on the rule’s criticality (e.g., "priority: high" for security-related rules).

- **Avoid Overlap:**  
  Ensure similar rules do not conflict by clearly differentiating their scopes using specific glob patterns and distinct rule type settings.

- **Document Intent:**  
  Include version numbers or a brief changelog (within comments or a separate document) to track modifications over time.

---

## 6. Testing and Verification

- **Automatic Verification:**  
  Confirm that your rule files are loaded by checking the “Attach Rules” interface in Cursor. For example, open a new chat and verify that rules set to Always or Auto Attached appear.

- **Scenario Testing:**  
  - For **Auto Attached** rules: Open or modify a file that matches the glob pattern (e.g., a `.ts` file in `src`) and verify the rule is injected.
  - For **Agent Requested** rules: Pose queries that should trigger the rule based on its description, then check that the agent fetches the rule when applicable.
  - For **Manual** rules: Explicitly reference the rule (e.g., using an `@` mention) and ensure it is included.

- **Feedback Loop:**  
  Monitor the agent’s responses to ensure the rule’s intended behavior is reflected. If the AI isn’t selecting the rule appropriately, adjust the description or rule type.

- **Performance Considerations:**  
  Encourage the agent to keep rules succinct and to minimize extraneous text, ensuring that essential rules do not overload the context window.

---

## 7. Continuous Improvement and Documentation

- **Versioning:**  
  Track changes over time by updating version numbers or maintaining a changelog for your rule files, allowing for rollbacks or comparisons.

- **Regular Reviews:**  
  Periodically review your rule set to remove redundant or obsolete rules and consolidate overlapping ones.

- **Dual Documentation:**  
  Maintain two layers:
  - **AI-Focused Rules:** Lean, directly actionable rules for the agent.
  - **Developer Documentation:** Expanded explanations and rationale behind each rule for human maintainers.

- **LLM Agent Prompts for Rule Creation:**  
  Provide sample prompts or meta-instructions for the agent to follow when generating new rules. For example:
  - *"Based on the current codebase context, create a rule that enforces secure API key handling. The rule should include a clear trigger condition and specify that it is Agent Requested with an example description."*
  
- **Community Collaboration:**  
  Engage with the Cursor community (via forums or Reddit) to learn from others’ experiences and incorporate best practices as the system evolves.

---

## 8. Enhancements Specific to LLM Agent Effectiveness

To maximize the likelihood that an LLM agent creates highly effective Cursor rules, consider incorporating the following enhancements:
  
- **Modularity and Composability:**  
  Instruct the agent to create rules that are self-contained and modular. Rules should focus on a single concern and be easily composed with others.  
  *Example Instruction:* "Design this rule so it addresses only SQL query parameterization without mixing in unrelated security guidelines."

- **Self-Check and Trigger Conditions:**  
  Require that each rule includes a brief "Trigger Condition" or “Usage Scenario” in its description. This helps the agent decide when to attach the rule.  
  *Example:* "USE WHEN handling user login requests: Validate that passwords are not logged in plain text."

- **Prioritization Guidance:**  
  Encourage the agent to assign a priority level based on the rule’s criticality (e.g., "priority: high" for security rules or "priority: low" for stylistic suggestions).

- **Performance and Context Efficiency:**  
  Emphasize the need for brevity. The agent should remove any nonessential text to minimize token overhead while preserving actionable detail.

- **Dual-Layer Documentation:**  
  Instruct the agent to generate a short summary for the rule (for the AI’s context) and a more detailed explanation for human maintainers.  
  *Example:* "Provide a one-sentence summary for quick agent reference and a two‑to‑three sentence explanation for developer documentation."

- **Consistency in Formatting:**  
  Reinforce the importance of a consistent structure across all rules. This includes using the same format for frontmatter, a consistent style in descriptions, and standardized examples.

- **Testable Conditions:**  
  Ask the agent to include, where applicable, examples or simple test cases (as inline comments) that illustrate when the rule should be triggered. This helps in verifying the rule’s effectiveness later.

---

## Conclusion

This enhanced framework provides comprehensive, explicit guidance for developing and managing Cursor rule files. By ensuring proper metadata, carefully defining glob patterns, selecting the appropriate rule type (Manual, Agent Requested, Auto Attached, or Always), and incorporating enhancements specific to LLM agent effectiveness, you can fine-tune which rules are injected into the AI’s context and when. The framework’s added emphasis on modularity, self-check guidance, performance considerations, and dual-layer documentation ensures that both the AI and human developers can benefit from clear, actionable, and efficient rules.

With these best practices in place, your Cursor rules will be robust, easier to manage, and will effectively steer the AI’s behavior according to your project’s specific requirements.
