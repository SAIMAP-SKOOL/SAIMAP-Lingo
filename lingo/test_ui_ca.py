import asyncio, subprocess, time, sys
from playwright.async_api import async_playwright
async def main():
    srv=subprocess.Popen([sys.executable,'-m','http.server','8772','--directory','platform'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
    async with async_playwright() as p:
        b=await p.chromium.launch(); errs=[]
        pg=await (await b.new_context(viewport={'width':400,'height':860},device_scale_factor=2)).new_page()
        pg.on('console',lambda m: errs.append(m.text) if m.type=='error' and 'net::' not in m.text and 'Failed to load' not in m.text else None); pg.on('pageerror',lambda e: errs.append('PAGEERROR '+str(e)))
        await pg.route('**/*',lambda r: r.continue_() if 'localhost' in r.request.url else r.abort())
        await pg.add_init_script("localStorage.setItem('sl.ca.pref',JSON.stringify({audio:true,sfx:false,free:true}))")
        await pg.goto('http://localhost:8772/index.html'); await pg.wait_for_timeout(1200)
        await pg.screenshot(path='shots-ca/0-picker.png')
        await pg.click('[data-lang="ca"]'); await pg.wait_for_selector('.node'); await pg.wait_for_timeout(500)
        await pg.screenshot(path='shots-ca/1-home.png'); print('overflow',await pg.evaluate('document.documentElement.scrollWidth-innerWidth'))
        seen=set()
        for mod in ['1.1','4.4','16.2','35.3','49.1']:
            await pg.evaluate(f'SaimapLingo.start && 0'); 
            await pg.click(f'[data-mod="{mod}"]'); await pg.click(f'.sheet [data-start="{mod}"]')
            if await pg.query_selector('[data-act="begin"]'):
                if 'intro' not in seen: seen.add('intro'); await pg.screenshot(path='shots-ca/2-intro.png')
                await pg.click('[data-act="begin"]')
            steps=0
            while await pg.query_selector('.lesson') and steps<60:
                steps+=1; t=await pg.evaluate('SaimapLingo.current.ex.type')
                if t not in seen: seen.add(t); await pg.screenshot(path=f'shots-ca/x-{t}.png')
                if t=='match':
                    for k in await pg.evaluate('SaimapLingo.current.ex.items.map(i=>i.k)'): await pg.click(f'[data-ml="{k}"]'); await pg.click(f'[data-mr="{k}"]')
                elif t in('order','listenOrder'):
                    for i in await pg.evaluate('(()=>{const e=SaimapLingo.current.ex,u=[];return e.tokens.map(t=>{const i=e.bank.findIndex((b,j)=>b===t&&!u.includes(j));u.push(i);return i})})()'): await pg.click(f'#bank [data-tile="{i}"]')
                    await pg.click('#go')
                elif t=='type':
                    ans=await pg.evaluate('SaimapLingo.current.ex.answer')
                    if 'kb' not in seen:
                        seen.add('kb')
                        # escribir sin acentos y con l.l → debe dar "accent"; los botones de letras añaden caracteres
                        await pg.click('#answer'); await pg.keyboard.type(ans.replace('·','.').translate(str.maketrans('àèéíïòóúü','aeeiioouu')))
                        if await pg.query_selector('.keys [data-key="ç"]'): await pg.click('.keys [data-key="ç"]'); await pg.keyboard.press('Backspace')
                        await pg.screenshot(path='shots-ca/x-type-kb.png')
                        await pg.click('#go'); await pg.wait_for_timeout(300); print('typed', ans, '→', await pg.eval_on_selector('#answer','e=>e.value'), await pg.inner_text('.foot') if await pg.query_selector('.foot') else '')
                    else:
                        await pg.fill('#answer',ans); await pg.click('#go')
                elif t in('speak',):
                    await pg.click('text=Saltar'); await pg.wait_for_timeout(300)
                    if not await pg.query_selector('[data-act="next"]'): continue
                else:
                    i=await pg.evaluate('SaimapLingo.current.ex.options.indexOf(SaimapLingo.current.ex.answer)')
                    await pg.click(f'[data-opt="{i}"]'); await pg.click('#go')
                await pg.wait_for_selector('[data-act="next"]'); await pg.click('[data-act="next"]')
            await pg.wait_for_selector('.center'); await pg.wait_for_timeout(500)
            if 'result' not in seen: seen.add('result'); await pg.screenshot(path='shots-ca/3-result.png')
            await pg.click('#go'); await pg.wait_for_selector('.node')
        print('seen',sorted(seen)); print('errs',errs[:5])
        await b.close()
    srv.kill()
asyncio.run(main())
