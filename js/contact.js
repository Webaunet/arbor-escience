(function(){
var f=document.getElementById('devis-form');if(!f)return;
var rec=document.getElementById('recap'),pre=document.getElementById('recap-text');
var rules={
nom:function(v){return v.trim().length>=2||'Indiquez votre nom (2 lettres minimum).'},
tel:function(v){return /^(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}$/.test(v.trim())||'Indiquez un numéro valide, par exemple 06 12 34 56 78.'},
commune:function(v){return v.trim().length>=2||'Indiquez votre commune.'},
besoin:function(v){return v!==''||'Choisissez votre besoin dans la liste.'}};
function check(el){var r=rules[el.name];if(!r)return true;var res=r(el.value),box=el.closest('.fld'),m=box.querySelector('.err');
if(res===true){box.classList.remove('bad');el.removeAttribute('aria-invalid');return true}
m.textContent=res;box.classList.add('bad');el.setAttribute('aria-invalid','true');return false}
f.querySelectorAll('input,select').forEach(function(el){el.addEventListener('blur',function(){check(el)});el.addEventListener('input',function(){if(el.getAttribute('aria-invalid'))check(el)})});
f.addEventListener('submit',function(e){e.preventDefault();var first=null;
f.querySelectorAll('input,select').forEach(function(el){if(!check(el)&&!first)first=el});
if(first){first.focus();return}
var d=new FormData(f),t='Demande de devis – ARBOR\'ESCIENCE\nNom : '+d.get('nom').trim()+'\nTéléphone : '+d.get('tel').trim()+'\nCommune : '+d.get('commune').trim()+'\nBesoin : '+d.get('besoin')+(d.get('message').trim()?'\nMessage : '+d.get('message').trim():'');
pre.textContent=t;var enc=encodeURIComponent(t);
document.getElementById('b-sms').href='sms:+33621381189?&body='+enc;
document.getElementById('b-mail').href='mailto:arborescience@free.fr?subject='+encodeURIComponent('Demande de devis')+'&body='+enc;
f.hidden=true;document.getElementById('form-head').hidden=true;rec.classList.add('show');rec.setAttribute('tabindex','-1');rec.focus();rec.scrollIntoView({behavior:'smooth',block:'start'})});
document.getElementById('b-copy').addEventListener('click',function(){var b=this,t=pre.textContent;
function done(){b.textContent='Copié ✔';setTimeout(function(){b.textContent='Copier'},2000)}
if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(done,function(){sel()})}else sel();
function sel(){var r=document.createRange();r.selectNodeContents(pre);var s=getSelection();s.removeAllRanges();s.addRange(r);try{document.execCommand('copy');done()}catch(x){}}});
document.getElementById('b-edit').addEventListener('click',function(){rec.classList.remove('show');f.hidden=false;document.getElementById('form-head').hidden=false;f.querySelector('input').focus()});
})();
