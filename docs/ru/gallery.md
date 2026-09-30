[EN](../en/gallery.md) · [Выбор языка / Language](../../README.md)

# Галерея экранов и компонентов

Избранные экраны из моей работы в OneTwoTrip и Solar. **Изображений: 27 · направлений: 9.** Нажмите на превью, чтобы открыть оригинал.

[Оплата и финансы](#financial-screens) · [Состояния](#states) · [Компоненты](#components)

<a name="financial-screens"></a>

## Оплата, балансы и карты

Три технических кейса и оригинальные snapshot-компоненты на тестовых данных. Полный процесс описан в кейсах; ниже показаны отдельные блоки интерфейса.

### Оплата eSIM: цена и подтверждение

SwiftUI · TCA · REST API · 3DS · polling. Детализация и итоговая стоимость — два независимых тестовых состояния компонентов оплаты. В кейсе: промокоды, полная скидка, ошибки и таймер после возвращения из фона.

[Технический разбор и мой вклад](cases/esim.md)

| Цена eSIM: скидка, промокод и итог | Итог и переход к деталям оплаты |
| :---: | :---: |
| <a name="visual-esim-payment-price"></a><a href="../../assets/screenshots/esim-payment-price.png"><img src="../../assets/screenshots/esim-payment-price.png" alt="Цена eSIM: скидка, промокод и итог" width="250"></a> | <a name="visual-esim-payment"></a><a href="../../assets/screenshots/esim-payment.png"><img src="../../assets/screenshots/esim-payment.png" alt="Итог и переход к деталям оплаты" width="250"></a> |

<details>
<summary>Пояснения к компонентам</summary>

- **Цена eSIM: скидка, промокод и итог.** Детализация цены в bottom sheet: базовая стоимость, скидка тарифа, промокод и итог. Значения заданы тестом; это компонент экрана оплаты. _Оригинальный snapshot компонента на тестовых данных._
- **Итог и переход к деталям оплаты.** Компонент с итоговой стоимостью и кнопкой открытия детализации. Это самостоятельный тестовый пример; сумма отличается от примера с промокодом. _Реальный snapshot-baseline компонента на тестовых данных; не снимок production-сессии._

</details>

### Кэшбэк: балансы, карты и лимиты

UIKit · TCA · async/await · REST API. Блоки одного финансового экрана: несколько счетов и единиц баланса, статусы карт и доступные действия. В кейсе: загрузка данных, ошибки и обновление после выпуска карты.

[Технический разбор и мой вклад](cases/loyalty.md)

| Кэшбэк: карты и счета | Повышенный кэшбэк и лимиты карты |
| :---: | :---: |
| <a name="visual-cashback-accounts"></a><a href="../../assets/screenshots/cashback-accounts.png"><img src="../../assets/screenshots/cashback-accounts.png" alt="Кэшбэк: карты и счета" width="250"></a> | <a name="visual-cashback-upgrade"></a><a href="../../assets/screenshots/cashback-upgrade.png"><img src="../../assets/screenshots/cashback-upgrade.png" alt="Повышенный кэшбэк и лимиты карты" width="250"></a> |

<details>
<summary>Пояснения к компонентам</summary>

- **Кэшбэк: карты и счета.** Блок экрана кэшбэка с пластиковой и виртуальной картами, бонусным и накопительным счетами. Балансы и маски карт заданы snapshot-тестом. _Оригинальный snapshot компонента на тестовых данных._
- **Повышенный кэшбэк и лимиты карты.** Состояние блока повышения уровня: лимиты на операцию и месяц, условия кэшбэка и действие перехода. Это тестовый пример интерфейса, а не актуальные банковские условия. _Оригинальный snapshot компонента на тестовых данных._

</details>

### Кабинет карты: состояния и сложные данные

UIKit · Props · SnapshotTesting. Два состояния шапки: выпуск с блокировкой баланса и длинная сумма на ширине 320 pt. В кейсе также разобрана история операций на TCA: фильтр дат, пагинация, обновление и прокрутка.

[Технический разбор и мой вклад](cases/virtual-card.md)

| Карта выпускается: заблокированный баланс | Большая сумма на компактном экране |
| :---: | :---: |
| <a name="visual-card-locked-balance"></a><a href="../../assets/screenshots/card-locked-balance.png"><img src="../../assets/screenshots/card-locked-balance.png" alt="Карта выпускается: заблокированный баланс" width="250"></a> | <a name="visual-card-long-balance"></a><a href="../../assets/screenshots/card-long-balance.png"><img src="../../assets/screenshots/card-long-balance.png" alt="Большая сумма на компактном экране" width="250"></a> |

<details>
<summary>Пояснения к компонентам</summary>

- **Карта выпускается: заблокированный баланс.** Шапка кабинета со статусом выпуска и индикатором блокировки баланса. Статус и доступность денег должны читаться отдельно от суммы. _Оригинальный snapshot компонента на тестовых данных._
- **Большая сумма на компактном экране.** Snapshot при ширине 320 pt: крупная тестовая сумма, дробная часть, валюта и иконка карты. Пример адаптации размера текста к длинному балансу. _Оригинальный snapshot компонента на тестовых данных._

</details>

<a name="states"></a>

## Состояния интерфейса

Дополнительные сценарии: пустые данные, ожидание, компактный экран и восстановление.

<details>
<summary>Stories — коллекция, iPhone SE, пустое состояние</summary>

| Solar Stories: заполненная коллекция | Solar Stories на компактном экране | Сохранённые Stories: пустое состояние |
| :---: | :---: | :---: |
| <a name="visual-stories-solar-grid"></a><a href="../../assets/screenshots/stories-solar-grid.png"><img src="../../assets/screenshots/stories-solar-grid.png" alt="Solar Stories: заполненная коллекция" width="180"></a> | <a name="visual-stories-small-screen"></a><a href="../../assets/screenshots/stories-small-screen.png"><img src="../../assets/screenshots/stories-small-screen.png" alt="Solar Stories на компактном экране" width="180"></a> | <a name="visual-stories-empty"></a><a href="../../assets/screenshots/stories-empty.png"><img src="../../assets/screenshots/stories-empty.png" alt="Сохранённые Stories: пустое состояние" width="180"></a> |

- **Solar Stories: заполненная коллекция.** Полный snapshot экрана с четырьмя историями. Повторяющееся изображение кота — fixture теста. Моя работа включала перенос состояния и интеграцию сохранённой коллекции. _Snapshot-тест на подготовленных данных._
- **Solar Stories на компактном экране.** Вариант для iPhone SE с семью историями: две колонки и продолжение коллекции за границей видимой области. _Snapshot-тест на подготовленных данных._
- **Сохранённые Stories: пустое состояние.** Экран объясняет действие сохранения, когда коллекция ещё пуста. Это отдельное состояние представления. _Snapshot-тест на подготовленных данных._

[Подробный кейс](cases/stories.md)

</details>

<details>
<summary>Оплата — ожидание и ошибка</summary>

| Ожидание внешней оплаты | Ошибка оплаты: длинный текст и два действия |
| :---: | :---: |
| <a name="visual-payment-waiting"></a><a href="../../assets/screenshots/payment-waiting.png"><img src="../../assets/screenshots/payment-waiting.png" alt="Ожидание внешней оплаты" width="200"></a> | <a name="visual-payment-long-error"></a><a href="../../assets/screenshots/payment-long-error.png"><img src="../../assets/screenshots/payment-long-error.png" alt="Ошибка оплаты: длинный текст и два действия" width="200"></a> |

- **Ожидание внешней оплаты.** Полный snapshot общего контейнера оплаты. Пример показывает ожидание возврата из банковского приложения; это вариант SberPay, а не иллюстрация именно СБП. _Snapshot-тест на подготовленных данных._
- **Ошибка оплаты: длинный текст и два действия.** Стрессовый набор данных проверяет, как длинное сообщение сосуществует с действиями «Повторить» и «Закрыть». _Snapshot-тест на подготовленных данных._

[Подробный кейс](cases/payments.md)

</details>

<a name="components"></a>

## Компоненты

Небольшие элементы сгруппированы по продуктовым направлениям.

<details>
<summary>eSIM · 2</summary>

| Баланс eSIM | Карточка тарифа eSIM |
| :---: | :---: |
| <a name="visual-esim-balance"></a><a href="../../assets/screenshots/esim-balance.png"><img src="../../assets/screenshots/esim-balance.png" alt="Баланс eSIM" width="250"></a> | <a name="visual-esim-tariff"></a><a href="../../assets/screenshots/esim-tariff.png"><img src="../../assets/screenshots/esim-tariff.png" alt="Карточка тарифа eSIM" width="250"></a> |

- **Баланс eSIM.** Остаток пакета и состояние услуги в одном компактном блоке. _Реальный snapshot-baseline компонента на тестовых данных; не снимок production-сессии._
- **Карточка тарифа eSIM.** Карточка связывает условия пакета и действие выбора тарифа. _Реальный snapshot-baseline компонента на тестовых данных; не снимок production-сессии._

[Подробный кейс](cases/esim.md)

</details>

<details>
<summary>Карточки и хронология путешествий · 5</summary>

| Карточка путешествия | Элемент истории поездки |
| :---: | :---: |
| <a name="visual-travel-card"></a><a href="../../assets/screenshots/travel-card.png"><img src="../../assets/screenshots/travel-card.png" alt="Карточка путешествия" width="250"></a> | <a name="visual-travel-timeline"></a><a href="../../assets/screenshots/travel-timeline.png"><img src="../../assets/screenshots/travel-timeline.png" alt="Элемент истории поездки" width="250"></a> |

| Статистика путешествий | Железнодорожная точка маршрута |
| :---: | :---: |
| <a name="visual-travel-statistics"></a><a href="../../assets/screenshots/travel-statistics.png"><img src="../../assets/screenshots/travel-statistics.png" alt="Статистика путешествий" width="250"></a> | <a name="visual-travel-rail"></a><a href="../../assets/screenshots/travel-rail.png"><img src="../../assets/screenshots/travel-rail.png" alt="Железнодорожная точка маршрута" width="250"></a> |

| Карточка: длинные даты и несколько типов поездки |
| :---: |
| <a name="visual-travel-card-dense"></a><a href="../../assets/screenshots/travel-card-dense.png"><img src="../../assets/screenshots/travel-card-dense.png" alt="Карточка: длинные даты и несколько типов поездки" width="250"></a> |

- **Карточка путешествия.** Обложка, даты, направление и типы поездки собраны в переиспользуемую карточку. _Реальный snapshot-baseline компонента на тестовых данных; не снимок production-сессии._
- **Элемент истории поездки.** Точка маршрута сохраняет общую хронологию и собственное представление транспорта. _Реальный snapshot-baseline компонента на тестовых данных; не снимок production-сессии._
- **Статистика путешествий.** Статистика используется в нескольких частях истории путешествий. _Реальный snapshot-baseline компонента на тестовых данных; не снимок production-сессии._
- **Железнодорожная точка маршрута.** Транспортный виджет показывает станции, местное время и длительность внутри общей хронологии. _Snapshot-тест на подготовленных данных._
- **Карточка: длинные даты и несколько типов поездки.** Узкий вариант шириной 320 pt с длинным диапазоном дат, числом городов и дополнительными иконками. Видимое сокращение текста — часть проверяемого состояния. _Snapshot-тест на подготовленных данных._

[Подробный кейс](cases/travel-history.md)

</details>

<details>
<summary>Авиа: поиск и тарифы · 2</summary>

| Карточка авиатарифа UI 2.0 | Форма поиска: туда и обратно |
| :---: | :---: |
| <a name="visual-avia-tariff"></a><a href="../../assets/screenshots/avia-tariff.png"><img src="../../assets/screenshots/avia-tariff.png" alt="Карточка авиатарифа UI 2.0" width="250"></a> | <a name="visual-avia-search"></a><a href="../../assets/screenshots/avia-search.png"><img src="../../assets/screenshots/avia-search.png" alt="Форма поиска: туда и обратно" width="250"></a> |

- **Карточка авиатарифа UI 2.0.** Условия авиатарифа и доступное действие в общем визуальном стиле UI 2.0. _Реальный snapshot-baseline компонента на тестовых данных; не снимок production-сессии._
- **Форма поиска: туда и обратно.** Состояние поиска с двумя направлениями и связанными параметрами поездки. _Реальный snapshot-baseline компонента на тестовых данных; не снимок production-сессии._

[Подробный кейс](cases/avia.md)

</details>

<details>
<summary>Общие поля и панель действий · 3</summary>

| Общее поле ввода | Общее поле выбора |
| :---: | :---: |
| <a name="visual-input-field"></a><a href="../../assets/screenshots/input-field.png"><img src="../../assets/screenshots/input-field.png" alt="Общее поле ввода" width="250"></a> | <a name="visual-select-field"></a><a href="../../assets/screenshots/select-field.png"><img src="../../assets/screenshots/select-field.png" alt="Общее поле выбора" width="250"></a> |

| Нижняя панель с ценой и действием |
| :---: |
| <a name="visual-bottom-bar"></a><a href="../../assets/screenshots/bottom-bar.png"><img src="../../assets/screenshots/bottom-bar.png" alt="Нижняя панель с ценой и действием" width="250"></a> |

- **Общее поле ввода.** Общее поле ввода для переиспользования в продуктовых формах. _Реальный snapshot-baseline компонента на тестовых данных; не снимок production-сессии._
- **Общее поле выбора.** Поле выбора с единым отображением значения и состояния. _Реальный snapshot-baseline компонента на тестовых данных; не снимок production-сессии._
- **Нижняя панель с ценой и действием.** Цена и основное действие остаются отдельным переиспользуемым элементом. _Реальный snapshot-baseline компонента на тестовых данных; не снимок production-сессии._

[Подробный кейс](cases/design-system.md)

</details>

<details>
<summary>Виртуальная карта · 2</summary>

| Лимиты карты | Строка финансовой операции |
| :---: | :---: |
| <a name="visual-card-limits"></a><a href="../../assets/screenshots/card-limits.png"><img src="../../assets/screenshots/card-limits.png" alt="Лимиты карты" width="250"></a> | <a name="visual-card-operation"></a><a href="../../assets/screenshots/card-operation.png"><img src="../../assets/screenshots/card-operation.png" alt="Строка финансовой операции" width="250"></a> |

- **Лимиты карты.** Отображение лимитов — часть сценария управления виртуальной картой. _Реальный snapshot-baseline компонента на тестовых данных; не снимок production-сессии._
- **Строка финансовой операции.** Компонент истории: назначение, дата, время, сумма и тип операции. Пагинация, фильтрация и состояния списка разобраны в кейсе карт. _Оригинальный snapshot компонента на тестовых данных._

[Подробный кейс](cases/virtual-card.md)

</details>

<details>
<summary>Программа лояльности · 1</summary>

| Прогресс до статуса Премиум |
| :---: |
| <a name="visual-loyalty-progress"></a><a href="../../assets/screenshots/loyalty-progress.png"><img src="../../assets/screenshots/loyalty-progress.png" alt="Прогресс до статуса Премиум" width="250"></a> |

- **Прогресс до статуса Премиум.** Счётчик, прогресс и условия статуса в UI 2.0. Иллюстрация направления лояльности; общий дизайн и тестовый baseline — работа команды. _Snapshot-тест на подготовленных данных._

[Подробный кейс](cases/loyalty.md)

</details>

<details>
<summary>Чат поддержки · 1</summary>

| Варианты ответа в чате |
| :---: |
| <a name="visual-chat-options"></a><a href="../../assets/screenshots/chat-options.png"><img src="../../assets/screenshots/chat-options.png" alt="Варианты ответа в чате" width="250"></a> |

- **Варианты ответа в чате.** Быстрые ответы как часть управляемого сценария поддержки. _Реальный snapshot-baseline компонента на тестовых данных; не снимок production-сессии._

[Подробный кейс](cases/chat.md)

</details>

---

**Об изображениях.** Дизайн и общая архитектура создавались командой; мой вклад описан в кейсах. Здесь представлены неизменённые snapshot-тесты на подготовленных данных. Исходный язык интерфейса сохранён.

[Все кейсы](cases/index.md) · [Резюме](career/summary.md) · [О материалах](methodology.md)
