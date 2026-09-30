#!/usr/bin/env python3
"""Render publication-ready SVG and PNG charts from the checked-in statistics."""
import os,json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parents[1]
os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'.research/mplconfig'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
S=json.loads((ROOT/'data/statistics.json').read_text()); OUT=ROOT/'assets/charts';OUT.mkdir(parents=True,exist_ok=True)
TRANSLATIONS=json.loads((ROOT/'data/chart-labels.en.json').read_text())
def tr(text):
 if LANG=='ru' or not re.search('[А-Яа-яЁё]',text):return text
 return TRANSLATIONS[text]
INK='#162e34';TEAL='#16796f'; GOLD='#b48124';GRAY='#68767a';BG='#faf9f5'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'text.color':INK,'axes.labelcolor':GRAY,'xtick.color':GRAY,'ytick.color':INK,'figure.facecolor':BG,'axes.facecolor':BG,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,'axes.spines.bottom':False,'svg.fonttype':'none','savefig.facecolor':BG,'svg.hashsalt':'portfolio'})
years=S['years'];labels=['2021*','2022','2023','2024','2025','2026*']; index=np.arange(6)
def setup(title,subtitle,size=(11,6)):
 f,a=plt.subplots(figsize=size);f.subplots_adjust(left=.11,right=.96,top=.78,bottom=.16)
 f.text(.055,.94,tr(title),fontsize=21,fontweight='bold',va='top');f.text(.055,.87,tr(subtitle),fontsize=10,color=GRAY,va='top');a.set_axisbelow(True);a.tick_params(length=0,pad=9);return f,a
def save(f,name,note):
 f.text(.055,.035,tr(note),fontsize=9,color=GRAY)
 for ext in ['svg','png']:f.savefig(OUT/f'{name}.{ext}',dpi=160,metadata={'Date':None} if ext=='svg' else {})
 plt.close(f)
def nums(a,bars):
 for b in bars:a.text(b.get_x()+b.get_width()/2,b.get_height()+12,str(int(b.get_height())),ha='center',fontsize=12,fontweight='bold')
for LANG in ['ru','en']:
 OUT=ROOT/'assets/charts'/LANG;OUT.mkdir(parents=True,exist_ok=True)
 f,a=setup('История изменений в Git','4 046 авторских коммитов без merge · все доступные локальные refs')
 bars=a.bar(index,[y['commits'] for y in years],color=[GRAY,TEAL,TEAL,TEAL,TEAL,GOLD],width=.6);nums(a,bars);a.set_xticks(index,labels);a.set_ylim(0,1200);a.grid(axis='y',alpha=.15)
 save(f,'commits-yearly','* 2021: с 22 декабря; 2026: по 28 сентября. Коммиты не равны фичам или продуктивности.')
 f,a=setup('Задачи по годам','831 задача · год первого собственного коммита по задаче')
 bars=a.bar(index,[y['newIssueReferences'] for y in years],color=TEAL,width=.6)
 for b in bars:a.text(b.get_x()+b.get_width()/2,b.get_height()+4,str(int(b.get_height())),ha='center',fontweight='bold')
 a.set_xticks(index,labels);a.set_ylim(0,285);a.grid(axis='y',alpha=.15)
 save(f,'issues-yearly','* Неполные годы. Это не число завершённых или выпущенных фич.')
 f,a=setup('Продуктовые и инженерные направления','831 задача · для каждой выбрано одно направление · редакционная классификация',(12,10))
 f.subplots_adjust(left=.33,bottom=.1,top=.83);pairs=list(S['domains'].items())[::-1];b=a.barh([tr(p[0]) for p in pairs],[p[1] for p in pairs],color=TEAL,height=.68)
 for bar in b:a.text(bar.get_width()+2,bar.get_y()+bar.get_height()/2,str(int(bar.get_width())),va='center',fontsize=10)
 a.set_xlim(0,175);a.grid(axis='x',alpha=.15)
 save(f,'domains','Число задач отражает структуру истории, а не трудоёмкость, долю кода или бизнес-эффект.')
 f,a=setup('Как менялся характер задач','Задачи по первому собственному изменению · взаимоисключающие категории',(12,7))
 f.subplots_adjust(bottom=.29);bottom=np.zeros(6);colors=[TEAL,'#8ca7a6','#d1a64d','#435968','#c6cdc9']
 for name,col in zip(S['kinds'],colors):
  vals=np.array([y['kinds'].get(name,0) for y in years]);a.bar(index,vals,bottom=bottom,label=tr(name),color=col,width=.6);bottom+=vals
 a.set_xticks(index,labels);a.grid(axis='y',alpha=.15);a.legend(loc='upper left',bbox_to_anchor=(-.07,-.12),ncol=2,frameon=False,fontsize=9)
 save(f,'work-mix','* Неполные годы. Категории определены по содержанию задач; не являются оценкой сложности.')
 f,a=setup('Ритм изменений по месяцам','Авторские non-merge коммиты · пустая ячейка означает период вне наблюдаемого среза',(12,6))
 matrix=np.full((6,12),np.nan)
 for date,n in S['monthlyCommits'].items():y,m=map(int,date.split('-'));matrix[y-2021,m-1]=n
 cmap=LinearSegmentedColormap.from_list('portfolio',['#e7efeb',TEAL]);a.imshow(np.ma.masked_invalid(matrix),cmap=cmap,vmin=0,vmax=150,aspect='auto')
 a.set_xticks(range(12),[tr(m) for m in ['Янв','Фев','Мар','Апр','Май','Июн','Июл','Авг','Сен','Окт','Ноя','Дек']]);a.set_yticks(range(6),[str(y['year']) for y in years])
 for y in range(6):
  for m in range(12):
   if not np.isnan(matrix[y,m]):a.text(m,y,str(int(matrix[y,m])),ha='center',va='center',fontsize=10,color='white' if matrix[y,m]>80 else INK)
 save(f,'monthly','Срез 22.12.2021–28.09.2026. Паузы в Git не доказывают отсутствие работы.')
 f,a=setup('Изменения, затрагивающие тесты','788 из 4 046 non-merge коммитов меняют тестовые пути · доля внутри каждого года')
 vals=[100*y['commitsTouchingTests']/y['commits'] for y in years];bars=a.bar(index,vals,color=TEAL,width=.6)
 for b,y in zip(bars,years):a.text(b.get_x()+b.get_width()/2,b.get_height()+1.5,f"{b.get_height():.1f}%\n{y['commitsTouchingTests']} / {y['commits']}",ha='center',fontsize=10)
 a.set_xticks(index,labels);a.set_ylim(0,55);a.grid(axis='y',alpha=.15);a.set_ylabel(tr('% коммитов'))
 save(f,'test-work','Это не code coverage и не количество новых тестов: учитываются также обновления и удаления.')
 f,a=setup('Как менялся продуктовый фокус','Задачи по направлениям и году первого собственного изменения',(12,10))
 f.subplots_adjust(left=.33,right=.96,top=.83,bottom=.1)
 names=list(S['domains']);matrix=np.array([[y['domains'].get(name,0) for y in years] for name in names])
 a.imshow(matrix,cmap=cmap,vmin=0,vmax=100,aspect='auto')
 a.set_xticks(range(6),labels);a.set_yticks(range(len(names)),[tr(n) for n in names])
 for i in range(len(names)):
  for j in range(6):
   n=int(matrix[i,j]);a.text(j,i,str(n) if n else '—',ha='center',va='center',fontsize=10,color='white' if n>55 else INK)
 save(f,'domain-evolution','* Неполные годы. Число задач показывает распределение работы, а не затраты времени.')
 print('Rendered 7 employer-facing charts in SVG and PNG.')
# English readers can download aggregates with localized category names as well.
translated=json.loads(json.dumps(S))
for key in ['domains','kinds']:translated[key]={tr(k):v for k,v in S[key].items()}
for year in translated['years']:
 for key in ['domains','kinds']:year[key]={tr(k):v for k,v in year[key].items()}
(ROOT/'data/statistics.en.json').write_text(json.dumps(translated,ensure_ascii=False,indent=2)+'\n')
