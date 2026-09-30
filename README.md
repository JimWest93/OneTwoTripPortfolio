# Valeriy Veselov · iOS Developer

**OneTwoTrip & Solar · 2021–2026**

Swift · UIKit · SwiftUI · TCA · Testing · Jenkins

Продуктовые сценарии, мобильная архитектура и инженерная инфраструктура. Портфолио можно читать прямо на GitHub: выберите язык и интересующее направление.

Product journeys, mobile architecture and engineering infrastructure. Read the portfolio directly on GitHub: choose a language and an area of interest.

## Выберите язык / Choose your language

| Русский | English |
| --- | --- |
| [Полное портфолио](docs/ru/overview.md) | [Full portfolio](docs/en/overview.md) |
| [21 кейс](docs/ru/cases/index.md) | [21 case studies](docs/en/cases/index.md) |
| [Галерея экранов и компонентов](docs/ru/gallery.md) | [Screen and component gallery](docs/en/gallery.md) |
| [Краткое резюме](docs/ru/career/summary.md) | [Professional summary](docs/en/career/summary.md) |
| [Статистика и графики](docs/ru/statistics.md) | [Statistics and charts](docs/en/statistics.md) |

## Избранные кейсы / Selected cases

| Русский | English |
| --- | --- |
| [История путешествий](docs/ru/cases/travel-history.md) — карта, хронология, ручные маршруты | [Travel history](docs/en/cases/travel-history.md) — map, timeline, manual itineraries |
| [Solar Digital Collectibles](docs/ru/cases/digital-collectibles.md) — WebView, нативные экраны, TCA | [Solar Digital Collectibles](docs/en/cases/digital-collectibles.md) — WebView, native screens, TCA |
| [Оплата eSIM](docs/ru/cases/esim.md) — SwiftUI, TCA, REST API, 3DS, промокоды и таймер | [eSIM checkout](docs/en/cases/esim.md) — SwiftUI, TCA, REST API, 3DS, promo codes and timer |
| [Кэшбэк и счета](docs/ru/cases/loyalty.md) — балансы, состояния карт, загрузка данных и ошибки | [Cashback and accounts](docs/en/cases/loyalty.md) — balances, card states, data loading and errors |
| [Карты и операции](docs/ru/cases/virtual-card.md) — лимиты, фильтр дат, пагинация и обновление списка | [Cards and transactions](docs/en/cases/virtual-card.md) — limits, date filtering, pagination and refresh |
| [Jenkins](docs/ru/engineering/ci-details.md) — сборки, проверки и инструменты | [Jenkins](docs/en/engineering/ci-details.md) — builds, checks and tooling |

Обе языковые версии полные. Переключатель в начале каждой страницы ведёт к её переводу.

Both language editions are complete. The link at the top of each page opens its translation.

<details>
<summary>Для сопровождения репозитория / Repository maintenance</summary>

Основные материалы находятся в `docs/`. Каталог `site/` содержит дополнительную HTML-версию; для чтения портфолио на GitHub она не требуется.

The primary reading experience is in `docs/`. The `site/` directory contains an additional HTML edition; it is not required to read the portfolio on GitHub.

**Сборка / Build**

```sh
python3 -m venv .research/venv
.research/venv/bin/pip install -r scripts/requirements.txt
.research/venv/bin/python scripts/build_charts.py
.research/venv/bin/python scripts/build_portfolio.py
.research/venv/bin/python scripts/validate.py
```

</details>
