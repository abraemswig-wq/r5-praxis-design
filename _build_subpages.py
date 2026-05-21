#!/usr/bin/env python3
"""
Generiert Team-Detail-Seiten + Team-Index + autarke Blog-Artikel mit
Original-Inhalten + Studienverweisen für REHAB FIVE Praxis-Prototyp.
"""
from pathlib import Path

BASE = Path(__file__).parent
TEAM_DIR = BASE / "team"
BLOG_DIR = BASE / "blog"
TEAM_DIR.mkdir(exist_ok=True)
BLOG_DIR.mkdir(exist_ok=True)

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
<meta property="og:image" content="{og_image}"/>
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
  .card-glass:hover {{ background: rgba(251,241,224,0.07); border-color: rgba(217,145,41,0.4); }}
  a.btn-primary {{ background:#D99129; color:#1F342D; padding:14px 24px; border-radius:9999px; font-weight:700; display:inline-flex; gap:8px; align-items:center; transition: background 0.2s; }}
  a.btn-primary:hover {{ background:#C57F1F; }}
  a.btn-outline {{ border:1px solid rgba(251,241,224,0.3); color:#FBF1E0; padding:14px 24px; border-radius:9999px; font-weight:600; display:inline-flex; gap:8px; align-items:center; transition: background 0.2s; }}
  a.btn-outline:hover {{ background: rgba(251,241,224,0.1); }}
  .ulink {{ position: relative; padding-bottom: 4px; }}
  .ulink::after {{ content:""; position: absolute; left:0; bottom:0; width:100%; height:1px; background: currentColor; transform: scaleX(.35); transform-origin: left; transition: transform .35s; }}
  .ulink:hover::after {{ transform: scaleX(1); }}
  a:focus-visible, button:focus-visible {{ outline:2px solid #D99129; outline-offset:3px; }}
  .prose-rf p {{ margin-top: 1.25em; color: rgba(251,241,224,0.8); line-height: 1.7; font-size: 18px; }}
  .prose-rf h2 {{ margin-top: 2.5em; font-size: clamp(24px, 3vw, 36px); color: #FBF1E0; }}
  .prose-rf h3 {{ margin-top: 2em; font-size: clamp(20px, 2.5vw, 28px); color: #FBF1E0; }}
  .prose-rf ul {{ margin-top: 1em; padding-left: 1.5em; }}
  .prose-rf ul li {{ margin-top: 0.5em; color: rgba(251,241,224,0.8); list-style: none; position: relative; padding-left: 1.5em; }}
  .prose-rf ul li::before {{ content: "·"; color: #D99129; font-weight: 900; position: absolute; left: 0; font-size: 24px; line-height: 1; }}
  .prose-rf strong {{ color: #FBF1E0; font-weight: 700; }}
  .prose-rf .pull {{ border-left: 3px solid #D99129; padding: 16px 0 16px 24px; margin: 2em 0; font-style: italic; color: #FBF1E0; }}
  .prose-rf .sources {{ margin-top: 3em; padding-top: 2em; border-top: 1px solid rgba(251,241,224,0.15); }}
  .prose-rf .sources li {{ font-size: 15px; color: rgba(251,241,224,0.65); }}

  /* Mobile */
  @media (max-width: 640px) {{
    .site-header span.micro {{ display: none !important; }}
  }}
</style>
</head>
<body class="bg-forest-700 text-white">

<header class="site-header sticky top-0 z-50 bg-[#1F342D]/85 backdrop-blur border-b border-[#FBF1E0]/10">
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
# TEAM — alle Personen aus rehab-five.com/ueber-uns/team
# (korrigiert gegen Live-Seite Mai 2026)
# ============================================================

TEAM = [
    # ── Leitung ────────────────────────────────────────────
    {"slug": "aric-bramswig", "name": "Aric Brämswig", "role": "Gründer & CEO", "subtitle": "Manuelle Therapie · Athletik", "photo": "aric-bramswig.jpg", "location": "Beide Standorte", "category": "Leitung"},
    {"slug": "hagen-heidinger", "name": "Hagen Heidinger", "role": "COO", "subtitle": "Operations · Digitales", "photo": "hagen-heidinger.jpg", "location": "Beide Standorte", "category": "Leitung"},
    {"slug": "christian-schlueter", "name": "Christian Schlüter", "role": "HR · BGM & BGF", "subtitle": "B2B-Lead · Firmen & Vereine", "photo": "christian-schlueter.jpg", "location": "Beide Standorte", "category": "Leitung"},
    {"slug": "rene", "name": "Rene Ruwe", "role": "Head of Physiotherapie", "subtitle": "Standort Scharnhorststraße", "photo": "rene.jpg", "location": "Scharnhorststraße 40", "category": "Leitung"},
    {"slug": "constantin-lingenfelser", "name": "Constantin Lingenfelser", "role": "Head of Physiotherapie", "subtitle": "Standort Friedrich-Ebert-Straße", "photo": "constantin-lingenfelser.jpg", "location": "Friedrich-Ebert-Straße 127", "category": "Leitung"},
    {"slug": "stephan-otte", "name": "Stephan Otte", "role": "2nd Head of Physiotherapie", "subtitle": "Standort Scharnhorststraße", "photo": "stephan-otte.jpg", "location": "Scharnhorststraße 40", "category": "Leitung"},
    {"slug": "fiete-tewinkel", "name": "Fiete Tewinkel", "role": "2nd Head of Physiotherapie", "subtitle": "Standort Friedrich-Ebert-Straße", "photo": "fiete-tewinkel.jpg", "location": "Friedrich-Ebert-Straße 127", "category": "Leitung"},

    # ── Therapie ───────────────────────────────────────────
    {"slug": "simon-brueggemann", "name": "Simon Brüggemann", "role": "Physiotherapeut · B.A. Sportwissenschaften", "subtitle": "Diagnostik · Athletik", "photo": "simon-brueggemann.jpg", "location": "Beide Standorte", "category": "Therapie"},
    {"slug": "alexander-ditz", "name": "Alexander", "role": "Physiotherapeut", "subtitle": "", "photo": "alexander-ditz.jpg", "location": "Friedrich-Ebert-Straße 127", "category": "Therapie"},
    {"slug": "sven-nobis", "name": "Sven Nobis", "role": "Physiotherapeut", "subtitle": "", "photo": "sven-nobis.jpg", "location": "Scharnhorststraße 40", "category": "Therapie"},
    {"slug": "tim-steinhoff", "name": "Tim Steinhoff", "role": "Physiotherapeut", "subtitle": "", "photo": "tim-steinhoff.jpg", "location": "Friedrich-Ebert-Straße 127", "category": "Therapie"},
    {"slug": "tim", "name": "Tim Skambraks", "role": "Physiotherapeut", "subtitle": "", "photo": "tim.jpg", "location": "Beide Standorte", "category": "Therapie"},
    {"slug": "jonas-dobenecker", "name": "Jonas Dobenecker", "role": "Physiotherapeut", "subtitle": "", "photo": "jonas-dobenecker.jpg", "location": "Beide Standorte", "category": "Therapie"},
    {"slug": "jens", "name": "Jens", "role": "Physiotherapeut", "subtitle": "", "photo": "", "location": "Beide Standorte", "category": "Therapie"},
    {"slug": "niklas", "name": "Niklas", "role": "Physiotherapeut", "subtitle": "Präventionskurse", "photo": "", "location": "Beide Standorte", "category": "Therapie"},

    # ── Therapie & Rezeption ──────────────────────────────
    {"slug": "lisa-zimmermann", "name": "Lisa Zimmermann", "role": "Physiotherapeutin", "subtitle": "Rezeption", "photo": "lisa-zimmermann.jpg", "location": "Beide Standorte", "category": "Therapie & Rezeption"},
    {"slug": "freddy", "name": "Freddy", "role": "Physiotherapeutin", "subtitle": "Rezeption", "photo": "", "location": "Beide Standorte", "category": "Therapie & Rezeption"},
    {"slug": "luana", "name": "Luana", "role": "Physiotherapeutin", "subtitle": "Rezeption", "photo": "luana.jpg", "location": "Beide Standorte", "category": "Therapie & Rezeption"},

    # ── Ernährung ─────────────────────────────────────────
    {"slug": "lena", "name": "Lena", "role": "Diätassistentin · Ernährungsberaterin (VDD)", "subtitle": "Ernährung · Rezeption", "photo": "", "location": "Beide Standorte", "category": "Ernährung"},

    # ── Rezeption & Backoffice ────────────────────────────
    {"slug": "maya-pilgram", "name": "Maya Pilgram", "role": "B.Sc. Oecotrophologie · M.Sc. i.A. Sport, Bewegung & Ernährung", "subtitle": "Rezeption · Ernährung", "photo": "maya-pilgram.jpg", "location": "Beide Standorte", "category": "Rezeption & Backoffice"},
    {"slug": "laura-van-oosterwijck", "name": "Laura van Oosterwijck", "role": "Backoffice", "subtitle": "", "photo": "laura-van-oosterwijck.jpg", "location": "Beide Standorte", "category": "Rezeption & Backoffice"},
    {"slug": "josephine-ackermann", "name": "Josephine Ackermann", "role": "Backoffice", "subtitle": "", "photo": "josephine-ackermann.jpg", "location": "Beide Standorte", "category": "Rezeption & Backoffice"},
    {"slug": "jantie", "name": "Jantie", "role": "Backoffice · Rezeption", "subtitle": "", "photo": "", "location": "Beide Standorte", "category": "Rezeption & Backoffice"},
    {"slug": "melissa", "name": "Melissa", "role": "B.A. Sportwiss. · M.A. i.A. Prävention/Reha", "subtitle": "Backoffice", "photo": "melissa.jpg", "location": "Beide Standorte", "category": "Rezeption & Backoffice"},
    {"slug": "rania", "name": "Rania", "role": "B.A. Mediendesign", "subtitle": "Design & Marketing", "photo": "", "location": "Beide Standorte", "category": "Rezeption & Backoffice"},
]


def initials(name):
    parts = [p for p in name.split() if p]
    if not parts:
        return "?"
    if len(parts) == 1:
        return parts[0][:2].upper()
    return (parts[0][0] + parts[-1][0]).upper()


# Voll-Bios für die 7 Hauptpersonen
BIOS = {
    "aric-bramswig": {
        "bio": [
            "Aric ist Gründer und CEO der REHAB FIVE Gruppe. Vor 2018 war er Therapeut in einer klassischen Praxis und hat dort gesehen, was bei Patient*innen nach sechs Rezept-Sitzungen passiert: meistens nichts.",
            "Das war der Auslöser, REHAB FIVE zu bauen — eine Praxis, die nicht entlässt, sondern begleitet. Mit dem 5-Säulen-Modell, das Therapie, Training, Athletik, Prävention und Diagnostik unter einem Dach verbindet.",
            "Heute leitet er die strategische Entwicklung der gesamten Gruppe (Praxis, Health Club, Nutrition, Business). Behandelt parallel weiterhin Patient*innen mit Schwerpunkt Manuelle Therapie und Athletik-Aufbau nach OP."
        ],
        "schwerpunkte": ["Manuelle Therapie", "Athletik nach Reha", "Komplexe Schmerzbilder", "Strategie & Konzept"],
        "weiterbildung": ["B.Sc. Physiotherapie", "Manuelle Therapie (Cyriax / Kaltenborn)", "Athletik-Coach", "Sportwissenschaftliche Grundlagen"]
    },
    "hagen-heidinger": {
        "bio": [
            "Hagen ist COO der REHAB FIVE Gruppe und verantwortet alles Operative — von Personalplanung über IT bis zur Website-Strategie.",
            "Sein Job: dafür sorgen, dass die Praxis-Realität so reibungslos läuft, dass das Team Zeit für das hat, was zählt — die Patient*innen.",
            "Wenn du operative Fragen hast (Abrechnung, Onboarding, Kooperationen), bist du bei ihm richtig."
        ],
        "schwerpunkte": ["Operations Management", "Personal & Prozesse", "Digitales & Webflow", "Kooperations-Partnerschaften"],
        "weiterbildung": ["Webflow", "Business Operations", "Healthcare Management"]
    },
    "christian-schlueter": {
        "bio": [
            "Christian leitet den B2B-Bereich von REHAB FIVE BUSINESS. Er bringt Unternehmen und Sportvereine mit unserer Praxis-Kompetenz zusammen — vom BGM-Konzept über Workshops bis zur Mannschaftstherapie.",
            "Er weiß, wie HR-Manager*innen ticken — und worauf es ankommt, damit BGM-Maßnahmen tatsächlich wirken.",
            "Erstgespräche für Firmen und Vereine laufen direkt über ihn."
        ],
        "schwerpunkte": ["BGM / BGF-Konzepte", "Workshops & Gesundheitstage", "Vereins-Athletik", "Verhandlungen & Vertrags-Setup"],
        "weiterbildung": ["BGM-Berater (zertifiziert §20b SGB V)", "Personalentwicklung", "Verhandlungspsychologie"]
    },
    "constantin-lingenfelser": {
        "bio": [
            "Constantin leitet die Physiotherapie am Standort Friedrich-Ebert-Straße. Er ist verantwortlich für die fachliche Qualität, die Therapiepläne und das Team vor Ort.",
            "Sein Schwerpunkt liegt auf Manueller Therapie und Sport-Reha — er begleitet Patient*innen durch alle fünf Säulen, von der Akutbehandlung bis zum Comeback im Sport oder Alltag.",
            "Wenn du komplexere Befunde hast, übernimmt er auch persönlich Erstgespräche."
        ],
        "schwerpunkte": ["Manuelle Therapie", "Sport-Reha", "Wirbelsäule", "Sehnen & Bänder"],
        "weiterbildung": ["Manuelle Therapie", "Sportphysiotherapie (DVGS)", "Komplexe Bewegungsanalyse"]
    },
    "stephan-otte": {
        "bio": [
            "Stephan ist zweiter Leitender am Standort Scharnhorststraße. Sein Schwerpunkt: Knie, Hüfte und Reha nach OP — er bringt jahrelange Erfahrung in Sport-Reha mit.",
            "Patient*innen schätzen seine ruhige, methodische Art und seine Fähigkeit, schwierige Fälle durch klare Therapiepläne zu strukturieren.",
            "Er ist auch zuständig für die Übergabe zwischen Therapie und Training — also dem Übergang von Säule 01 zu 02."
        ],
        "schwerpunkte": ["Knie & Hüfte", "Reha nach OP", "Übergabe Therapie ↔ Training", "Manuelle Therapie"],
        "weiterbildung": ["Manuelle Therapie", "Sport-Reha", "Nachsorge nach OP"]
    },
    "fiete-tewinkel": {
        "bio": [
            "Fiete unterstützt Constantin am Standort Friedrich-Ebert und ist Ansprechpartner für komplexe Schulter- und Nackenbeschwerden.",
            "Sein Ansatz: hartnäckig nach der echten Ursache suchen, statt Symptome zu behandeln. Patient*innen mit langer Vorgeschichte landen häufig bei ihm.",
            "Spezialisierungen: Frozen Shoulder, Rotatorenmanschetten-Verletzungen, chronischer Nacken."
        ],
        "schwerpunkte": ["Schulter & Nacken", "Frozen Shoulder", "Manuelle Therapie", "Chronische Schmerzbilder"],
        "weiterbildung": ["Manuelle Therapie", "Schulter-Spezialisierung", "Schmerz-Neurowissenschaft"]
    },
    "simon-brueggemann": {
        "bio": [
            "Simon kombiniert Physiotherapie mit sportwissenschaftlichem Hintergrund (B.A. Sportwissenschaften). Er ist unser Spezialist für die Bewegungsdiagnostik (Säule 05) und für die Übergabe zum Athletik-Training.",
            "Wenn du eine 149-€-Diagnostik buchst, bist du häufig bei ihm. Wenn du danach in das Athletik-Programm willst, ebenfalls.",
            "Er erklärt komplexe Bewegungsanalysen so, dass du sie verstehst — und einen Plan in der Hand hast, der wirklich funktioniert."
        ],
        "schwerpunkte": ["Bewegungsdiagnostik", "Athletik-Programme", "Return-to-Sport", "Daten-basierte Therapieplanung"],
        "weiterbildung": ["B.A. Sportwissenschaften", "Bewegungs- und Belastungsdiagnostik", "Athletik-Coach"]
    }
}


def render_team_person(p):
    bio_data = BIOS.get(p["slug"])

    schema = (
        '<script type="application/ld+json">'
        '{{"@context":"https://schema.org","@type":"Person","name":"' + p["name"] + '",'
        '"jobTitle":"' + p["role"] + '",'
        '"worksFor":{{"@type":"Organization","name":"REHAB FIVE"}},'
        '"image":"https://rehab-five.com/team/' + p["slug"] + '.jpg"}}'
        '</script>'
    ).replace('{{', '{').replace('}}', '}')

    if bio_data:
        bio_html = "\n".join(f'        <p class="mt-5 text-[#FBF1E0]/80 text-lg leading-[1.65]">{b}</p>' for b in bio_data["bio"])
        schwerpunkte = "\n".join(
            f'          <li class="flex items-start gap-3 py-3 border-b border-[#FBF1E0]/10"><span class="text-[#D99129]">·</span> {s}</li>'
            for s in bio_data["schwerpunkte"])
        weiterbildung = "\n".join(
            f'          <li class="flex items-start gap-3 py-3 border-b border-[#FBF1E0]/10"><span class="text-[#D99129]">·</span> {w}</li>'
            for w in bio_data["weiterbildung"])
        detail_block = f"""
      <div class="mt-10 max-w-2xl">
{bio_html}
      </div>

      <div class="mt-12 grid sm:grid-cols-2 gap-10">
        <div>
          <div class="micro text-[#D99129] mb-3">Schwerpunkte</div>
          <ul class="text-[#FBF1E0]/85">
{schwerpunkte}
          </ul>
        </div>
        <div>
          <div class="micro text-[#D99129] mb-3">Weiterbildung</div>
          <ul class="text-[#FBF1E0]/85">
{weiterbildung}
          </ul>
        </div>
      </div>
"""
    else:
        detail_block = f"""
      <div class="mt-10 max-w-2xl">
        <p class="text-[#FBF1E0]/80 text-lg leading-[1.65]">{p['name']} ist Teil des REHAB-FIVE-Teams seit mehreren Jahren. Detaillierte Profil-Informationen folgen — gerne lernst du {p['name']} bei einem Termin persönlich kennen.</p>
      </div>
"""

    sub = p.get("subtitle", "")
    sub_html = f'<p class="mt-3 text-xl text-[#FBF1E0]/65">{sub}</p>' if sub else ""

    if p.get("photo"):
        photo_html = f'<img src="../img/team/{p["photo"]}" alt="{p["name"]}" class="w-full h-full object-cover"/>'
    else:
        photo_html = (
            f'<div class="w-full h-full flex items-center justify-center bg-[#FBF1E0]/5">'
            f'<span class="display text-[#D99129]/70" style="font-size:clamp(80px,12vw,160px);letter-spacing:-0.02em;">{initials(p["name"])}</span>'
            f'</div>'
        )

    content = f"""
  <a href="index.html" class="ulink inline-flex items-center gap-2 text-[#FBF1E0]/70 text-sm mb-12">
    <span class="text-[#D99129]">←</span> Zurück zum Team
  </a>

  <div class="grid lg:grid-cols-12 gap-10 lg:gap-16 items-start">
    <div class="lg:col-span-5">
      <div class="relative">
        <div class="absolute -top-3 -left-3 right-12 h-[2px] bg-[#D99129]"></div>
        <div class="absolute -top-3 -left-3 w-[2px] h-32 bg-[#D99129]"></div>
        <div class="aspect-[3/4] rounded-sm overflow-hidden bg-[#FBF1E0]/5 border border-[#FBF1E0]/10">
          {photo_html}
        </div>
      </div>
    </div>

    <div class="lg:col-span-7">
      <div class="micro text-[#D99129]">{p['role']}</div>
      <h1 class="display text-[clamp(40px,6vw,84px)] text-[#FBF1E0] mt-4 leading-[0.95]">{p['name']}</h1>
      {sub_html}
{detail_block}
      <div class="mt-12 pt-8 border-t border-[#FBF1E0]/15">
        <div class="micro text-[#D99129]">Termine</div>
        <p class="mt-2 text-lg text-[#FBF1E0]">{p['location']}</p>

        <div class="mt-8 flex flex-wrap gap-3">
          <a href="https://termin.docmedico-rezeption.de/j9u4c9m7a" target="_blank" rel="noopener" class="btn-primary">
            Termin buchen
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </a>
          <a href="tel:+4925174788200" class="btn-outline">Anruf</a>
        </div>
      </div>
    </div>
  </div>
"""

    og_img = f"https://rehab-five.com/img/team/{p['photo']}" if p.get("photo") else "https://rehab-five.com/og.jpg"
    return HEAD_TPL.format(
        title=f"{p['name']} · {p['role']} · REHAB FIVE",
        description=f"{p['name']} — {p['role']} bei REHAB FIVE Physiotherapie Münster. {p.get('subtitle','')}".strip(),
        canonical=f"https://rehab-five.com/team/{p['slug']}",
        og_type="profile",
        og_image=og_img,
        schema=schema,
        content=content
    )


def render_team_index():
    by_cat = {}
    for p in TEAM:
        by_cat.setdefault(p["category"], []).append(p)

    cat_order = ["Leitung", "Therapie", "Therapie & Rezeption", "Ernährung", "Rezeption & Backoffice"]
    sections = []
    for cat in cat_order:
        if cat not in by_cat:
            continue
        cards = []
        for p in by_cat[cat]:
            sub = p.get("subtitle", "")
            sub_html = f'<p class="mt-1 text-[13px] text-[#FBF1E0]/55">{sub}</p>' if sub else ""
            if p.get("photo"):
                thumb = f'<img src="../img/team/{p["photo"]}" alt="{p["name"]}" class="w-full h-full object-cover group-hover:scale-[1.03] transition duration-500"/>'
            else:
                thumb = (
                    f'<div class="w-full h-full flex items-center justify-center bg-[#FBF1E0]/5 group-hover:bg-[#FBF1E0]/10 transition">'
                    f'<span class="display text-[#D99129]/70" style="font-size:clamp(36px,5vw,64px);letter-spacing:-0.02em;">{initials(p["name"])}</span>'
                    f'</div>'
                )
            cards.append(f"""
        <a href="{p['slug']}.html" class="card-glass rounded-sm p-5 group transition flex flex-col">
          <div class="aspect-[3/4] overflow-hidden rounded-sm bg-[#FBF1E0]/5 border border-[#FBF1E0]/10 mb-4">
            {thumb}
          </div>
          <div class="micro text-[#D99129]">{p['role']}</div>
          <h3 class="display-up text-base text-[#FBF1E0] mt-2">{p['name']}</h3>
          {sub_html}
          <span class="ulink mt-3 inline-flex text-[13px] font-bold text-[#D99129]">Profil →</span>
        </a>
""")
        sections.append(f"""
    <div class="mt-16">
      <div class="micro text-[#D99129] mb-6">{cat}</div>
      <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
{''.join(cards)}
      </div>
    </div>
""")

    content = f"""
  <a href="../index.html#team" class="ulink inline-flex items-center gap-2 text-[#FBF1E0]/70 text-sm mb-12">
    <span class="text-[#D99129]">←</span> Zur Startseite
  </a>

  <div class="max-w-3xl">
    <div class="micro text-[#D99129]">Team</div>
    <h1 class="display text-[clamp(48px,8vw,120px)] text-[#FBF1E0] mt-4 leading-[0.95]">
      Das Team <span class="text-[#D99129]">hinter REHAB FIVE.</span>
    </h1>
    <p class="mt-8 text-xl text-[#FBF1E0]/70 leading-[1.55]">
      {len(TEAM)} Menschen, die jeden Tag dafür sorgen, dass du nicht nur „behandelt“ wirst, sondern wirklich vorankommst. Spezialisierungen statt Generalist*innen — wir matchen dich mit der Person, die zu deiner Beschwerde passt.
    </p>
  </div>

{''.join(sections)}
"""

    return HEAD_TPL.format(
        title=f"Team · {len(TEAM)} Therapeut*innen · REHAB FIVE Münster",
        description=f"Das gesamte Team von REHAB FIVE Physiotherapie Münster — {len(TEAM)} Mitarbeiter*innen mit Spezialisierungen in Manueller Therapie, Sport-Reha, Diagnostik und Athletik.",
        canonical="https://rehab-five.com/team/",
        og_type="website",
        og_image="https://rehab-five.com/og.jpg",
        schema="",
        content=content
    )


# ============================================================
# BLOG — Originalinhalte aus rehab-five.com/blog mit Studienverweisen
# ============================================================

BLOG_ARTICLES = [
    {
        "slug": "schmerzen-verstehen",
        "title": "Schmerzen verstehen — Physiotherapie & moderne Schmerzforschung",
        "category": "Schmerzforschung",
        "date": "13.05.2026",
        "lead": "Ist Schmerz immer ein Zeichen von Gewebeschäden? Schmerz ist ein Schutzsignal des Gehirns — wir zeigen, wie wir bei REHAB FIVE helfen, wieder aktiv zu werden.",
        "body": [
            ("h2", "Warum „Aua“ nicht immer „kaputt“ bedeutet"),
            ("p", "Viele Patient*innen in Münster stellen sich die Frage, ob starke Schmerzen auf ernsthafte Schäden hindeuten müssen. Die Antwort der modernen Wissenschaft überrascht: Das ist nicht zwingend der Fall."),
            ("p", "Schmerz ist kein direktes Maß für Gewebeschaden. Stattdessen ist er ein <strong>hochkomplexes Schutzsignal</strong> des Nervensystems. Wir unterstützen dabei, dieses Signal richtig zu verstehen und die Angst vor Bewegung zu überwinden."),
            ("h2", "Was ist Schmerz überhaupt? Spoiler: Es findet im Kopf statt"),
            ("p", "Schmerz ist nicht bloß ein mechanisches Problem. Die Schmerzforscher Butler und Moseley (2005) beschreiben Schmerz als <em>„eine Entscheidung deines Gehirns“</em>. Das Gehirn bewertet eingehende Informationen und fragt: Ist das eine Bedrohung?"),
            ("h3", "Zentrale Erkenntnisse"),
            ("ul", [
                "Das Gehirn trifft die finale Entscheidung über Schmerz",
                "Schmerz kann extrem real sein, auch wenn MRT-Befunde unauffällig sind",
                "Schmerz funktioniert wie eine Alarmanlage — manchmal durch echte Gefahren ausgelöst, manchmal durch Sensibilisierung"
            ]),
            ("h2", "Warum Schmerz manchmal stärker ist als der MRT-Befund"),
            ("p", "Ein häufiges Phänomen: Der medizinische Befund zeigt kaum Auffälligkeiten, aber die Lebensqualität ist stark eingeschränkt. Dies wird oft durch <strong>zentrale Sensibilisierung</strong> erklärt — das Nervensystem befindet sich in einem permanenten Alarmmodus."),
            ("p", "Reize, die früher harmlos waren (langes Bürositzen, Spaziergänge), werden vom Gehirn plötzlich als gefährlich bewertet."),
            ("h3", "Faktoren, die das Schmerz-Volumen erhöhen"),
            ("ul", [
                "Angst vor Bewegung (wer Aktivität als schädlich ansieht, empfindet mehr Schmerz)",
                "Stress und Schlafmangel (ein müdes System ist empfindlicher)",
                "Frühere Erfahrungen (das Gehirn lernt Schmerz)"
            ]),
            ("h2", "Warum reine Schonung oft das Problem verschärft"),
            ("p", "Vermeidungsverhalten hat langfristige Konsequenzen: Gelenke und Muskeln werden weniger belastbar. Butler und Moseley beschreiben Bewegung als <em>„Nahrung für das Gehirn“</em>. Gezielte Aktivität hilft dem Nervensystem zu verstehen, dass Belastung sicher ist."),
            ("h3", "Wir arbeiten nach drei Säulen"),
            ("ul", [
                "<strong>Aufklärung (Education):</strong> Verständnis für die Schmerzursachen reduziert das Bedrohungsgefühl",
                "<strong>Pacing:</strong> Die Belastung wird so kleinschrittig gesteigert, dass das Alarmsystem nicht überreagiert",
                "<strong>Vertrauensaufbau:</strong> Patienten lernen wieder, ihrem Körper zu vertrauen — beim Sport, beim Radfahren oder im Alltag"
            ]),
            ("h2", "Moderne Physiotherapie bei REHAB FIVE Münster"),
            ("p", "Der therapeutische Ansatz beschränkt sich nicht auf die schmerzende Stelle. Das gesamte System wird behandelt."),
            ("ul", [
                "Schmerz wird nicht verharmlost, sondern wissenschaftlich fundiert eingeordnet",
                "Die Gründe für die Nervensystemempfindlichkeit werden erforscht",
                "Aktive Therapie verbessert die Belastbarkeit für echtes Leben",
                "Individuelle Steuerung findet das richtige Gleichgewicht zwischen Fordern und Fördern"
            ]),
            ("pull", "Schmerz ist ein Warnsignal, kein Urteil. Rücken, Knie oder Schulter sind oft viel belastbarer, als Schmerz vermuten lässt."),
            ("p", "Ein besseres Verständnis der Schmerzphysiologie ist häufig der erste und wichtigste Schritt zur Besserung."),
        ],
        "sources": [
            "Butler, D. S., Moseley, G. L., & Moog, M. E. (2005). <em>Schmerzen verstehen.</em>"
        ],
        "author": "Aric Brämswig · B.Sc. Physiotherapie",
        "related": ["achilles-tendinopathie", "rotatorenmanschettenruptur"],
        "hero_image": "img/scenes/community.jpg",
        "image_alt": "Bewegung als Therapie — REHAB FIVE Praxis Münster",
        "faq": [
            {"q": "Mein MRT zeigt keinen Befund — warum habe ich trotzdem Schmerzen?", "a": "Schmerz entsteht nicht in der Struktur, sondern im Nervensystem. Selbst bei unauffälligem MRT kann eine zentrale Sensibilisierung dafür sorgen, dass dein System Reize stärker bewertet als nötig. Das macht den Schmerz nicht eingebildet — es heißt nur, dass die Behandlung am Bewegungsverhalten und an der Belastbarkeit ansetzt, nicht an einer „kaputten\" Stelle."},
            {"q": "Hilft Schonung bei chronischem Schmerz?", "a": "Selten. Längere Schonung macht Strukturen weniger belastbar und das Nervensystem empfindlicher. Wer in den ersten Wochen schont, kann das verstehen — wer es über Monate macht, verstärkt das Problem meist. Gezielte, dosierte Bewegung ist in der Schmerzforschung der besser belegte Weg."},
            {"q": "Wie lange dauert es, bis aktive Therapie greift?", "a": "Erste Veränderungen merken viele Patient*innen nach 2–4 Wochen, deutliche Veränderungen oft nach 8–12 Wochen. Chronische Bilder können 3–6 Monate brauchen. Wichtig ist, dass es eine Tendenz nach oben gibt, nicht dass jede Sitzung „besser\" sein muss."},
            {"q": "Wann muss ich zum Arzt statt zur Physiotherapie?", "a": "Bei plötzlichem, sehr starkem Schmerz mit Unfall, bei Taubheit oder Lähmung, bei Fieber/Nachtschweiß, bei ungeklärtem Gewichtsverlust oder bei Brustschmerzen. Für solche Bilder sind Hausarzt und Notaufnahme die richtige Anlaufstelle — wir übernehmen danach."},
            {"q": "Was passiert in der ersten Sitzung bei REHAB FIVE?", "a": "Wir hören dir 20–30 Minuten zu, machen einen funktionellen Befund (was geht, was nicht, mit welcher Intensität) und besprechen einen realistischen Plan. Du verlässt die Praxis mit einer Einschätzung — nicht mit „mal sechs Sitzungen schauen\"."},
        ]
    },
    {
        "slug": "achilles-tendinopathie",
        "title": "Achilles-Tendinopathie — Effektive Hilfe bei Achillessehnenschmerzen",
        "category": "Achillessehne",
        "date": "06.05.2026",
        "lead": "Für aktive Menschen in Münster ist eine belastbare Achillessehne essentiell. Wenn sie morgens steif ist, beim Anlaufen schmerzt oder nach dem Sport empfindlich bleibt, steckt oft eine Tendinopathie dahinter.",
        "body": [
            ("h2", "Symptome: Woran erkennst du eine Achilles-Tendinopathie?"),
            ("p", "Die Tendinopathie entwickelt sich typischerweise schleichend. Folgende Anzeichen sollten beachtet werden:"),
            ("ul", [
                "<strong>Anlaufschmerz &amp; Morgensteifigkeit:</strong> Erste Schritte aus dem Bett wirken hölzern und schmerzhaft",
                "<strong>Lokale Druckempfindlichkeit:</strong> Meist 2 bis 6 cm oberhalb des Fersenbeins oder am Sehnenansatz",
                "<strong>Belastungsreaktion:</strong> Schmerzen treten oft erst nach dem Training oder bei intensiveren Belastungen auf",
                "<strong>Verdickung:</strong> Die Sehne kann im Seitenvergleich deutlich dicker und knotiger erscheinen"
            ]),
            ("h2", "Ursachen: Warum schmerzt die Sehne?"),
            ("p", "Entgegen früherer Annahmen ist Achilles-Tendinopathie keine einfache Entzündung. Die systematische Übersicht von <strong>van der Vlist et al. (2019)</strong> zeigt, dass es häufig kein einzelnes Auslöseereignis gibt. Stattdessen wirkt ein Zusammenspiel von Faktoren:"),
            ("ul", [
                "<strong>Verminderte Wadenkraft:</strong> Ein schwacher Muskel überbelastet die Sehne als Verbindungselement",
                "<strong>Belastungswechsel:</strong> Plötzliche Trainingsumfang-Änderungen oder Untergrundwechsel (z.B. von Waldboden zu Asphalt)",
                "<strong>Individuelle Faktoren:</strong> Frühere Verletzungen oder ungünstige Belastungssteuerung"
            ]),
            ("h2", "Physiotherapie in Münster: Belastung statt Schonung"),
            ("p", "Das frühere Konzept der Schonungspause ist überholt. Moderne Forschung zeigt: Sehnen benötigen mechanische Reize für die Heilung. Bei REHAB FIVE setzen wir auf aktive Rehabilitation."),
            ("h3", "Unser Behandlungsansatz"),
            ("ul", [
                "<strong>Progressive Kräftigung:</strong> Systematisches Training der Wadenmuskulatur zur Steigerung der Sehnenleistungsfähigkeit",
                "<strong>Schmerz-Monitoring:</strong> Vermittlung richtiger Deutung von Schmerzschwankungen für sichere Trainingssteuerung",
                "<strong>Belastungsmanagement:</strong> Anpassung alltäglicher Geh- und Laufbelastung bei Vermeidung von Sehnenreizung"
            ]),
            ("h2", "Langzeiterfolg: Was die Forschung verspricht"),
            ("p", "Die 5-Jahres-Studie von <strong>Silbernagel et al. (2011)</strong> ist vielversprechend: Etwa 80 % der Patient*innen genesen vollständig durch ein konsequentes Trainingsprogramm. Ein Schlüsselfaktor für Erfolg war die Überwindung von Bewegungsangst."),
            ("pull", "Achillessehnenschmerzen sollten nicht ignoriert werden — sind aber sehr gut behandelbar. Mit strukturierter Physiotherapie bekommst du die Kontrolle zurück."),
        ],
        "sources": [
            "van der Vlist, A. C., et al. (2019). Clinical risk factors for Achilles tendinopathy. <em>British Journal of Sports Medicine (BJSM)</em>.",
            "Silbernagel, K. G., et al. (2011). The majority of patients with painful eccentric Achilles tendinopathy recover fully when treated with exercise alone. <em>American Journal of Sports Medicine (AJSM)</em>."
        ],
        "author": "Aric Brämswig",
        "related": ["achillessehnenruptur", "schmerzen-verstehen"],
        "hero_image": "img/beschwerden/sport.jpg",
        "image_alt": "Laufen nach Achilles-Tendinopathie — Reha bei REHAB FIVE",
        "faq": [
            {"q": "Wie unterscheide ich eine Tendinopathie von einem Achillessehnenriss?", "a": "Bei einer Tendinopathie tut die Sehne weh, du kannst aber laufen, dich auf die Zehen stellen und abdrücken — es schmerzt nur. Bei einem Riss spürst du einen knallartigen Schmerz, kannst dich nicht mehr auf die Zehen stellen und tastest oft eine Lücke in der Sehne. Letzteres ist ein Notfall."},
            {"q": "Soll ich bei Achillessehnenschmerzen mit dem Laufen aufhören?", "a": "Nicht zwingend. In den meisten Fällen darf weiter belastet werden, solange der Schmerz unter etwa 3/10 bleibt und sich am nächsten Morgen nicht verschlechtert. Komplette Schonung verlängert das Problem in der Regel — die Sehne braucht Reize, um sich neu zu organisieren."},
            {"q": "Welche Übungen helfen wirklich gegen Tendinopathie?", "a": "Wissenschaftlich am besten belegt sind langsame, schwere Wadenheber (Heavy Slow Resistance) und exzentrische Wadenbeugen. Wir bauen die Belastung so auf, dass du nach 8–12 Wochen 80–100 % deiner Funktion zurückhast — gemessen, nicht geschätzt."},
            {"q": "Wie lange dauert die Heilung einer Achilles-Tendinopathie?", "a": "Realistisch 8–24 Wochen — abhängig davon, wie lange das Problem schon besteht, wie konsequent du das Programm umsetzt und wie viel du parallel belastest. Frische Bilder gehen schneller, chronische Sehnen brauchen Geduld."},
            {"q": "Kann eine Tendinopathie chronisch werden?", "a": "Ja, wenn sie ignoriert wird oder nur mit Schmerzmitteln „weggedrückt\" wird. Mit strukturiertem Kraftaufbau ist die Prognose dagegen sehr gut — eine 5-Jahres-Studie zeigt rund 80 % vollständige Genesung bei konsequentem Training."},
        ]
    },
    {
        "slug": "rotatorenmanschettenruptur",
        "title": "Rotatorenmanschettenruptur — Hilfe bei Sehnenriss & Schulterschmerz",
        "category": "Schulter",
        "date": "29.04.2026",
        "lead": "Wer beim Anziehen, beim kraftvollen Treten oder beim Greifen ins obere Regal plötzlich stechende Schulterschmerzen spürt, vermutet oft eine Überlastung. Doch wenn Kraft nachlässt und Schmerz bleibt, kann eine Rotatorenmanschettenruptur dahinterstecken.",
        "body": [
            ("h2", "Wie entsteht ein Riss der Rotatorenmanschette?"),
            ("p", "Die Rotatorenmanschette besteht aus einer Gruppe von Sehnen, die den Oberarmkopf stabilisieren und zentrieren. Ein Riss entwickelt sich nicht immer durch Unfalltraumata. Gemäß <strong>Nho et al. (2008)</strong> entstehen viele Rupturen schleichend durch:"),
            ("ul", [
                "<strong>Altersbedingte Degeneration:</strong> Natürlicher Verschleiß des Sehnengewebes",
                "<strong>Wiederholte Mikrobelastungen:</strong> Überlastung bei Überkopfarbeiten oder sportlichen Aktivitäten",
                "<strong>Anatomische Einflüsse:</strong> Engpässe unter dem Schulterdach (Impingement)"
            ]),
            ("pull", "Ein Riss im MRT bedeutet nicht automatisch das Ende sportlicher Aktivität. Viele Personen leben beschwerdefrei trotz kleinerer Sehnenrisse."),
            ("h2", "Typische Symptome"),
            ("ul", [
                "<strong>Kraftverlust:</strong> Besonders das seitliche Armheben fällt schwer",
                "<strong>Nachtschmerz:</strong> Beschwerden beim Liegen auf der betroffenen Seite",
                "<strong>Ausstrahlung:</strong> Ziehen bis in den Oberarm oder Nacken",
                "<strong>Alltagseinschränkungen:</strong> Schwierigkeiten beim Haarekämmen oder beim Griff nach hinten"
            ]),
            ("h2", "Warum der MRT-Befund nicht alles erklärt"),
            ("p", "Aktuelle Forschung von <strong>Garcia et al. (2024)</strong> unterstreicht: Entscheidend ist nicht allein das bildgebende Ergebnis, sondern die <strong>tatsächliche Alltagsfunktion</strong>. Während vollschichtige Risse zur Größenzunahme neigen, lassen sich viele Teilrisse und komplette Rupturen hervorragend konservativ stabilisieren."),
            ("h2", "Physiotherapie in Münster: Konservative Behandlung"),
            ("p", "In vielen Fällen — besonders bei degenerativen Rissen — ist eine <strong>konservative Behandlung</strong> der erste und oft erfolgreichste Weg. Wir setzen auf:"),
            ("ul", [
                "<strong>Gezielte Kräftigung:</strong> Training der intakten Rotatorenmanschettenanteile und der Schulterblattmuskulatur",
                "<strong>Bewegungskontrolle:</strong> Optimierung des Zusammenspiels zwischen Schulterblatt und Oberarm",
                "<strong>Schmerzmanagement:</strong> Manuelle Techniken zur Gelenkentlastung in der Akutphase",
                "<strong>Belastungsanpassung:</strong> Rückkehr zu beruflichen, sportlichen oder alltäglichen Aktivitäten"
            ]),
            ("h2", "Wann ist eine Operation sinnvoll?"),
            ("ul", [
                "Frischem, traumatischem Riss",
                "Massivem Kraftverlust",
                "Ausbleibenden Erfolgen der konservativen Therapie über mehrere Monate"
            ]),
            ("p", "Die Entscheidung erfolgt individuell, basierend auf dem persönlichen Belastungsanspruch."),
        ],
        "sources": [
            "Nho, S. J., et al. (2008). Rotator cuff degeneration: etiology and pathogenesis. <em>American Journal of Sports Medicine (AJSM)</em>.",
            "Garcia, M. J., et al. (2024). Disparities in Rotator Cuff Tear Progression Definitions. <em>JBJS Open Access</em>."
        ],
        "author": "Aric Brämswig",
        "related": ["schmerzen-verstehen", "achillessehnenruptur"],
        "hero_image": "img/beschwerden/schulter.jpg",
        "image_alt": "Schulter nach Rotatorenmanschettenruptur — REHAB FIVE Münster",
        "faq": [
            {"q": "Muss eine Rotatorenmanschettenruptur immer operiert werden?", "a": "Nein. Bei degenerativen, kleinen oder Teilrupturen ist konservative Therapie oft die erste Wahl und führt bei vielen Patient*innen zu sehr guten Ergebnissen. Operiert wird bei frischem, traumatischem Riss, massivem Kraftverlust oder wenn drei bis sechs Monate Therapie nicht greifen."},
            {"q": "Wie schnell soll ich nach einem Riss zur Physiotherapie?", "a": "So früh wie möglich. Die ersten 2 Wochen geht es um Schmerz- und Schwellungsmanagement, danach starten wir mit kontrollierter Bewegung — schon bevor entschieden ist, ob operiert wird. Frühes Therapiestarten verbessert den Verlauf nachweislich."},
            {"q": "Welche Symptome sind typisch?", "a": "Kraftverlust beim seitlichen Armheben, Nachtschmerz beim Liegen auf der betroffenen Seite, Ausstrahlung in den Oberarm und Probleme beim Haarekämmen oder Anziehen. Wenn mehrere davon zusammenkommen, lohnt sich ein klinischer Befund."},
            {"q": "Was ist der Unterschied zwischen Teilriss und kompletter Ruptur?", "a": "Ein Teilriss betrifft nur einen Teil der Sehnendicke — die Sehne hält noch, aber überlastet schneller. Eine komplette Ruptur ist ein Riss durch die ganze Sehne. Beide können konservativ behandelt werden, die OP-Indikation hängt von Alter, Aktivitätsniveau und Kraftverlust ab — nicht nur vom MRT-Bild."},
            {"q": "Kann ich nach einem Riss wieder zum Sport zurück?", "a": "In den meisten Fällen ja, auch ohne OP. Wir steuern die Rückkehr über funktionelle Tests (Kraft, Symmetrie, sportartspezifische Bewegungen). Bei konservativer Behandlung 4–6 Monate, nach OP 6–9 Monate bis Vollbelastung."},
        ]
    },
    {
        "slug": "morbus-bechterew",
        "title": "Morbus Bechterew — Physiotherapie bei Wirbelsäulenrheuma",
        "category": "Wirbelsäule",
        "date": "22.04.2026",
        "lead": "Wer morgens mit steifer Wirbelsäule aufwacht, nachts durch tiefsitzende Schmerzen gestört wird oder feststellt, dass Bewegung die Beschwerden lindert, sollte aufmerksam werden. Dahinter kann Morbus Bechterew stehen.",
        "body": [
            ("h2", "Was ist Morbus Bechterew?"),
            ("p", "Morbus Bechterew stellt eine chronisch-rheumatische Erkrankung dar, die vornehmlich die Wirbelsäule und die <strong>Iliosakralgelenke (ISG)</strong> in Mitleidenschaft zieht. Entzündliche Prozesse an Sehnenansätzen und Gelenken können unbehandelt zu einer fortschreitenden Versteifung führen."),
            ("h3", "Typische Symptome frühzeitig erkennen"),
            ("ul", [
                "<strong>Entzündlicher Rückenschmerz:</strong> Beschwerden entstehen vor allem in Ruhephasen (nachts/morgens)",
                "<strong>Morgensteifigkeit:</strong> Die Rückenbeweglichkeit benötigt oft über 30 Minuten zum Normalisieren",
                "<strong>Besserung durch Aktivität:</strong> Anders als bei Bandscheibenproblemen führt Bewegung hier häufig zur schnellen Linderung",
                "<strong>Beteiligung zusätzlicher Gelenke:</strong> Sehnenansätze (z.B. Achillessehne) oder Augen (Uveitis) können ebenfalls betroffen sein"
            ]),
            ("h2", "Warum Physiotherapie der Schlüssel zur Lebensqualität ist"),
            ("p", "Physiotherapie kommt bei Morbus Bechterew nicht als ergänzender Baustein, sondern als grundlegender Therapiepfeiler zum Einsatz. Eine aktuelle Metaanalyse von <strong>Gravaldi et al. (2022)</strong> verdeutlicht, dass <em>betreute Bewegungstherapie und gezielt gestaltete Übungsprogramme die Krankheitsaktivität reduzieren und die Wirbelsäulenfunktion erheblich verbessern</em>."),
            ("pull", "Die Wirbelsäule sollte möglichst beweglich und aufrecht bleiben, um eine Versteifung zu verhindern."),
            ("h2", "Dein aktiver Behandlungsplan bei REHAB FIVE"),
            ("ul", [
                "<strong>Mobilisation:</strong> Spezialisierte Techniken für Wirbelsäule und Hüften, um den Versteifungsprozess zu verlangsamen",
                "<strong>Atemgymnastik:</strong> Besondere Übungen zur Brustkorberweiterung, um die Lungenfunktion zu sichern",
                "<strong>Muskelstabilisierung:</strong> Kräftigung von Rumpf- und Hüftmuskulatur für eine aufrechte Körperposition",
                "<strong>Patientenaufklärung:</strong> Schulung zur frühzeitigen Schub-Erkennung und Umsetzung individualisierter Heimprogramme"
            ]),
            ("p", "Morbus Bechterew stellt eine Herausforderung dar, rechtfertigt aber nicht physische Untätigkeit. Eine zeitnahe Diagnose und konsequente physiotherapeutische Begleitung verbessern die Prognose für ein bewegliches Leben in Münster erheblich."),
        ],
        "sources": [
            "Gravaldi, L. P., et al. (2022). Effectiveness of Physiotherapy in Patients with Ankylosing Spondylitis. <em>Healthcare (Basel)</em>."
        ],
        "author": "Aric Brämswig",
        "related": ["schmerzen-verstehen", "rotatorenmanschettenruptur"],
        "hero_image": "img/beschwerden/ruecken.jpg",
        "image_alt": "Wirbelsäulen-Mobilisation bei Morbus Bechterew — REHAB FIVE",
        "faq": [
            {"q": "Wie äußert sich Morbus Bechterew zu Beginn?", "a": "Typisch sind nächtlicher und morgendlicher Rückenschmerz, mehr als 30 Minuten Morgensteifigkeit und Besserung durch Bewegung. Wer aufsteht und sich erstmal „warmlaufen\" muss, sollte das ernst nehmen — gerade bei jungen Erwachsenen."},
            {"q": "Kann Physiotherapie den Krankheitsverlauf bremsen?", "a": "Ja. Aktuelle Metaanalysen zeigen, dass strukturierte Bewegungstherapie Krankheitsaktivität, Wirbelsäulenfunktion und Lebensqualität messbar verbessert. Wer früh aktiv bleibt, behält langfristig deutlich mehr Beweglichkeit."},
            {"q": "Welche Bewegungsarten sind besonders hilfreich?", "a": "Mobilisation der Brust- und Lendenwirbelsäule, Atemgymnastik zur Brustkorbweite, Kräftigung der Rumpf- und Hüftmuskulatur. Schwimmen und gezielte Yoga-Varianten sind oft günstig — Kontaktsportarten mit Stoßbelastung weniger."},
            {"q": "Wie unterscheidet sich Bechterew-Schmerz von einem Bandscheibenproblem?", "a": "Bandscheibenprobleme verstärken sich meist durch Belastung und bessern sich durch Schonung. Beim Bechterew ist es umgekehrt: Ruhe verschlechtert, Bewegung verbessert. Wer morgens schlechter ist als abends, sollte auf eine entzündliche Ursache hin abklären lassen."},
            {"q": "Wie oft sollte ich Physiotherapie machen?", "a": "In aktiver Krankheitsphase 1–2 Mal pro Woche begleitet, dazu tägliche kurze Heimprogramme (15–20 Minuten). In stabilen Phasen reichen oft betreute Einheiten alle 2–4 Wochen plus eigene Routine."},
        ]
    },
    {
        "slug": "achillessehnenruptur",
        "title": "Achillessehnenruptur — Reha nach Sehnenriss",
        "category": "Achillessehne · Reha",
        "date": "15.04.2026",
        "lead": "Die Achillessehne ist die kräftigste Sehne des Körpers — ein „biologischer Turbolader“ bei sportlichen Aktivitäten. Ein Riss ist einschneidend, aber strukturierte Physiotherapie ermöglicht eine schrittweise Rückkehr zu Stabilität und Schnellkraft.",
        "body": [
            ("h2", "Wie entsteht ein Riss der Achillessehne?"),
            ("p", "Typischerweise tritt eine Ruptur während explosiver Bewegungen oder schneller Richtungswechsel auf — beispielsweise beim Tennis oder Fußball. Patient*innen berichten häufig von dem Empfinden, <em>als sei jemandem in die Wade getreten worden</em>, oft begleitet von einem knallartigen Geräusch."),
            ("h3", "Typische Ursachen & Risikofaktoren"),
            ("ul", [
                "<strong>Sportliche Spitzenbelastungen:</strong> Schnelle Sprints und Sprünge überfordern die Sehnenkapazität",
                "<strong>Degenerative Veränderungen:</strong> Vorschädigungen oder chronische Reize schwächen das Gewebe schleichend",
                "<strong>Trainingsfehler:</strong> Zu schnelle Intensitätssteigerung ohne ausreichende Regeneration",
                "<strong>Systemische Faktoren:</strong> Stoffwechselerkrankungen oder bestimmte Medikamente beeinflussen die Sehnenstruktur"
            ]),
            ("h2", "Symptome: Woran erkennst du die Ruptur?"),
            ("ul", [
                "<strong>Tastbare Delle:</strong> Im Sehenverlauf (meist 2–6 cm über dem Fersenbein) ist eine Lücke palpierbar",
                "<strong>Kraftverlust:</strong> Aktives Abdrücken des Fußes oder Zehenstand sind nicht mehr möglich",
                "<strong>Schwellung &amp; Hämatom:</strong> Rasche Einblutung im Bereich der Ferse und Wade"
            ]),
            ("h2", "Der Heilungsverlauf: Geduld und Struktur"),
            ("p", "Die Achillessehne benötigt Zeit zum Wiederaufbau mechanischer Belastbarkeit. Unabhängig von operativer oder konservativer Versorgung:"),
            ("ul", [
                "<strong>Dauer:</strong> Mehrere Monate intensive Rehabilitation erforderlich",
                "<strong>Return to Sport:</strong> Rückkehr zu High-Impact-Sportarten erfolgt üblicherweise nach <strong>6 bis 9 Monaten</strong>, basierend auf funktionellen Tests (Kraft, Sprungqualität, Symmetrie)"
            ]),
            ("h2", "Physiotherapie in Münster: Phasenorientierte Rehabilitation"),
            ("p", "Die Reha-Strategie folgt einem kriteriumsorientierten Ansatz — Patient*innen steigen erst in höhere Belastungsstufen auf, wenn der Körper bereit ist."),
            ("h3", "Reha-Schwerpunkte"),
            ("ul", [
                "<strong>Frühphase:</strong> Management von Schwellung und Schmerz, vorsichtige frühfunktionelle Mobilisation im Spezialstiefel (Vacoped)",
                "<strong>Kraftaufbau:</strong> Systematische Kräftigung der Wadenmuskulatur und der gesamten kinetischen Kette (Hüfte/Knie)",
                "<strong>Neuromuskuläres Training:</strong> Wiederherstellung von Koordination und Balance zur Rückgewinnung alltäglicher Sicherheit",
                "<strong>Plyometrisches Training:</strong> Vorbereitung auf reaktive Belastungen wie Laufen und Springen"
            ]),
            ("pull", "Eine Achillessehnenruptur erfordert Disziplin während der Rehabilitation, bietet aber bei richtiger Steuerung eine exzellente Prognose."),
        ],
        "sources": [],
        "author": "Aric Brämswig · Sportphysiotherapie & Rehabilitationsmanagement",
        "related": ["achilles-tendinopathie", "schmerzen-verstehen"],
        "hero_image": "img/beschwerden/reha.jpg",
        "image_alt": "Reha nach Achillessehnenruptur — REHAB FIVE Münster",
        "faq": [
            {"q": "Operation oder konservative Behandlung — was ist besser?", "a": "Beide Wege führen heute zu vergleichbaren Endergebnissen, wenn die Reha strukturiert läuft. Konservativ wird häufiger bei älteren oder weniger aktiven Patient*innen gewählt, die OP eher bei jungen, sportlich ambitionierten Menschen mit klar diastasiertem Riss. Entscheidend ist nicht die Methode, sondern die Reha danach."},
            {"q": "Wann darf ich nach der OP wieder belasten?", "a": "Frühfunktionelle Reha ist heute Standard: oft schon nach wenigen Tagen Teilbelastung im Spezialstiefel (Vacoped), zunehmend frei in den ersten 6–8 Wochen. Konkrete Freigaben besprechen wir kriteriumsbasiert — du musst sie nicht aus dem Kalender ablesen."},
            {"q": "Wie lange muss ich den Spezialstiefel tragen?", "a": "In der Regel 6–8 Wochen, mit schrittweiser Reduktion der Fersenkeil-Höhe. Danach Übergang in normales Schuhwerk mit Ferseneinlage. Das ist nicht in Stein gemeißelt — wir entscheiden anhand der Heilung, nicht nach starrem Plan."},
            {"q": "Wann darf ich wieder Sport machen?", "a": "Joggen oft nach 4–6 Monaten, kontaktarme Sportarten nach 6 Monaten, Sprung- und Kontaktsport nach 6–9 Monaten. Voraussetzung: 90 %+ Symmetrie in Wadenkraft, Sprungtests und neuromuskulärer Kontrolle — sonst ist das Risiko einer Re-Ruptur deutlich erhöht."},
            {"q": "Wie hoch ist das Risiko für eine zweite Ruptur?", "a": "Bei strukturierter Reha mit Krafttests vor Sportfreigabe liegt es bei 2–5 %. Ohne Tests, also „nach Gefühl\" zurück, deutlich höher. Deshalb messen wir, bevor wir freigeben — auch wenn sich das nach Übervorsicht anfühlt."},
        ]
    },
]


def render_body(body):
    parts = []
    for kind, val in body:
        if kind == "h2":
            parts.append(f'<h2>{val}</h2>')
        elif kind == "h3":
            parts.append(f'<h3>{val}</h3>')
        elif kind == "p":
            parts.append(f'<p>{val}</p>')
        elif kind == "ul":
            lis = "\n".join(f"      <li>{it}</li>" for it in val)
            parts.append(f"<ul>\n{lis}\n    </ul>")
        elif kind == "pull":
            parts.append(f'<div class="pull">{val}</div>')
    return "\n    ".join(parts)


def render_blog_article(a):
    body_html = render_body(a["body"])

    sources_html = ""
    if a["sources"]:
        items = "\n".join(f"      <li>{s}</li>" for s in a["sources"])
        sources_html = f"""
      <div class="sources">
        <div class="micro text-[#D99129] mb-4">Wissenschaftliche Quellen</div>
        <ul>
{items}
        </ul>
      </div>
"""

    # Hero image absolute URL for schema
    hero_url = f"https://rehab-five.com/{a.get('hero_image','og.jpg')}"

    article_schema = (
        '<script type="application/ld+json">{"@context":"https://schema.org",'
        '"@type":"Article","headline":"' + a['title'].replace('"', '\\"') + '",'
        '"description":"' + a['lead'].replace('"', '\\"') + '",'
        '"author":{"@type":"Person","name":"' + a['author'] + '"},'
        '"publisher":{"@type":"Organization","name":"REHAB FIVE",'
        '"logo":{"@type":"ImageObject","url":"https://rehab-five.com/img/logo-white.png"}},'
        '"datePublished":"2026-04-22","image":"' + hero_url + '"}'
        '</script>'
    )

    # Hero-Image Block
    hero_html = ""
    if a.get("hero_image"):
        alt = a.get("image_alt", a['title'])
        hero_html = (
            '\n    <figure class="mt-10 -mx-6 sm:mx-0">\n'
            '      <div class="relative aspect-[16/9] overflow-hidden rounded-sm bg-[#FBF1E0]/5 border border-[#FBF1E0]/10">\n'
            f'        <img src="../{a["hero_image"]}" alt="{alt}" class="w-full h-full object-cover" loading="eager"/>\n'
            '        <div class="absolute inset-0" style="background: linear-gradient(180deg, transparent 60%, rgba(31,52,45,0.45) 100%);"></div>\n'
            '      </div>\n'
            f'      <figcaption class="mt-3 text-[12px] text-[#FBF1E0]/45 px-6 sm:px-0">{alt}</figcaption>\n'
            '    </figure>'
        )

    # FAQ-Block + FAQPage-Schema
    faq_html = ""
    faq_schema = ""
    if a.get("faq"):
        items = []
        for qa in a["faq"]:
            q = qa["q"].replace('<','&lt;').replace('>','&gt;')
            ans = qa["a"]
            items.append(
                f'      <details class="card-glass rounded-sm p-5 sm:p-6 group">\n'
                f'        <summary class="flex justify-between items-start gap-4 cursor-pointer list-none">\n'
                f'          <h3 class="text-[#FBF1E0] text-[17px] sm:text-[19px] leading-snug font-bold normal-case tracking-normal flex-1">{q}</h3>\n'
                f'          <span class="text-[#D99129] text-2xl font-bold leading-none mt-1 group-open:rotate-45 transition-transform">+</span>\n'
                f'        </summary>\n'
                f'        <p class="mt-4 text-[#FBF1E0]/75 text-[15px] leading-[1.65]">{ans}</p>\n'
                f'      </details>'
            )
        faq_html = (
            '\n    <section class="mt-16 pt-10 border-t border-[#FBF1E0]/15" aria-labelledby="faq-h">\n'
            '      <div class="micro text-[#D99129] mb-4">Häufige Fragen</div>\n'
            '      <h2 id="faq-h" class="display text-[clamp(28px,4.5vw,52px)] text-[#FBF1E0] leading-[1] mb-8">\n'
            '        Was Patient*innen <span class="text-[#D99129]">am häufigsten</span> fragen.\n'
            '      </h2>\n'
            '      <div class="space-y-3">\n'
            + '\n'.join(items)
            + '\n      </div>\n'
            '    </section>'
        )

        # FAQPage-Schema for AI/SEO
        faq_items_json = ",".join(
            '{"@type":"Question","name":"' + qa["q"].replace('"','\\"') + '",'
            '"acceptedAnswer":{"@type":"Answer","text":"' + qa["a"].replace('"','\\"') + '"}}'
            for qa in a["faq"]
        )
        faq_schema = (
            '<script type="application/ld+json">{"@context":"https://schema.org",'
            '"@type":"FAQPage","mainEntity":[' + faq_items_json + ']}</script>'
        )

    related_html = ""
    if a.get("related"):
        cards = []
        for slug in a["related"]:
            rel = next((b for b in BLOG_ARTICLES if b["slug"] == slug), None)
            if rel:
                cards.append(f"""
          <a href="{slug}.html" class="card-glass rounded-sm p-6 flex flex-col group transition">
            <div class="micro text-[#D99129]">{rel['category']}</div>
            <h3 class="text-lg text-[#FBF1E0] mt-3 leading-snug flex-1 normal-case tracking-normal">{rel['title']}</h3>
            <span class="ulink mt-4 inline-flex text-sm font-bold text-[#D99129]">Artikel lesen →</span>
          </a>
""")
        if cards:
            related_html = f"""
      <div class="mt-20 pt-10 border-t border-[#FBF1E0]/15">
        <div class="micro text-[#D99129] mb-6">Weiterlesen</div>
        <div class="grid md:grid-cols-2 gap-3">{''.join(cards)}</div>
      </div>
"""

    content = f"""
  <a href="index.html" class="ulink inline-flex items-center gap-2 text-[#FBF1E0]/70 text-sm mb-12">
    <span class="text-[#D99129]">←</span> Alle Artikel
  </a>

  <article class="max-w-3xl">
    <div class="flex items-center gap-3 mb-6">
      <div class="micro text-[#D99129]">{a['category']}</div>
      <span class="text-[#FBF1E0]/30">·</span>
      <div class="micro text-[#FBF1E0]/50">{a['date']}</div>
    </div>
    <h1 class="display text-[clamp(32px,5.5vw,68px)] text-[#FBF1E0] leading-[1.0]">{a['title']}</h1>
    <p class="mt-8 text-xl text-[#FBF1E0]/75 leading-[1.6]">{a['lead']}</p>
{hero_html}

    <div class="mt-12 pt-8 border-t border-[#FBF1E0]/15 prose-rf">
    {body_html}
{sources_html}
    </div>

    <div class="mt-12 pt-8 border-t border-[#FBF1E0]/15 micro text-[#FBF1E0]/55">
      Autor: {a['author']}
    </div>
{faq_html}

    <div class="mt-16 p-10 card-glass rounded-sm border-l-2 border-[#D99129]">
      <div class="micro text-[#D99129]">Therapie starten</div>
      <h2 class="text-3xl text-[#FBF1E0] mt-4 leading-tight">Beschwerden, die in diesem Artikel auftauchen?</h2>
      <p class="mt-4 text-[#FBF1E0]/70 leading-[1.6]">Ein Erstgespräch oder eine Diagnostik bei REHAB FIVE ist der einfachste Weg zu einem klaren Plan.</p>
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
        og_image=hero_url,
        schema=article_schema + faq_schema,
        content=content
    )


def render_blog_index():
    cards = []
    for a in BLOG_ARTICLES:
        thumb_html = ""
        if a.get("hero_image"):
            alt = a.get("image_alt", a['title'])
            thumb_html = (
                '<div class="aspect-[16/10] overflow-hidden rounded-sm bg-[#FBF1E0]/5 border border-[#FBF1E0]/10 mb-5 -mx-2 -mt-2">'
                f'<img src="../{a["hero_image"]}" alt="{alt}" class="w-full h-full object-cover group-hover:scale-[1.03] transition duration-500" loading="lazy"/>'
                '</div>'
            )
        cards.append(f"""
      <a href="{a['slug']}.html" class="card-glass rounded-sm p-7 flex flex-col group transition">
        {thumb_html}
        <div class="flex items-center gap-3 mb-4">
          <div class="micro text-[#D99129]">{a['category']}</div>
          <span class="text-[#FBF1E0]/30">·</span>
          <div class="micro text-[#FBF1E0]/45">{a['date']}</div>
        </div>
        <h2 class="text-2xl text-[#FBF1E0] leading-snug flex-1">{a['title']}</h2>
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
      Fundierte Artikel aus der Praxis — über Schmerzforschung, häufige Diagnosen und was die aktuelle Sportwissenschaft für deine Therapie bedeutet. Mit Studienverweisen. Geschrieben von Therapeut*innen, nicht von SEO-Agenturen.
    </p>
  </div>

  <div class="grid md:grid-cols-2 gap-3">
{''.join(cards)}
  </div>
"""

    return HEAD_TPL.format(
        title="Wissen · Blog · REHAB FIVE Physiotherapie Münster",
        description="Fundierte Artikel aus der Praxis mit Studienverweisen — Schmerzforschung, Achilles-Tendinopathie, Rotatorenmanschette, Morbus Bechterew, Achillessehnenruptur.",
        canonical="https://rehab-five.com/blog/",
        og_type="website",
        og_image="https://rehab-five.com/og.jpg",
        schema="",
        content=content
    )


# ============================================================
# Ausführen
# ============================================================

if __name__ == "__main__":
    print("=== Team-Detail-Seiten ===")
    for p in TEAM:
        path = TEAM_DIR / f"{p['slug']}.html"
        path.write_text(render_team_person(p), encoding="utf-8")
        print(f"  · team/{p['slug']}.html")

    print(f"\n=== Team-Übersichts-Seite ===")
    (TEAM_DIR / "index.html").write_text(render_team_index(), encoding="utf-8")
    print(f"  · team/index.html ({len(TEAM)} Personen)")

    print(f"\n=== Blog ===")
    (BLOG_DIR / "index.html").write_text(render_blog_index(), encoding="utf-8")
    print(f"  · blog/index.html")
    for a in BLOG_ARTICLES:
        path = BLOG_DIR / f"{a['slug']}.html"
        path.write_text(render_blog_article(a), encoding="utf-8")
        print(f"  · blog/{a['slug']}.html")

    print("\nFertig.")
