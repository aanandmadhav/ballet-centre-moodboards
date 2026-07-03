"""
Ballet Centre mood board asset generation (Imagen 4.0).
Generates imagery for two directions into ./images/.
Re-run safe: files are versioned by the VERSION tag below.
"""
import os, sys, time
from pathlib import Path
from dotenv import load_dotenv

VERSION = "v1"
HERE = Path(__file__).parent
IMG = HERE / "images"
IMG.mkdir(parents=True, exist_ok=True)

# Load key from Brain utilities .env
load_dotenv(Path("/Users/aanandmadhav/projects/Brain/utilities/.env"))

from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = "imagen-4.0-generate-001"

# (name, aspect_ratio, prompt)
JOBS = [
    # ---- Direction A: Timeless Stage (heritage, ivory, editorial, muted) ----
    ("a-hero", "4:3",
     "Fine-art editorial photograph, a single elegant ballerina en pointe in graceful arabesque, "
     "backlit by soft window light, shot in a bright airy studio with cream and ivory tones and a dusty "
     "lavender wash, lots of negative space, muted film photography, timeless and premium, no text."),
    ("a-shoes", "3:4",
     "Still life, a pair of satin ballet pointe shoes resting on an aged parquet studio floor, warm soft "
     "window light, cream and ivory palette with a faint violet cast, elegant analog film photography, "
     "shallow depth of field, refined and nostalgic, no text."),
    ("a-detail", "1:1",
     "Intimate close-up still life, a violin resting on a velvet upholstered theatre seat beside a folded "
     "programme, warm golden light, cream and deep plum tones, elegant editorial film photography, "
     "premium performing arts mood, no text."),

    # ---- Direction B: The Programme (bold, saturated colour per act) ----
    ("b-hero", "16:9",
     "Bold graphic poster art, dynamic silhouette of a dancer leaping mid-air captured with energetic "
     "motion blur, set against a striking split colour-field background transitioning from hot magenta "
     "to cobalt blue, high contrast, confident modern art direction, gallery exhibition poster, no text."),
    ("b-ballet", "3:4",
     "Bold studio poster photograph, a dancer in a dramatic ballet pose rendered as an energetic silhouette "
     "with slight motion blur, against a solid saturated rose-magenta seamless backdrop (#E23A6D), "
     "high contrast, graphic and modern, no text."),
    ("b-dance", "3:4",
     "Bold studio poster photograph, a dynamic contemporary street-dance figure mid-movement as an energetic "
     "silhouette with motion streaks, against a solid saturated tangerine-orange seamless backdrop (#E85D0A), "
     "high contrast, graphic and modern, no text."),
    ("b-drama", "3:4",
     "Bold theatrical still life, classic comedy and tragedy drama masks lit by a single hard spotlight, "
     "against a solid saturated crimson-red seamless backdrop (#D12A2A), dramatic shadows, graphic poster "
     "style, high contrast, no text."),
    ("b-music", "3:4",
     "Bold studio poster still life, a violin and scattered sheet music arranged graphically, lit dramatically, "
     "against a solid saturated cobalt-blue seamless backdrop (#2F5DF0), high contrast, modern gallery poster, "
     "no text."),
    ("b-taekwondo", "3:4",
     "Bold studio poster photograph, an energetic silhouette of a martial artist in a taekwondo dobok mid high-kick "
     "with motion blur, against a solid saturated emerald-green seamless backdrop (#0E8F63), high contrast, "
     "graphic and modern, no text."),
    ("b-art", "3:4",
     "Bold overhead still life, an artist's palette with vivid wet paint strokes and brushes arranged graphically, "
     "against a solid saturated violet-purple seamless backdrop (#7B3FF2), high contrast, modern gallery poster, "
     "no text."),
]

ok, fail = [], []
for name, ar, prompt in JOBS:
    out = IMG / f"{name}-{VERSION}.png"
    try:
        print(f"[gen] {name} ({ar}) ...", flush=True)
        resp = client.models.generate_images(
            model=MODEL, prompt=prompt,
            config=types.GenerateImagesConfig(number_of_images=1, aspect_ratio=ar),
        )
        imgs = getattr(resp, "generated_images", None) or []
        if not imgs:
            print(f"   NO IMAGE returned (likely filtered) for {name}", flush=True)
            fail.append(name); continue
        imgs[0].image.save(str(out))
        print(f"   saved {out.name}", flush=True)
        ok.append(name)
    except Exception as e:
        print(f"   ERROR {name}: {e}", flush=True)
        fail.append(name)
    time.sleep(1)

print("\n==== SUMMARY ====")
print("OK  :", ", ".join(ok) or "none")
print("FAIL:", ", ".join(fail) or "none")
