[RU](../../ru/cases/product-maintenance.md) · [Language selection](../../../README.md)

# Hotels, trains and everyday product reliability

**2021–2026 · OneTwoTrip / iOS**

Much of my work involved steadily improving the existing app: bugs, navigation, locales and screen states.

## Context

Major features rely on handling real edge cases. Early tasks show how I learned a large codebase, moving from visual defects to asynchronous data, network failures and navigation between screens.

## My contribution

- In hotels, fixed favorites, review loading, photos and galleries, results states, calendars, safe areas, scrolling and post-search navigation.
- In rail journeys, added documents for canceled orders, status checking after payment errors and cancellation/repeating of electronic registration.
- Worked on shared orders: pull-to-refresh, empty states, archived-order deep links and consistent authentication.
- Fixed date formatting, locale changes, offline WebViews, the status bar, keyboard behavior and small-device presentation.
- Continued maintaining shared and product-specific journeys alongside new features.

## Technologies

Swift, UIKit, Legacy Objective-C interoperability, REST, WebKit, DateFormatter / localization, Navigation / coordinators, Debugging.

## Practical examples

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Hotel journeys | Fixed favorites, reviews, galleries, search results, calendars and post-search navigation. | Diagnosing regressions in an existing product. |
| Rail orders | Worked on cancellation documents, post-payment-error state and electronic registration. | Aligning client UI with order state. |
| Shared order list | Refined refresh, empty states, archived links and authentication. | Reusable navigation and data updates. |
| Platform behavior | Fixed dates, locales, offline WebViews, the keyboard and small screens. | Reliability across different environments. |


## Engineering decisions

- Fixing UI often means finding the cause in lifecycle, data or routing rather than simply changing a constraint.
- Maintenance work across several products complements the larger feature case studies.

## Quality and checks

- My recorded engineering work begins in December 2021; the career overview describes its progression.
- The cases distinguish bug fixes, new journeys and maintenance of existing team modules.

## Outcome and scope

This work built practical understanding of a large app and provided a foundation for more independent features, shared components and engineering tools.

## Topics for an interview

- How do you isolate a regression in a large app with shared components?
- Which states are easy to miss when fixing navigation and order refresh?

[All cases](index.md) · [Practical examples](../archive/index.md) · [Technologies](../engineering/technologies.md)
