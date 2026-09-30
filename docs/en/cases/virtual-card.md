[RU](../../ru/cases/virtual-card.md) · [Language selection](../../../README.md)

# Cards and transaction history: limits, pagination and states

**2024–2025 · OneTwoTrip / iOS**

Updated virtual and physical card accounts: UIKit, account state, limits and TCA-based transaction history with filtering, pagination and refresh.

[View screens and states](#screens) · [Full gallery](../gallery.md)

## Context

Users need a financial section with a clear card state, available actions and limitations. Implementation covers account data, transactions and asynchronous status changes as well as the card shown on screen.

## My contribution

- Worked on the virtual/physical card home screen, plastic-card issuance states and transaction history.
- Implemented spending limits, a dedicated limits screen and service information.
- Added skeleton states and snackbar/bottom-sheet errors, updated business logic and addressed design-review feedback.
- Developed tests for issuance, identity verification, 401 handling, transactions, card tiers and physical cards.
- Shortened specific UI-test journeys with targeted deep links and refactored shared loyalty-test infrastructure.
- Developed transaction history: date filtering, pagination, pull-to-refresh, grouping by month and navigation to details; fixed empty-list and scrolling behaviour.

## Technologies

Swift, UIKit, TCA, Presenter / Interactor / Router, REST, Swinject, Props, SnapshotTesting, XCTest, XCUITest.

## Practical examples

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Card account | Worked on virtual and physical cards, issuance states and transactions. | Multiple states of a financial product. |
| Limits and servicing | Implemented spending limits, a dedicated screen and service terms. | Clear presentation of product constraints. |
| Financial transaction history | Developed transaction and bonus lists, a date filter and pagination resets on period changes and refresh; fixed scrolling. | TCA, REST API, pagination and list states. |
| Checking user journeys | Developed issuance, identity and error tests; used targeted deep links. | Testability and UI-test maintenance. |


## Engineering decisions

- Transactions and limits have their own modules; the financial home screen should not own every detail of nested processes.
- A UI redesign does not imply changing banking logic. My contribution covers the mobile client and its integrations.
- Test values and states are used for UI checks; the portfolio contains no real payment or customer data.

## Quality and checks

- Checks include account-screen snapshots and UI tests for the main card, transactions, limits and physical cards.
- Checks covered empty history, different card levels and error handling. The snapshot suite includes a locked balance and a long amount at 320 and 430 pt widths.

## Outcome and scope

The card account gained a more coherent mobile interface with separate states and testable user journeys.

## A closer look at the journey

### Balance, fund availability and issuance status

The account header combines the amount with card type, a masked number and status. I worked on the card screen and snapshot checks, including locked balances and long amounts. A large value on a compact screen uses an adjusted text style to preserve the fractional amount, currency and adjacent icon. The account screen uses Presenter/Interactor/Router, while transaction history is a separate TCA module: the shared UI does not erase those architectural boundaries.

### Transaction history: filtering and pagination

Developed the client-side money and bonus transaction lists. For money transactions, selecting a period clears the previous selection and starts at page one; refresh also resets the page number. Fetching another page accounts for both remaining results and an in-flight request. Received operations are merged, sorted by date and grouped by month; selecting a row opens details. My changes included date ranges, pagination resets, group headers and the next-page loading indicator.

### Loading, empty results and scrolling

Initial loading, refreshing an existing list and no results are different UI states. I worked on unified loading state, filter presentation and a scrolling fix for bonus history. Financial-journey checks complement component snapshots: one operation row does not establish pagination or filter correctness. The gallery labels these materials separately from the list behaviour explained here.

<a name="screens"></a>

## Screens and interface states

Original snapshot-test images using prepared data. Each example identifies its source type. Design and overall architecture were team work; my contribution is described above. Select an image to inspect the details.

| Card being issued: locked balance | Large balance on a compact screen |
| :---: | :---: |
| <a name="visual-card-locked-balance"></a><a href="../../../assets/screenshots/card-locked-balance.png"><img src="../../../assets/screenshots/card-locked-balance.png" alt="Card being issued: locked balance" width="250"></a> | <a name="visual-card-long-balance"></a><a href="../../../assets/screenshots/card-long-balance.png"><img src="../../../assets/screenshots/card-long-balance.png" alt="Large balance on a compact screen" width="250"></a> |

| Card limits | Financial operation row |
| :---: | :---: |
| <a name="visual-card-limits"></a><a href="../../../assets/screenshots/card-limits.png"><img src="../../../assets/screenshots/card-limits.png" alt="Card limits" width="250"></a> | <a name="visual-card-operation"></a><a href="../../../assets/screenshots/card-operation.png"><img src="../../../assets/screenshots/card-operation.png" alt="Financial operation row" width="250"></a> |

<details>
<summary>Image context and notes</summary>

- **Card being issued: locked balance.** Account header showing issuance status and a locked-balance indicator. Status and fund availability need to remain distinct from the amount. _Original component snapshot using test data._
- **Large balance on a compact screen.** Snapshot at 320 pt width: a large test balance, fractional amount, currency and card icon. An example of adapting text size to a long balance. _Original component snapshot using test data._
- **Card limits.** Limit presentation is part of the virtual card management journey. _Original component snapshot using test data._
- **Financial operation row.** A history component showing purpose, date, time, amount and operation type. The card case explains pagination, filtering and list states. _Original component snapshot using test data._

</details>

[Full screen and component gallery](../gallery.md)

## Topics for an interview

- How do you separate loading, error and card-issuance states?
- How do you coordinate date filtering, pagination, refresh and an empty transaction-history state?

[All cases](index.md) · [Practical examples](../archive/index.md) · [Technologies](../engineering/technologies.md)
