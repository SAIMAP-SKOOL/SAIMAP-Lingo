globalThis.window=globalThis; require('./src/pics.js'); require('./src/data.js'); require('./src/data-a2.js'); require('./src/data-b1.js'); require('./src/data-b2.js'); require('./src/data-c1.js'); require('./src/data-c2.js'); require('./src/engine.js');
const E=Engine, C=COURSE; let bad=0; const err=m=>{bad++;console.log('ERR',m)};
// datos
for(const i of E.ITEMS){
  if(i.kind==='g'){ if(!i.q.includes('___'))err('sin hueco '+i.k); if(i.o.includes(i.a)||i.o[0]===i.o[1]||!i.o[0]||!i.o[1]||!i.es)err('gap '+i.k+' '+i.q);}
  else if(!i.it||!i.es) err('vacío '+i.k);
}
const cnt=k=>E.ITEMS.filter(i=>i.kind===k).length; console.log('items',E.ITEMS.length,'v',cnt('v'),'s',cnt('s'),'g',cnt('g'));
// duplicados de traducción dentro de un módulo (ambigüedad en opciones)
for(const u of C.units)for(let m=1;m<=4;m++){const v=E.ITEMS.filter(i=>i.u===u.n&&i.m===m&&i.kind==='v');const s=new Set();for(const i of v){if(s.has(i.es))err('dup es '+i.k+' '+i.es);s.add(i.es)}}
// lecciones
let rows=[];
for(const u of C.units)for(let m=1;m<=5;m++){
  let S=E.blank(); let tot=0,rev=0,min=99;
  for(let r=0;r<40;r++){const L=E.gen(S,u.n,m,{voice:r%2}); tot+=L.length; rev+=L.filter(x=>x.review).length; min=Math.min(min,L.length);
    for(const x of L){ if(x.review){const it=x.item; if(m<5? E.ord(it.u,it.m)>=E.ord(u.n,m): it.u>=u.n)err('repaso no anterior');}
      if(x.options){ if(new Set(x.options).size!==x.options.length)err('opciones repetidas '+x.item.k+' '+x.options); if(!x.options.includes(x.answer))err('sin respuesta'); if(x.options.length<3)err('pocas opciones '+x.item.k+' '+x.type);}
      if(x.tokens&&!E.checkOrder(x,x.tokens))err('order');
      if(x.type==='type'&&E.checkType(x,x.answer)!=='ok')err('type');
      if(x.item)E.record(S,x.item.k,Math.random()<.8); }
  }
  rows.push(`${u.n}.${m}: n=${(tot/40).toFixed(1)} repaso=${(100*rev/tot).toFixed(0)}% min=${min}`);
}
console.log(rows.join('\n'));
// merge y finish
let a=E.blank(),b=E.blank(); E.record(a,'1.1.v0',true); E.finish(a,'1.1',1); E.record(b,'1.1.v0',false); b.xp=50; const mg=E.merge(a,b);
console.log('merge',JSON.stringify(mg).slice(0,160), 'unlock 1.2',E.unlocked(mg,1,2), 'unlock 1.3',E.unlocked(mg,1,3), 'next',JSON.stringify(E.nextUp(mg)));
console.log('tokens',E.tokens('Ecco il resto. Buona giornata!'),E.tokens('Scusi, Lei è il signor Rossi?'));
console.log(bad?'FALLOS '+bad:'OK');
