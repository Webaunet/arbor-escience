import sys,os,json,glob,threading,http.server,socketserver,functools
from playwright.sync_api import sync_playwright
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H=functools.partial(http.server.SimpleHTTPRequestHandler,directory=R)
class Q(H.func):
    def log_message(s,*a):pass
S=socketserver.TCPServer(('127.0.0.1',0),functools.partial(Q,directory=R));P=S.server_address[1]
threading.Thread(target=S.serve_forever,daemon=True).start()
pages=sorted(os.path.basename(f) for f in glob.glob(R+'/*.html'))
W=[360,414,768,821,980,981,1280,1920]
JS="""()=>{const o=[];const vw=innerWidth;
if(document.documentElement.scrollWidth>vw)o.push('overflow-x '+document.documentElement.scrollWidth);
document.querySelectorAll('body *').forEach(e=>{const s=getComputedStyle(e);if(s.display=='none'||s.visibility=='hidden')return;
const t=[...e.childNodes].some(n=>n.nodeType==3&&n.textContent.trim());if(t&&parseFloat(s.fontSize)<15.5&&!e.closest('small'))o.push('font '+parseFloat(s.fontSize)+' '+e.tagName+' '+e.textContent.trim().slice(0,20));
if(['A','BUTTON','INPUT','SELECT','TEXTAREA'].includes(e.tagName)){const r=e.getBoundingClientRect();if(r.width&&(r.height<43.5||r.width<43.5)&&!e.closest('.skip')&&!(e.classList.contains('skip')))o.push('tap '+Math.round(r.width)+'x'+Math.round(r.height)+' '+(e.textContent.trim().slice(0,20)||e.className))}});
document.querySelectorAll('img').forEach(i=>{if(!i.complete||!i.naturalWidth)o.push('img-broken '+i.getAttribute('src'));else if(i.naturalWidth<i.clientWidth-1)o.push('img-upscaled '+i.getAttribute('src'));
const r=i.getBoundingClientRect();if(i.naturalWidth&&Math.abs(i.naturalWidth/i.naturalHeight-i.width/i.height)>.02&&getComputedStyle(i).objectFit=='fill'&&r.width)o.push('img-ratio '+i.getAttribute('src'))});
const hh=[...document.querySelectorAll('main>section,.hero')].map(s=>Math.round(s.getBoundingClientRect().height/innerHeight*100));
const f=document.querySelector('footer');const fh=f?Math.round(f.getBoundingClientRect().height/innerHeight*100):0;
const hd=document.querySelector('.hd');const lg=document.querySelector('.logo').getBoundingClientRect(),cl=document.querySelector('.call').getBoundingClientRect(),nv=document.querySelector('.nav');
const nr=getComputedStyle(nv).display!='none'&&getComputedStyle(nv).position!='absolute'?nv.getBoundingClientRect():null;
if(nr&&(nr.left<lg.right||nr.right>cl.left))o.push('nav-overlap');
return {o,hh,fh,h1:document.querySelectorAll('h1').length,nav:nr?'full':'burger'}}"""
bad=0
with sync_playwright() as p:
    b=p.chromium.launch();
    for pg in pages:
        for w in W:
            c=b.new_context(viewport={'width':w,'height':900 if w>600 else 800});g=c.new_page();g.goto(f'http://127.0.0.1:{P}/{pg}',wait_until='networkidle');g.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')");g.wait_for_timeout(300)
            r=g.evaluate(JS);exp='full' if w>980 else 'burger'
            iss=r['o']+([] if r['nav']==exp else ['nav-mode '+r['nav']])+([] if r['h1']==1 else ['h1 x'+str(r['h1'])])+(['footer %d%%'%r['fh']] if r['fh']>30 else [])
            if iss:bad+=1;print(pg,w,sorted(set(iss))[:8])
            if w in(390,1280) or w==414:print(pg,w,'sections%',r['hh'],'footer%',r['fh']) if '-v' in sys.argv else None
            c.close()
    # liens et poids
    import re
    for pg in pages:
        h=open(R+'/'+pg,encoding='utf8').read()
        for l in re.findall(r'(?:href|src)="(?!https?:|tel:|mailto:|sms:)([^"#]+)',h):
            if not os.path.exists(os.path.join(R,l)) and l not in pages:print(pg,'lien-manquant',l)
        t=sum(os.path.getsize(R+'/'+s) for s in set(re.findall(r'src="(images/[^"]+\.jpg)"',h)))+(os.path.getsize(R+'/images/hero.jpg') if pg=='index.html' else 0)
        print(pg,'images ko',t//1024)
print('ECARTS',bad)
