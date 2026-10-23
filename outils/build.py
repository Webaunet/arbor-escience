# Génère les pages intérieures à partir de l'en-tête/pied de page de index.html. Usage : python3 outils/build.py
import re,os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
idx=open(R+'/index.html',encoding='utf8').read()
HEAD=re.search(r'<body>\n(.*?</header>)',idx,re.S).group(1)
FOOT=re.search(r'(<footer.*?</footer>)',idx,re.S).group(1)
def ic(n,c='ic'):return f'<svg class="{c}" aria-hidden="true"><use href="images/icons.svg#i-{n}"/></svg>'
def page(fn,title,desc,cur,body,extra=''):
    h=HEAD.replace(' aria-current="page"','')
    if cur:h=h.replace(f'<a href="{cur}">',f'<a href="{cur}" aria-current="page">')
    s=f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" type="image/png" href="images/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700&family=Nunito+Sans:wght@400;600;700;800&display=swap">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
{h}
<main id="contenu">
{body}
</main>
{FOOT}
<script src="js/main.js" defer></script>{extra}
</body></html>
'''
    open(R+'/'+fn,'w',encoding='utf8').write(s)
BT='<a class="btn btn-p" href="contact.html">Demander un devis</a>'
TEL='<a class="btn btn-o" href="tel:+33621381189">Appeler le 06 21 38 11 89</a>'
def li(t):return f'<li>{ic("check")}<span>{t}</span></li>'

# ---------- PRESTATIONS ----------
page('prestations.html',"Prestations de paysagiste à Orgeval – ARBOR'ESCIENCE","Création de jardin, aménagement, entretien : les prestations d'ARBOR'ESCIENCE, paysagiste à Orgeval (Yvelines).",'prestations.html',f'''
<section class="ph ph-g on-dark"><div class="wrap row2">
<div><span class="kick">Nos prestations</span><h1>Du premier croquis à l’entretien de chaque saison</h1>
<p class="lead">Création, aménagement et entretien : Arbor’Escience prend en charge votre jardin de A à Z, avec des solutions sur mesure adaptées à votre sol, votre exposition et vos envies.</p>
<div class="cta">{BT}{TEL}</div></div>
<div class="mosaic"><img src="images/creation.jpg" width="900" height="491" alt="Jardin récemment créé avec massifs, pelouse et cheminement"><img src="images/amenagement.jpg" width="900" height="491" alt="Terrasse en bois en cours de pose devant une maison en pierre"><img src="images/entretien.jpg" width="900" height="672" alt="Taille d'une haie dans un jardin"></div>
</div></section>

<section class="sec sheet" id="creation" style="background:var(--cream)"><div class="wrap row2">
<div><span class="kick">Création de jardin</span><h2>Profitez du jardin qui vous correspond</h2>
<p class="lead">Votre jardin prolonge votre intérieur dès les beaux jours. Choisissez votre atmosphère, nous l’accordons à son exposition, à la nature de son sol et à son ensoleillement.</p>
<ul class="tag-row"><li>Coloré</li><li>Épuré</li><li>Méditerranéen</li><li>Champêtre</li></ul>
<ol class="steps"><li><div><strong>Visite sur place</strong><span>Nous nous rendons chez vous pour comprendre les lieux.</span></div></li><li><div><strong>Projet défini ensemble</strong><span>Vos envies et les contraintes du jardin, associées avec soin.</span></div></li><li><div><strong>Plan et esquisse</strong><span>Des supports visuels pour vous aider à vous projeter.</span></div></li></ol></div>
<img class="" src="images/creation.jpg" width="900" height="491" loading="lazy" alt="Création de jardin : pelouse, massifs et cheminement autour d'une maison contemporaine" style="border-radius:var(--r);box-shadow:var(--sh);width:100%;aspect-ratio:6/5;object-fit:cover">
</div></section>

<section class="sec sheet" id="amenagement" style="background:#fff"><div class="wrap">
<div class="head"><span class="kick">Aménagement du jardin</span><h2>Paysagez votre jardin de manière durable</h2><p class="lead">Arbor’Escience assure la mise en œuvre de votre projet, avec des finitions soignées et un réseau de fournisseurs sélectionnés pour leur proximité et la qualité de leurs produits.</p></div>
<div class="cards3">
<div class="k"><span class="ico">{ic("leaf")}</span><h3>Végétalisation</h3><p>Plantations, création de massifs et engazonnement.</p></div>
<div class="k"><span class="ico">{ic("deck")}</span><h3>Terrasses en bois</h3><p>Réalisation de terrasses en bois pour prolonger la maison.</p></div>
<div class="k"><span class="ico">{ic("drop")}</span><h3>Arrosage automatique</h3><p>Installation de systèmes d’arrosage automatique.</p></div>
<div class="k"><span class="ico">{ic("check")}</span><h3>Petites maçonneries</h3><p>Réalisation de petites maçonneries paysagères.</p></div>
<div class="k"><span class="ico">{ic("pin")}</span><h3>Clôtures</h3><p>Réalisation de clôtures adaptées à votre jardin.</p></div>
<div class="k"><span class="ico">{ic("clock")}</span><h3>Éclairage extérieur</h3><p>Installation de systèmes d’éclairage extérieur.</p></div>
</div></div></section>

<section class="sec sheet dark on-dark" id="entretien"><div class="wrap">
<div class="row2"><div><span class="kick">Entretien du jardin</span><h2>Profitez de votre jardin en toute sérénité</h2>
<p class="lead">Un jardin n’est pas figé : les végétaux grandissent, les besoins évoluent au fil des saisons. Interventions régulières, ponctuelles ou contrat annuel, nous composons une formule personnalisée.</p>
<ul class="tag-row"><li>Régulier</li><li>Ponctuel</li><li>Contrat annuel</li></ul></div>
<img src="images/tonte.jpg" width="900" height="502" loading="lazy" alt="Tonte de la pelouse devant une maison, haies et massifs fleuris" style="border-radius:var(--r);width:100%;aspect-ratio:16/10;object-fit:cover"></div>
<h3 style="margin-top:44px">Exemples d’interventions au printemps</h3>
<div class="cards3">
<div class="k dk"><h3>Pelouse</h3><ul>{li("Tonte")}{li("Scarification et regarnissage")}{li("Fertilisation")}</ul></div>
<div class="k dk"><h3>Massifs fleuris</h3><ul>{li("Désherbage")}{li("Paillage")}{li("Fertilisation")}{li("Suppression des fleurs fanées")}</ul></div>
<div class="k dk"><h3>Arbres et arbustes</h3><ul>{li("Taille des arbustes à floraison")}</ul><p style="margin-top:10px">Pour la taille et l’abattage des grands sujets, voir la page Élagage.</p></div>
</div></div></section>

<section class="sheet cta-l"><div class="wrap band-cta"><div><h2>Un projet de jardin ?</h2><p>Racontez-nous votre idée : nous passons la voir sur place.</p></div><div class="cta" style="margin:0"><a class="btn btn-d" href="contact.html">Demander un devis</a><a class="btn btn-l" href="tel:+33621381189" style="border-color:#1b2a05;color:#1b2a05">06 21 38 11 89</a></div></div></section>''')

# ---------- ELAGAGE ----------
page('elagage.html',"Élagage et abattage d'arbres à Orgeval – ARBOR'ESCIENCE","Taille douce, abattage, démontage, haubanage et rognage de souche à Orgeval et dans l'ouest des Yvelines.",'elagage.html',f'''
<section class="ph ph-photo bg-elagage on-dark"><div class="wrap"><span class="kick">Élagage et abattage</span><h1>Prendre soin de vos arbres</h1>
<p>Une taille « douce », raisonnée, qui préserve l’identité architecturale de l’arbre et assure sa pérennité. Quand c’est nécessaire, nous assurons aussi l’abattage et le démontage.</p>
<div class="cta">{BT}{TEL}</div></div></section>

<section class="sec sheet" id="pourquoi" style="background:var(--cream)"><div class="wrap row2 rev">
<div><span class="kick">Pourquoi intervenir</span><h2>L’arbre est un élément majeur du jardin, qui demande une attention particulière</h2>
<div class="cards3 c2" style="margin-top:22px">
<div class="k"><h3>Cohabitation</h3><p>Avec le bâti ou les autres végétaux, en milieu urbain.</p></div>
<div class="k"><h3>Sécurité</h3><p>Risques de rupture et mise en danger du public.</p></div>
<div class="k" style="grid-column:1/-1"><h3>Santé de l’arbre</h3><p>Maladies à repérer et à traiter par une taille adaptée.</p></div></div></div>
<img src="images/demontage.jpg" width="900" height="491" loading="lazy" alt="Élagueur encordé travaillant sur un grand arbre, bois coupé au sol" style="border-radius:var(--r);box-shadow:var(--sh);width:100%;aspect-ratio:6/5;object-fit:cover">
</div></section>

<section class="sec sheet" id="taille-douce" style="background:#fff"><div class="wrap row2">
<img src="images/equipe.jpg" width="900" height="491" loading="lazy" alt="Deux élagueurs préparant leur matériel de cordes devant leur camionnette" style="border-radius:var(--r);box-shadow:var(--sh);width:100%;aspect-ratio:5/4;object-fit:cover">
<div><span class="kick">Notre approche</span><h2>La taille « douce », plus respectueuse de l’arbre</h2>
<p class="lead">Nous proposons des solutions adaptées et raisonnées, plus respectueuses de l’architecture et de la biologie de l’arbre.</p>
<p class="quote">Notre objectif : préserver son identité architecturale et assurer sa pérennité.</p>
<p>Lorsque l’état de l’arbre l’impose, nous réalisons les travaux d’abattage et de démontage.</p></div>
</div></section>

<section class="sec sheet band on-dark" id="travaux"><div class="wrap">
<div class="head"><span class="kick">Nos travaux</span><h2>Cinq interventions pour vos arbres</h2></div>
<div class="cards3">
<div class="k dk"><span class="ico">{ic("tree")}</span><h3>Taille</h3><p>Travaux de taille adaptés à chaque sujet.</p></div>
<div class="k dk"><span class="ico">{ic("check")}</span><h3>Abattage</h3><p>Travaux d’abattage lorsque c’est nécessaire.</p></div>
<div class="k dk"><span class="ico">{ic("arrow")}</span><h3>Démontage</h3><p>Quand l’abattage en direct n’est pas possible.</p></div>
<div class="k dk"><span class="ico">{ic("leaf")}</span><h3>Haubanage</h3><p>Installation de hauban.</p></div>
<div class="k dk" style="grid-column:span 2"><span class="ico">{ic("deck")}</span><h3>Rognage de souche</h3><p>Pour retrouver un terrain net après l’abattage.</p></div>
</div></div></section>

<section class="sheet cta-d"><div class="wrap band-cta"><h2>Un arbre vous inquiète ?</h2><p>Appelez-nous, nous vous répondons du lundi au vendredi de 8h à 19h et le samedi de 8h à 17h.</p><a class="tel-big" href="tel:+33621381189">06 21 38 11 89</a></div></section>''')

# ---------- CONSEILS ----------
page('conseils.html',"Coaching et conseils jardin à Orgeval – ARBOR'ESCIENCE","Coaching jardin et conseils de saison par ARBOR'ESCIENCE, à Orgeval : plantation, essences, taille d'arbustes.",'conseils.html',f'''
<section class="ph ph-c"><div class="wrap split">
<div><span class="kick">Conseils &amp; coaching</span><h1>Prenez votre jardin en main, nous vous guidons</h1>
<p class="lead">Une question sur une plantation, une essence ou la taille d’un arbuste ? Arbor’Escience vous conseille, vous accompagne et vous fait bénéficier de son savoir-faire.</p>
<div class="cta">{BT}<a class="btn btn-l" href="#conseil">Le conseil d’octobre</a></div></div>
<div class="card-photo"><img src="images/conseil.jpg" width="1000" height="545" alt="Plan de jardin sur une tablette, devant un jardin en cours d'aménagement"></div>
</div></section>

<section class="sec sheet" id="coaching" style="background:#fff"><div class="wrap">
<div class="head"><span class="kick">Coaching</span><h2>Être conseillé, être assisté</h2><p class="lead">Vous voulez réaliser certaines tâches vous-même ? Nous vous accompagnons, avec des forfaits adaptés à vos attentes.</p></div>
<div class="cards3">
<div class="k"><span class="ico">{ic("leaf")}</span><h3>Réussir une plantation</h3><p>La manière de planter, l’emplacement, les gestes à connaître.</p></div>
<div class="k"><span class="ico">{ic("tree")}</span><h3>Connaître une essence</h3><p>Les caractéristiques d’une plante avant de la choisir.</p></div>
<div class="k"><span class="ico">{ic("chat")}</span><h3>Tailler un arbuste</h3><p>Le bon moment et la bonne façon de le tailler.</p></div>
</div></div></section>

<section class="sec sheet sand" id="conseil"><div class="wrap">
<div class="row2"><div><span class="kick">Le conseil d’octobre</span><h2>Camélia Sasanqua : la beauté florale d’automne</h2>
<p class="lead">Un arbuste à floraison automnale, aux fleurs délicates et parfumées, roses, blanches ou rouges, qui colorent le jardin quand la plupart des plantes se reposent.</p>
<p>Facile à entretenir et très durable, il garde un feuillage vert foncé persistant. Idéal pour apporter du raffinement à vos massifs ou à votre terrasse.</p></div>
<img src="images/plantation.jpg" width="900" height="491" loading="lazy" alt="Jardinier plantant des arbustes dans un massif" style="border-radius:var(--r);box-shadow:var(--sh);width:100%;aspect-ratio:16/10;object-fit:cover"></div>
<div class="cards3 c2">
<div class="k"><h3>En pleine terre</h3><ul>{li("Sol légèrement acide, bien drainé, riche en humus")}{li("Emplacement semi-ombragé, à l’abri des vents froids")}{li("Plantation à l’automne ou au printemps, hors période de gel")}{li("Arrosage régulier les premières années, paillage organique")}</ul></div>
<div class="k"><h3>En pot</h3><ul>{li("Contenant d’au moins 40 cm de diamètre, avec drainage")}{li("Terreau acide ou terre de bruyère")}{li("Lumière du matin, protection du soleil direct l’après-midi")}{li("Substrat humide sans excès ; voile d’hivernage en hiver")}</ul></div>
</div></div></section>

<section class="sheet cta-w"><div class="wrap band-cta"><div><h2>Une question sur votre jardin ?</h2><p>Posez-la-nous par téléphone ou via le formulaire.</p></div><div class="cta" style="margin:0"><a class="btn btn-d" href="contact.html">Nous écrire</a><a class="btn btn-l" href="tel:+33640753043">06 40 75 30 43</a></div></div></section>''')

# ---------- CONTACT ----------
page('contact.html',"Contact et devis – ARBOR'ESCIENCE à Orgeval","Contactez ARBOR'ESCIENCE à Orgeval pour un devis jardin ou élagage : téléphone, e-mail et formulaire de demande.",'contact.html',f'''
<section class="ph ph-d on-dark"><div class="wrap ph-in">
<div><span class="kick">Contact</span><h1>Parlons de votre projet</h1><p class="lead">Appelez-nous ou remplissez le formulaire : nous revenons vers vous pour définir votre projet, sur place si besoin.</p></div>
<div class="big-tel"><a class="tel-card" href="tel:+33621381189">{ic("phone")}<span><small>Téléphone</small><strong>06 21 38 11 89</strong></span></a>
<a class="tel-card" href="tel:+33640753043">{ic("phone")}<span><small>Second numéro</small><strong>06 40 75 30 43</strong></span></a>
<a class="tel-card" href="mailto:arborescience@free.fr">{ic("mail")}<span><small>E-mail</small><strong style="font-size:1.3rem">arborescience@free.fr</strong></span></a></div>
</div></section>

<section class="sec sheet" id="formulaire" style="background:var(--cream)"><div class="wrap row2" style="align-items:start">
<div class="form-card">
<div id="form-head"><h2 style="font-size:1.8rem">Demande de devis</h2><p style="color:var(--ink2)">Cinq champs, une minute. Les champs marqués * sont obligatoires.</p></div>
<form id="devis-form" novalidate>
<div class="fld"><label for="f-nom">Nom *</label><input id="f-nom" name="nom" type="text" autocomplete="name" required aria-describedby="e-nom"><p class="err" id="e-nom" role="alert"></p></div>
<div class="fld"><label for="f-tel">Téléphone *</label><input id="f-tel" name="tel" type="tel" autocomplete="tel" inputmode="tel" required aria-describedby="e-tel"><p class="err" id="e-tel" role="alert"></p></div>
<div class="fld"><label for="f-commune">Commune *</label><input id="f-commune" name="commune" type="text" autocomplete="address-level2" required aria-describedby="e-commune"><p class="err" id="e-commune" role="alert"></p></div>
<div class="fld"><label for="f-besoin">Votre besoin *</label><select id="f-besoin" name="besoin" required aria-describedby="e-besoin"><option value="">Choisir…</option><option>Création de jardin</option><option>Aménagement (terrasse, clôture, arrosage…)</option><option>Entretien du jardin</option><option>Élagage ou taille d'arbres</option><option>Abattage ou démontage</option><option>Coaching jardin</option><option>Autre demande</option></select><p class="err" id="e-besoin" role="alert"></p></div>
<div class="fld"><label for="f-msg">Message <span class="opt">(facultatif)</span></label><textarea id="f-msg" name="message"></textarea></div>
<button class="btn btn-d" type="submit">Préparer ma demande</button>
</form>
<div class="recap" id="recap" aria-live="polite"><p class="ok">{ic("check")} Votre demande est prête</p><h2>Choisissez comment nous l’envoyer</h2><p style="color:var(--ink2)">Rien n’est envoyé automatiquement : utilisez l’un des boutons ci-dessous.</p><pre id="recap-text"></pre>
<div class="acts"><a class="btn btn-d" id="b-sms" href="sms:+33621381189">Envoyer par SMS</a><button class="btn btn-l" type="button" id="b-copy">Copier</button><a class="btn btn-l" href="tel:+33621381189">Appeler</a><a class="btn btn-l" id="b-mail" href="mailto:arborescience@free.fr">Envoyer par e-mail</a></div>
<p style="margin:18px 0 0"><button class="btn btn-l" type="button" id="b-edit" style="min-height:48px;width:auto">Modifier ma demande</button></p></div>
</div>
<div class="info">
<div class="k">{ic("pin","ic")}<div><h3>Adresse</h3><p>19 rue des Cottages<br>78630 Orgeval</p></div></div>
<div class="k"><div><h3>Horaires</h3><dl class="hours" style="margin:0"><dt>Lundi au vendredi</dt><dd>8h00 – 19h00</dd><dt>Samedi</dt><dd>8h00 – 17h00</dd></dl></div></div>
<div class="k"><div><h3>Où intervenons-nous ?</h3><p>Principalement dans l’ouest de l’Île-de-France : Poissy, Chambourcy, Villennes-sur-Seine, Saint-Germain-en-Laye, Versailles, Maisons-Laffitte et alentours.</p></div></div>
</div></div></section>''','\n<script src="js/contact.js" defer></script>')

# ---------- MENTIONS ----------
page('mentions-legales.html',"Mentions légales – ARBOR'ESCIENCE à Orgeval","Mentions légales du site de démonstration d'ARBOR'ESCIENCE, Orgeval (78).",'',f'''
<section class="ph ph-s"><div class="wrap" style="max-width:820px"><span class="kick">Informations légales</span><h1>Mentions légales</h1></div></section>
<section class="sheet legal"><div class="wrap">
<h2>Éditeur</h2>
<dl><dt>Entreprise</dt><dd>ARBOR'ESCIENCE</dd><dt>SIREN</dt><dd>827 788 217</dd><dt>Dirigeant</dt><dd>Emmanuel Gorguet</dd><dt>Adresse</dt><dd>19 rue des Cottages, 78630 Orgeval</dd><dt>Téléphone</dt><dd><a href="tel:+33621381189">06 21 38 11 89</a></dd><dt>E-mail</dt><dd><a href="mailto:arborescience@free.fr">arborescience@free.fr</a></dd></dl>
<h2>Maquette</h2><p>Cette page fait partie d’une maquette de démonstration, présentée à l’entreprise à titre de proposition. Elle n’est pas référencée par les moteurs de recherche.</p>
<h2>Données personnelles</h2><p>Le formulaire de contact ne transmet aucune donnée : il prépare un message que le visiteur envoie lui-même par SMS, par e-mail ou par téléphone.</p>
</div></section>''')
print('pages ok')
