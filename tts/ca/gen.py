import json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
B='../sherpa-onnx-v1.10.30-linux-x64-static/bin/sherpa-onnx-offline-tts'; M='../vits-piper-ca_ES-upc_ona-medium'
os.makedirs('mp3',exist_ok=True); os.makedirs('wav',exist_ok=True)
L=json.load(open('lista.json',encoding='utf8'))
def one(it):
    out=f"mp3/{it['k']}.mp3"
    if os.path.exists(out) and os.path.getsize(out)>300: return 0
    w=f"wav/{it['k']}.wav"; t=it['texto']
    if not t.endswith(('.','!','?')): t+='.'
    r=subprocess.run([B,f'--vits-model={M}/ca_ES-upc_ona-medium.onnx',f'--vits-tokens={M}/tokens.txt',f'--vits-data-dir={M}/espeak-ng-data','--num-threads=1','--vits-length-scale=1.05',f'--output-filename={w}',t],capture_output=True)
    if r.returncode or not os.path.exists(w): print('FALLO',it['k'],flush=True); return 0
    subprocess.run(['ffmpeg','-loglevel','error','-y','-i',w,'-af','silenceremove=start_periods=1:start_threshold=-50dB,apad=pad_dur=0.12','-ac','1','-ar','22050','-b:a','32k',out]); os.remove(w); return 1
with ThreadPoolExecutor(4) as ex:
    n=0
    for i,r in enumerate(ex.map(one,L),1):
        n+=r
        if i%200==0: print(i,'de',len(L),flush=True)
print('HECHO',n,flush=True)
