[RU](../../ru/archive/index.md) · [Language selection](../../../README.md)

# Practical examples

84 selected examples from 21 cases: scenario, my contribution and technical focus. Find experience relevant to a role. Examples overlap and do not add up to a count of released features.

## Product journeys

### [eSIM: SwiftUI, payments, 3DS and service management](../cases/esim.md)

**2025–2026** · Swift, SwiftUI + UIKit / UIHostingController, TCA, Combine, Swift Concurrency / async-await, Swinject, REST / Codable, 3DS, Tuist, XCTest / SnapshotTesting / XCUITest

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Buying mobile data | Connected the catalog, plan selection, authentication and payment screen into one journey. | An end-to-end flow spanning several modules. |
| Payment and returning to the app | Worked on 3DS, status polling, errors and recalculating the payment timer after backgrounding. | Asynchronous state and the application lifecycle. |
| Topping up an existing eSIM | Extended order details, balance and top-ups, preserving differences between purchase and top-up data. | Shared mechanisms with different business rules. |
| Accessing the service while traveling | Contributed to offline states and setup guidance; added checks for key journeys. | Network constraints and testing. |


### [Travel history: maps, trips and personal journeys](../cases/travel-history.md)

**2025–2026** · Swift, SwiftUI + UIKit, TCA, Combine, Swinject, CoreLocation, Map SDK abstraction / YandexMapKit, REST, XCTest / SnapshotTesting / XCUITest

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Trip map and list | Built pins, clusters, a carousel and list sheet; fixed synchronization after changes. | Consistent state across multiple views. |
| Manual itinerary creation | Developed route-point entry, location selection and trip-detail editing. | Forms, validation and reusable search. |
| Trip details | Worked on the timeline and presentation of different transport types. | Turning heterogeneous data into a clear interface. |
| Checking trip changes | Covered creation, editing and errors with unit and UI tests. | Testable business logic and user journeys. |


### [A custom support chat replacing the Zendesk SDK](../cases/chat.md)

**2022–2024** · Swift, UIKit, Socket.IO, Alamofire, ChatLayout, DifferenceKit, Nuke, WebKit, Swinject, TCA / Combine in the current implementation

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Messages and chatbot actions | Developed text, suggested replies, attachments and order navigation. | An interactive interface over a support API. |
| Connection loss | Worked on undelivered messages, reconnection and errors. | Realtime state under network failures. |
| Support within an order | Added deep links and support entry points from orders and payment failures. | Navigation that preserves user context. |
| Long conversations | Fixed scrolling, keyboard behavior, obscured messages and read receipts. | Maintaining a complex UIKit interface. |


### [Solar: launching and developing a separate app](../cases/solar.md)

**2022–2024** · Swift, UIKit, Tuist / multi-target, Coordinator, Swinject, TCA, WebKit, AVKit / Lottie, AppsFlyer / Adjust, XCUITest

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Composing a separate app | Contributed to the Solar target, AppDelegate, Coordinator and tab bar. | A separate product on a shared codebase. |
| Home screen | Developed menus, Stories, banners and unfinished bookings. | Configurable product-screen composition. |
| Sign-in and section navigation | Worked on authentication, profile, orders and quick actions. | Consistent user journeys. |
| Different configurations | Handled currencies, links, analytics and regressions following shared changes. | Maintaining multiple application variants. |


### [Solar Digital Collectibles: native UI and WebView](../cases/digital-collectibles.md)

**2023–2024** · Swift, UIKit, WebKit / native–web communication, TCA, Combine, REST, LinkPresentation, Swinject, XCTest

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Planets and achievement lists | Created cards, the sheet list, zoom controls and supporting actions. | A distinctive interface and navigation model. |
| Native screen and WebView | Integrated the achievements API, WebView communication and reward-screen logic. | Connecting different presentation technologies. |
| Achievement actions | Added claiming, wallet actions, sharing and universal links. | Product actions connected to external navigation. |
| Moving state to TCA | Contributed to module migration, wrote unit tests and handled errors. | State architecture and testability. |


### [Profile, personal details and notifications](../cases/profile.md)

**2023–2026** · Swift, UIKit, TCA, PropsBuilder, Swinject, Nuke, Push notifications, REST, XCTest / XCUITest

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Profile across sign-in states | Moved the Solar profile to TCA and developed its header and account sections. | Screen composition and state lifecycle. |
| Editing personal details | Worked on UI 2.0 fields, validation and support navigation for contact changes. | Forms and product-contract constraints. |
| Notification channels | Implemented UI, business logic and scrolling to unread messages. | Aligning data, navigation and presentation. |
| Widgets and social journeys | Added favorites, statistics and travel history in other users&#x27; profiles. | Module reuse and user context. |


### [Cashback and accounts: balances, cards and screen states](../cases/loyalty.md)

**2023–2025** · Swift, UIKit, TCA, Swift Concurrency / async-await, PropsBuilder, Swinject, REST / mapping, SnapshotTesting, XCTest, XCUITest

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Solar Cash balance | Added credit/debit history, empty states and hotel integration. | Financial data within a product interface. |
| New cashback screen | Migrated card, Tripcoin and boosted-cashback blocks to UI 2.0. | Migrating a complex screen while preserving rules. |
| Controlled UI rollout | Separated old and new implementations and added configuration and a feature flag. | Incremental introduction of changes. |
| Edge states | Checked card statuses, network errors and updates after tier changes. | Systematic checks of financial journeys. |


### [Cards and transaction history: limits, pagination and states](../cases/virtual-card.md)

**2024–2025** · Swift, UIKit, TCA, Presenter / Interactor / Router, REST, Swinject, Props, SnapshotTesting, XCTest, XCUITest

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Card account | Worked on virtual and physical cards, issuance states and transactions. | Multiple states of a financial product. |
| Limits and servicing | Implemented spending limits, a dedicated screen and service terms. | Clear presentation of product constraints. |
| Financial transaction history | Developed transaction and bonus lists, a date filter and pagination resets on period changes and refresh; fixed scrolling. | TCA, REST API, pagination and list states. |
| Checking user journeys | Developed issuance, identity and error tests; used targeted deep links. | Testability and UI-test maintenance. |


### [Stories: architecture, video and interactive journeys](../cases/stories.md)

**2024–2026** · Swift, UIKit, TCA, Combine, AVFoundation / video integration, Nuke, Swinject, REST, XCTest / SnapshotTesting / XCUITest

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Separating Stories modules | Moved state to TCA and separated catalog, preview, slides and infrastructure. | Architectural migration of an existing feature. |
| Preparing video | Replaced loading every slide upfront with bounded media preparation. | Resource management in a media journey. |
| Interactive giveaway | Developed the decision slide, backend participation and dynamic branches. | A journey driven by user choices and effects. |
| Sign-in over a story | Worked on authentication, return to viewing and successful-sign-in analytics. | Preserving context across external navigation. |


### [Flights: search forms, fares and order journeys](../cases/avia.md)

**2022–2026** · Swift, UIKit, TCA, PropsBuilder, Swinject, Common UI components, Feature flags, XCTest / SnapshotTesting / XCUITest

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| UI 2.0 search form | Built simple and multi-city routes with shared components, events and UI checks. | A product form with multiple modes. |
| Fare selection | Moved cards, prices, selection and the booking transition to UI 2.0. | Updating UI while preserving purchase rules. |
| Order maintenance | Fixed parameters, statuses, documents, filters and navigation. | Regression work across a long product journey. |
| Additional services | Worked on seats in existing orders and eSIM offers. | Integrating related products into order context. |


### [Business-trip journeys inside the consumer app](../cases/b2b-scenarios.md)

**2026** · Swift, UIKit, TCA / state management, Feature flags, REST, Cross-module configuration, XCUITest

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Business-trip search | Added the business-trip flag to flights, hotels and trains. | One journey across multiple product areas. |
| Profile and order entry points | Implemented profile sheets and a banner placement in rail orders. | Coordinated cross-module navigation. |
| Backend-contract changes | Refined banner requests and corporate-card checks after requirements changed. | Adapting client logic to an API. |
| Checking combined journeys | Added and fixed UI tests for business trips inside the consumer app. | Integration checks of the user journey. |


### [Payment integrations and completing a purchase](../cases/payments.md)

**2022–2026** · Swift, UIKit / SwiftUI, WebKit, 3DS, REST / polling, TCA, Coordinator, BridgerPay / NowPayments integrations, XCUITest

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| External payment providers | Integrated BridgerPay in hotels and maintained NowPayments in Solar. | Client-side integration of payment journeys. |
| Waiting for SBP payment | Worked on the shared payment loader and its UI tests. | Reusable presentation of an intermediate state. |
| Buying an eSIM | Developed payment UI, backend interaction, contact handling and order navigation. | Orchestrating several purchase steps. |
| Returning after failure | Fixed order state after payment errors and completion of external journeys. | Error handling and interface recovery. |


### [Hotels, trains and everyday product reliability](../cases/product-maintenance.md)

**2021–2026** · Swift, UIKit, Legacy Objective-C interoperability, REST, WebKit, DateFormatter / localization, Navigation / coordinators, Debugging

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Hotel journeys | Fixed favorites, reviews, galleries, search results, calendars and post-search navigation. | Diagnosing regressions in an existing product. |
| Rail orders | Worked on cancellation documents, post-payment-error state and electronic registration. | Aligning client UI with order state. |
| Shared order list | Refined refresh, empty states, archived links and authentication. | Reusable navigation and data updates. |
| Platform behavior | Fixed dates, locales, offline WebViews, the keyboard and small screens. | Reliability across different environments. |


## Shared components

### [Authentication across different product journeys](../cases/auth.md)

**2022–2024** · Swift, UIKit, Presenter / Interactor / Router, Swinject, REST, Deep Links / Universal Links, WebKit, Apple ID / Google ID integrations, XCUITest

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Continuing checkout after sign-in | Worked on email/PIN, switching to phone and requesting missing contacts. | Authentication as part of a product journey. |
| Repeat sign-in on a device | Developed repeat authentication and consistent user-session behaviour. | Session state and reusable flows. |
| Signing in to Solar | Contributed to magic links, Apple ID, Google ID and incoming links. | Integration of multiple authentication methods. |
| Errors and repeated actions | Handled CAPTCHA, missing connectivity, code resends and method changes. | Explicit edge states and validation. |


### [A shared calendar across product areas](../cases/calendar.md)

**2022–2023** · Swift, UIKit, UICollectionView, Props / render, Presenter / Interactor / Router, Swinject, Tuist, Localization / DateFormatter

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Shared date selection | Developed calendar configuration, public entry points, presenter and PropsBuilder. | Designing a reusable UI module. |
| Different product areas | Integrated the calendar into flights, hotels and trains while preserving constraints. | A shared component with product configuration. |
| Returning to a selected date | Fixed initial scrolling and editing an existing date range. | Correct state restoration. |
| Locales and working days | Worked on months, weekdays, weekends and the working-day calendar. | Localization and calendar behavior. |


### [Shared UI components and the move to UI 2.0](../cases/design-system.md)

**2022–2026** · Swift, UIKit, SwiftUI interoperability, Props, PinLayout, Design tokens / styles, SnapshotTesting, XCTest, Accessibility identifiers

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Consistent input fields | Developed input fields and search fields with errors, disabled states, icons and compact presentation. | A shared component&#x27;s contract and states. |
| Selection fields and controls | Extended selection fields, the segmented control and floating buttons. | Interface composition across screens. |
| Bottom action bar | Added bottom action bars variants with prices, long text, buttons and loading. | Flexible layout and action states. |
| New styles across the app | Updated buttons, the palette and component consumers in product modules. | A staged migration in a large application. |


## Quality

### [Quality: unit, snapshot and user-journey checks](../cases/quality.md)

**2023–2026** · XCTest, XCUITest, SnapshotTesting, TCA TestStore, Mocks, Accessibility identifiers, Allure, Jenkins

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Checking business state | Wrote unit tests for profiles, achievements, finance, eSIM and trips. | Testing logic independently of appearance. |
| Checking components | Added snapshots for UI sizes, text and states. | Visual regressions and the design system. |
| End-to-end journeys | Developed XCUITest flows for sign-in, purchases, profiles and integrations. | Checking app behavior from the user&#x27;s perspective. |
| Maintaining tests | Maintained mocks and accessibility identifiers, fixed instability and used deep links. | Practical maintenance of automated checks. |


## Engineering tools

### [Jenkins: build diagnostics and CI maintenance](../cases/jenkins.md)

**2025–2026** · Jenkins Declarative Pipeline, Groovy, Bash, Ruby / Fastlane, macOS agents, Firebase Crashlytics dSYM, mise, Git

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Uploading dSYMs | Created a pipeline selecting artifacts by app/build, uploading in parallel and retrying failures. | Automating iOS diagnostics. |
| Maintaining a macOS agent | Added a manual cleanup pipeline with checks and free-space measurements. | Controlled operations on the CI environment. |
| Build and review context | Added agent names to build information and completed-review reporting. | Diagnostics and team workflow. |
| Isolating Ruby | Worked with pinned Ruby, user gems and shared cleanup. | Reproducible infrastructure scripts. |


### [Repository metrics: history, test analysis and delivery](../cases/repository-metrics.md)

**2026** · Swift / SwiftSyntax, Swift Package Manager, Ruby, Python, Bash, Groovy / Jenkins CPS, Static code analysis / cloc, VictoriaMetrics, Grafana, mise

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Historical calculation | Added monthly Git-state backfill and fixed timestamps. | Reproducible analysis of repository history. |
| Static test analysis | Developed a SwiftSyntax XCTest/Quick analyzer with Codex and explicit diagnostic limits. | Source analysis and correct metric semantics. |
| Delivery after network failure | Separated payload and progress, added batches, retries and Restart from Stage. | Recovery of a long infrastructure operation. |
| Checking Jenkins behavior | Added bootstrap and a local fixture for sandbox/CPS and recovery. | Infrastructure checks outside production. |


### [Documentation, AI tools and engineering workflow](../cases/engineering-workflow.md)

**2026** · Codex, Repository skills, Jira / Bitbucket integrations, Markdown, Tuist manifests, Ruby / Python tooling, Git / release workflow

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| From analysis to a task | Developed and refined a workflow that turns systems analysis into mobile stories. | Formalizing input requirements for development. |
| Module documentation | Created a README preparation/update process and applied it to eSIM and Stories. | Maintaining the team&#x27;s architectural context. |
| Working with AI tools | Used agents for research and implementation, recorded their contribution and checked results. | Setting constraints and evaluating generated changes. |
| Application variants | Contributed to OTT, Solar and KZ release configuration. | Managing product differences on a shared foundation. |


### [Systems analysis and technical documentation](../cases/analysis-documentation.md)

**2023–2026** · Systems analysis, Confluence / Jira, API contracts, Backward compatibility, Feature configuration, Deep links and analytics

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Manual trip creation | Analyzed city/date selection, timeline refresh, segment deletion and restoration. | Systems analysis of a user journey. |
| Data compatibility | Examined editability flags and optional fields&#x27; impact on older versions. | API agreement and backward compatibility. |
| Configuration contracts | Documented Solar, home-screen widgets and Quick Actions for colleagues. | Technical documentation people can use. |
| Clarifying mobile requirements | Contributed to formalizing B2B journeys and offline eSIM access. | Connecting product requirements with client implementation. |
