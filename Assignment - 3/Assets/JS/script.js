
window.addEventListener('DOMContentLoaded',()=>{
  const root=document.documentElement;
  const t=document.getElementById('theme-toggle');
  function setTheme(m){ root.dataset.theme=m; localStorage.setItem('theme',m); if(t){t.textContent=(m==='dark'?'☀ Light':'☾ Dark');} }
  setTheme(localStorage.getItem('theme') || (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark':'light'));
  if(t){ t.addEventListener('click',()=> setTheme(root.dataset.theme==='dark'?'light':'dark')); }
  document.querySelectorAll('.group > button').forEach(btn=>{
    btn.addEventListener('click',()=>{
      const panel=btn.nextElementSibling;
      const open=panel.getAttribute('data-open')==='true';
      panel.style.display=open?'none':'block';
      panel.setAttribute('data-open', (!open).toString());
      btn.setAttribute('aria-expanded', (!open).toString());
    });
    const panel=btn.nextElementSibling;
    panel.style.display='block'; panel.setAttribute('data-open','true'); btn.setAttribute('aria-expanded','true');
  });
  const jump=document.getElementById('jump-select');
  if(jump){ jump.addEventListener('change',()=>{ const v=jump.value; if(v){ location.href=v; } }); }

  function g(id){return document.getElementById(id);} function v(id){const e=g(id);return e?e.value.trim():"";} function out(id,txt){const e=g(id); if(e) e.textContent=txt;}
  function download(filename, text){ const blob=new Blob([text],{type:'text/plain'}); const a=document.createElement('a'); a.href=URL.createObjectURL(blob); a.download=filename; a.click(); setTimeout(()=>URL.revokeObjectURL(a.href),1200); }

  if(g('validator-app')){
    g('gen-plan').addEventListener('click',()=>{
      const hyp=`For ${v('v-audience')||'a small segment'}, solving "${v('v-problem')||'a pain'}" leads to ${v('v-outcome')||'a result'}.`;
      const qs=['When did this last happen?','What have you tried?','How do you solve it today?','What would make this a must-have?','Pilot for 7 days?'];
      out('v-output',`Hypothesis:\n  ${hyp}\n\nMVP:\n  Landing page + waitlist + concierge trial.\n\nInterview questions:\n  - ${qs.join('\n  - ')}\n\nMetrics:\n  10 signups • 3 replies • 2 pilots in 7 days.`);
    });
    g('copy-plan').addEventListener('click',()=> navigator.clipboard.writeText(g('v-output').textContent||''));
    g('dl-plan').addEventListener('click',()=> download('validation-plan.txt', g('v-output').textContent||''));
    g('v-reset').addEventListener('click',()=> out('v-output',''));
  }
  if(g('positioning-app')){
    g('gen-pos').addEventListener('click',()=>{
      const stmt=`For ${v('p-seg')||'a focused segment'} who need ${v('p-need')||'a need'}, ${v('p-prod')||'our product'} provides ${v('p-benefit')||'a key benefit'} unlike ${v('p-diff')||'alternatives'}.`;
      out('p-output', stmt);
    });
    g('p-reset').addEventListener('click',()=> out('p-output',''));
  }
  if(g('brand-app')){
    g('gen-brand').addEventListener('click',()=>{
      const seeds=(v('b-kws')||'simple,fast,clean').split(',').map(s=>s.trim()).filter(Boolean);
      const tone=v('b-tone')||'friendly';
      function idea(seed,i){return (seed||'nova')+['ly','loop','hub','forge','nest'][i%5];}
      const names=Array.from({length:5},(_,i)=>idea(seeds[i%seeds.length],i));
      out('b-output',`Name ideas:\n - ${names.join('\n - ')}\n\nTagline: ${tone} value, delivered.`);
    });
    g('b-reset').addEventListener('click',()=> out('b-output',''));
  }
  if(g('unit-app')){
    g('calc-unit').addEventListener('click',()=>{
      const price=parseFloat(v('m-price')||'0')||0, cogs=parseFloat(v('m-cogs')||'0')||0, cac=parseFloat(v('m-cac')||'0')||0, months=parseFloat(v('m-months')||'0')||0;
      const gm=price>0?(price-cogs)/price:0, ltv=months>0?price*gm*months:0, ratio=cac>0?ltv/cac:0;
      out('m-output',`Gross margin: ${(gm*100).toFixed(1)}%\nLTV: $${ltv.toFixed(2)}\nCAC: $${cac.toFixed(2)}\nLTV:CAC: ${ratio.toFixed(2)}`);
    });
    g('m-reset').addEventListener('click',()=> out('m-output',''));
  }
  if(g('sop-app')){
    g('sop-add').addEventListener('click',()=>{
      const list=document.getElementById('sop-steps'); const i=(list.children.length||0)+1;
      const div=document.createElement('div'); div.innerHTML=`<label>Step ${i}</label><input type="text" class="sop-step" placeholder="Describe step ${i}">`; list.appendChild(div);
    });
    g('sop-gen').addEventListener('click',()=>{
      const steps=Array.from(document.querySelectorAll('.sop-step')).map((el,i)=>` ${i+1}. ${el.value||'TBD'}`).join('\n');
      out('sop-output',`SOP: ${v('sop-name')||'Untitled'}\n\nSteps:\n${steps}`);
    });
    g('sop-reset').addEventListener('click',()=>{ document.getElementById('sop-steps').innerHTML=''; out('sop-output',''); });
  }
  if(g('legal-app')){
    g('gen-legal').addEventListener('click',()=>{
      out('l-output',`Checklist:\n - Structure: ${v('l-type')||'Sole trader'}\n - ABN/ASIC\n - Bank account\n - ATO registrations\n - Insurance\n - Website privacy/terms\n - Record keeping in ${v('l-state')||'ACT'}`);
    });
    g('l-reset').addEventListener('click',()=> out('l-output',''));
  }
  const cform=document.getElementById('contact-form');
  if(cform){ cform.addEventListener('submit',(e)=>{e.preventDefault(); const name=v('c-name'),email=v('c-email'),msg=v('c-msg'); location.href=`mailto:u3311230@uni.canberra.edu.au?subject=Contact from ${name||'Visitor'}&body=${encodeURIComponent('Name: '+name+'\nEmail: '+email+'\n\n'+msg)}`; }); }
});
