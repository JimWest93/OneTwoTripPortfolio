[RU](../../ru/cases/engineering-workflow.md) · [Language selection](../../../README.md)

# Documentation, AI tools and engineering workflow

**2026 · OneTwoTrip / iOS**

I developed repeatable workflows for systems analysis, module documentation and preparing changes.

## Context

In a large modular codebase, progress depends on context: public contracts, feature entry points, available tests and current requirements. I began formalizing that context in documentation and tools.

## My contribution

- Developed and refined a skill for turning systems analysis into a mobile story, including a shared process for iOS and Android.
- Created a process for preparing and incrementally updating Tuist-module READMEs to reflect entry points, configuration, dependencies and checks.
- Added documentation for eSIM and Stories modules, connecting descriptions to code and tests.
- Used AI agents for research, implementation and verification, documenting the extent of their assistance in review descriptions.
- Contributed to OTT, Solar and KZ release changes: configuration, product differences and integration checks.

## Technologies

Codex, Repository skills, Jira / Bitbucket integrations, Markdown, Tuist manifests, Ruby / Python tooling, Git / release workflow.

## Practical examples

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| From analysis to a task | Developed and refined a workflow that turns systems analysis into mobile stories. | Formalizing input requirements for development. |
| Module documentation | Created a README preparation/update process and applied it to eSIM and Stories. | Maintaining the team&#x27;s architectural context. |
| Working with AI tools | Used agents for research and implementation, recorded their contribution and checked results. | Setting constraints and evaluating generated changes. |
| Application variants | Contributed to OTT, Solar and KZ release configuration. | Managing product differences on a shared foundation. |


## Engineering decisions

- Documentation should explain a module's boundaries, entry points and verification, rather than repeat filenames.
- AI assistance is explicit. Owning a task includes setting constraints, evaluating solutions and checking results; it does not mean writing every change by hand.
- README presence does not prove quality: coverage counts files, while content review is a separate activity.

## Quality and checks

- The history includes creating the process, fixing it and applying it to eSIM and Stories.
- For AI-assisted changes I separately described the author's role, tool contribution and completed verification.

## Outcome and scope

My engineering work expanded from implementing screens to improving how the team and tools understand and change the project.

## Topics for an interview

- What should a module README contain to help the next developer?
- How do you verify an AI-assisted change and describe your own role?

[All cases](index.md) · [Practical examples](../archive/index.md) · [Technologies](../engineering/technologies.md)
