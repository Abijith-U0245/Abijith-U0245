import os
import urllib.request
import base64

BASE = os.path.dirname(os.path.abspath(__file__))
NAV_DIR = os.path.join(BASE, "nav")
HEADERS_DIR = os.path.join(BASE, "headers")

os.makedirs(NAV_DIR, exist_ok=True)
os.makedirs(HEADERS_DIR, exist_ok=True)

# Color Palette
NAVY = "#0F172A"
INDIGO_DARK = "#1E1B4B"
INDIGO = "#312E81"
ACCENT = "#4F46E5"
ACCENT_LIGHT = "#818CF8"
LILAC = "#C7D2FE"
SLATE = "#94A3B8"
SLATE_LIGHT = "#E2E8F0"
WHITE = "#FFFFFF"

# Download GitHub DP and encode as Base64
avatar_url = "https://github.com/Abijith-U0245.png"
avatar_b64 = ""
try:
    req = urllib.request.Request(avatar_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        img_bytes = resp.read()
        avatar_b64 = base64.b64encode(img_bytes).decode('utf-8')
        print(f"Downloaded profile DP ({len(img_bytes)} bytes)")
except Exception as e:
    print(f"Failed to fetch profile DP: {e}")

# 1. GENERATE NAV PILL SVGS
nav_items = [
    ("about", "About", "👤", 115),
    ("experience", "Experience", "💼", 145),
    ("now-building", "Now Building", "🚀", 160),
    ("stack", "Tech Stack", "⚡", 140),
    ("projects", "Projects", "💻", 130),
    ("activity", "Activity", "📊", 130),
    ("achievements", "Achievements", "🏆", 165),
    ("connect", "Connect", "📬", 125),
]

def generate_nav_pill(key, label, icon, width):
    return f'''<svg width="{width}" height="38" viewBox="0 0 {width} 38" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg-nav-{key}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E1B4B"/>
      <stop offset="100%" stop-color="#312E81"/>
    </linearGradient>
    <linearGradient id="border-nav-{key}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#6366F1"/>
      <stop offset="100%" stop-color="#A5B4FC"/>
    </linearGradient>
  </defs>
  <rect x="1" y="1" width="{width-2}" height="36" rx="18" fill="url(#bg-nav-{key})" stroke="url(#border-nav-{key})" stroke-width="1.5"/>
  <circle cx="20" cy="19" r="4" fill="#818CF8"/>
  <text x="32" y="24" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif" font-size="13" font-weight="600" fill="#F8FAFC">{label}</text>
</svg>'''

for key, label, icon, width in nav_items:
    with open(os.path.join(NAV_DIR, f"{key}.svg"), "w", encoding="utf-8") as f:
        f.write(generate_nav_pill(key, label, icon, width))

# 2. GENERATE SECTION HEADERS SVGS
headers_data = [
    ("about", "01", "About Me"),
    ("experience", "02", "Work Experience"),
    ("now-building", "03", "Currently Building"),
    ("stack", "04", "Tech Stack"),
    ("projects", "05", "Featured Projects"),
    ("activity", "06", "GitHub Activity"),
    ("achievements", "07", "Achievements"),
    ("connect", "08", "Connect with Me"),
]

def generate_header_svg(key, num, title):
    return f'''<svg width="920" height="68" viewBox="0 0 920 68" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg-grad-{key}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="40%" stop-color="#1E1B4B"/>
      <stop offset="100%" stop-color="#312E81"/>
    </linearGradient>
    <linearGradient id="badge-grad-{key}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4F46E5"/>
      <stop offset="100%" stop-color="#818CF8"/>
    </linearGradient>
    <linearGradient id="line-grad-{key}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#6366F1"/>
      <stop offset="50%" stop-color="#A5B4FC" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#0F172A" stop-opacity="0"/>
    </linearGradient>
  </defs>
  
  <rect width="920" height="68" rx="14" fill="url(#bg-grad-{key})" stroke="#3730A3" stroke-width="1.2"/>
  <rect x="16" y="16" width="46" height="36" rx="10" fill="url(#badge-grad-{key})"/>
  <text x="39" y="40" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif" font-size="16" font-weight="800" fill="#FFFFFF" text-anchor="middle">{num}</text>
  <text x="78" y="42" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif" font-size="22" font-weight="700" fill="#F8FAFC">{title}</text>
  <rect x="78" y="52" width="780" height="2" rx="1" fill="url(#line-grad-{key})"/>
  <circle cx="875" cy="34" r="5" fill="#818CF8"/>
  <circle cx="890" cy="34" r="3" fill="#6366F1" opacity="0.6"/>
</svg>'''

for key, num, title in headers_data:
    with open(os.path.join(HEADERS_DIR, f"{key}.svg"), "w", encoding="utf-8") as f:
        f.write(generate_header_svg(key, num, title))

# 3. DIVIDER SVG
divider = f'''<svg width="920" height="4" viewBox="0 0 920 4" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="d-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0F172A" stop-opacity="0"/>
      <stop offset="25%" stop-color="#4F46E5"/>
      <stop offset="50%" stop-color="#818CF8"/>
      <stop offset="75%" stop-color="#4F46E5"/>
      <stop offset="100%" stop-color="#0F172A" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect width="920" height="4" rx="2" fill="url(#d-grad)"/>
</svg>'''

with open(os.path.join(BASE, "divider.svg"), "w", encoding="utf-8") as f:
    f.write(divider)

# 4. HERO BANNER SVG
img_tag = f'<image href="data:image/png;base64,{avatar_b64}" x="705" y="55" width="150" height="150" clip-path="url(#avatar-clip)"/>' if avatar_b64 else '<image href="https://github.com/Abijith-U0245.png" x="705" y="55" width="150" height="150" clip-path="url(#avatar-clip)"/>'

hero = f'''<svg width="920" height="260" viewBox="0 0 920 260" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <linearGradient id="bg-hero" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{NAVY}"/>
      <stop offset="50%" stop-color="{INDIGO_DARK}"/>
      <stop offset="100%" stop-color="{INDIGO}"/>
    </linearGradient>
    <radialGradient id="glow-hero" cx="75%" cy="30%" r="65%">
      <stop offset="0%" stop-color="{ACCENT}" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="{ACCENT}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="avatar-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{ACCENT_LIGHT}"/>
      <stop offset="100%" stop-color="{ACCENT}"/>
    </linearGradient>
    <clipPath id="avatar-clip">
      <circle cx="780" cy="130" r="70"/>
    </clipPath>
  </defs>

  <rect width="920" height="260" rx="16" fill="url(#bg-hero)"/>
  <rect width="920" height="260" rx="16" fill="url(#glow-hero)"/>
  
  <text x="45" y="95" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="44" font-weight="800" fill="{WHITE}">Abijith U</text>
  <text x="47" y="132" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="18" font-weight="600" fill="{LILAC}">Edge AI Engineer · Full-Stack Developer · IoT Builder</text>
  <text x="47" y="168" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="14" fill="{SLATE}">CSE @ Chennai Institute of Technology · Class of 2028</text>
  
  <g font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="13" fill="{SLATE}">
    <text x="47" y="205">Chennai, India</text>
    <text x="165" y="205">·</text>
    <text x="180" y="205">Available now</text>
    <text x="305" y="205">·</text>
    <text x="320" y="205">GDG On Campus Secretary, CIT</text>
  </g>

  <!-- Glowing Outer Rings -->
  <circle cx="780" cy="130" r="78" fill="none" stroke="#6366F1" stroke-width="1.5" opacity="0.5"/>
  <circle cx="780" cy="130" r="73" fill="none" stroke="url(#avatar-border)" stroke-width="4"/>
  
  <!-- Avatar Image -->
  {img_tag}
</svg>'''

with open(os.path.join(BASE, "hero-banner.svg"), "w", encoding="utf-8") as f:
    f.write(hero)

# 5. STUNNING HIGH-CONTRAST SKILL CARDS SVG
def skill_card_svg(x, title, items, level):
    lines = "".join(
        f'<text x="{x+20}" y="{65+20*i}" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="13" font-weight="500" fill="{SLATE_LIGHT}">• {it}</text>'
        for i, it in enumerate(items)
    )
    bar_w = int(175 * level / 100)
    return f'''
  <!-- Card Base -->
  <rect x="{x}" y="0" width="215" height="170" rx="14" fill="url(#card-bg)" stroke="#3730A3" stroke-width="1.5"/>
  
  <!-- Category Header -->
  <rect x="{x+15}" y="15" width="185" height="28" rx="8" fill="url(#badge-bg)"/>
  <text x="{x+25}" y="34" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="14" font-weight="700" fill="#FFFFFF">{title}</text>
  
  <!-- Items -->
  {lines}
  
  <!-- Progress Bar -->
  <rect x="{x+20}" y="150" width="175" height="6" rx="3" fill="#0F172A"/>
  <rect x="{x+20}" y="150" width="{bar_w}" height="6" rx="3" fill="url(#bar-grad)"/>
'''

cards_data = [
    (10, "Full-Stack", ["React / Next.js", "FastAPI / Node.js", "MongoDB / MySQL", "Tailwind CSS"], 90),
    (240, "Edge AI & CV", ["YOLO11n / ONNX", "OpenCV / PyTorch", "Axelera Metis", "Camera Calibration"], 85),
    (470, "IoT Systems", ["ESP32 / Arduino", "MQTT / InfluxDB", "Raspberry Pi", "Redis Caching"], 88),
    (700, "Applied ML", ["XGBoost / Prophet", "Isolation Forest", "Scikit-learn", "LangChain / RAG"], 92),
]

cards_body = "".join(skill_card_svg(x, t, it, lv) for x, t, it, lv in cards_data)

skill_cards = f'''<svg width="920" height="175" viewBox="0 0 920 175" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E1B4B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <linearGradient id="badge-bg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4F46E5"/>
      <stop offset="100%" stop-color="#6366F1"/>
    </linearGradient>
    <linearGradient id="bar-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#6366F1"/>
      <stop offset="100%" stop-color="#A5B4FC"/>
    </linearGradient>
  </defs>
  {cards_body}
</svg>'''

with open(os.path.join(BASE, "skill-cards.svg"), "w", encoding="utf-8") as f:
    f.write(skill_cards)

print("Generated stunning high-contrast skill-cards.svg!")
