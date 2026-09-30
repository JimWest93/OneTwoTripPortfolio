[EN](../../en/engineering/technologies.md) · [Выбор языка / Language](../../../README.md)

# Технологии и инженерные практики

Матрица показывает технологии в областях подтверждённого вклада. Она не утверждает первичное авторство общей архитектуры или всех используемых библиотек.

| Область | Практика и технологии | Где проявляется |
| --- | --- | --- |
| Язык и платформенный UI | Swift, UIKit, SwiftUI; интеграция через UIHostingController | [eSIM](../cases/esim.md), [авиа](../cases/avia.md), [UI-компоненты](../cases/design-system.md) |
| Модульность | Tuist, отдельные feature/infrastructure-модули, публичные интерфейсы | [история путешествий](../cases/travel-history.md), [Solar](../cases/solar.md) |
| Состояние и эффекты | TCA, Combine, однонаправленный поток состояния; PropsBuilder для представления | [Stories](../cases/stories.md), [eSIM](../cases/esim.md) |
| Существующая архитектура | Presenter / Interactor / Router; DI через Swinject | [календарь](../cases/calendar.md), [чат](../cases/chat.md), [авторизация](../cases/auth.md) |
| Компоновка UIKit | Общие стили, PinLayout, конфигурируемые компоненты | [UI 2.0](../cases/design-system.md), [календарь](../cases/calendar.md) |
| Сеть и модели | REST, Codable; Alamofire и Socket.IO в текущем модуле чата | [чат](../cases/chat.md), [eSIM](../cases/esim.md) |
| Навигация | Router/coordinator, диплинки, продолжение действия после авторизации | [вход](../cases/auth.md), [B2B](../cases/b2b-scenarios.md), [платежи](../cases/payments.md) |
| Платёжный путь | 3DS, polling статуса, таймер, возврат из фона, банковские и сохранённые карты | [eSIM](../cases/esim.md), [платежи](../cases/payments.md) |
| Медиа и web | WebKit, AVKit, Lottie; загрузка изображений Nuke в актуальных модулях | [Digital Collectibles](../cases/digital-collectibles.md), [Stories](../cases/stories.md) |
| Продуктовая конфигурация | Feature flags, разные flavor приложения, локали, BI-события | [Solar](../cases/solar.md), [B2B](../cases/b2b-scenarios.md), [SA](../cases/analysis-documentation.md) |
| Автоматизированные проверки | XCTest, SnapshotTesting, XCUITest, accessibility identifiers | [качество](../cases/quality.md), [карта](../cases/virtual-card.md), [лояльность](../cases/loyalty.md) |
| CI/CD | Jenkins/Groovy, Fastlane/Ruby, dSYM, macOS build agents | [Jenkins](../cases/jenkins.md) |
| Метрики и инструменты | SwiftSyntax, статический анализ тестов, Python, Ruby, HTTP delivery | [метрики](../cases/repository-metrics.md) |
| Командный контекст | Git/Bitbucket, Jira, Confluence, SA и README модулей | [документация](../cases/analysis-documentation.md), [процессы](../cases/engineering-workflow.md) |

## Архитектурные темы для обсуждения на собеседовании

1. Как отделить состояние и эффекты экрана от навигации, особенно в платёжной оркестрации.
2. Как проектировать общий компонент, когда разные вертикали имеют разные ограничения дат и сценарии использования.
3. Как обновлять UI существующего продукта, сохраняя бизнес-правила, аналитику и корректность переходов.
4. Что сохранять при возврате из авторизации или из фона и как пересчитывать абсолютный дедлайн оплаты.
5. Как выбирать уровень проверки: бизнес-состояния — unit, внешний вид — snapshot, пользовательский маршрут — UI/E2E.
6. Как обеспечить повторяемую доставку метрик при временных ошибках сети и перезапуске Jenkins stage.
7. Почему статический подсчёт тестов, количество прогонов и code coverage — разные метрики.

Ответы следует строить вокруг конкретных решений из кейсов. Наличие технологии в таблице не означает одинаковую глубину опыта во всех её возможностях.
