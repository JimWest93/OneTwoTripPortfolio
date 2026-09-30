/* Dependency-free search across self-contained examples. */
(()=>{
  const rows=window.PORTFOLIO_ROWS||[],ui=window.PORTFOLIO_UI;
  const query=document.getElementById('query'),group=document.getElementById('group'),year=document.getElementById('year'),results=document.getElementById('results'),count=document.getElementById('result-count'),more=document.getElementById('more');
  let limit=20;
  const el=(tag,text,cls)=>{const n=document.createElement(tag);if(text)n.textContent=text;if(cls)n.className=cls;return n;};
  function render(){
    const term=query.value.trim().toLocaleLowerCase();
    const found=rows.filter(x=>{
      const years=x.period.match(/\d{4}/g).map(Number);
      const withinPeriod=year.value==='all'||(+year.value>=years[0]&&+year.value<=years[years.length-1]);
      const matchesTerm=!term||[x.scenario,x.contribution,x.focus,x.caseTitle,...x.technologies].join(' ').toLocaleLowerCase().includes(term);
      return (group.value==='all'||x.group===group.value)&&withinPeriod&&matchesTerm;
    });
    results.replaceChildren();
    count.textContent=ui.count.replace('{count}',found.length).replace('{shown}',Math.min(limit,found.length));
    if(!found.length)results.append(el('p',ui.empty,'empty'));
    for(const x of found.slice(0,limit)){
      const card=el('article',null,'result'),top=el('div',null,'result-top');
      top.append(el('span',x.group,'badge'),el('span',x.period));
      card.append(top,el('h2',x.scenario),el('p',x.contribution));
      const focus=el('p');focus.append(el('strong',ui.focus),document.createTextNode(x.focus));card.append(focus);
      const details=el('a',`${ui.details}${x.caseTitle} →`);details.href=x.caseUrl;
      const bottom=el('div',null,'evidence-links');bottom.append(details);card.append(bottom);results.append(card);
    }
    more.hidden=found.length<=limit;
  }
  for(const control of [query,group,year])control.addEventListener('input',()=>{limit=20;render();});
  more.addEventListener('click',()=>{limit+=20;render();});render();
})();
