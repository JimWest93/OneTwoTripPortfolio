[RU](../../ru/cases/avia.md) · [Language selection](../../../README.md)

# Flights: search forms, fares and order journeys

**2022–2026 · OneTwoTrip / iOS**

I developed flight screens and contributed to migrating search and fare selection to UI 2.0.

[View screens and states](#screens) · [Full gallery](../gallery.md)

## Context

The journey from search to fare selection and order depends on navigation, selected parameters and correct prices. My contribution includes early fixes and later, broader presentation changes.

## My contribution

- Fixed search parameters, order statuses and navigation, travel documents, filters and related regressions.
- Built the new search form from shared components, supported simple and multi-city routes, animations and analytics, and added UI checks.
- Moved fare selection to UI 2.0: cards, selection state, prices, advice, banners, errors and the transition to booking.
- Worked on selecting seats in existing orders, consistent passenger-avatar colors and eSIM offers.

## Technologies

Swift, UIKit, TCA, PropsBuilder, Swinject, Common UI components, Feature flags, XCTest / SnapshotTesting / XCUITest.

## Practical examples

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| UI 2.0 search form | Built simple and multi-city routes with shared components, events and UI checks. | A product form with multiple modes. |
| Fare selection | Moved cards, prices, selection and the booking transition to UI 2.0. | Updating UI while preserving purchase rules. |
| Order maintenance | Fixed parameters, statuses, documents, filters and navigation. | Regression work across a long product journey. |
| Additional services | Worked on seats in existing orders and eSIM offers. | Integrating related products into order context. |


## Engineering decisions

- The new fare screen is a presentation layer over existing product logic and the backend contract.
- Solar retained separate search-form behavior. Redesigning OTT should not automatically change the second product.
- Price, selected fare and navigation parameters must remain consistent as the interface updates.

## Quality and checks

- Added UI checks for the new search form and fares; maintained tests for subsequent order-journey changes.
- Separate checks cover the search form and fares, while later order fixes include their own tests and review.

## Outcome and scope

This experience spans several steps of the flight journey and UI migration while preserving business rules.

<a name="screens"></a>

## Screens and interface states

Original snapshot-test images using prepared data. Each example identifies its source type. Design and overall architecture were team work; my contribution is described above. Select an image to inspect the details.

| UI 2.0 flight fare card | Round-trip search form |
| :---: | :---: |
| <a name="visual-avia-tariff"></a><a href="../../../assets/screenshots/avia-tariff.png"><img src="../../../assets/screenshots/avia-tariff.png" alt="UI 2.0 flight fare card" width="250"></a> | <a name="visual-avia-search"></a><a href="../../../assets/screenshots/avia-search.png"><img src="../../../assets/screenshots/avia-search.png" alt="Round-trip search form" width="250"></a> |

<details>
<summary>Image context and notes</summary>

- **UI 2.0 flight fare card.** Fare conditions and the available action follow the shared UI 2.0 style. _Original component snapshot using test data._
- **Round-trip search form.** Round-trip search with linked journey parameters. _Original component snapshot using test data._

</details>

[Full screen and component gallery](../gallery.md)

## Topics for an interview

- How would you design a shared form for simple and multi-city routes?
- How do you update fare-selection UI without changing purchase rules?

[All cases](index.md) · [Practical examples](../archive/index.md) · [Technologies](../engineering/technologies.md)
