[RU](../../ru/cases/quality.md) · [Language selection](../../../README.md)

# Quality: unit, snapshot and user-journey checks

**2023–2026 · OneTwoTrip / iOS**

I supported product changes with several levels of automated checks and developed the test journeys themselves.

## Context

A large iOS app needs correct logic, stable presentation and working end-to-end journeys. These levels complement one another and catch different regressions.

## My contribution

- Wrote state and business-logic unit tests for the Solar profile, Digital Collectibles, finance, eSIM and travel history.
- Added snapshots for input fields, card accounts, eSIM and travel history with different sizes, text and states.
- Developed XCUITest journeys for authentication, profile, loyalty, virtual cards, eSIM, travel history, flights and B2B integrations.
- Maintained accessibility identifiers and mocks; updated journeys for UI 2.0 and contract changes.
- Shortened specific test routes with deep links and fixed unstable or broken checks.

## Technologies

XCTest, XCUITest, SnapshotTesting, TCA TestStore, Mocks, Accessibility identifiers, Allure, Jenkins.

## Practical examples

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Checking business state | Wrote unit tests for profiles, achievements, finance, eSIM and trips. | Testing logic independently of appearance. |
| Checking components | Added snapshots for UI sizes, text and states. | Visual regressions and the design system. |
| End-to-end journeys | Developed XCUITest flows for sign-in, purchases, profiles and integrations. | Checking app behavior from the user&#x27;s perspective. |
| Maintaining tests | Maintained mocks and accessibility identifiers, fixed instability and used deep links. | Practical maintenance of automated checks. |


## Engineering decisions

- Unit tests check decisions and state, snapshots catch visual regressions, and UI tests check connected screens and actions. One level does not replace the others.
- Error states need controlled responses and network conditions rather than waiting for an accidental production failure.
- Test files, methods, runs and snapshot images are different metrics and are not mixed in the statistics.

## Quality and checks

- The analysis distinguishes testing tasks from commits that touch tests. Neither figure is a code-coverage percentage.
- The included images are genuine snapshot baselines; application tests were not rerun to create this portfolio.

## Outcome and scope

Testing became both part of my feature work and a separate engineering contribution: creating checks, maintaining them and diagnosing regressions.

## Topics for an interview

- Which errors are best caught by unit, snapshot and UI tests?
- How do you distinguish a test problem from an application regression?

[All cases](index.md) · [Practical examples](../archive/index.md) · [Technologies](../engineering/technologies.md)
