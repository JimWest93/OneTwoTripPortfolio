"""Editorial gallery: product screens first, then optional supporting material."""
from html import escape
from github_layout import financial_collections


def build_gallery(images, lang, image_url):
    t = lambda ru, en: ru if lang == 'ru' else en
    titles = {
        'nft-system': t('Планетарная система', 'Planetary system'),
        'nft-locked': t('Закрытая награда', 'Locked reward'),
        'nft-available': t('Полученная награда', 'Earned reward'),
        'nft-wallet': t('Награда в кошельке', 'Reward in wallet'),
        'travel-map': t('Карта поездок', 'Trip map'),
        'travel-list': t('Список путешествий', 'Trip list'),
        'travel-details': t('Детали маршрута', 'Itinerary details'),
        'travel-onboarding': t('Подготовка карты', 'Preparing the map'),
        'travel-undo': t('Отмена удаления', 'Undo deletion'),
        'stories-solar-grid': t('Коллекция Stories', 'Stories collection'),
        'stories-small-screen': t('Компактный экран', 'Compact screen'),
        'stories-empty': t('Пустая коллекция', 'Empty collection'),
        'payment-waiting': t('Ожидание оплаты', 'Payment pending'),
        'payment-long-error': t('Ошибка и повтор', 'Error and retry'),
    }
    def shot(id):
        x = images[id]
        title = escape(titles.get(id, x['caption']))
        url = image_url(x)
        description = escape(x['description'] if lang == 'ru' else x['descriptionEn'])
        origin = escape(x['kind'] if lang == 'ru' else x['kindEn'])
        return f'''<figure class="gallery-shot shot-{x['format']}" id="visual-{id}">
<a class="shot-image" href="{url}" aria-label="{t('Открыть в полном размере: ', 'Open full size: ')}{title}"><img loading="lazy" decoding="async" width="{x['width']}" height="{x['height']}" src="{url}" alt="{escape(x['caption'])}"></a>
<figcaption><strong>{title}</strong><details class="shot-notes"><summary>{t('О снимке', 'About this image')}</summary><p>{description}</p><p class="shot-origin">{origin}</p><a href="{url}">{t('Полный размер', 'Full size')} ↗</a></details></figcaption></figure>'''

    def shots(ids, extra=''):
        return '<div class="shot-grid '+extra+'">'+''.join(shot(id) for id in ids)+'</div>'

    def chapter(id, number, title, text):
        return f'<div class="gallery-chapter" id="{id}"><span class="chapter-number">{number}</span><div><h2>{title}</h2><p>{text}</p></div></div>'

    def collection(slug, title, text, ids, theme):
        return f'''<section class="screen-collection collection-{theme}" aria-labelledby="collection-{slug}"><div class="collection-intro"><p class="eyebrow">{t('Продуктовый сценарий', 'Product journey')}</p><h3 id="collection-{slug}">{title}</h3><p>{text}</p><a class="collection-link" href="cases/{slug}.md">{t('Мой вклад и решения', 'My contribution and decisions')} ↗</a></div>{shots(ids)}</section>'''

    def disclosure(id, title, text, ids, case, open=False):
        count = f'{len(ids):02d}'
        return f'''<details class="gallery-folder" id="{id}"{' open' if open else ''}><summary><span class="folder-count">{count}</span><span class="folder-label"><strong>{title}</strong><span>{text}</span></span><span class="folder-toggle" aria-hidden="true"></span></summary><div class="folder-content">{shots(ids)}<a class="folder-case" href="cases/{case}.md">{t('Открыть подробный кейс', 'Read the full case')} ↗</a></div></details>'''

    chunks = [t('# Интерфейсы в деталях.', '# Interfaces, in detail.')]
    chunks.append('<div class="gallery-intro"><p>'+t(
        'Оплата, финансовые интерфейсы и состояния продукта. Snapshot-тесты экранов и компонентов из моей работы над OneTwoTrip и Solar.',
        'Payments, financial interfaces and product states. Screen and component snapshots from my work on OneTwoTrip and Solar.')+'</p><span class="gallery-total">'+t(f'Изображений: {len(images)} · направлений: {len({x["case"] for x in images.values()})}', f'{len(images)} images · {len({x["case"] for x in images.values()})} areas')+'</span></div>')
    nav = [('financial-screens',t('Оплата и финансы','Payments and finance')),('interface-states',t('Состояния','States')),('ui-components',t('Компоненты','Components'))]
    chunks.append('<nav class="gallery-navigation" aria-label="'+t('Разделы галереи','Gallery sections')+'">'+''.join(f'<a href="#{id}"><span>{i:02d}</span>{label}</a>' for i,(id,label) in enumerate(nav,1))+'</nav>')
    chunks.append(chapter('financial-screens','01',t('Оплата, балансы и карты','Payments, balances and cards'),t('Три технических кейса и оригинальные snapshot-компоненты на тестовых данных. Здесь показаны отдельные блоки интерфейса.', 'Three technical cases with original component snapshots using test data. These images show individual interface blocks.')))
    featured = set()
    for slug,title,intro,ids in financial_collections(lang):
        featured.update(ids)
        chunks.append(collection(slug,title,intro,ids,'finance'))
    chunks.append(chapter('interface-states','02',t('Что происходит между экранами.','What happens between screens.'),t('Загрузка, пустые данные, компактная раскладка и восстановление после ошибки. Откройте интересующий сценарий.','Loading, empty data, compact layouts and error recovery. Expand a journey to explore its states.')))
    chunks.append(disclosure('states-stories','Stories',t('Коллекция, iPhone SE и пустое состояние','Collection, iPhone SE and empty state'),['stories-solar-grid','stories-small-screen','stories-empty'],'stories'))
    chunks.append(disclosure('states-payments',t('Оплата','Payments'),t('Ожидание внешнего приложения и ошибка с повтором','External-app handoff and an error with retry'),['payment-waiting','payment-long-error'],'payments'))
    chunks.append(chapter('ui-components','03',t('Детали, из которых собран продукт.','The details that build the product.'),t('Небольшие элементы сгруппированы по назначению. Выберите направление, чтобы увидеть примеры.','Smaller elements grouped by purpose. Choose an area to see the examples.')))
    groups = [
        ('esim','eSIM',t('Тариф и баланс пакета','Plan and package balance')),
        ('travel-history',t('Карточки путешествий','Travel cards'),t('Поездка, хронология и статистика','Trip, timeline and statistics')),
        ('avia',t('Авиа','Flights'),t('Форма поиска и условия тарифа','Search form and fare conditions')),
        ('design-system',t('Общие элементы UI','Shared UI'),t('Поля ввода, выбор и основное действие','Input, selection and primary action')),
        ('virtual-card',t('Виртуальная карта','Virtual card'),t('Лимиты и строка операции','Limits and an operation row')),
        ('loyalty',t('Лояльность','Loyalty'),t('Прогресс до следующего статуса','Progress toward the next status')),
        ('chat',t('Чат поддержки','Support chat'),t('Быстрые варианты ответа','Quick reply options')),
    ]
    for slug,title,text in groups:
        ids = [x['id'] for x in images.values() if x['case']==slug and x['format']=='component' and x['id'] not in featured]
        if not ids: continue
        chunks.append(disclosure('components-'+slug,title,text,ids,slug))
    chunks.append('<aside class="gallery-provenance"><h2>'+t('Об изображениях','About the images')+'</h2><p>'+t('Дизайн и общая архитектура — командная работа. Мой вклад описан в кейсах. В галерее представлены оригинальные snapshot-тесты на подготовленных данных; язык интерфейса сохранён.','Design and overall architecture are team work. The cases describe my contribution. This gallery contains original snapshot-test baselines using prepared data, preserving their interface language.')+'</p><a href="methodology.md">'+t('Подробнее о материалах','More about the materials')+' ↗</a></aside>')
    return '\n\n'.join(chunks)
