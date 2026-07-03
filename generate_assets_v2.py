"""Round 2 imagery — dominant-purple boards. Outputs to ./images/ with v2 tag."""
import os, time
from pathlib import Path
from dotenv import load_dotenv

VERSION = "v2"
IMG = Path(__file__).parent / "images"
IMG.mkdir(parents=True, exist_ok=True)
load_dotenv(Path("/Users/aanandmadhav/projects/Brain/utilities/.env"))
from google import genai
from google.genai import types
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = "imagen-4.0-generate-001"

JOBS = [
    # Board 3 — Dominant Purple (copy.ai #693EE0 + later.com bold/playful)
    ("c-hero", "4:3",
     "Bold high-energy editorial advertising photograph, a joyful young dancer leaping mid-air with arms "
     "thrown up and a big smile, against a solid vivid electric-violet background (#693EE0), bright even "
     "studio light, playful modern and premium, lots of clean negative space, high contrast, no text."),
    ("c-life", "3:4",
     "Bright candid advertising photograph, a happy child at a performing-arts class mid-activity, warm "
     "violet and purple colour grade, soft studio lighting, energetic joyful and modern, no text."),

    # Board 4 — Purple Spectrum (one shade of purple per class)
    ("d-hero", "16:9",
     "Elegant graphic poster art, a dancer captured as a smooth silhouette in a graceful leap, against a "
     "seamless purple gradient background flowing from fuchsia through violet to deep indigo, high contrast, "
     "modern gallery poster, refined, no text."),
    ("d-ballet", "3:4",
     "Bold studio poster photograph, a ballet dancer as an energetic silhouette in an elegant pose with slight "
     "motion blur, against a solid saturated fuchsia-pink seamless backdrop (#C724B1), high contrast, graphic, no text."),
    ("d-dance", "3:4",
     "Bold studio poster photograph, a contemporary dancer as a dynamic silhouette mid-movement with motion "
     "streaks, against a solid saturated violet seamless backdrop (#7C3AED), high contrast, graphic, no text."),
    ("d-drama", "3:4",
     "Bold theatrical still life, comedy and tragedy drama masks lit by a hard spotlight, against a solid "
     "saturated deep-plum seamless backdrop (#5B21B6), dramatic shadows, graphic poster style, no text."),
    ("d-music", "3:4",
     "Bold studio poster still life, a violin with scattered sheet music arranged graphically and dramatically "
     "lit, against a solid saturated indigo seamless backdrop (#4338CA), high contrast, modern poster, no text."),
    ("d-taekwondo", "3:4",
     "Bold studio poster photograph, an energetic silhouette of a martial artist in a taekwondo dobok mid "
     "high-kick with motion blur, against a solid saturated periwinkle-blue seamless backdrop (#6366F1), "
     "high contrast, graphic, no text."),
    ("d-art", "3:4",
     "Bold overhead still life, an artist palette with vivid wet paint strokes and brushes arranged graphically, "
     "against a solid saturated magenta seamless backdrop (#A21CAF), high contrast, modern poster, no text."),
]

ok, fail = [], []
for name, ar, prompt in JOBS:
    out = IMG / f"{name}-{VERSION}.png"
    try:
        print(f"[gen] {name} ({ar}) ...", flush=True)
        resp = client.models.generate_images(
            model=MODEL, prompt=prompt,
            config=types.GenerateImagesConfig(number_of_images=1, aspect_ratio=ar))
        imgs = getattr(resp, "generated_images", None) or []
        if not imgs:
            print(f"   NO IMAGE (filtered) {name}", flush=True); fail.append(name); continue
        imgs[0].image.save(str(out)); print(f"   saved {out.name}", flush=True); ok.append(name)
    except Exception as e:
        print(f"   ERROR {name}: {e}", flush=True); fail.append(name)
    time.sleep(1)

print("\n==== SUMMARY ====")
print("OK  :", ", ".join(ok) or "none")
print("FAIL:", ", ".join(fail) or "none")
