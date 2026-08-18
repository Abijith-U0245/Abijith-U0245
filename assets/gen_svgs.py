import os

BASE = "/home/claude/profile-readme/assets"
os.makedirs(f"{BASE}/headers", exist_ok=True)

NAVY = "#0F172A"
INDIGO_DARK = "#1E1B4B"
INDIGO = "#312E81"
ACCENT = "#4F46E5"
LILAC = "#A5B4FC"
SLATE = "#94A3B8"
WHITE = "#E2E8F0"

def header_svg(title, icon_path_d=None):
    return f'''<svg width="920" height="64" viewBox="0 0 920 64" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{INDIGO_DARK}"/>
      <stop offset="100%" stop-color="{INDIGO}"/>
    </linearGradient>
  </defs>
  <rect width="920" height="64" rx="10" fill="url(#g)"/>
  <rect x="0" y="0" width="6" height="64" rx="3" fill="{ACCENT}"/>
  <text x="34" y="41" font-family="JetBrains Mono, Consolas, monospace" font-size="24" font-weight="700" fill="{LILAC}">{title}</text>
</svg>'''

headers = {
    "about": "01 · About",
    "experience": "02 · Experience",
    "now-building": "03 · Now Building",
    "stack": "04 · Stack",
    "projects": "05 · Projects",
    "activity": "06 · GitHub Activity",
    "achievements": "07 · Achievements",
    "connect": "08 · Connect",
}

for key, label in headers.items():
    with open(f"{BASE}/headers/{key}.svg", "w") as f:
        f.write(header_svg(label))

# Divider
divider = f'''<svg width="920" height="3" viewBox="0 0 920 3" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="d" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{NAVY}" stop-opacity="0"/>
      <stop offset="50%" stop-color="{ACCENT}"/>
      <stop offset="100%" stop-color="{NAVY}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect width="920" height="3" fill="url(#d)"/>
</svg>'''
with open(f"{BASE}/divider.svg", "w") as f:
    f.write(divider)

# Hero banner (name + role, richer than capsule-render alone)
hero = f'''<svg width="920" height="260" viewBox="0 0 920 260" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{NAVY}"/>
      <stop offset="50%" stop-color="{INDIGO_DARK}"/>
      <stop offset="100%" stop-color="{INDIGO}"/>
    </linearGradient>
    <radialGradient id="glow" cx="80%" cy="20%" r="60%">
      <stop offset="0%" stop-color="{ACCENT}" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="{ACCENT}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="920" height="260" rx="16" fill="url(#bg)"/>
  <rect width="920" height="260" rx="16" fill="url(#glow)"/>
  <text x="60" y="110" font-family="JetBrains Mono, Consolas, monospace" font-size="52" font-weight="800" fill="{WHITE}">Abijith U</text>
  <text x="62" y="145" font-family="JetBrains Mono, Consolas, monospace" font-size="18" fill="{LILAC}">Edge AI Engineer · Full-Stack Developer · IoT Builder</text>
  <text x="62" y="180" font-family="JetBrains Mono, Consolas, monospace" font-size="14" fill="{SLATE}">CSE @ Chennai Institute of Technology · Class of 2028</text>
  <g font-family="JetBrains Mono, Consolas, monospace" font-size="13" fill="{SLATE}">
    <text x="62" y="215">Chennai, India</text>
    <text x="220" y="215">·</text>
    <text x="235" y="215">Available now</text>
    <text x="400" y="215">·</text>
    <text x="415" y="215">GDG On Campus Secretary, CIT</text>
  </g>
  <circle cx="850" cy="60" r="34" fill="none" stroke="{ACCENT}" stroke-width="2" opacity="0.6"/>
  <circle cx="850" cy="60" r="22" fill="none" stroke="{LILAC}" stroke-width="1.5" opacity="0.4"/>
</svg>'''
with open(f"{BASE}/hero-banner.svg", "w") as f:
    f.write(hero)

# Skill radar-style cards (4 category cards row)
def skill_card(x, title, items, level):
    lines = "".join(
        f'<text x="{x+18}" y="{58+18*i}" font-family="JetBrains Mono, monospace" font-size="12" fill="{SLATE}">• {it}</text>'
        for i, it in enumerate(items)
    )
    bar_w = int(200 * level / 100)
    return f'''
  <rect x="{x}" y="0" width="220" height="{58+18*len(items)+30}" rx="10" fill="{INDIGO_DARK}" stroke="{ACCENT}" stroke-opacity="0.4"/>
  <text x="{x+18}" y="30" font-family="JetBrains Mono, monospace" font-size="15" font-weight="700" fill="{LILAC}">{title}</text>
  {lines}
  <rect x="{x+18}" y="{58+18*len(items)+8}" width="184" height="6" rx="3" fill="{NAVY}"/>
  <rect x="{x+18}" y="{58+18*len(items)+8}" width="{bar_w-16 if bar_w>16 else 4}" height="6" rx="3" fill="{ACCENT}"/>
'''

cards = [
    (0, "Full-Stack", ["React / Next.js", "FastAPI / Node.js", "MongoDB / MySQL", "Tailwind CSS"], 90),
    (230, "Edge AI / CV", ["YOLO11n / ONNX", "OpenCV", "PyTorch", "Axelera Metis"], 82),
    (460, "IoT Systems", ["ESP32 / Arduino", "MQTT / InfluxDB", "Raspberry Pi", "Redis"], 85),
    (690, "Applied ML", ["XGBoost / Prophet", "Isolation Forest", "Scikit-learn", "LangChain / RAG"], 88),
]

max_h = max(58+18*len(c[2])+40 for c in cards)
body = "".join(skill_card(x, t, it, lv) for x, t, it, lv in cards)
skill_cards = f'''<svg width="920" height="{max_h}" viewBox="0 0 920 {max_h}" xmlns="http://www.w3.org/2000/svg">
{body}
</svg>'''
with open(f"{BASE}/skill-cards.svg", "w") as f:
    f.write(skill_cards)

print("done")
