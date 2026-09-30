[RU](../../ru/cases/chat.md) · [Language selection](../../../README.md)

# A custom support chat replacing the Zendesk SDK

**2022–2024 · OneTwoTrip / iOS**

I contributed to a custom support interface integrated with the Helpdesk API and application journeys.

[View screens and states](#screens) · [Full gallery](../gallery.md)

## Context

Users need to talk to a bot or support agent inside the app, send documents and return to previous conversations. Moving from a packaged SDK required UI, networking, delivery states and authentication integration.

## My contribution

- Developed chat and chatbot interactions: text messages, suggested replies, images, attachments, links and navigation to orders.
- Worked on undelivered-message indicators, errors, reconnection, scrolling and read receipts.
- Added a feature flag, chat deep link and analytics events; contributed to removing Zendesk SDK and moving FAQ to a WebView.
- Extended chat in Solar with a separate tab, entry points from orders and payment errors, and support for GuideGPT/Solly journeys.
- Fixed regressions involving endless loading, sending without a socket connection, attachments, the keyboard and obscured messages.

## Technologies

Swift, UIKit, Socket.IO, Alamofire, ChatLayout, DifferenceKit, Nuke, WebKit, Swinject, TCA / Combine in the current implementation.

## Practical examples

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Messages and chatbot actions | Developed text, suggested replies, attachments and order navigation. | An interactive interface over a support API. |
| Connection loss | Worked on undelivered messages, reconnection and errors. | Realtime state under network failures. |
| Support within an order | Added deep links and support entry points from orders and payment failures. | Navigation that preserves user context. |
| Long conversations | Fixed scrolling, keyboard behavior, obscured messages and read receipts. | Maintaining a complex UIKit interface. |


## Engineering decisions

- Transport, message state and UI have separate responsibilities. Tapping Send does not mean delivery: intermediate and error states are necessary.
- Authentication and order navigation must work from the support context; unavailable networking and a broken socket connection need separate handling.
- The module evolved over several years: the listed stack reflects its current structure, not only its initial version.

## Quality and checks

- Journeys and requirements were checked against the main chat task and its subtasks. The repository contains snapshots for bubbles, suggested replies and undelivered-message state.
- The fixes show ongoing maintenance after integration, beyond the initial UI implementation.

## Outcome and scope

Support gained a custom mobile interface and product navigation. My contribution included building, integrating and stabilizing parts of this team-owned solution.

<a name="screens"></a>

## Screens and interface states

Original snapshot-test images using prepared data. Each example identifies its source type. Design and overall architecture were team work; my contribution is described above. Select an image to inspect the details.

| Chat reply options |
| :---: |
| <a name="visual-chat-options"></a><a href="../../../assets/screenshots/chat-options.png"><img src="../../../assets/screenshots/chat-options.png" alt="Chat reply options" width="250"></a> |

<details>
<summary>Image context and notes</summary>

- **Chat reply options.** Quick replies as part of a guided support conversation. _Original component snapshot using test data._

</details>

[Full screen and component gallery](../gallery.md)

## Topics for an interview

- How should chat behave after connection loss or an undelivered message?
- What makes scrolling and keyboard handling difficult in a conversation?

[All cases](index.md) · [Practical examples](../archive/index.md) · [Technologies](../engineering/technologies.md)
