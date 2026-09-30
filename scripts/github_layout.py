"""Portable Markdown layouts for reading directly on GitHub without CSS."""
from html import escape


def financial_collections(lang):
    t = lambda ru, en: ru if lang == 'ru' else en
    return [
        ('esim', t('Оплата eSIM: цена и подтверждение', 'eSIM checkout: pricing and confirmation'),
         t('SwiftUI · TCA · REST API · 3DS · polling. Детализация и итоговая стоимость — два независимых тестовых состояния компонентов оплаты. В кейсе: промокоды, полная скидка, ошибки и таймер после возвращения из фона.',
           'SwiftUI · TCA · REST API · 3DS · polling. The price breakdown and final total are two independent checkout-component test states. The case covers promo codes, full discounts, errors and the timer after app resumption.'),
         ['esim-payment-price', 'esim-payment']),
        ('loyalty', t('Кэшбэк: балансы, карты и лимиты', 'Cashback: balances, cards and limits'),
         t('UIKit · TCA · async/await · REST API. Блоки одного финансового экрана: несколько счетов и единиц баланса, статусы карт и доступные действия. В кейсе: загрузка данных, ошибки и обновление после выпуска карты.',
           'UIKit · TCA · async/await · REST API. Blocks from one financial screen: multiple accounts and balance units, card statuses and available actions. The case covers data loading, errors and refresh after card issuance.'),
         ['cashback-accounts', 'cashback-upgrade']),
        ('virtual-card', t('Кабинет карты: состояния и сложные данные', 'Card account: states and challenging data'),
         t('UIKit · Props · SnapshotTesting. Два состояния шапки: выпуск с блокировкой баланса и длинная сумма на ширине 320 pt. В кейсе также разобрана история операций на TCA: фильтр дат, пагинация, обновление и прокрутка.',
           'UIKit · Props · SnapshotTesting. Two header states: issuance with a locked balance, and a long amount at 320 pt width. The case also explores TCA transaction history: date filtering, pagination, refresh and scrolling.'),
         ['card-locked-balance', 'card-long-balance']),
    ]


def image_tables(ids, images, image_url, lang, columns=2, titles=None):
    titles = titles or {}
    chunks = []
    for start in range(0, len(ids), columns):
        batch = ids[start:start+columns]
        headings, cells = [], []
        for id in batch:
            x = images[id]
            title = titles.get(id, x['caption'])
            headings.append(escape(title).replace('|', '&#124;'))
            width = 200 if x['format']=='screen' else 250
            if columns == 3: width = 180 if x['format']=='screen' else 210
            if x['format']=='comparison': width = 640
            url = escape(image_url(x), quote=True)
            cells.append(f'<a name="visual-{id}"></a><a href="{url}"><img src="{url}" alt="{escape(x["caption"],quote=True)}" width="{width}"></a>')
        chunks.append('| '+' | '.join(headings)+' |\n| '+' | '.join([':---:']*len(batch))+' |\n| '+' | '.join(cells)+' |')
    return '\n\n'.join(chunks)


def image_notes(ids, images, lang):
    lines = []
    for id in ids:
        x = images[id]
        description = x['description'] if lang=='ru' else x['descriptionEn']
        origin = x['kind'] if lang=='ru' else x['kindEn']
        lines.append(f'- **{x["caption"]}.** {description} _{origin}_')
    return '\n'.join(lines)


def disclosure(title, body):
    return f'<details>\n<summary>{escape(title)}</summary>\n\n{body}\n\n</details>'


def case_images(ids, images, image_url, lang):
    chunks=[]
    for kind in ['screen','component','comparison']:
        selected=[id for id in ids if images[id]['format']==kind]
        if selected:chunks.append(image_tables(selected,images,image_url,lang))
    chunks.append(disclosure('Сценарии и пояснения к изображениям' if lang=='ru' else 'Image context and notes',image_notes(ids,images,lang)))
    return '\n\n'.join(chunks)


def github_gallery(images, lang, image_url):
    t=lambda ru,en:ru if lang=='ru' else en
    count, areas = len(images), len({x['case'] for x in images.values()})
    chunks=[t('# Галерея экранов и компонентов','# Screens and components'),t(f'Избранные экраны из моей работы в OneTwoTrip и Solar. **Изображений: {count} · направлений: {areas}.** Нажмите на превью, чтобы открыть оригинал.',f'Selected screens from my work at OneTwoTrip and Solar. **{count} images · {areas} areas.** Select a preview to open the original.')]
    chunks += [' · '.join(f'[{title}](#{anchor})' for title,anchor in [(t('Оплата и финансы','Payments and finance'),'financial-screens'),(t('Состояния','States'),'states'),(t('Компоненты','Components'),'components')])]
    chunks += ['<a name="financial-screens"></a>\n\n## '+t('Оплата, балансы и карты','Payments, balances and cards'),t('Три технических кейса и оригинальные snapshot-компоненты на тестовых данных. Полный процесс описан в кейсах; ниже показаны отдельные блоки интерфейса.', 'Three technical cases with original component snapshots using test data. The cases explain the complete journeys; the images below show individual interface blocks.')]
    featured = set()
    for case, title, intro, ids in financial_collections(lang):
        featured.update(ids)
        chunks += ['### '+title, intro, f'[{t("Технический разбор и мой вклад", "Technical breakdown and my contribution")}](cases/{case}.md)', image_tables(ids, images, image_url, lang), disclosure(t('Пояснения к компонентам', 'Component notes'), image_notes(ids, images, lang))]
    chunks += ['<a name="states"></a>\n\n## '+t('Состояния интерфейса','Interface states'),t('Дополнительные сценарии: пустые данные, ожидание, компактный экран и восстановление.','Supporting scenarios: empty data, waiting, compact screens and recovery.')]
    states=[('Stories — '+t('коллекция, iPhone SE, пустое состояние','collection, iPhone SE, empty state'),['stories-solar-grid','stories-small-screen','stories-empty'],'stories'),(t('Оплата — ожидание и ошибка','Payments — waiting and error'),['payment-waiting','payment-long-error'],'payments')]
    for title,ids,case in states:
        body=image_tables(ids,images,image_url,lang,min(3,len(ids)))+'\n\n'+image_notes(ids,images,lang)+f'\n\n[{t("Подробный кейс","Full case")}](cases/{case}.md)'
        chunks.append(disclosure(title,body))
    chunks += ['<a name="components"></a>\n\n## '+t('Компоненты','Components'),t('Небольшие элементы сгруппированы по продуктовым направлениям.','Smaller elements grouped by product area.')]
    for case,title in [('esim','eSIM'),('travel-history',t('Карточки и хронология путешествий','Travel cards and timeline')),('avia',t('Авиа: поиск и тарифы','Flights: search and fares')),('design-system',t('Общие поля и панель действий','Shared fields and action bar')),('virtual-card',t('Виртуальная карта','Virtual card')),('loyalty',t('Программа лояльности','Loyalty programme')),('chat',t('Чат поддержки','Support chat'))]:
        ids=[id for id,x in images.items() if x['case']==case and x['format']=='component' and id not in featured]
        if not ids: continue
        body=image_tables(ids,images,image_url,lang)+'\n\n'+image_notes(ids,images,lang)+f'\n\n[{t("Подробный кейс","Full case")}](cases/{case}.md)'
        chunks.append(disclosure(title+' · '+str(len(ids)),body))
    chunks += ['---',t('**Об изображениях.** Дизайн и общая архитектура создавались командой; мой вклад описан в кейсах. Здесь представлены неизменённые snapshot-тесты на подготовленных данных. Исходный язык интерфейса сохранён.','**About the images.** Design and overall architecture were team work; the cases describe my contribution. Images are unchanged snapshot-test baselines using prepared data. The original interface language is preserved.'),t('[Все кейсы](cases/index.md) · [Резюме](career/summary.md) · [О материалах](methodology.md)','[All cases](cases/index.md) · [Summary](career/summary.md) · [About the materials](methodology.md)')]
    return '\n\n'.join(chunks)
