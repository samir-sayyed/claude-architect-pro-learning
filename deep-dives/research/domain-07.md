# Domain 7 research and verification

Research checked: **2026-10-13**. Scope: the three supplied Domain 7 objectives,
practical team enablement first, original exam-style reasoning checks second.
Primary sources only. All links below were opened and the relevant passages read.
Vendor documentation is mutable; these are documented capabilities on the review
date, not a claim that every installed release implements the same behavior.

## Evidence used

| ID | Primary source | Finding actually used |
| --- | --- | --- |
| D7-S01 | [Settings and precedence](https://code.claude.com/docs/en/settings) | Ordinary stack: managed, session --settings, project-local, shared project, user. Lists merge. Environment-variable interactions are key-specific. /status shows loaded sources, not full per-key provenance. |
| D7-S02 | [Project memory](https://code.claude.com/docs/en/memory) | CLAUDE.md is behavioral context, not hard enforcement. |
| D7-S03 | [Permissions](https://code.claude.com/docs/en/permissions) | Deny before ask before allow. Rules combine across settings scopes. Arbitrary scripts can read files indirectly, so file-tool permissions are not comprehensive process isolation. |
| D7-S04 | [Hooks reference](https://code.claude.com/docs/en/hooks) | PreToolUse exit 2 blocks the proposed call. PostToolUse cannot undo an executed effect. Async command hooks cannot block via decision fields. Exit behavior is event-specific; PermissionRequest requires structured denial. |
| D7-S05 | [Skills](https://code.claude.com/docs/en/skills) | Descriptions support discovery; detailed content loads on invocation. allowed-tools pre-approves for the invoking turn, rather than restricting all available tools. Managed controls can limit grants. |
| D7-S06 | [MCP connections](https://code.claude.com/docs/en/mcp) | MCP local scope is in the project entry of ~/.claude.json; project scope uses .mcp.json; user scope applies across projects. This differs from ordinary settings scope. |
| D7-S07 | [Sandboxing](https://code.claude.com/docs/en/sandboxing) | Shell-command sandboxing is an OS boundary for covered commands. Built-in file tools, local MCP servers and hooks are outside that shell sandbox. Platform support differs. |
| D7-S08 | [Development containers](https://code.claude.com/docs/en/devcontainer) | First-party reproducible development-container workflow exists; actual mounts, privilege and network determine its isolation. |
| D7-S09 | [GitHub Actions](https://code.claude.com/docs/en/github-actions) | First-party CI integration exists. It runs in a runner context rather than inheriting the developer's whole laptop environment. |
| D7-S10 | [GitHub secure use](https://docs.github.com/en/actions/reference/security/secure-use) | Untrusted workflow input, permissions and secrets need explicit controls. |
| D7-S11 | [Best practices](https://code.claude.com/docs/en/best-practices) | Give the agent observable verification evidence; exploration and independent review are useful workflow practices. |
| D7-S12 | [Common workflows](https://code.claude.com/docs/en/common-workflows) | Worktrees separate checkouts/branches. Plan-first and verifiable workflows are documented. A worktree is not an OS or external-service security boundary. |
| D7-S13 | [METR July 2025 experiment](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) | 16 experienced developers, 246 real tasks, randomized AI allowance; early-2025 assistance produced 19% longer completion in that setting. Authors explicitly limit generalization. |
| D7-S14 | [METR February 2026 update](https://metr.org/blog/2026-02-24-uplift-update/) | Later estimates suggest possible acceleration, but task/developer selection and time measurement limit effect-size inference. The update is not a universal productivity guarantee. |
| D7-S15 | [DORA 2025 report page](https://dora.dev/research/2025/dora-report/) | The report describes AI as amplifying existing organizational strengths and weaknesses. No universal causal speedup percentage is inferred. |
| D7-S16 | [Claude API errors](https://platform.claude.com/docs/en/api/errors) | Error categories and request IDs support diagnosis; streaming errors can arrive after initial HTTP success. |
| D7-S17 | [Monitoring](https://code.claude.com/docs/en/monitoring-usage) | OpenTelemetry correlation includes prompt.id. Content logging has separate controls and can expose private context. Exporter field details are version-dependent. |
| D7-S18 | [Troubleshooting](https://code.claude.com/docs/en/troubleshooting) | claude doctor and /mcp aid setup checks. A heap snapshot can contain full conversation strings and credentials; exclude it from public support bundles. |
| D7-S19 | [MCP authorization, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) | HTTP resource servers must validate intended token audience. |
| D7-S20 | [MCP security, 2026-07-28](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) | Token passthrough is prohibited; audience mistakes and confused-deputy behavior are concrete risks. |
| D7-S21 | [Managed settings](https://code.claude.com/docs/en/managed-settings) | Organization policies have distinct delivery surfaces. Device files are not automatically present in a hosted runner; administrators must verify enforcement. |

## Original teaching material and limits

- NutriMind, Quiet Hours and marketplace cases are **proposed design exercises**,
  not assertions about those repositories' current implementations or test commands.
- Provider charge and booking examples are fictional. Actual provider idempotency,
  retention, retry and reconciliation contracts must be checked before integration.
- The offline Python lab demonstrates a lost reply after commit and a fresh-key
  retry defect. It is single-process and in-memory, explicitly unsuitable as a
  production payment implementation. It does not establish durability, atomic
  concurrent admission, provider guarantees or cross-process correctness.
- Settings JSON is a reviewed inert example, not installed policy or a comprehensive
  security profile. Strict JSON parsing is checked locally. Live Claude Code policy
  behavior has not been executed in this environment; it must be verified on the
  team's installed release and execution surfaces.
- Diagram sequences, task contracts, worksheets, cases, arithmetic and ten checks
  are original. No live exam questions or purported recalled items were used.
- This module targets the supplied three guide objectives. The parent task rereads
  the user's attached official exam guide; this research file does not claim an
  independently measured live-exam difficulty or pass prediction.

## Local verification

- `python3 templates/domain-07/lab.py buggy`: expected nonzero assertion, exactly
  three provider charges for one logical intent.
- `python3 templates/domain-07/lab.py fixed`: all four named checks pass.
- Lab reject cases: changed amount causes no side effect; distinct tenant is
  independent; zero, negative, fractional and boolean money values are rejected.
- JSON data parsed; 10 sections, 7 diagrams, 10 four-option checks, 21 unique sources,
  3 objectives and 12 glossary terms. Every check has four option-specific rationales.
- Teaching math: implementation reduction `(70-45)/70 = 35.71%`; total effort
  reduction `(90-85)/90 = 5.56%`. Values are labeled illustrative, not empirical.
- Parent handles shared rendering, navigation, full-site validation and browser review.
