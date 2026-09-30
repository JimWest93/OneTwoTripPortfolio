[RU](../../ru/cases/profile.md) · [Language selection](../../../README.md)

# Profile, personal details and notifications

**2023–2026 · OneTwoTrip / iOS**

I developed OTT and Solar profiles, personal-data editing, bonus sections and notification channels.

## Context

The profile brings together authentication, personal data, loyalty, favorites, support and social features. It needs consistent state, correct validation and navigation to independent modules.

## My contribution

- Moved the Solar profile to the original TCA implementation, developed the header and its business logic, wallet/account sections and guest state.
- Worked on profile photos, data editing, About the app, favorite hotels and marketing statistics.
- Developed the OTT personal-details screen in UI 2.0 with new fields, validation and support navigation for contact changes.
- Implemented notification-channel UI and business logic, scrolling to the first unread message, notification subsystem changes and events.
- Contributed to social journeys: reporting a user, travel history in another user's profile and onboarding updates.

## Technologies

Swift, UIKit, TCA, PropsBuilder, Swinject, Nuke, Push notifications, REST, XCTest / XCUITest.

## Practical examples

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Profile across sign-in states | Moved the Solar profile to TCA and developed its header and account sections. | Screen composition and state lifecycle. |
| Editing personal details | Worked on UI 2.0 fields, validation and support navigation for contact changes. | Forms and product-contract constraints. |
| Notification channels | Implemented UI, business logic and scrolling to unread messages. | Aligning data, navigation and presentation. |
| Widgets and social journeys | Added favorites, statistics and travel history in other users&#x27; profiles. | Module reuse and user context. |


## Engineering decisions

- Guest, signed-in and loyalty-tier states need explicit presentation rather than unrelated rules that hide individual views.
- Cached profile data needs to match the new session when switching accounts; I worked on keeping this behaviour consistent.
- Notification channels and support share navigation but have different data and behavior.

## Quality and checks

- Checks include a Solar profile unit test and UI tests for sections, photos and personal-data editing.
- Regression work covers avatar caching, validation, keyboard behavior, small screens and preserving channel state.

## Outcome and scope

The profile became an ongoing area of my contribution, from screen composition to product widgets, testing and maintenance.

## Topics for an interview

- How should guest and signed-in profiles share logic without diverging?
- Which states need checking when users edit their contact details?

[All cases](index.md) · [Practical examples](../archive/index.md) · [Technologies](../engineering/technologies.md)
