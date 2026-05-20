#!/usr/bin/env python3
"""
Generiert die Team-Detail-Seiten und die autarken Blog-Artikel-Seiten
für den REHAB FIVE Praxis-Prototyp.
"""
from pathlib import Path
import re

BASE = Path(__file__).parent
TEAM_DIR = BASE / "team"
BLOG_DIR = BASE / "blog"
TEAM_DIR.mkdir(exist_ok=True)
BLOG_DIR.mkdir(exist_ok=True)

# ============================================================
# Gemeinsamer Header (für team/* und blog/* — Pfade ../img relativ)
# ============================================================

HEAD_TPL = """<!doctype html>
<html lang="de">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title}</title>
<meta name="description" content="{description}"/>
<meta name="theme-color" content="#1F342D"/>
<meta name="robots" content="index, follow, max-image-preview:large"/>
<link rel="canonical" href="{canonical}"/>
<meta property="og:type" content="{og_type}"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{description}"/>
<meta property="og:image" content="../og.jpg"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<script src="https://cdn.tailwindcss.com"></script>
<script>
  tailwind.config = {{ theme: {{ extend: {{
    colors: {{
      ink:    {{ 50:'#FAFAFA', 100:'#F5F5F5', 200:'#C9C9C9', 700:'#4A4A4A', 900:'#1A1A1A' }},
      forest: {{ 700:'#1F342D' }},
      brand:  {{ 100:'#FBF1E0', 500:'#D99129', 600:'#C57F1F' }}
    }},
    fontFamily: {{ sans: ['Barlow','system-ui','sans-serif'] }}
  }}}}}}
</script>
<script async src="https://cdn.docmedico-rezeption.de/j9u4c9m7a/reception_embed.js"></script>
{schema}
<style>
  html {{ scroll-behavior: smooth; }}
  body {{ font-family: 'Barlow', system-ui, sans-serif; background: #1F342D; color:#FBF1E0; font-size:18px; line-height:1.6; -webkit-font-smoothing: antialiased; }}
  .display    {{ font-weight: 800; letter-spacing: -0.01em; line-height: 0.95; text-transform: uppercase; }}
  .display-up {{ font-weight: 800; letter-spacing: 0.005em; text-transform: uppercase; }}
  .micro      {{ font-size: 13px; font-weight: 700; letter-spacing: 0.22em; text-transform: uppercase; }}
  h1, h2, h3 {{ font-family: 'Barlow', sans-serif; font-weight: 800; text-transform: uppercase; letter-spacing: -0.01em; }}
  .card-glass {{ background: rgba(251,241,224,0.04); border:1px solid rgba(251,241,224,0.12); }}
  a.btn-primary {{ background:#D99129; color:#1F342D; padding:14px 24px; border-radius:9999px; font-weight:700; display:inline-flex; gap:8px; align-items:center; transition: background 0.2s; }}
  a.btn-primary:hover {{ background:#C57F1F; }}
  a.btn-outline {{ border:1px solid rgba(251,241,224,0.3); color:#FBF1E0; padding:14px 24px; border-radius:9999px; font-weight:600; display:inline-flex; gap:8px; align-items:center; transition: background 0.2s; }}
  a.btn-outline:hover {{ background: rgba(251,241,224,0.1); }}
  .ulink {{ position: relative; padding-bottom: 4px; }}
  .ulink::after {{ content:""; position: absolute; left:0; bottom:0; width:100%; height:1px; background: currentColor; transform: scaleX(.35); transform-origin: left; transition: transform .35s; }}
  .ulink:hover::after {{ transform: scaleX(1); }}
  .num {{ color:#D99129; font-weight:900; line-height:0.85; letter-spacing:-0.04em; }}
  a:focus-visible, button:focus-visible {{ outline:2px solid #D99129; outline-offset:3px; }}
</style>
</head>
<body class="bg-forest-700 text-white">

<!-- HEADER -->
<header class="sticky top-0 z-50 bg-[#1F342D]/85 backdrop-blur border-b border-[#FBF1E0]/10">
  <div class="max-w-[1280px] mx-auto px-6 lg:px-10 h-[68px] flex items-center justify-between">
    <a href="../index.html" class="flex items-center gap-4">
      <img src="../img/logo-white.png" alt="REHAB FIVE" class="h-7 w-auto"/>
      <span class="hidden md:inline micro text-[#FBF1E0]/55 border-l border-[#FBF1E0]/20 pl-4">Physiotherapie · Münster</span>
    </a>
    <div class="flex items-center gap-3">
      <a href="tel:+4925174788200" class="hidden sm:inline-flex items-center gap-2 border border-[#FBF1E0]/30 hover:bg-[#FBF1E0]/10 transition px-5 py-2.5 rounded-full text-[#FBF1E0] text-sm font-semibold">
        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.37 1.9.72 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.35 1.85.59 2.81.72A2 2 0 0 1 22 16.92z"/></svg>
        Anruf
      </a>
      <a href="https://termin.docmedico-rezeption.de/j9u4c9m7a" target="_blank" rel="noopener" class="inline-flex items-center gap-2 bg-[#D99129] hover:bg-[#C57F1F] text-[#1F342D] font-bold text-sm px-5 py-2.5 rounded-full">
        Online-Rezeption
      </a>
    </div>
  </div>
</header>

<main class="max-w-[1280px] mx-auto px-6 lg:px-10 py-[clamp(48px,8vw,120px)]">
{content}
</main>

<!-- FOOTER -->
<footer class="bg-black border-t border-[#FBF1E0]/10 py-12 mt-16">
  <div class="max-w-[1280px] mx-auto px-6 lg:px-10 flex flex-wrap items-center justify-between gap-6">
    <a href="../index.html" class="flex items-center gap-4">
      <img src="../img/logo-white.png" alt="REHAB FIVE" class="h-6 w-auto"/>
      <span class="micro text-[#FBF1E0]/45 border-l border-[#FBF1E0]/20 pl-4">Physiotherapie · Münster</span>
    </a>
    <p class="text-[#D99129] text-base">Therapie ist nur eine von fünf Säulen.</p>
    <p class="text-[#FBF1E0]/40 text-sm">© 2026 REHAB FIVE Gruppe</p>
  </div>
</footer>

</body>
</html>
"""


# ============================================================
# TEAM
# ============================================================

TEAM = [
    {
        "slug": "aric-bramswig",
        "name": "Aric Brämswig",
        "role": "Gründer & CEO",
        "subtitle": "Manuelle Therapie · Athletik",
        "photo": "aric-bramswig.jpg",
        "bio": [
            "Aric ist Gründer der REHAB FIVE Gruppe. Vor 2018 war er Therapeut in einer klassischen Praxis und hat dort gesehen, was bei Patient*innen nach sechs Rezept-Sitzungen passiert: meistens nichts.",
            "Das war der Auslöser, REHAB FIVE zu bauen — eine Praxis, die nicht entlässt, sondern begleitet. Mit dem 5-Säulen-Modell, das Therapie, Training, Athletik, Prävention und Diagnostik unter einem Dach verbindet.",
            "Heute leitet er die strategische Entwicklung der gesamten Gruppe (Praxis, Health Club, Nutrition, Business). Behandelt parallel weiterhin Patient*innen mit Schwerpunkt Manuelle Therapie und Athletik-Aufbau nach OP."
        ],
        "schwerpunkte": ["Manuelle Therapie", "Athletik nach Reha", "Komplexe Schmerzbilder", "Strategie & Konzept"],
        "weiterbildung": ["Manuelle Therapie (Cyriax / Kaltenborn)", "Athletik-Coach", "Sportwissenschaftliche Grundlagen"],
        "location": "Beide Standorte"
    },
    {
        "slug": "hagen-heidinger",
        "name": "Hagen Heidinger",
        "role": "COO",
        "subtitle": "Operations · Webflow · Digitales",
        "photo": "hagen-heidinger.jpg",
        "bio": [
            "Hagen ist seit 2020 COO der REHAB FIVE Gruppe und verantwortet alles Operative — von Personalplanung über IT bis zur Website-Strategie.",
            "Sein Job: dafür sorgen, dass die Praxis-Realität so reibungslos läuft, dass das Team Zeit für das hat, was zählt — die Patient*innen.",
            "Wenn du operative Fragen hast (Abrechnung, Onboarding, Kooperationen), bist du bei ihm richtig."
        ],
        "schwerpunkte": ["Operations Management", "Personal & Prozesse", "Digitales & Webflow", "Kooperations-Partnerschaften"],
        "weiterbildung": ["Webflow", "Business Operations", "Healthcare Management"],
        "location": "Beide Standorte"
    },
    {
        "slug": "christian-schlueter",
        "name": "Christian Schlüter",
        "role": "HR · BGM & BGF",
        "subtitle": "B2B-Lead · Firmen- &amp; Vereinsbetreuung",
        "photo": "christian-schlueter.jpg",
        "bio": [
            "Christian leitet den B2B-Bereich von REHAB FIVE BUSINESS. Er bringt Unternehmen und Sportvereine mit unserer Praxis-Kompetenz zusammen — vom BGM-Konzept über Workshops bis zur Mannschaftstherapie.",
            "Vor REHAB FIVE war er in Personal- und Gesundheitsentwicklung mehrerer Mittelständler tätig. Er weiß, wie HR-Manager*innen ticken — und worauf es ankommt, damit BGM-Maßnahmen tatsächlich wirken.",
            "Erstgespräche für Firmen und Vereine laufen direkt über ihn."
        ],
        "schwerpunkte": ["BGM / BGF-Konzepte", "Workshops & Gesundheitstage", "Vereins-Athletik", "Verhandlungen & Vertrags-Setup"],
        "weiterbildung": ["BGM-Berater (zertifiziert §20b SGB V)", "Personalentwicklung", "Verhandlungspsychologie"],
        "location": "Beide Standorte · Termine nach Vereinbarung"
    },
    {
        "slug": "constantin-lingenfelser",
        "name": "Constantin Lingenfelser",
        "role": "Head of Physiotherapie",
        "subtitle": "Standort Friedrich-Ebert-Straße",
        "photo": "constantin-lingenfelser.jpg",
        "bio": [
            "Constantin leitet die Physiotherapie am Standort Friedrich-Ebert-Straße. Er ist verantwortlich für die fachliche Qualität, die Therapiepläne und das Team vor Ort.",
            "Sein Schwerpunkt liegt auf Manueller Therapie und Sport-Reha — er begleitet Patient*innen durch alle fünf Säulen, von der Akutbehandlung bis zum Comeback im Sport oder Alltag.",
            "Wenn du komplexere Befunde hast, übernimmt er auch persönlich Erstgespräche."
        ],
        "schwerpunkte": ["Manuelle Therapie", "Sport-Reha", "Wirbelsäule", "Sehnen & Bänder"],
        "weiterbildung": ["Manuelle Therapie", "Sportphysiotherapie (DVGS)", "Komplexe Bewegungsanalyse"],
        "location": "Friedrich-Ebert-Straße 122"
    },
    {
        "slug": "stephan-otte",
        "name": "Stephan Otte",
        "role": "2nd Head of Physiotherapie",
        "subtitle": "Standort Scharnhorststraße",
        "photo": "stephan-otte.jpg",
        "bio": [
            "Stephan ist zweiter Leitender am Standort Scharnhorststraße. Sein Schwerpunkt: Knie, Hüfte und Reha nach OP — er bringt jahrelange Erfahrung in Sport-Reha mit.",
            "Patient*innen schätzen seine ruhige, methodische Art und seine Fähigkeit, schwierige Fälle durch klare Therapiepläne zu strukturieren.",
            "Er ist auch zuständig für die Übergabe zwischen Therapie und Training — also dem Übergang von Säule 01 zu 02."
        ],
        "schwerpunkte": ["Knie & Hüfte", "Reha nach OP", "Übergabe Therapie ↔ Training", "Manuelle Therapie"],
        "weiterbildung": ["Manuelle Therapie", "Sport-Reha", "Nachsorge nach OP"],
        "location": "Scharnhorststraße"
    },
    {
        "slug": "fiete-tewinkel",
        "name": "Fiete Tewinkel",
        "role": "2nd Head of Physiotherapie",
        "subtitle": "Standort Friedrich-Ebert-Straße",
        "photo": "fiete-tewinkel.jpg",
        "bio": [
            "Fiete unterstützt Constantin am Standort Friedrich-Ebert und ist Ansprechpartner für komplexe Schulter- und Nackenbeschwerden.",
            "Sein Ansatz: hartnäckig nach der echten Ursache suchen, statt Symptome zu behandeln. Patient*innen mit langer Vorgeschichte landen häufig bei ihm.",
            "Spezialisierungen: Frozen Shoulder, Rotatorenmanschetten-Verletzungen, chronischer Nacken."
        ],
        "schwerpunkte": ["Schulter & Nacken", "Frozen Shoulder", "Manuelle Therapie", "Chronische Schmerzbilder"],
        "weiterbildung": ["Manuelle Therapie", "Schulter-Spezialisierung", "Schmerz-Neurowissenschaft"],
        "location": "Friedrich-Ebert-Straße 122"
    },
    {
        "slug": "simon-brueggemann",
        "name": "Simon Brüggemann",
        "role": "Physiotherapeut · B.A. Sportwiss.",
        "subtitle": "Diagnostik · Athletik",
        "photo": "simon-brueggemann.jpg",
        "bio": [
            "Simon kombiniert Physiotherapie mit sportwissenschaftlichem Hintergrund (B.A. Sportwissenschaften). Er ist unser Spezialist für die Bewegungsdiagnostik (Säule 05) und für die Übergabe zum Athletik-Training.",
            "Wenn du eine 149-€-Diagnostik buchst, bist du häufig bei ihm. Wenn du danach in das Athletik-Programm willst, ebenfalls.",
            "Er erklärt komplexe Bewegungsanalysen so, dass du sie verstehst — und einen Plan in der Hand hast, der wirklich funktioniert."
        ],
        "schwerpunkte": ["Bewegungsdiagnostik", "Athletik-Programme", "Return-to-Sport", "Daten-basierte Therapieplanung"],
        "weiterbildung": ["B.A. Sportwissenschaften", "Bewegungs- und Belastungsdiagnostik", "Athletik-Coach"],
        "location": "Beide Standorte"
    },
]


def render_team_page(person):
    schema = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Person","name":"{person['name']}","jobTitle":"{person['role']}","worksFor":{{"@type":"Organization","name":"REHAB FIVE","url":"https://rehab-five.com/"}},"image":"https://rehab-five.com/team/{person['slug']}.jpg"}}
</script>"""

    bio_html = "\n".join(f"          <p class=\"mt-5 text-[#FBF1E0]/80 text-lg leading-[1.65]\">{p}</p>" for p in person["bio"])
    schwerpunkte_html = "\n".join(
        f"            <li class=\"flex items-start gap-3 py-3 border-b border-[#FBF1E0]/10\"><span class=\"text-[#D99129]\">·</span> {s}</li>"
        for s in person["schwerpunkte"]
    )
    weiterbildung_html = "\n".join(
        f"            <li class=\"flex items-start gap-3 py-3 border-b border-[#FBF1E0]/10\"><span class=\"text-[#D99129]\">·</span> {w}</li>"
        for w in person["weiterbildung"]
    )

    content = f"""
  <a href="../index.html#team" class="ulink inline-flex items-center gap-2 text-[#FBF1E0]/70 text-sm mb-12">
    <span class="text-[#D99129]">←</span> Zurück zum Team
  </a>

  <div class="grid lg:grid-cols-12 gap-10 lg:gap-16 items-start">
    <!-- Foto -->
    <div class="lg:col-span-5">
      <div class="relative">
        <div class="absolute -top-3 -left-3 right-12 h-[2px] bg-[#D99129]"></div>
        <div class="absolute -top-3 -left-3 w-[2px] h-32 bg-[#D99129]"></div>
        <div class="aspect-[3/4] rounded-sm overflow-hidden bg-[#FBF1E0]/5 border border-[#FBF1E0]/10">
          <img src="../img/team/{person['photo']}" alt="{person['name']}" class="w-full h-full object-cover"/>
        </div>
      </div>
    </div>

    <!-- Info -->
    <div class="lg:col-span-7">
      <div class="micro text-[#D99129]">{person['role']}</div>
      <h1 class="display text-[clamp(40px,6vw,84px)] text-[#FBF1E0] mt-4 leading-[0.95]">{person['name']}</h1>
      <p class="mt-3 text-xl text-[#FBF1E0]/65">{person['subtitle']}</p>

      <div class="mt-10 max-w-2xl">
{bio_html}
      </div>

      <!-- Schwerpunkte + Weiterbildung -->
      <div class="mt-12 grid sm:grid-cols-2 gap-10">
        <div>
          <div class="micro text-[#D99129] mb-3">Schwerpunkte</div>
          <ul class="text-[#FBF1E0]/85">
{schwerpunkte_html}
          </ul>
        </div>
        <div>
          <div class="micro text-[#D99129] mb-3">Weiterbildung</div>
          <ul class="text-[#FBF1E0]/85">
{weiterbildung_html}
          </ul>
        </div>
      </div>

      <!-- Location + CTAs -->
      <div class="mt-12 pt-8 border-t border-[#FBF1E0]/15">
        <div class="micro text-[#D99129]">Termine</div>
        <p class="mt-2 text-lg text-[#FBF1E0]">{person['location']}</p>

        <div class="mt-8 flex flex-wrap gap-3">
          <a href="https://termin.docmedico-rezeption.de/j9u4c9m7a" target="_blank" rel="noopener" class="btn-primary">
            Termin buchen
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </a>
          <a href="tel:+4925174788200" class="btn-outline">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.37 1.9.72 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.35 1.85.59 2.81.72A2 2 0 0 1 22 16.92z"/></svg>
            Anruf
          </a>
        </div>
      </div>
    </div>
  </div>
"""

    return HEAD_TPL.format(
        title=f"{person['name']} · {person['role']} · REHAB FIVE",
        description=f"{person['name']} — {person['role']} bei REHAB FIVE Physiotherapie Münster. {person['subtitle']}.",
        canonical=f"https://rehab-five.com/team/{person['slug']}",
        og_type="profile",
        schema=schema,
        content=content
    )


# ============================================================
# BLOG
# ============================================================

BLOG_ARTICLES = [
    {
        "slug": "schmerzen-verstehen",
        "title": "Schmerzen verstehen — Physiotherapie und moderne Schmerzforschung",
        "category": "Schmerzforschung",
        "lead": "Warum dein Schmerz nicht immer das Problem ist und was die Neurowissenschaft heute weiß.",
        "intro": "„Mein MRT sagt, da ist nichts. Aber ich habe trotzdem Schmerzen.“ — diesen Satz hören wir mehrmals pro Woche. Die moderne Schmerzforschung erklärt, warum das kein Widerspruch ist.",
        "body_md": [
            ("Schmerz ist ein Signal, kein Befund", "Wir behandeln Schmerz lange Zeit so, als wäre er ein direktes Abbild von Gewebeschaden. Heute wissen wir: Das Gehirn entscheidet, ob etwas weh tut — basierend auf Daten aus dem Körper, aber auch aus dem Kontext, der Erfahrung und dem aktuellen Stresslevel."),
            ("Warum MRT-Bilder oft nicht weiterhelfen", "Studien zeigen: 30–50 % aller schmerzfreien Erwachsenen über 40 haben Bandscheibenvorwölbungen im MRT. Andersrum gibt es Menschen mit massivem MRT-Befund, die völlig schmerzfrei sind. Das MRT zeigt Struktur. Schmerz ist eine Funktion."),
            ("Was wir bei REHAB FIVE anders machen", "Wir arbeiten mit Bewegungsdiagnostik (Säule 05), die zeigt, wie dein Körper sich tatsächlich bewegt, wo Belastungen verteilt werden, welche Muster sich eingeschlichen haben. Das ist die Datenbasis, auf der wir den Therapieplan bauen — nicht das MRT allein."),
            ("Was du selbst tun kannst", "Bewegung ist meistens die bessere Antwort als Ruhe. Schlaf, Stress und mentale Verfassung beeinflussen Schmerzempfindung massiv. Verstehen, dass Schmerz nicht automatisch Schaden bedeutet, reduziert die Schmerzintensität nachweisbar."),
        ],
        "faq": [
            ("Heißt das, mein Schmerz ist 'nur im Kopf'?", "Nein — er ist real und du fühlst ihn. Aber Schmerz wird nicht 1:1 vom Gewebe an das Gehirn weitergegeben. Das Gehirn interpretiert die Signale und entscheidet, wie stark der Schmerz wird. Diese Interpretation kann man durch Therapie und Verstehen positiv beeinflussen."),
            ("Wie lange dauert es, bis chronischer Schmerz besser wird?", "Sehr unterschiedlich. Aktive Therapie + Verstehen + Bewegung sind die drei wichtigsten Faktoren. Manche Patient*innen erleben innerhalb von Wochen Verbesserungen, andere brauchen Monate. Wichtig: nicht in passiver Therapie verharren."),
        ],
        "related": ["achillessehnenruptur", "rotatorenmanschettenruptur"]
    },
    {
        "slug": "achilles-tendinopathie",
        "title": "Achilles-Tendinopathie — Effektive Hilfe bei Achillessehnenschmerzen",
        "category": "Achillessehne",
        "lead": "Eccentric Training, Belastungssteuerung und warum Ruhe meistens die falsche Antwort ist.",
        "intro": "Achillessehnen-Beschwerden gehören zu den häufigsten Verletzungen bei Hobby-Läufer*innen ab 35. Die typische Reaktion ist Ruhe — und die ist meistens kontraproduktiv.",
        "body_md": [
            ("Was passiert in der Sehne?", "Tendinopathie ist keine reine Entzündung — sie ist eine Belastungs-Anpassungs-Störung. Die Sehnenstruktur verändert sich, weil sie über lange Zeit fehlbelastet wurde. Ruhe verringert die Belastbarkeit weiter, statt sie zu erhöhen."),
            ("Eccentric Training — was Studien zeigen", "Heavy slow resistance Training (langsame, exzentrische Belastung) ist die best-untersuchte Intervention bei Achilles-Tendinopathie. Studien zeigen 60–80 % Verbesserung über 12 Wochen — deutlich besser als passive Maßnahmen."),
            ("Belastungssteuerung statt Pause", "Wir arbeiten mit Belastungs-Monitoring. Zu wenig: die Sehne bleibt schwach. Zu viel: Reizung. Der Sweet Spot ist ein Bereich, der nach 24 Stunden nicht stärker schmerzt als vor der Belastung — und der über Wochen langsam gesteigert wird."),
            ("Wann zum Arzt?", "Bei akutem Knall + Funktionsverlust (Verdacht auf Ruptur), sehr starken Nachtschmerzen oder Schwellung im Knochen-Bereich. Sonst: zu uns."),
        ],
        "faq": [
            ("Wie lange dauert die Therapie?", "Typisch 8–16 Wochen für signifikante Verbesserung. Vollständige Belastbarkeit (z.B. Marathon) oft 4–6 Monate."),
            ("Darf ich weiter laufen?", "Meistens ja — aber angepasst. Wir bauen ein Lauf-Plan, der die Sehne stimuliert, aber nicht überlastet."),
        ],
        "related": ["achillessehnenruptur", "schmerzen-verstehen"]
    },
    {
        "slug": "rotatorenmanschettenruptur",
        "title": "Rotatorenmanschettenruptur — Hilfe bei Sehnenriss & Schulterschmerz",
        "category": "Schulter",
        "lead": "Wann konservativ, wann OP — und was nach der ersten Diagnose wirklich passiert.",
        "intro": "Eine Rotatorenmanschettenruptur ist nicht immer eine OP-Indikation. Studien zeigen: bei vielen Patient*innen ist konservative Therapie gleichwertig oder besser.",
        "body_md": [
            ("Akut vs. degenerativ", "Junge Patient*innen mit klarer Trauma-Geschichte profitieren oft von OP. Bei älteren Patient*innen mit degenerativen Rissen (häufig auch bei beschwerdefreien Personen sichtbar im MRT) ist konservative Therapie häufig erste Wahl."),
            ("Was konservative Therapie heißt", "Strukturiertes Aufbau-Training der noch funktionsfähigen Anteile, gezieltes Mobilitätstraining, Belastungssteuerung. Über 12–16 Wochen mit kontinuierlicher Anpassung."),
            ("Wenn OP, dann was?", "Die Reha-Phase nach OP ist genauso wichtig wie die OP selbst. Wir nehmen Patient*innen nach OP in unsere Säulen-Struktur auf: Therapie → Training → Athletik. Über 6–9 Monate."),
            ("Was Studien sagen", "Mehrere RCTs (z.B. Boorman et al., Kukkonen et al.) zeigen vergleichbare 1-Jahres-Outcomes zwischen konservativer Therapie und OP bei degenerativen Rissen. OP ist nicht automatisch die bessere Option."),
        ],
        "faq": [
            ("Wie weiß ich, ob ich OP brauche?", "Das entscheidet kein einzelner Test. Wir empfehlen: Diagnostik bei uns + Zweitmeinung Sportorthopäde + Risiko-Abwägung. Niemals nur auf Basis eines MRT entscheiden."),
            ("Wie lange Reha nach OP?", "6–9 Monate strukturierte Reha ist Standard. Volle Belastbarkeit (Sport) oft 9–12 Monate."),
        ],
        "related": ["schmerzen-verstehen"]
    },
    {
        "slug": "morbus-bechterew",
        "title": "Morbus Bechterew — Physiotherapie bei Wirbelsäulenrheuma",
        "category": "Wirbelsäule",
        "lead": "Wie aktive Therapie und gezieltes Training die Beweglichkeit erhalten.",
        "intro": "Morbus Bechterew (axiale Spondyloarthritis) ist eine chronisch-entzündliche Erkrankung der Wirbelsäule. Aktive Physiotherapie ist eine der wichtigsten Säulen der Behandlung.",
        "body_md": [
            ("Was passiert bei Bechterew?", "Entzündliche Prozesse im Bereich der Wirbelsäulen-Gelenke führen über Zeit zu Versteifung. Ohne Bewegung beschleunigt sich das."),
            ("Warum Bewegung der Schlüssel ist", "Studien zeigen: konsequente Bewegungstherapie verlangsamt die Versteifung und erhält Lebensqualität deutlich besser als reine medikamentöse Behandlung. Schwimmen, gezieltes Krafttraining, Mobilität — kombiniert mit Atemtraining."),
            ("Was wir bei REHAB FIVE machen", "Wir bauen einen individuellen Trainingsplan, der auf den aktuellen Befund und das Krankheits-Stadium angepasst ist. Mit dem Ziel, dass du langfristig selbstständig trainierst — nicht abhängig von Therapie-Terminen."),
            ("Zusammenarbeit mit deinem Rheumatologen", "Wir koordinieren mit deiner medikamentösen Therapie. Bewegungstherapie ersetzt keine Medikamente — aber sie macht den entscheidenden Unterschied bei Lebensqualität."),
        ],
        "faq": [
            ("Wie oft sollte ich trainieren?", "Mindestens 3-4 Mal pro Woche, davon mindestens 1 strukturierte Einheit. Klein dosieren, langfristig konsequent."),
            ("Was, wenn ich an einem Tag mehr Beschwerden habe?", "Trotzdem bewegen — angepasst. Pause macht es langfristig schlimmer, nicht besser. Wir helfen dir, den Sweet Spot zu finden."),
        ],
        "related": ["schmerzen-verstehen"]
    },
    {
        "slug": "achillessehnenruptur",
        "title": "Achillessehnenruptur — Reha nach Sehnenriss",
        "category": "Achillessehne · Reha",
        "lead": "Der Weg über alle fünf Säulen: Therapie → Training → Athletik → Comeback.",
        "intro": "Eine Achillessehnenruptur ist ein schwerer Eingriff in den Alltag — aber mit strukturierter Reha kommen die meisten Patient*innen vollständig zurück. Manchmal sogar mit besserer Performance als vorher.",
        "body_md": [
            ("Akute Phase (Wochen 0–6)", "Nach OP oder konservativer Versorgung: Schwellungsreduktion, vorsichtige Mobilisation, Erhalt der nicht-betroffenen Strukturen. Lymphdrainage spielt hier eine wichtige Rolle."),
            ("Re-Mobilisation (Wochen 6–14)", "Wir bringen die Beweglichkeit zurück. Kraft-Aufbau startet vorsichtig — viele Patient*innen sind hier zu hektisch und reißen die Sehne sekundär."),
            ("Aufbau-Phase (Monat 4–9)", "Hier übergibt Therapie an Training (Säule 02). Eccentric Training, schwere Belastung, Plyometrie — alles dosiert und progressiv."),
            ("Return-to-Sport (ab Monat 9)", "Sport-spezifisches Athletik-Training (Säule 03). Mit Diagnostik-Checks (Säule 05) prüfen wir, ob die Sehne bereit ist. Comeback Card wird ausgehändigt, wenn das Return-to-X-Ziel erreicht ist."),
        ],
        "faq": [
            ("Wie lange bis ich wieder normal laufen kann?", "Normales Gehen meist nach 12 Wochen. Joggen ab Monat 6, Wettkampf-Lauf ab Monat 9–12."),
            ("Brauche ich nach OP zwingend Physiotherapie?", "Ja — ohne strukturierte Reha ist das Risiko einer schlechten Ausheilung deutlich erhöht. Die OP allein ist nur der erste Schritt."),
        ],
        "related": ["achilles-tendinopathie", "schmerzen-verstehen"]
    },
]


def render_blog_index():
    cards = []
    for a in BLOG_ARTICLES:
        cards.append(f"""
      <a href="{a['slug']}.html" class="card-glass rounded-sm p-7 flex flex-col hover:border-[#D99129] transition group">
        <div class="micro text-[#D99129]">{a['category']}</div>
        <h2 class="display text-2xl text-[#FBF1E0] mt-4 leading-snug flex-1">{a['title']}</h2>
        <p class="mt-3 text-[#FBF1E0]/65 text-base leading-[1.55]">{a['lead']}</p>
        <span class="ulink mt-5 inline-flex text-sm font-bold text-[#D99129]">Artikel lesen →</span>
      </a>
""")

    content = f"""
  <a href="../index.html#wissen" class="ulink inline-flex items-center gap-2 text-[#FBF1E0]/70 text-sm mb-12">
    <span class="text-[#D99129]">←</span> Zurück zur Startseite
  </a>

  <div class="max-w-3xl mb-16">
    <div class="micro text-[#D99129]">Wissen · Blog</div>
    <h1 class="display text-[clamp(48px,8vw,120px)] text-[#FBF1E0] mt-4 leading-[0.95]">
      Lies dich <span class="text-[#D99129]">tiefer ein.</span>
    </h1>
    <p class="mt-8 text-xl text-[#FBF1E0]/70 leading-[1.55]">
      Fundierte Artikel aus der Praxis — über Schmerzforschung, häufige Diagnosen und was die aktuelle Sportwissenschaft für deine Therapie bedeutet. Geschrieben von Therapeut*innen, nicht von SEO-Agenturen.
    </p>
  </div>

  <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-3">
{''.join(cards)}
  </div>
"""

    return HEAD_TPL.format(
        title="Wissen · Blog · REHAB FIVE Physiotherapie Münster",
        description="Fundierte Artikel aus der Praxis: Schmerzforschung, Achilles-Tendinopathie, Rotatorenmanschette, Morbus Bechterew, Achillessehnenruptur.",
        canonical="https://rehab-five.com/blog/",
        og_type="website",
        schema="",
        content=content
    )


def render_blog_article(a):
    faq_schema_items = ",".join(
        f'{{"@type":"Question","name":{q!r},"acceptedAnswer":{{"@type":"Answer","text":{ans!r}}}}}'
        for q, ans in a["faq"]
    )
    article_schema = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":{a['title']!r},"description":{a['lead']!r},"author":{{"@type":"Organization","name":"REHAB FIVE"}},"publisher":{{"@type":"Organization","name":"REHAB FIVE","logo":{{"@type":"ImageObject","url":"https://rehab-five.com/img/logo-white.png"}}}},"datePublished":"2026-05-20","image":"https://rehab-five.com/og.jpg"}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_schema_items}]}}
</script>"""

    body_html = "\n".join(
        f"""
      <section class="mt-12">
        <h2 class="text-2xl md:text-3xl font-bold text-[#FBF1E0]">{h}</h2>
        <p class="mt-4 text-[#FBF1E0]/80 text-lg leading-[1.65]">{txt}</p>
      </section>
"""
        for h, txt in a["body_md"]
    )

    faq_html = "\n".join(
        f"""
        <details class="card-glass rounded-sm p-6 mb-3" {('open' if i == 0 else '')}>
          <summary class="cursor-pointer flex justify-between items-center font-bold text-lg text-[#FBF1E0] list-none">
            {q}
            <span class="text-[#D99129] text-2xl">+</span>
          </summary>
          <p class="mt-4 text-[#FBF1E0]/70 text-base leading-[1.65]">{ans}</p>
        </details>
"""
        for i, (q, ans) in enumerate(a["faq"])
    )

    related_html = ""
    if a.get("related"):
        related_cards = []
        for slug in a["related"]:
            rel = next((b for b in BLOG_ARTICLES if b["slug"] == slug), None)
            if rel:
                related_cards.append(f"""
        <a href="{slug}.html" class="card-glass rounded-sm p-6 flex flex-col group hover:border-[#D99129] transition">
          <div class="micro text-[#D99129]">{rel['category']}</div>
          <h3 class="display text-lg text-[#FBF1E0] mt-3 leading-snug flex-1">{rel['title']}</h3>
          <span class="ulink mt-4 inline-flex text-sm font-bold text-[#D99129]">Artikel lesen →</span>
        </a>
""")
        if related_cards:
            related_html = f"""
      <div class="mt-20 pt-10 border-t border-[#FBF1E0]/15">
        <div class="micro text-[#D99129] mb-6">Weiterlesen</div>
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-3">{''.join(related_cards)}</div>
      </div>
"""

    content = f"""
  <a href="index.html" class="ulink inline-flex items-center gap-2 text-[#FBF1E0]/70 text-sm mb-12">
    <span class="text-[#D99129]">←</span> Alle Artikel
  </a>

  <article class="max-w-3xl">
    <div class="micro text-[#D99129]">{a['category']}</div>
    <h1 class="display text-[clamp(34px,5.5vw,72px)] text-[#FBF1E0] mt-4 leading-[1.0]">{a['title']}</h1>
    <p class="mt-8 text-xl text-[#FBF1E0]/75 leading-[1.6]">{a['lead']}</p>

    <div class="mt-14 pt-8 border-t border-[#FBF1E0]/15">
      <p class="text-[#FBF1E0]/85 text-lg leading-[1.7] italic">{a['intro']}</p>
{body_html}
    </div>

    <!-- FAQ -->
    <section class="mt-20">
      <h2 class="text-2xl md:text-3xl font-bold text-[#FBF1E0]">Häufige Fragen</h2>
      <div class="mt-8">
{faq_html}
      </div>
    </section>

    <!-- CTA -->
    <div class="mt-20 p-10 card-glass rounded-sm border-l-2 border-[#D99129]">
      <div class="micro text-[#D99129]">Therapie starten</div>
      <h2 class="display text-3xl text-[#FBF1E0] mt-4 leading-tight">Hast du Beschwerden, die in diesem Artikel auftauchen?</h2>
      <p class="mt-4 text-[#FBF1E0]/70 leading-[1.6]">Ein Erstgespräch oder eine Diagnostik bei REHAB FIVE ist der einfachste Weg, einen klaren Plan zu bekommen.</p>
      <div class="mt-7 flex flex-wrap gap-3">
        <a href="https://termin.docmedico-rezeption.de/j9u4c9m7a" target="_blank" rel="noopener" class="btn-primary">
          Termin buchen
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
        </a>
        <a href="tel:+4925174788200" class="btn-outline">Anruf</a>
      </div>
    </div>

{related_html}
  </article>
"""

    return HEAD_TPL.format(
        title=f"{a['title']} · REHAB FIVE",
        description=a["lead"],
        canonical=f"https://rehab-five.com/blog/{a['slug']}",
        og_type="article",
        schema=article_schema,
        content=content
    )


# ============================================================
# Ausführen
# ============================================================

if __name__ == "__main__":
    print("=== Team-Seiten ===")
    for p in TEAM:
        path = TEAM_DIR / f"{p['slug']}.html"
        path.write_text(render_team_page(p), encoding="utf-8")
        print(f"  · {path.relative_to(BASE)}")

    print("\n=== Blog-Seiten ===")
    (BLOG_DIR / "index.html").write_text(render_blog_index(), encoding="utf-8")
    print(f"  · blog/index.html")
    for a in BLOG_ARTICLES:
        path = BLOG_DIR / f"{a['slug']}.html"
        path.write_text(render_blog_article(a), encoding="utf-8")
        print(f"  · {path.relative_to(BASE)}")

    print("\nFertig.")
