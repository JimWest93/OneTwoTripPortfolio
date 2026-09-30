[RU](../../ru/engineering/technologies.md) · [Language selection](../../../README.md)

# Technologies and engineering practices

This matrix covers technologies in areas of verified contribution. It does not claim original authorship of the overall architecture or every library used.

| Area | Practices and technologies | Relevant work |
| --- | --- | --- |
| Language and platform UI | Swift, UIKit, SwiftUI; UIHostingController integration | [eSIM](../cases/esim.md), [flights](../cases/avia.md), [UI components](../cases/design-system.md) |
| Modularity | Tuist, separate feature/infrastructure modules, public interfaces | [Travel history](../cases/travel-history.md), [Solar](../cases/solar.md) |
| State and effects | TCA, Combine, unidirectional state flow; PropsBuilder for presentation | [Stories](../cases/stories.md), [eSIM](../cases/esim.md) |
| Existing architecture | Presenter / Interactor / Router; dependency injection with Swinject | [Calendar](../cases/calendar.md), [chat](../cases/chat.md), [authentication](../cases/auth.md) |
| UIKit layout | Shared styles, PinLayout, configurable components | [UI 2.0](../cases/design-system.md), [calendar](../cases/calendar.md) |
| Networking and models | REST, Codable; Alamofire and Socket.IO in the current chat module | [Chat](../cases/chat.md), [eSIM](../cases/esim.md) |
| Navigation | Routers/coordinators, deep links, continuing actions after sign-in | [Authentication](../cases/auth.md), [business trips](../cases/b2b-scenarios.md), [payments](../cases/payments.md) |
| Payment journeys | 3DS, status polling, timers, background return, bank and saved cards | [eSIM](../cases/esim.md), [payments](../cases/payments.md) |
| Media and web | WebKit, AVKit, Lottie; Nuke image loading in current modules | [Digital Collectibles](../cases/digital-collectibles.md), [Stories](../cases/stories.md) |
| Product configuration | Feature flags, application flavors, locales, analytics events | [Solar](../cases/solar.md), [business trips](../cases/b2b-scenarios.md), [systems analysis](../cases/analysis-documentation.md) |
| Automated checks | XCTest, SnapshotTesting, XCUITest, accessibility identifiers | [Quality](../cases/quality.md), [virtual card](../cases/virtual-card.md), [loyalty](../cases/loyalty.md) |
| CI/CD | Jenkins/Groovy, Fastlane/Ruby, dSYMs, macOS build agents | [Jenkins](../cases/jenkins.md) |
| Metrics and tools | SwiftSyntax, static test analysis, Python, Ruby, HTTP delivery | [Metrics](../cases/repository-metrics.md) |
| Team context | Git/Bitbucket, Jira, Confluence, systems analysis and module READMEs | [Documentation](../cases/analysis-documentation.md), [workflow](../cases/engineering-workflow.md) |

## Architecture topics for an interview

1. Separating screen state and effects from navigation, especially in payment orchestration.
2. Designing a shared component when product areas have different date constraints and use cases.
3. Updating an existing product's UI while preserving business rules, analytics and navigation.
4. Deciding what to preserve after authentication or backgrounding, and recalculating an absolute payment deadline.
5. Choosing the right check: unit tests for business state, snapshots for appearance, UI/E2E for journeys.
6. Making metric delivery repeatable under temporary network errors and Jenkins stage restarts.
7. Distinguishing static test counts, execution counts and code coverage.

Answers should draw on concrete decisions in the cases. A technology appearing here does not imply equal depth across every one of its capabilities.
