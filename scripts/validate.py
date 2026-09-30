#!/usr/bin/env python3
"""Validate bilingual coverage, links, data integrity and reader-facing content."""
import hashlib,json,pathlib,re,urllib.parse
from PIL import Image
from html import unescape
from html.parser import HTMLParser
R=pathlib.Path(__file__).resolve().parents[1];errors=[]
def check(ok,msg):
 if not ok:errors.append(msg)
def read(path):return json.loads((R/path).read_text())
s=read('data/statistics.json');cases={l:read('data/cases.json' if l=='ru' else 'data/cases.en.json') for l in ['ru','en']};images=read('data/screenshots.json')
check(sum(x['commits'] for x in s['years'])==s['nonMergeCommits']==4046,'Commit totals mismatch')
check(sum(s['monthlyCommits'].values())==4046,'Monthly totals mismatch')
check(sum(x['commitsTouchingTests'] for x in s['years'])==s['testTouchingCommits']==788,'Test totals mismatch')
check(sum(s['domains'].values())==sum(s['kinds'].values())==sum(x['newIssueReferences'] for x in s['years'])==s['workItems']==831,'Work-item totals mismatch')
for y in s['years']:check(sum(y['domains'].values())==sum(y['kinds'].values())==y['newIssueReferences'],f"Annual totals: {y['year']}")
se=read('data/statistics.en.json')
for key in ['nonMergeCommits','mergeCommits','workItems','monthlyCommits','testTouchingCommits','authoredMergedPRs']:check(s[key]==se[key],f'Aggregate mismatch: {key}')
check(list(s['domains'].values())==list(se['domains'].values()),'Translated domain counts differ')
check(list(s['kinds'].values())==list(se['kinds'].values()),'Translated work categories differ')
check(len(cases['ru'])==len(cases['en'])==21,'Case count mismatch')
for ru,en in zip(cases['ru'],cases['en']):
 for key in ['slug','period','images']:check(ru[key]==en[key],f"Case identity mismatch: {ru['slug']} / {key}")
 for key in ['work','decisions','quality','examples','discussion','technologies']:check(len(ru[key])==len(en[key]),f"Incomplete translation: {ru['slug']} / {key}")
 for key in ['walkthrough','flow']:check(len(ru.get(key,[]))==len(en.get(key,[])),f"Incomplete visual narrative: {ru['slug']} / {key}")
 check(len(ru['examples'])==4 and len(ru['discussion'])==2,'Incomplete case structure')
 for c in [ru,en]:
  check(not {'issues','sources'}&set(c),'Private evidence fields in cases')
  for e in c['examples']:check(all(e.get(k,'').strip() for k in ['scenario','contribution','focus']),f"Empty example: {c['slug']}")
check(not re.search('[А-Яа-яЁё]',json.dumps(cases['en'],ensure_ascii=False)),'Untranslated English case text')
image_ids={x['id'] for x in images}
check(len(image_ids)==len(images),'Duplicate image IDs')
check({p.relative_to(R).as_posix() for p in (R/'assets/screenshots').iterdir() if p.is_file()}=={x['file'] for x in images},'Image manifest and files differ')
for c in cases['ru']:
 check(set(c['images'])<=image_ids,f"Unknown case image: {c['slug']}")
for x in images:
 check(hashlib.sha256((R/x['file']).read_bytes()).hexdigest()==x['sha256'],f"Image modified: {x['id']}")
 check(x['edited'] is False and x.get('titleEn'),'Missing original image metadata or English caption')
 check(x['sourceType']=='snapshot','Only reviewed test fixtures belong in the public image manifest')
 check(x['format'] in ['screen','component','comparison'],'Unknown visual format')
 check(all(x.get(k,'').strip() for k in ['description','descriptionEn','kind','kindEn']),'Missing bilingual image explanation')
 check(not re.search('[А-Яа-яЁё]',' '.join(x[k] for k in ['titleEn','descriptionEn','kindEn'])),f"Untranslated image metadata: {x['id']}")
 with Image.open(R/x['file']) as im:check(im.size==(x['width'],x['height']),f"Incorrect image dimensions: {x['id']}")
# Resolve local paths and fragments in all generated pages.
class Page(HTMLParser):
 def __init__(self,path):super().__init__();self.path=path;self.ids=set();self.links=[];self.language=None;self.switches={};self.headings=[]
 def handle_starttag(self,tag,attrs):
  v=dict(attrs)
  if tag=='html':self.language=v.get('lang')
  if v.get('id'):
   check(v['id'] not in self.ids,f'Duplicate HTML ID: {self.path} / {v["id"]}');self.ids.add(v['id'])
  if tag=='a' and v.get('name'):self.ids.add(v['name'])
  if v.get('data-language'):self.switches[v['data-language']]=v['href']
  if tag in ['h1','h2','h3']:self.headings.append(tag)
  for k in ['href','src']:
   if v.get(k):self.links.append(v[k])
pages={}
for p in (R/'site').rglob('*.html'):
 obj=Page(p);obj.feed(p.read_text());pages[p.resolve()]=obj

def link(src,url):
 parsed=urllib.parse.urlsplit(unescape(url))
 if parsed.scheme or parsed.netloc:return
 target=(src.parent/urllib.parse.unquote(parsed.path)).resolve() if parsed.path else src.resolve()
 check(target.exists(),f'Broken link: {src.relative_to(R)} -> {url}')
 check(target==R or R in target.parents,f'Link outside repository: {url}')
 if parsed.fragment and target in pages:check(urllib.parse.unquote(parsed.fragment) in pages[target].ids,f'Missing anchor: {url} in {src.relative_to(R)}')
for p,obj in pages.items():
 for url in obj.links:link(p,url)
md=[R/'README.md',*list((R/'docs').rglob('*.md'))]
for p in md:
 for url in re.findall(r'\]\(([^)]+)\)',p.read_text()):link(p,url)
 obj=Page(p);obj.feed(p.read_text())
 for url in obj.links:link(p,url)
 # GitHub removes custom CSS: primary documents must stand on their own.
 check(not re.search(r'<(?:div|span|figure|figcaption|nav|section|aside)\b|\b(?:class|style)="',p.read_text()),f'CSS-dependent markup in Markdown: {p.relative_to(R)}')
 for tag in re.findall(r'<img\b[^>]*>',p.read_text()):
  width=re.search(r'\bwidth="(\d+)"',tag)
  check(width is not None and 100<=int(width[1])<=640,f'Unbounded GitHub image: {p.relative_to(R)}')
  check(not re.search(r'\bheight=',tag),f'Fixed aspect ratio in GitHub preview: {p.relative_to(R)}')
for kind,suffix in [('docs','.md'),('site','.html')]:
 sets={l:{p.relative_to(R/kind/l) for p in (R/kind/l).rglob('*'+suffix)} for l in ['ru','en']}
 check(sets['ru']==sets['en'],f'{kind}: different page coverage')
 for path in sets['ru']:
  ru=R/kind/'ru'/path;en=R/kind/'en'/path
  if kind=='docs':check(len(re.findall(r'^#{1,3} ',ru.read_text(),re.M))==len(re.findall(r'^#{1,3} ',en.read_text(),re.M)),f'Different section coverage: {path}')
  else:check(pages[ru.resolve()].headings==pages[en.resolve()].headings,f'Different HTML structure: {path}')
for lang in ['ru','en']:
 other='en' if lang=='ru' else 'ru';root=R/'site'/lang
 for path in root.rglob('*.html'):
  obj=pages[path.resolve()];check(obj.language==lang,f'Wrong document language: {path}')
  check(set(obj.switches)=={'ru','en'},f'Missing language switch: {path}')
  for chosen,url in obj.switches.items():check((path.parent/url).resolve()==(R/'site'/chosen/path.relative_to(root)).resolve(),f'Language switch loses current page: {path}')
 js=(root/'catalog-data.js').read_text();rows=json.loads(js.split('window.PORTFOLIO_ROWS = ',1)[1].split(';\nwindow.PORTFOLIO_UI',1)[0])
 check(len(rows)==84,f'{lang}: catalog count mismatch')
 expected=[dict(**e,caseTitle=c['title'],period=c['period'],group=c['group'],technologies=c['technologies'],caseUrl='docs/cases/'+c['slug']+'.html') for c in cases[lang] for e in c['examples']]
 check(rows==expected,f'{lang}: catalog differs from cases')
 for row in rows:check((root/row['caseUrl']).exists(),'Catalog link missing')
 check({'query','group','year','result-count','results','more'}<=pages[(root/'catalog.html').resolve()].ids,'Missing search controls')
 check({f'visual-{id}' for id in image_ids}<=pages[(root/'docs/gallery.html').resolve()].ids,f'{lang}: gallery omits images')
 for c in cases[lang]:check({f'visual-{id}' for id in c['images']}<=pages[(root/'docs/cases'/f"{c['slug']}.html").resolve()].ids,f"{lang}: missing case visual for {c['slug']}")
 check(len(list((R/'assets/charts'/lang).glob('*.svg')))==len(list((R/'assets/charts'/lang).glob('*.png')))==7,f'{lang}: expected seven chart pairs')
public=md+[p for name in ['data','site','assets/charts','templates'] for p in (R/name).rglob('*') if p.suffix in ['.json','.html','.js','.svg']]
for p in public:
 text=p.read_text()
 check(not re.search(r'(?:jira|bitbucket|confluence)\.twiket\.com|\b(?:IOS|GROW|VC)-\d+\b|\bPR\s*#\d+|\b[0-9a-f]{40}\b',text),f'Private reference: {p.relative_to(R)}')
 check('/Users/' not in text,f'Local path: {p.relative_to(R)}')
 check(not re.search(r'\b(?:actual/|Sources/|UnitTests/|UITests/|fastlane/)[\w./-]+',text),f'Implementation path: {p.relative_to(R)}')
 check(not re.search(r'\b[\w./-]+\.(?:swift|groovy|plist|xcconfig)\b',text),f'Implementation filename: {p.relative_to(R)}')
 check(not re.search(r'(?i)\b(?:sandbox-\d+|envid)\b',text),f'Environment marker: {p.relative_to(R)}')
 check(not re.search(r'(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b',text),f'Email address requires review: {p.relative_to(R)}')
 if any(p.is_relative_to(R/base/'en') for base in ['docs','site','assets/charts','templates']) or p.name in ['cases.en.json','statistics.en.json']:
  check(not re.search('[А-Яа-яЁё]',text),f'Untranslated Russian in English content: {p.relative_to(R)}')
check(not list((R/'site/docs').rglob('*.html')),'Obsolete single-language pages remain')
check(not list((R/'assets/charts').glob('*.svg')),'Obsolete single-language charts remain')
if errors:
 print('\n'.join(errors));raise SystemExit(1)
print(f'PASS: 33 pages per language; 21 cases, 84 examples, 42 discussion topics and 7 chart pairs per edition; locale switches, links, totals, translation coverage and {len(images)} unchanged images with bilingual context.')
