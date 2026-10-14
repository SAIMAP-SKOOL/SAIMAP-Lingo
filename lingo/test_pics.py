import asyncio, subprocess, time, sys, json
from playwright.async_api import async_playwright
async def main():
    srv=subprocess.Popen([sys.executable,'-m','http.server','8767','--directory','web'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'); errs=[]
        ctx=await b.new_context(viewport={'width':400,'height':860},device_scale_factor=2); pg=await ctx.new_page()
        pg.on('console',lambda m: errs.append(m.text) if m.type=='error' and 'net::' not in m.text else None); pg.on('pageerror',lambda e: errs.append('PAGEERROR '+str(e)))
        await pg.route('**/*',lambda r: r.continue_() if 'localhost' in r.request.url else r.abort())
        await pg.add_init_script("""if(!localStorage.getItem('sl.pref')){localStorage.setItem('sl.pref',JSON.stringify({audio:true,sfx:true,free:true}));
          const it={};for(let m=1;m<=4;m++)for(let i=0;i<14;i++)it['8.'+m+'.v'+i]=[1,0,Date.now()];
          localStorage.setItem('sl.state',JSON.stringify({v:1,xp:45,dx:15,streak:3,day:new Date().toISOString().slice(0,10),done:{'1.1':{s:3,n:1},'1.2':{s:2,n:1}},it,t:1}))}""")
        await pg.goto('http://localhost:8767/index.html'); await pg.wait_for_selector('.node'); await pg.wait_for_timeout(300)
        await pg.screenshot(path='shots/n-home.png'); print('overflow',await pg.evaluate('document.documentElement.scrollWidth-innerWidth'))
        seen=set()
        for rnd in range(4):
            await pg.click('[data-mod="8.1"]'); await pg.click('.sheet [data-start="8.1"]')
            if await pg.query_selector('[data-act="begin"]'):
                if 'intro' not in seen: seen.add('intro'); await pg.screenshot(path='shots/n-intro.png')
                await pg.click('[data-act="begin"]')
            steps=0
            while await pg.query_selector('.lesson') and steps<60:
                steps+=1; t=await pg.evaluate('SaimapLingo.current.ex.type')
                if t not in seen: seen.add(t); await pg.screenshot(path=f'shots/n-{t}.png')
                if t=='match':
                    for k in await pg.evaluate('SaimapLingo.current.ex.items.map(i=>i.k)'): await pg.click(f'[data-ml="{k}"]'); await pg.click(f'[data-mr="{k}"]')
                elif t in('order','listenOrder'):
                    for i in await pg.evaluate('(()=>{const e=SaimapLingo.current.ex,u=[];return e.tokens.map(t=>{const i=e.bank.findIndex((b,j)=>b===t&&!u.includes(j));u.push(i);return i})})()'): await pg.click(f'#bank [data-tile="{i}"]')
                    await pg.click('#go')
                elif t=='type': await pg.fill('#answer',await pg.evaluate('SaimapLingo.current.ex.answer')); await pg.click('#go')
                else:
                    i=await pg.evaluate('SaimapLingo.current.ex.options.indexOf(SaimapLingo.current.ex.answer)')
                    if t=='picIE' and 'bad' not in seen: i=(i+1)%4
                    await pg.click(f'[data-opt="{i}"]'); await pg.click('#go')
                    if t=='picIE' and 'bad' not in seen: seen.add('bad'); await pg.wait_for_timeout(450); await pg.screenshot(path='shots/n-bad.png')
                    elif 'good' not in seen and steps>4: seen.add('good'); await pg.wait_for_timeout(450); await pg.screenshot(path='shots/n-good.png')
                await pg.wait_for_selector('[data-act="next"]'); await pg.click('[data-act="next"]')
            await pg.wait_for_selector('.center'); 
            if 'result' not in seen: seen.add('result'); await pg.wait_for_timeout(700); await pg.screenshot(path='shots/n-result.png')
            await pg.click('#go'); await pg.wait_for_selector('.node')
            if {'picIE','picEI'}<=seen: break
        print('tipos',sorted(seen)); await pg.click('[data-act="me"]'); await pg.screenshot(path='shots/n-me.png',full_page=True)
        ctx2=await b.new_context(viewport={'width':400,'height':860},device_scale_factor=2,color_scheme='dark'); p2=await ctx2.new_page()
        await p2.route('**/*',lambda r: r.continue_() if 'localhost' in r.request.url else r.abort()); await p2.goto('http://localhost:8767/index.html'); await p2.wait_for_selector('.node'); await p2.evaluate('scrollTo(0,500)'); await p2.wait_for_timeout(200); await p2.screenshot(path='shots/n-dark.png')
        print('errores',errs[:5]); await b.close()
    srv.terminate()
asyncio.run(main())
