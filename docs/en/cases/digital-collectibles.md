[RU](../../ru/cases/digital-collectibles.md) · [Language selection](../../../README.md)

# Solar Digital Collectibles: native UI and WebView

**2023–2024 · OneTwoTrip / iOS**

I implemented the digital-achievements catalog, planetary interface and actions for earned rewards.

## Context

The feature combined a visual planetary system in a WebView with native achievement cards. Rewards could be unavailable, earned or added to a wallet; those states determined the interface and available actions.

## My contribution

- Created planet cards, the bottom-sheet list, zoom controls and supporting actions.
- Integrated the achievements API, WebView communication, reward screen and its business logic.
- Added claiming and wallet actions, sharing, deep links and universal links to achievements.
- Migrated the module to TCA, wrote unit tests and handled errors and recovery after network issues.
- Refined text, images, video, sharing locales, small-screen behavior and profile entry points.

## Technologies

Swift, UIKit, WebKit / native–web communication, TCA, Combine, REST, LinkPresentation, Swinject, XCTest.

## Practical examples

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Planets and achievement lists | Created cards, the sheet list, zoom controls and supporting actions. | A distinctive interface and navigation model. |
| Native screen and WebView | Integrated the achievements API, WebView communication and reward-screen logic. | Connecting different presentation technologies. |
| Achievement actions | Added claiming, wallet actions, sharing and universal links. | Product actions connected to external navigation. |
| Moving state to TCA | Contributed to module migration, wrote unit tests and handled errors. | State architecture and testability. |


## Engineering decisions

- Native state and WebView content must stay synchronized when a card is selected or an achievement's availability changes.
- My scope was the mobile achievements interface, API integration, WebView and user actions.

## Quality and checks

- Wrote module unit tests and supported the migration of state to TCA.
- After launch, improved sharing, links, error handling and presentation across screens.

## Outcome and scope

The feature combined an unusual visual model with production-app requirements: state, navigation, analytics and error handling.

## A closer look at the journey

1. **Select a planet.** WebView or card event
2. **Reward screen.** Find the ID in the collection
3. **Wallet.** Validate input and call the API
4. **New status.** Polling and updating the views

A simplified route through one journey. Error branches and additional actions are discussed below.

### One journey across two UI technologies

A planet tap arrives as a WebView message. The native layer extracts the identifier, finds the achievement in the loaded collection and opens its screen. Navigation also tracks whether the collection sheet was open so that its state can be restored on return. My work connected the visual system, native cards and routing.

### Adding to a wallet is an asynchronous journey

The client checks connectivity and an empty field, then sends the address for server validation. Starting the operation introduces an intermediate status; later updates arrive through the API and polling. The achievement card and collection need to reflect the same result. I worked on this client logic and its checks; backend NFT issuance and address validation were outside my scope.

### Recovery and screen dismissal

A loading error offers a retry action. The planetary view also supports a WebView reload. Leaving the feature cancels status polling and dismisses related sheets and notifications. TCA expresses these transitions as actions and effects; unit tests exercise navigation, state, retry and related events.

### A link needs to open a specific achievement

An external link can arrive before the catalogue loads. I worked on coordinating universal links, network loading and UI readiness so that the correct item opens.

## Topics for an interview

- How do you synchronize native state with WebView events?
- What changes in testing when a module moves to TCA?

[All cases](index.md) · [Practical examples](../archive/index.md) · [Technologies](../engineering/technologies.md)
