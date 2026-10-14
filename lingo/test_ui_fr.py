import asyncio, subprocess, time, sys, json
from playwright.async_api import async_playwright
CH='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
ICON='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" rx="{r}" fill="#1F5FD1"/><circle cx="386" cy="132" r="44" fill="#F5B81F"/><text x="248" y="340" text-anchor="middle" font-family="DejaVu Sans,Arial,sans-serif" font-weight="800" font-size="{fs}" fill="#fff" letter-spacing="-8">SL</text></svg>'''
async def main():
    srv=subprocess.Popen([sys.executable,'-m','http.server','8777','--directory','web-fr'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path=CH)
        errs=[]
        async def run(scheme,tag):
            ctx=await b.new_context(viewport={'width':400,'height':860},color_scheme=scheme,device_scale_factor=2)
            pg=await ctx.new_page(); pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None); pg.on('pageerror',lambda e: errs.append('PAGEERROR '+str(e)))
            await pg.route('**/*',lambda r: r.continue_() if 'localhost' in r.request.url else r.abort())
            await pg.goto('http://localhost:8777/index.html'); await pg.wait_for_selector('.node')
            ov=await pg.evaluate('document.documentElement.scrollWidth-innerWidth'); print(tag,'overflow',ov)
            await pg.screenshot(path=f'shots-fr/{tag}-home.png')
            if scheme=='dark': await ctx.close(); return
            await pg.click('[data-guide="1"]'); await pg.wait_for_selector('.pic'); await pg.wait_for_timeout(400); await pg.screenshot(path='shots-fr/guide.png'); await pg.click('.sheet [data-act="hide"]')
            await pg.click('[data-mod="1.1"]'); await pg.screenshot(path='shots-fr/sheet.png'); await pg.click('.sheet [data-start=\"1.1\"]'); await pg.screenshot(path='shots-fr/intro.png'); await pg.click('[data-act="begin"]')
            seen=set(); wrongDone=False; steps=0
            while await pg.query_selector('.lesson') and steps<60:
                steps+=1
                t=await pg.evaluate('SaimapLingo.current.ex.type')
                if t not in seen: seen.add(t); await pg.screenshot(path=f'shots-fr/ex-{t}.png')
                if t=='match':
                    ks=await pg.evaluate('SaimapLingo.current.ex.items.map(i=>i.k)')
                    for k in ks: await pg.click(f'[data-ml="{k}"]'); await pg.click(f'[data-mr="{k}"]')
                elif t in('order','listenOrder'):
                    idx=await pg.evaluate('(()=>{const e=SaimapLingo.current.ex,u=[];return e.tokens.map(t=>{const i=e.bank.findIndex((b,j)=>b===t&&!u.includes(j));u.push(i);return i})})()')
                    for i in idx: await pg.click(f'#bank [data-tile="{i}"]')
                    await pg.click('#go')
                elif t=='speak':
                    await pg.click('[data-act="skipspeak"]'); continue
                elif t=='type':
                    await pg.fill('#answer',await pg.evaluate('SaimapLingo.current.ex.answer')); await pg.click('#go')
                else:
                    i=await pg.evaluate('SaimapLingo.current.ex.options.indexOf(SaimapLingo.current.ex.answer)')
                    if not wrongDone and t!='mcIE'or False:
                        pass
                    if not wrongDone and steps>3: i=(i+1)%3; wrongDone=True
                    await pg.click(f'[data-opt="{i}"]'); await pg.click('#go')
                    if wrongDone and 'bad' not in seen and await pg.query_selector('.lfoot.bad'): seen.add('bad'); await pg.screenshot(path='shots-fr/feedback-bad.png')
                await pg.wait_for_selector('[data-act="next"]'); await pg.click('[data-act="next"]')
            await pg.wait_for_selector('.center'); await pg.screenshot(path='shots-fr/result.png')
            print('pasos',steps,'tipos',sorted(seen)); print('estado',await pg.evaluate('JSON.stringify({xp:SaimapLingo.state.xp,done:SaimapLingo.state.done,streak:SaimapLingo.state.streak,items:Object.keys(SaimapLingo.state.it).length})'))
            await pg.click('#go'); await pg.wait_for_selector('.node.done'); await pg.screenshot(path='shots-fr/home-after.png')
            # segunda lección: debe traer repaso
            await pg.click('[data-mod="1.2"]'); await pg.click('.sheet [data-start=\"1.2\"]')
            print('1.2 repaso',await pg.evaluate('SaimapLingo.lesson.q.filter(x=>x.review).length'),'de',await pg.evaluate('SaimapLingo.lesson.q.length'))
            await pg.click('[data-act="askquit"]'); await pg.click('[data-act="quit"]'); await pg.click('[data-act="me"]'); await pg.screenshot(path='shots-fr/me.png',full_page=True)
            await pg.reload(); await pg.wait_for_selector('.node.done'); print('persistencia local ok')
            await ctx.close()
        import os; os.makedirs('shots-fr',exist_ok=True)
        await run('light','light'); await run('dark','dark')
        print('errores consola:',[e for e in errs if 'ERR_FAILED' not in e and 'net::' not in e][:8])
        await b.close()
    srv.terminate()
asyncio.run(main())
