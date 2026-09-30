[RU](../../ru/cases/jenkins.md) · [Language selection](../../../README.md)

# Jenkins: build diagnostics and CI maintenance

**2025–2026 · OneTwoTrip / iOS**

I developed practical tools for dSYM handling, macOS-agent maintenance, build information and the review process.

## Context

iOS builds need crash-diagnostic symbols, available disk space on macOS agents and clear environment information. I developed these tools within the team’s existing Jenkins and Fastlane infrastructure.

## My contribution

- Created a pipeline to upload dSYMs from a selected macOS agent's cache by app, version and build number. Added input/cache checks, parallel uploads and retries for failed files only.
- Extended dSYM uploads to debug builds of release tasks and added the agent name to build details.
- Added a CI-agent maintenance pipeline with manual execution, a system-cleaner availability check, disk state before/after and freed-space reporting.
- Extended the review process: Fastlane review notifications reports completed reviews before the move to testing.
- Fixed the metrics environment with pinned Ruby, execution without user gems and shared post-cleanup.

## Technologies

Jenkins Declarative Pipeline, Groovy, Bash, Ruby / Fastlane, macOS agents, Firebase Crashlytics dSYM, mise, Git.

## Practical examples

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Uploading dSYMs | Created a pipeline selecting artifacts by app/build, uploading in parallel and retrying failures. | Automating iOS diagnostics. |
| Maintaining a macOS agent | Added a manual cleanup pipeline with checks and free-space measurements. | Controlled operations on the CI environment. |
| Build and review context | Added agent names to build information and completed-review reporting. | Diagnostics and team workflow. |
| Isolating Ruby | Worked with pinned Ruby, user gems and shared cleanup. | Reproducible infrastructure scripts. |


## Engineering decisions

- dSYM retries are bounded by the overall job timeout; this differs from the bounded HTTP retries in the later metrics publisher.
- The maintenance pipeline manually cleans a selected agent and reports the result through available disk space.
- My contribution centers on pipeline orchestration and integrating existing system tools.

## Quality and checks

- For dSYM handling and agent maintenance, I accounted for input checks, required-file availability and unsuccessful operations.
- Ruby launcher checks covered gem conflicts and entry-point integration. Local checks do not establish production reliability.

## Outcome and scope

Dedicated maintenance and diagnostic tools became available for iOS CI, and build information became more useful for investigating failures. I do not claim unmeasured time savings or availability gains.

## Topics for an interview

- How do you retry failed artifact uploads without repeating successful ones?
- Which checks should precede maintenance on a selected CI agent?

[All cases](index.md) · [Practical examples](../archive/index.md) · [Technologies](../engineering/technologies.md)
