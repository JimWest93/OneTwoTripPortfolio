[RU](../../ru/cases/auth.md) · [Language selection](../../../README.md)

# Authentication across different product journeys

**2022–2024 · OneTwoTrip / iOS**

I developed phone and email sign-in, repeat authentication, magic links and social sign-in for Solar.

## Context

Authentication is used in profiles, orders and checkout, so a failure can affect multiple product areas. I worked on transitions between sign-in methods, incomplete contact details and returning users to their original journey.

## My contribution

- Developed repeat authentication, session-state handling and user feedback.
- Worked on the new email/PIN journey, switching to phone sign-in, requesting a missing phone number and continuing checkout.
- Contributed to Solar authentication: magic links, Apple ID and Google ID, incoming-link handling and product configuration differences.
- Handled edge cases involving connectivity, CAPTCHA, resending codes, switching methods, the keyboard, validation and registration during checkout.
- Added account-deletion confirmation and updated authentication events and Solar tests.

## Technologies

Swift, UIKit, Presenter / Interactor / Router, Swinject, REST, Deep Links / Universal Links, WebKit, Apple ID / Google ID integrations, XCUITest.

## Practical examples

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Continuing checkout after sign-in | Worked on email/PIN, switching to phone and requesting missing contacts. | Authentication as part of a product journey. |
| Repeat sign-in on a device | Developed repeat authentication and consistent user-session behaviour. | Session state and reusable flows. |
| Signing in to Solar | Contributed to magic links, Apple ID, Google ID and incoming links. | Integration of multiple authentication methods. |
| Errors and repeated actions | Handled CAPTCHA, missing connectivity, code resends and method changes. | Explicit edge states and validation. |


## Engineering decisions

- Successful sign-in returns control to the initiating journey: profile, orders or checkout. The completion context matters more than simply dismissing the form.
- Remembering a device does not replace server-side session validation; this portfolio describes the user journey without reproducing the internal token scheme.
- Shared sign-in and return-to-action states account for provider differences and product configuration.

## Quality and checks

- A dedicated Solar authentication UI test and successive fixes cover checkout and incoming-link journeys.
- Responsibility boundaries were checked against the implementation and module contracts.

## Outcome and scope

Different entry points gained a consistent sign-in journey that continues the user's action and handles errors explicitly.

## Topics for an interview

- How do you continue the original action after authentication?
- How do you keep state consistent when the user changes sign-in methods?

[All cases](index.md) · [Practical examples](../archive/index.md) · [Technologies](../engineering/technologies.md)
