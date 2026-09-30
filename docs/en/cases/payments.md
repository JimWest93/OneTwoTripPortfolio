[RU](../../ru/cases/payments.md) · [Language selection](../../../README.md)

# Payment integrations and completing a purchase

**2022–2026 · OneTwoTrip / iOS**

I worked on client-side payment journeys across products and shared payment-progress presentation.

[View screens and states](#screens) · [Full gallery](../gallery.md)

## Context

Payments connect external providers, WebView/3DS, waiting for server status and returning to an order. Users need to understand whether an operation is continuing and what to do after an error.

## My contribution

- Integrated BridgerPay into the hotel journey and maintained related payment-method identification and widget UI changes.
- Supported NowPayments in Solar flights and hotels; fixed completion and presentation of external payment journeys.
- Worked on the shared SBP payment loader and its UI tests.
- Developed the eSIM payment screen and client integration, contacts, errors, timer and order navigation.
- Fixed order behavior after payment errors and related states in the rail product.

## Technologies

Swift, UIKit / SwiftUI, WebKit, 3DS, REST / polling, TCA, Coordinator, BridgerPay / NowPayments integrations, XCUITest.

## Practical examples

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| External payment providers | Integrated BridgerPay in hotels and maintained NowPayments in Solar. | Client-side integration of payment journeys. |
| Waiting for SBP payment | Worked on the shared payment loader and its UI tests. | Reusable presentation of an intermediate state. |
| Buying an eSIM | Developed payment UI, backend interaction, contact handling and order navigation. | Orchestrating several purchase steps. |
| Returning after failure | Fixed order state after payment errors and completion of external journeys. | Error handling and interface recovery. |


## Engineering decisions

- The external payment UI status can differ from the final order status. The client completes the journey according to the backend contract.
- Payment methods have different transitions, but progress indication and error handling should be consistent.
- My scope is client-side provider integration, payment state and navigation to the purchase result.

## Quality and checks

- The history includes integration fixes, eSIM unit/UI tests and a UI test for the shared SBP loader.
- Requirements and implementation are separated by product and provider.

## Outcome and scope

I gained experience supporting purchases from the form to confirmation, including rejection, waiting and returning from an external interface.

## A closer look at the journey

### Waiting for an external result

Opening a banking app or WebView does not complete a purchase by itself. The client needs to show waiting, handle return and obtain the outcome according to the provider contract. My work included Solar and eSIM payment integrations, the shared loader and transition checks.

### eSIM: a detailed checkout case

For eSIM I worked on the SwiftUI screen, user contacts, REST API integration, 3DS, polling, promo codes and the timer. [The dedicated case](esim.md) explains payment transitions, protection against stale promo responses, a fully discounted purchase without card selection and resuming after screen lock; it also includes the original price-breakdown snapshot.

### An error should leave a clear next step

Retry and Close have different consequences for the purchase journey. A full-screen baseline with a long message shows another concern: actions must remain accessible with awkward data. These snapshots belong to the shared team payment container; my contribution is described in the integration and state-handling examples.

<a name="screens"></a>

## Screens and interface states

Original snapshot-test images using prepared data. Each example identifies its source type. Design and overall architecture were team work; my contribution is described above. Select an image to inspect the details.

| Waiting for external payment | Payment error: long text and two actions |
| :---: | :---: |
| <a name="visual-payment-waiting"></a><a href="../../../assets/screenshots/payment-waiting.png"><img src="../../../assets/screenshots/payment-waiting.png" alt="Waiting for external payment" width="200"></a> | <a name="visual-payment-long-error"></a><a href="../../../assets/screenshots/payment-long-error.png"><img src="../../../assets/screenshots/payment-long-error.png" alt="Payment error: long text and two actions" width="200"></a> |

<details>
<summary>Image context and notes</summary>

- **Waiting for external payment.** A full-screen snapshot of the shared payment container. It shows waiting for a banking-app handoff; this is the SberPay variant, not a screenshot of SBP specifically. _Snapshot test using prepared data._
- **Payment error: long text and two actions.** Stress-test data checks how a long message coexists with Retry and Close actions. _Snapshot test using prepared data._

</details>

[Full screen and component gallery](../gallery.md)

## Topics for an interview

- Which states does the client pass through between payment initiation and order confirmation?
- How do you restore a clear interface after an external provider rejects a payment?

[All cases](index.md) · [Practical examples](../archive/index.md) · [Technologies](../engineering/technologies.md)
