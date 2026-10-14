import asyncio, subprocess, time, sys
from playwright.async_api import async_playwright
async def main():
    srv=subprocess.Popen([sys.executable,'-m','http.server','8769','--directory','web-en'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--autoplay-policy=no-user-gesture-required']); errs=[]
        for url in ('http://localhost:8769/index.html','file:///home/claude/lingo/web-en/index.html'):
            pg=await b.new_page(viewport={'width':400,'height':860}); pg.on('pageerror',lambda e: errs.append(str(e)))
            await pg.route('**/*',lambda r: r.continue_() if ('localhost' in r.request.url or r.request.url.startswith('file:')) else r.abort())
            await pg.add_init_script("window.__played=[];const A=window.Audio;window.Audio=function(s){const a=new A(s);a.addEventListener('playing',()=>window.__played.push(Math.round(a.duration*100)/100));a.addEventListener('error',()=>window.__played.push('ERR'));return a}")
            await pg.goto(url); await pg.wait_for_selector('.node')
            await pg.click('[data-guide="4"]'); await pg.wait_for_selector('.sheet .say'); await pg.click('.sheet .say >> nth=1'); await pg.wait_for_timeout(1500)
            await pg.click('.sheet [data-act="hide"]'); await pg.click('[data-mod="1.1"]'); await pg.click('.sheet [data-start="1.1"]'); await pg.click('[data-act="begin"]'); await pg.wait_for_timeout(600)
            # primer ejercicio: emparejar → tocar una palabra italiana reproduce su audio
            await pg.click('[data-ml] >> nth=0'); await pg.wait_for_timeout(1500)
            print(url[:5],'reproducidos (s):',await pg.evaluate('window.__played'),'packs:',await pg.evaluate('Object.keys(window.LINGO_PACK)'))
            await pg.close()
        print('errores',errs[:3]); await b.close()
    srv.terminate()
asyncio.run(main())
