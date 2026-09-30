[RU](../../ru/cases/solar.md) · [Language selection](../../../README.md)

# Solar: launching and developing a separate app

**2022–2024 · OneTwoTrip / iOS**

I contributed to launching Solar on the OneTwoTrip codebase and developing its main screens.

[View screens and states](#screens) · [Full gallery](../gallery.md)

## Context

The new product reused existing travel capabilities but required its own composition, visual language, home screen, authentication, profile and analytics. Shared code needed clear boundaries from application-specific behavior.

## My contribution

- Contributed to the Solar target, AppDelegate and Coordinator, initial journey and tab bar.
- Developed the home screen: header menu, stories, banners, unfinished bookings, footer, configuration and analytics events.
- Worked on the profile, orders, notifications, magic links and social sign-in; adapted links, quick actions and section navigation.
- Maintained AppsFlyer/Adjust integrations and events, currency selection, payment differences and offline behavior.
- Fixed regressions after shared changes were integrated and contributed to preparing and maintaining Solar releases.

## Technologies

Swift, UIKit, Tuist / multi-target, Coordinator, Swinject, TCA, WebKit, AVKit / Lottie, AppsFlyer / Adjust, XCUITest.

## Practical examples

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Composing a separate app | Contributed to the Solar target, AppDelegate, Coordinator and tab bar. | A separate product on a shared codebase. |
| Home screen | Developed menus, Stories, banners and unfinished bookings. | Configurable product-screen composition. |
| Sign-in and section navigation | Worked on authentication, profile, orders and quick actions. | Consistent user journeys. |
| Different configurations | Handled currencies, links, analytics and regressions following shared changes. | Maintaining multiple application variants. |


## Engineering decisions

- A shared codebase does not imply identical products. Configuration and build composition define Solar-specific behavior.
- Shared changes require checking both apps: OTT navigation, styling or authentication changes can affect Solar.
- My work focused on mobile app composition, user journeys and integration with the team's shared platform.

## Quality and checks

- Separate UI tests cover the Solar home screen, tab bar, profile and authentication.
- Integration and release fixes demonstrate continued product work after the initial launch.

## Outcome and scope

I gained experience developing a separate app on a shared modular foundation, from initial composition to end-to-end journeys and release support.

<a name="screens"></a>

## Screens and interface states

Original snapshot-test images using prepared data. Each example identifies its source type. Design and overall architecture were team work; my contribution is described above. Select an image to inspect the details.

| Solar Stories: populated collection |
| :---: |
| <a name="visual-stories-solar-grid"></a><a href="../../../assets/screenshots/stories-solar-grid.png"><img src="../../../assets/screenshots/stories-solar-grid.png" alt="Solar Stories: populated collection" width="200"></a> |

<details>
<summary>Image context and notes</summary>

- **Solar Stories: populated collection.** A full-screen snapshot with four stories. The repeated cat image is a test fixture. My work included state migration and saved-collection integration. _Snapshot test using prepared data._

</details>

[Full screen and component gallery](../gallery.md)

## Topics for an interview

- How should multiple apps share a codebase while preserving their differences?
- What regressions can occur when shared changes reach a separate product?

[All cases](index.md) · [Practical examples](../archive/index.md) · [Technologies](../engineering/technologies.md)
