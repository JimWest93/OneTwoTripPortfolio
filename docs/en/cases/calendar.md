[RU](../../ru/cases/calendar.md) · [Language selection](../../../README.md)

# A shared calendar across product areas

**2022–2023 · OneTwoTrip / iOS**

I contributed to a shared calendar and migrated different date-selection journeys to it.

## Context

Flights, hotels, trains and other products select dates differently but need consistent behavior and a shared visual component. The work covered configuration, selected-date state, locales and integrations as well as appearance.

## My contribution

- Added the working-day calendar and weekend display, then worked on the shared calendar component.
- Developed PropsBuilder, configuration, presenter, public entry points and example scenarios.
- Integrated the shared calendar into hotel, flight, rail and other entry points; removed replaced legacy modules.
- Fixed initial scrolling to a selected date, month and weekday presentation across locales, date editing and selection constraints.

## Technologies

Swift, UIKit, UICollectionView, Props / render, Presenter / Interactor / Router, Swinject, Tuist, Localization / DateFormatter.

## Practical examples

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Shared date selection | Developed calendar configuration, public entry points, presenter and PropsBuilder. | Designing a reusable UI module. |
| Different product areas | Integrated the calendar into flights, hotels and trains while preserving constraints. | A shared component with product configuration. |
| Returning to a selected date | Fixed initial scrolling and editing an existing date range. | Correct state restoration. |
| Locales and working days | Worked on months, weekdays, weekends and the working-day calendar. | Localization and calendar behavior. |


## Engineering decisions

- The product area supplies configuration: product differences should not create hard dependencies from the calendar to every screen.
- Consumers were migrated separately. Integration compatibility was checked incrementally before old modules were removed.
- App and device locales can differ; formatting and calendar order must follow the chosen product behavior.

## Quality and checks

- The history distinguishes component implementation, integrations and regression fixes. Example apps were used to check different configurations.
- The work spans calendar integration in hotels, flights, trains and the virtual-card journey.

## Outcome and scope

Repeated date-selection interfaces were consolidated into a configurable shared implementation maintained across several products.

## Topics for an interview

- What belongs in a shared calendar's public configuration?
- How do you meet different product requirements without duplicating the component?

[All cases](index.md) · [Practical examples](../archive/index.md) · [Technologies](../engineering/technologies.md)
