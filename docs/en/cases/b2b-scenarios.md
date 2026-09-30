[RU](../../ru/cases/b2b-scenarios.md) · [Language selection](../../../README.md)

# Business-trip journeys inside the consumer app

**2026 · OneTwoTrip / iOS**

I integrated business trips into search forms, profiles and orders while preserving different product and session-state rules.

## Context

Users can book personal and business trips in one app. The work linked forms from several product areas with marketing communication without spreading one form's state to the others.

## My contribution

- Added a business-trip checkbox to Search Form 2.0 for flights, hotels and trains.
- Implemented profile sheets and a banner placement on the rail-order screen.
- Passed the business-trip flag in banner requests and refined corporate-card checks after the backend contract was clarified.
- Added and fixed UI tests for the combined journeys.

## Technologies

Swift, UIKit, TCA / state management, Feature flags, REST, Cross-module configuration, XCUITest.

## Practical examples

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Business-trip search | Added the business-trip flag to flights, hotels and trains. | One journey across multiple product areas. |
| Profile and order entry points | Implemented profile sheets and a banner placement in rail orders. | Coordinated cross-module navigation. |
| Backend-contract changes | Refined banner requests and corporate-card checks after requirements changed. | Adapting client logic to an API. |
| Checking combined journeys | Added and fixed UI tests for business trips inside the consumer app. | Integration checks of the user journey. |


## Engineering decisions

- Separated form-local state from session state with different lifetimes so that changing one journey did not affect another.
- Legacy forms and Solar were outside scope. Capabilities were controlled by separate flags rather than one shared condition.

## Quality and checks

- Checks covered different entry points, parameter passing and the consequences of state changes.
- Backend-parameter refinements and UI-test updates were handled as separate pieces of work.

## Outcome and scope

A cross-product journey with clear state-lifecycle rules and controlled feature activation.

## Topics for an interview

- Where should business-trip state live, and when should it reset?
- How do you check a shared journey across several product areas?

[All cases](index.md) · [Practical examples](../archive/index.md) · [Technologies](../engineering/technologies.md)
