[RU](../ru/gallery.md) · [Language selection](../../README.md)

# Screens and components

Selected screens from my work at OneTwoTrip and Solar. **27 images · 9 areas.** Select a preview to open the original.

[Payments and finance](#financial-screens) · [States](#states) · [Components](#components)

<a name="financial-screens"></a>

## Payments, balances and cards

Three technical cases with original component snapshots using test data. The cases explain the complete journeys; the images below show individual interface blocks.

### eSIM checkout: pricing and confirmation

SwiftUI · TCA · REST API · 3DS · polling. The price breakdown and final total are two independent checkout-component test states. The case covers promo codes, full discounts, errors and the timer after app resumption.

[Technical breakdown and my contribution](cases/esim.md)

| eSIM price: discount, promo code and total | Total and access to payment details |
| :---: | :---: |
| <a name="visual-esim-payment-price"></a><a href="../../assets/screenshots/esim-payment-price.png"><img src="../../assets/screenshots/esim-payment-price.png" alt="eSIM price: discount, promo code and total" width="250"></a> | <a name="visual-esim-payment"></a><a href="../../assets/screenshots/esim-payment.png"><img src="../../assets/screenshots/esim-payment.png" alt="Total and access to payment details" width="250"></a> |

<details>
<summary>Component notes</summary>

- **eSIM price: discount, promo code and total.** Payment breakdown in a bottom sheet: base price, plan discount, promo code and total. Values come from a test fixture; this is a payment-screen component. _Original component snapshot using test data._
- **Total and access to payment details.** A component with the final price and a button opening the breakdown. This is an independent test fixture; its amount differs from the promo-code example. _Original component snapshot using test data._

</details>

### Cashback: balances, cards and limits

UIKit · TCA · async/await · REST API. Blocks from one financial screen: multiple accounts and balance units, card statuses and available actions. The case covers data loading, errors and refresh after card issuance.

[Technical breakdown and my contribution](cases/loyalty.md)

| Cashback: cards and accounts | Higher cashback and card limits |
| :---: | :---: |
| <a name="visual-cashback-accounts"></a><a href="../../assets/screenshots/cashback-accounts.png"><img src="../../assets/screenshots/cashback-accounts.png" alt="Cashback: cards and accounts" width="250"></a> | <a name="visual-cashback-upgrade"></a><a href="../../assets/screenshots/cashback-upgrade.png"><img src="../../assets/screenshots/cashback-upgrade.png" alt="Higher cashback and card limits" width="250"></a> |

<details>
<summary>Component notes</summary>

- **Cashback: cards and accounts.** Cashback-screen block with physical and virtual cards, a bonus account and a savings account. Balances and masked card numbers are snapshot-test fixtures. _Original component snapshot using test data._
- **Higher cashback and card limits.** An upgrade-block state: per-transaction and monthly limits, cashback terms and the next action. This is a UI test example, not current banking terms. _Original component snapshot using test data._

</details>

### Card account: states and challenging data

UIKit · Props · SnapshotTesting. Two header states: issuance with a locked balance, and a long amount at 320 pt width. The case also explores TCA transaction history: date filtering, pagination, refresh and scrolling.

[Technical breakdown and my contribution](cases/virtual-card.md)

| Card being issued: locked balance | Large balance on a compact screen |
| :---: | :---: |
| <a name="visual-card-locked-balance"></a><a href="../../assets/screenshots/card-locked-balance.png"><img src="../../assets/screenshots/card-locked-balance.png" alt="Card being issued: locked balance" width="250"></a> | <a name="visual-card-long-balance"></a><a href="../../assets/screenshots/card-long-balance.png"><img src="../../assets/screenshots/card-long-balance.png" alt="Large balance on a compact screen" width="250"></a> |

<details>
<summary>Component notes</summary>

- **Card being issued: locked balance.** Account header showing issuance status and a locked-balance indicator. Status and fund availability need to remain distinct from the amount. _Original component snapshot using test data._
- **Large balance on a compact screen.** Snapshot at 320 pt width: a large test balance, fractional amount, currency and card icon. An example of adapting text size to a long balance. _Original component snapshot using test data._

</details>

<a name="states"></a>

## Interface states

Supporting scenarios: empty data, waiting, compact screens and recovery.

<details>
<summary>Stories — collection, iPhone SE, empty state</summary>

| Solar Stories: populated collection | Solar Stories on a compact screen | Saved Stories: empty state |
| :---: | :---: | :---: |
| <a name="visual-stories-solar-grid"></a><a href="../../assets/screenshots/stories-solar-grid.png"><img src="../../assets/screenshots/stories-solar-grid.png" alt="Solar Stories: populated collection" width="180"></a> | <a name="visual-stories-small-screen"></a><a href="../../assets/screenshots/stories-small-screen.png"><img src="../../assets/screenshots/stories-small-screen.png" alt="Solar Stories on a compact screen" width="180"></a> | <a name="visual-stories-empty"></a><a href="../../assets/screenshots/stories-empty.png"><img src="../../assets/screenshots/stories-empty.png" alt="Saved Stories: empty state" width="180"></a> |

- **Solar Stories: populated collection.** A full-screen snapshot with four stories. The repeated cat image is a test fixture. My work included state migration and saved-collection integration. _Snapshot test using prepared data._
- **Solar Stories on a compact screen.** The iPhone SE variant with seven stories: two columns and a collection extending beyond the viewport. _Snapshot test using prepared data._
- **Saved Stories: empty state.** The screen explains how to save a story when the collection is empty. It is a separate presentation state. _Snapshot test using prepared data._

[Full case](cases/stories.md)

</details>

<details>
<summary>Payments — waiting and error</summary>

| Waiting for external payment | Payment error: long text and two actions |
| :---: | :---: |
| <a name="visual-payment-waiting"></a><a href="../../assets/screenshots/payment-waiting.png"><img src="../../assets/screenshots/payment-waiting.png" alt="Waiting for external payment" width="200"></a> | <a name="visual-payment-long-error"></a><a href="../../assets/screenshots/payment-long-error.png"><img src="../../assets/screenshots/payment-long-error.png" alt="Payment error: long text and two actions" width="200"></a> |

- **Waiting for external payment.** A full-screen snapshot of the shared payment container. It shows waiting for a banking-app handoff; this is the SberPay variant, not a screenshot of SBP specifically. _Snapshot test using prepared data._
- **Payment error: long text and two actions.** Stress-test data checks how a long message coexists with Retry and Close actions. _Snapshot test using prepared data._

[Full case](cases/payments.md)

</details>

<a name="components"></a>

## Components

Smaller elements grouped by product area.

<details>
<summary>eSIM · 2</summary>

| eSIM balance | eSIM plan card |
| :---: | :---: |
| <a name="visual-esim-balance"></a><a href="../../assets/screenshots/esim-balance.png"><img src="../../assets/screenshots/esim-balance.png" alt="eSIM balance" width="250"></a> | <a name="visual-esim-tariff"></a><a href="../../assets/screenshots/esim-tariff.png"><img src="../../assets/screenshots/esim-tariff.png" alt="eSIM plan card" width="250"></a> |

- **eSIM balance.** Remaining allowance and service status in a compact block. _Original component snapshot using test data._
- **eSIM plan card.** The card brings plan terms and the selection action together. _Original component snapshot using test data._

[Full case](cases/esim.md)

</details>

<details>
<summary>Travel cards and timeline · 5</summary>

| Trip card | Trip timeline item |
| :---: | :---: |
| <a name="visual-travel-card"></a><a href="../../assets/screenshots/travel-card.png"><img src="../../assets/screenshots/travel-card.png" alt="Trip card" width="250"></a> | <a name="visual-travel-timeline"></a><a href="../../assets/screenshots/travel-timeline.png"><img src="../../assets/screenshots/travel-timeline.png" alt="Trip timeline item" width="250"></a> |

| Travel statistics | Rail timeline item |
| :---: | :---: |
| <a name="visual-travel-statistics"></a><a href="../../assets/screenshots/travel-statistics.png"><img src="../../assets/screenshots/travel-statistics.png" alt="Travel statistics" width="250"></a> | <a name="visual-travel-rail"></a><a href="../../assets/screenshots/travel-rail.png"><img src="../../assets/screenshots/travel-rail.png" alt="Rail timeline item" width="250"></a> |

| Trip card: long dates and several travel types |
| :---: |
| <a name="visual-travel-card-dense"></a><a href="../../assets/screenshots/travel-card-dense.png"><img src="../../assets/screenshots/travel-card-dense.png" alt="Trip card: long dates and several travel types" width="250"></a> |

- **Trip card.** A reusable card combines cover art, dates, destination and travel types. _Original component snapshot using test data._
- **Trip timeline item.** A route item combines the shared timeline with transport-specific presentation. _Original component snapshot using test data._
- **Travel statistics.** Travel statistics are reused across several parts of the feature. _Original component snapshot using test data._
- **Rail timeline item.** A transport widget presents stations, local times and duration within the shared timeline. _Snapshot test using prepared data._
- **Trip card: long dates and several travel types.** A 320 pt variant with a long date range, city count and extra icons. Visible text truncation is part of the tested state. _Snapshot test using prepared data._

[Full case](cases/travel-history.md)

</details>

<details>
<summary>Flights: search and fares · 2</summary>

| UI 2.0 flight fare card | Round-trip search form |
| :---: | :---: |
| <a name="visual-avia-tariff"></a><a href="../../assets/screenshots/avia-tariff.png"><img src="../../assets/screenshots/avia-tariff.png" alt="UI 2.0 flight fare card" width="250"></a> | <a name="visual-avia-search"></a><a href="../../assets/screenshots/avia-search.png"><img src="../../assets/screenshots/avia-search.png" alt="Round-trip search form" width="250"></a> |

- **UI 2.0 flight fare card.** Fare conditions and the available action follow the shared UI 2.0 style. _Original component snapshot using test data._
- **Round-trip search form.** Round-trip search with linked journey parameters. _Original component snapshot using test data._

[Full case](cases/avia.md)

</details>

<details>
<summary>Shared fields and action bar · 3</summary>

| Shared input field | Shared selection field |
| :---: | :---: |
| <a name="visual-input-field"></a><a href="../../assets/screenshots/input-field.png"><img src="../../assets/screenshots/input-field.png" alt="Shared input field" width="250"></a> | <a name="visual-select-field"></a><a href="../../assets/screenshots/select-field.png"><img src="../../assets/screenshots/select-field.png" alt="Shared selection field" width="250"></a> |

| Price and action bottom bar |
| :---: |
| <a name="visual-bottom-bar"></a><a href="../../assets/screenshots/bottom-bar.png"><img src="../../assets/screenshots/bottom-bar.png" alt="Price and action bottom bar" width="250"></a> |

- **Shared input field.** A shared input field reused in product forms. _Original component snapshot using test data._
- **Shared selection field.** A selection field with consistent value and state presentation. _Original component snapshot using test data._
- **Price and action bottom bar.** Price and the primary action form a reusable component. _Original component snapshot using test data._

[Full case](cases/design-system.md)

</details>

<details>
<summary>Virtual card · 2</summary>

| Card limits | Financial operation row |
| :---: | :---: |
| <a name="visual-card-limits"></a><a href="../../assets/screenshots/card-limits.png"><img src="../../assets/screenshots/card-limits.png" alt="Card limits" width="250"></a> | <a name="visual-card-operation"></a><a href="../../assets/screenshots/card-operation.png"><img src="../../assets/screenshots/card-operation.png" alt="Financial operation row" width="250"></a> |

- **Card limits.** Limit presentation is part of the virtual card management journey. _Original component snapshot using test data._
- **Financial operation row.** A history component showing purpose, date, time, amount and operation type. The card case explains pagination, filtering and list states. _Original component snapshot using test data._

[Full case](cases/virtual-card.md)

</details>

<details>
<summary>Loyalty programme · 1</summary>

| Progress toward Premium status |
| :---: |
| <a name="visual-loyalty-progress"></a><a href="../../assets/screenshots/loyalty-progress.png"><img src="../../assets/screenshots/loyalty-progress.png" alt="Progress toward Premium status" width="250"></a> |

- **Progress toward Premium status.** Counter, progress and status conditions in UI 2.0. An illustration of the loyalty area; the shared design and test baseline are team work. _Snapshot test using prepared data._

[Full case](cases/loyalty.md)

</details>

<details>
<summary>Support chat · 1</summary>

| Chat reply options |
| :---: |
| <a name="visual-chat-options"></a><a href="../../assets/screenshots/chat-options.png"><img src="../../assets/screenshots/chat-options.png" alt="Chat reply options" width="250"></a> |

- **Chat reply options.** Quick replies as part of a guided support conversation. _Original component snapshot using test data._

[Full case](cases/chat.md)

</details>

---

**About the images.** Design and overall architecture were team work; the cases describe my contribution. Images are unchanged snapshot-test baselines using prepared data. The original interface language is preserved.

[All cases](cases/index.md) · [Summary](career/summary.md) · [About the materials](methodology.md)
