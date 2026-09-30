#!/usr/bin/env python3
"""Build complete, symmetric Russian and English portfolio editions."""
import html,json,os,pathlib,re
import markdown
from gallery import build_gallery
from github_layout import github_gallery, case_images
R=pathlib.Path(__file__).resolve().parents[1];SITE=R/'site'
load=lambda name:json.loads((R/name).read_text())
S=load('data/statistics.json');IM=load('data/screenshots.json')
LANGS=('ru','en')
def rel(path,base):return os.path.relpath(path,base).replace(os.sep,'/')
def write(path,text):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text.rstrip()+'\n')
def bullet(items):return '\n'.join('- '+x for x in items)
def cell(s):return html.escape(s).replace('|',' / ').replace('\n',' ')
def switch_md(path,lang):
 other='en' if lang=='ru' else 'ru';pair=R/'docs'/other/path.relative_to(R/'docs'/lang)
 return f'[{other.upper()}]({rel(pair,path.parent)}) · [{"Выбор языка / Language" if lang=="ru" else "Language selection"}]({rel(R/"README.md",path.parent)})\n\n'
def document(path,text,lang):write(path,switch_md(path,lang)+text)

def build(lang):
 t=lambda ru,en:ru if lang=='ru' else en
 root=R/'docs'/lang;web=SITE/lang;other='en' if lang=='ru' else 'ru'
 C=load('data/cases.json' if lang=='ru' else 'data/cases.en.json')
 images={x['id']:{**x,'caption':x['title'] if lang=='ru' else x['titleEn']} for x in IM}
 def figures(ids,base):
  result=[]
  for id in sorted(ids,key=lambda id:{'screen':0,'component':1,'comparison':2}[images[id]['format']]):
   x=images[id];url=rel(R/x['file'],base);caption=html.escape(x['caption']);kind=html.escape(x['kind'] if lang=='ru' else x['kindEn']);description=html.escape(x['description'] if lang=='ru' else x['descriptionEn'])
   result.append(f'<figure class="visual-card visual-{x["format"]}" id="visual-{id}"><a class="visual-image" href="{url}" aria-label="{t("Открыть оригинал: ","Open original: ")+caption}"><img loading="lazy" decoding="async" width="{x["width"]}" height="{x["height"]}" src="{url}" alt="{caption}"></a><figcaption><strong>{caption}</strong><span>{description}</span><small>{kind}</small><a href="{url}">{t("Открыть в полном размере","Open full size")} ↗</a></figcaption></figure>')
  return '<div class="visual-grid">'+''.join(result)+'</div>'
 def table(rows):
  return t('| Сценарий | Что я делал | Инженерный акцент |','| Scenario | My contribution | Engineering focus |')+'\n| --- | --- | --- |\n'+''.join('| '+' | '.join(cell(x[k]) for k in ['scenario','contribution','focus'])+' |\n' for x in rows)
 for c in C:
  path=root/'cases'/f"{c['slug']}.md"
  chunks=[f"# {c['title']}",f"**{c['period']} · OneTwoTrip / iOS**",c['lead']]
  if c['images']:chunks += [t('[Смотреть экраны и состояния](#screens) · [Вся галерея](../gallery.md)','[View screens and states](#screens) · [Full gallery](../gallery.md)')]
  for label,key,islist in [(t('Контекст','Context'),'context',False),(t('Мой вклад','My contribution'),'work',True)]:chunks+=['## '+label,bullet(c[key]) if islist else c[key]]
  chunks+=['## '+t('Технологии','Technologies'),', '.join(c['technologies'])+'.','## '+t('Примеры задач','Practical examples'),table(c['examples'])]
  for label,key in [(t('Инженерные решения','Engineering decisions'),'decisions'),(t('Качество и проверки','Quality and checks'),'quality')]:chunks+=['## '+label,bullet(c[key])]
  chunks+=['## '+t('Результат и границы','Outcome and scope'),c['result']]
  if c.get('walkthrough'):
   chunks+=['## '+t('Разбор сложного сценария','A closer look at the journey')]
   if c.get('flow'):
    chunks+=['\n'.join(f'{i}. **{step["title"]}.** {step["body"]}' for i,step in enumerate(c['flow'],1)),t('Упрощённый маршрут одного сценария. Ветки ошибок и дополнительные действия разобраны ниже.','A simplified route through one journey. Error branches and additional actions are discussed below.')]
   for section in c['walkthrough']:chunks+=['### '+section['title'],section['body']]
  if c['images']:
   chunks+=['<a name="screens"></a>\n\n## '+t('Экраны и состояния интерфейса','Screens and interface states'),t('Оригинальные изображения из snapshot-тестов на подготовленных данных. Тип материала указан под каждым примером. Дизайн и общая архитектура создавались командой; мой вклад описан выше. Нажмите на изображение, чтобы рассмотреть детали.','Original snapshot-test images using prepared data. Each example identifies its source type. Design and overall architecture were team work; my contribution is described above. Select an image to inspect the details.'),case_images(c['images'],images,lambda x:rel(R/x['file'],path.parent),lang),t('[Вся галерея экранов и компонентов](../gallery.md)','[Full screen and component gallery](../gallery.md)')]
  chunks+=['## '+t('Что можно обсудить на интервью','Topics for an interview'),bullet(c['discussion']),t('[Все кейсы](index.md) · [Практические задачи](../archive/index.md) · [Технологии](../engineering/technologies.md)','[All cases](index.md) · [Practical examples](../archive/index.md) · [Technologies](../engineering/technologies.md)')]
  document(path,'\n\n'.join(chunks),lang)
 index=t('# Все кейсы\n\n21 тематический разбор: контекст, личный вклад, примеры задач, инженерные решения и проверки. Каждый кейс читается самостоятельно и помогает подготовиться к техническому интервью.','# All case studies\n\n21 detailed cases covering context, personal contribution, practical examples, engineering decisions and checks. Each case stands on its own and provides a starting point for a technical interview.')
 index+='\n\n'+'\n\n'.join(f"## {i:02}. [{c['title']}]({c['slug']}.md)\n\n**{c['period']}** — {c['lead']}" for i,c in enumerate(C,1))
 document(root/'cases/index.md',index,lang)
 chartinfo=[
 ('commits-yearly',t('Изменения кода по годам','Code changes by year'),t('4 046 авторских коммитов без merge. Разные записи могут представлять переносы одного изменения.','4,046 authored non-merge commits. Different records can represent backports of the same change.')),
 ('issues-yearly',t('Задачи по годам','Work items by year'),t('831 задача, связанная с собственными изменениями кода. Год соответствует первому изменению по задаче, а не её завершению.','831 work items linked to authored code changes. The year represents the first change, not completion.')),
 ('domains',t('Направления работы','Areas of work'),t('Каждая задача отнесена к одному направлению; классификация подготовлена для портфолио.','Each item belongs to one area; the classification was prepared for this portfolio.')),
 ('work-mix',t('Характер задач','Types of work'),t('Фичи, исправления, проверки, инженерные изменения и релизы. Количество задач не отражает их трудоёмкость.','Features, fixes, checks, engineering changes and releases. Item counts do not reflect effort.')),
 ('monthly',t('История по месяцам','Monthly history'),t('Неполные декабрь 2021 и сентябрь 2026. Отсутствие коммитов не означает отсутствие работы.','December 2021 and September 2026 are partial. No commits does not mean no work.')),
 ('test-work',t('Работа с тестами','Work involving tests'),t('788 коммитов затрагивают тестовые пути. Это не покрытие кода и не число написанных тестов.','788 commits touch test paths. This is not code coverage or a count of tests written.')),
 ('domain-evolution',t('Как менялся продуктовый фокус','How product focus changed'),t('Распределение задач по направлениям и году первого собственного изменения. В ячейках указано число задач.','Work items by area and year of the first authored change. Each cell shows an item count.'))]
 chunks=[t('# Статистика вклада','# Contribution statistics'),t('Период: **22.12.2021–28.09.2026**. Графики показывают масштаб и структуру инженерной истории. [Кейсы](cases/index.md) раскрывают содержание работы и решения.','Period: **December 22, 2021–September 28, 2026**. Charts describe the scale and structure of the engineering history. [Cases](cases/index.md) explain the work and decisions.')]
 for id,title,desc in chartinfo:
  base=rel(R/'assets/charts'/lang/id,root);chunks += ['## '+title,desc,f'![{title}]({base}.svg)',f'[PNG]({base}.png) · [SVG]({base}.svg)']
 chunks += ['## '+t('Числовая таблица','Data table'),t('| Год | Коммиты без merge | Задачи с первым изменением в этом году | Коммиты с тестовыми путями |','| Year | Non-merge commits | Items first changed that year | Commits touching test paths |')+'\n| --- | ---: | ---: | ---: |\n'+''.join(f"| {y['year']}{'*' if y['year'] in [2021,2026] else ''} | {y['commits']} | {y['newIssueReferences']} | {y['commitsTouchingTests']} |\n" for y in S['years'])]
 aggregate='statistics.json' if lang=='ru' else 'statistics.en.json'
 chunks += [t('*Неполные годы. [Как читать показатели](methodology.md)','*Partial years. [How to read the metrics](methodology.md)')+f" · [{t('Агрегированные данные','Aggregate data')}]({rel(R/'data'/aggregate,root)})."]
 document(root/'statistics.md','\n\n'.join(chunks),lang)
 document(root/'gallery.md',github_gallery(images,lang,lambda x:rel(R/x['file'],root)),lang)
 chunks=[t('# Практические задачи','# Practical examples'),t('84 выбранных примера из 21 кейса: сценарий, мой вклад и технический акцент. Здесь удобно искать опыт, близкий к вакансии. Примеры пересекаются и не складываются в число выпущенных фич.','84 selected examples from 21 cases: scenario, my contribution and technical focus. Find experience relevant to a role. Examples overlap and do not add up to a count of released features.')]
 for group in dict.fromkeys(c['group'] for c in C):
  chunks+=['## '+group]
  for c in C:
   if c['group']==group:chunks+=[f"### [{c['title']}](../cases/{c['slug']}.md)",f"**{c['period']}** · "+', '.join(c['technologies']),table(c['examples'])]
 document(root/'archive/index.md','\n\n'.join(chunks),lang)
 # Add the same language navigation to authored documents without accumulating it.
 for name in ['overview.md','methodology.md','career/growth.md','career/summary.md','engineering/technologies.md','engineering/ci-details.md']:
  path=root/name;text=path.read_text();text=text[text.index('# '):];document(path,text,lang)
 def shell(title,body,dest,article=True):
  base=dest.parent;counterpart=SITE/other/dest.relative_to(web)
  nav=[(t('Кейсы','Cases'),'docs/cases/index.html'),(t('Галерея','Gallery'),'docs/gallery.html'),(t('Графики','Charts'),'docs/statistics.html'),(t('Задачи','Examples'),'catalog.html'),(t('Резюме','Summary'),'docs/career/summary.html')]
  links=''.join(f'<a href="{rel(web/p,base)}">{label}</a>' for label,p in nav)
  language=''.join(f'<a data-language="{l}" lang="{l}" hreflang="{l}" href="{rel(dest if l==lang else counterpart,base)}"'+(' aria-current="page"' if l==lang else '')+f'>{l.upper()}</a>' for l in LANGS)
  gallery_css=f'<link rel="stylesheet" href="{rel(SITE/"gallery.css",base)}">' if dest.name=='gallery.html' else ''
  return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="{t('Валерий Веселов — iOS Developer. Полное портфолио OneTwoTrip и Solar.','Valeriy Veselov — iOS Developer. Complete OneTwoTrip and Solar portfolio.')}"><title>{html.escape(title)} · Valeriy Veselov</title><link rel="alternate" hreflang="{other}" href="{rel(counterpart,base)}"><link rel="stylesheet" href="{rel(SITE/'styles.css',base)}">{gallery_css}</head><body><a class="skip" href="#main">{t('К содержанию','Skip to content')}</a><header class="site-header"><a class="wordmark" href="{rel(web/'index.html',base)}"><span class="mark">V.</span> Valeriy Veselov</a><nav aria-label="{t('Основная навигация','Main navigation')}">{links}</nav><nav class="language-switch" aria-label="{t('Язык страницы','Page language')}">{language}</nav></header><main id="main" class="{'article gallery-page' if dest.name=='gallery.html' else 'article' if article else ''}">{body}</main><footer><span>OneTwoTrip & Solar · 2021–2026</span><a href="{rel(web/'docs/methodology.html',base)}">{t('О показателях','About the metrics')}</a><a href="{rel(SITE/'index.html',base)}">{t('Выбрать язык','Choose a language')}</a><span>{t('Срез 29.09.2026','As of September 29, 2026')}</span></footer></body></html>'''
 for src in sorted(root.rglob('*.md')):
  dest=web/'docs'/src.relative_to(root).with_suffix('.html');text=src.read_text()
  if src.name=='gallery.md':text=switch_md(src,lang)+build_gallery(images,lang,lambda x:rel(R/x['file'],root))
  render_text=text.replace('<details>', '<details markdown="1">')
  body=markdown.markdown(render_text,extensions=['tables','fenced_code','toc','md_in_html'])
  def fix(m):
   attr,url=m.group(1),html.unescape(m.group(2))
   if re.match(r'^[a-z]+:|^#|^//',url):return m.group(0)
   path,sep,frag=url.partition('#');target=(src.parent/path).resolve()
   if target.suffix=='.md':
    if target==R/'README.md':target=SITE/'index.html'
    else:
     relative=target.relative_to(R/'docs');target=SITE/relative.parts[0]/'docs'/pathlib.Path(*relative.parts[1:]).with_suffix('.html')
   return attr+'="'+html.escape(rel(target,dest.parent)+(sep+frag if sep else ''),quote=True)+'"'
  body=re.sub(r'(href|src)="([^"]+)"',fix,body);title=next(line[2:] for line in text.splitlines() if line.startswith('# '))
  write(dest,shell(title,body,dest))
 cards=''.join(f'''<a class="case-card" href="docs/cases/{c['slug']}.html"><span class="eyebrow">{i:02d} / {c['period']}</span><h3>{html.escape(c['title'])}</h3><p>{html.escape(c['lead'])}</p><span class="card-bottom">{t('4 примера задач','4 practical examples')} <span aria-hidden="true">↗</span></span></a>''' for i,c in enumerate(C,1))
 gallery=figures(['esim-payment-price','cashback-accounts','stories-solar-grid'],web)
 home=(R/'templates'/lang/'home.html').read_text().replace('{{cards}}',cards).replace('{{gallery}}',gallery).replace('{{image_count}}',str(len(IM)))
 write(web/'index.html',shell('iOS Developer · OneTwoTrip & Solar',home,web/'index.html',False))
 rows=[dict(**e,caseTitle=c['title'],period=c['period'],group=c['group'],technologies=c['technologies'],caseUrl='docs/cases/'+c['slug']+'.html') for c in C for e in c['examples']]
 ui=dict(count=t('Найдено примеров: {count}. Показано: {shown}.','Examples found: {count}. Showing: {shown}.'),empty=t('Ничего не найдено. Попробуйте другую тему или сбросьте фильтры.','No matches. Try another topic or reset the filters.'),focus=t('Инженерный акцент: ','Engineering focus: '),details=t('Подробнее: ','Read the case: '))
 write(web/'catalog-data.js','window.PORTFOLIO_ROWS = '+json.dumps(rows,ensure_ascii=False).replace('</',r'<\/')+';\nwindow.PORTFOLIO_UI = '+json.dumps(ui,ensure_ascii=False)+';')
 catalog=f'''<div class="catalog-intro"><p class="eyebrow">{t('Практика / примеры работы','Practice / examples of work')}</p><h1>{t('Какие задачи я решал.','The problems I worked on.')}</h1><p>{t('84 примера из 21 кейса. Найдите сценарий, технологию или инженерную тему и откройте подробный разбор.','84 examples from 21 cases. Find a scenario, technology or engineering topic and open the detailed case.')}</p></div><form class="filters" role="search" onsubmit="return false"><label>{t('Тема или технология','Topic or technology')}<input id="query" type="search" placeholder="{t('Например: SwiftUI, оплата, календарь','For example: SwiftUI, payment, calendar')}"></label><label>{t('Область','Area')}<select id="group"><option value="all">{t('Все области','All areas')}</option>{''.join(f'<option>{html.escape(g)}</option>' for g in dict.fromkeys(c['group'] for c in C))}</select></label><label>{t('Период кейса','Case period')}<select id="year"><option value="all">{t('Все годы','All years')}</option>{''.join(f'<option>{y}</option>' for y in range(2021,2027))}</select></label></form><p class="muted">{t('Годы относятся к кейсу целиком, а не к дате каждой задачи. Примеры из разных кейсов могут пересекаться.','Years refer to the whole case, not the date of each task. Examples across cases may overlap.')}</p><p id="result-count" class="muted" role="status" aria-live="polite"></p><div id="results" class="catalog-results"></div><button id="more" class="button" type="button">{t('Показать ещё 20','Show 20 more')}</button><noscript><p>{t('Для поиска нужен JavaScript.','Search requires JavaScript.')} <a href="docs/archive/index.html">{t('Полный список примеров','Full list of examples')}</a></p></noscript><script src="catalog-data.js"></script><script src="../catalog.js"></script>'''
 write(web/'catalog.html',shell(t('Практические задачи','Practical examples'),catalog,web/'catalog.html'))
 return len(list(web.rglob('*.html')))

counts={lang:build(lang) for lang in LANGS}
chooser='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Valeriy Veselov · RU / EN</title><link rel="stylesheet" href="styles.css"></head><body><main class="language-entry"><a class="entry-mark" href="../README.md" aria-label="Portfolio README">V.</a><p class="eyebrow">Valeriy Veselov / iOS Developer</p><h1><span lang="ru">Выберите язык.</span><br>Choose your language.</h1><p class="entry-description"><span lang="ru">Полное портфолио работы в OneTwoTrip и Solar.</span><br>Complete OneTwoTrip and Solar portfolio.</p><div class="language-cards"><a href="ru/index.html" lang="ru" hreflang="ru"><span class="eyebrow">RU</span><h2>Русский</h2><p>21 кейс · 84 примера задач<br>Графики, технологии и профессиональный рост</p><span aria-hidden="true">↗</span></a><a href="en/index.html" lang="en" hreflang="en"><span class="eyebrow">EN</span><h2>English</h2><p>21 cases · 84 practical examples<br>Charts, technologies and professional growth</p><span aria-hidden="true">↗</span></a></div><p class="entry-note"><span lang="ru">Одинаковый объём материалов на обоих языках.</span><br>The same complete content in both languages.</p></main></body></html>'''
write(SITE/'index.html',chooser)
print('Built symmetric locale editions:',counts)
