"""Round 2.1 — natural, true-to-life photography (the realistic default). -> ./images/ *-nat.png"""
import os, time
from pathlib import Path
from dotenv import load_dotenv
IMG = Path(__file__).parent / "images"; IMG.mkdir(parents=True, exist_ok=True)
load_dotenv(Path("/Users/aanandmadhav/projects/Brain/utilities/.env"))
from google import genai
from google.genai import types
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = "imagen-4.0-generate-001"

JOBS = [
 ("nat-ballet","4:3","Authentic documentary photograph, young ballet students at the barre in a bright naturally lit dance studio with large windows and a wooden floor, candid mid-class moment, true-to-life natural colour, soft daylight, warm and real, minimal retouching, no text."),
 ("nat-music","3:4","Authentic documentary photograph, a child taking a piano lesson beside a teacher in a bright room with soft natural window light, candid and warm, true-to-life natural colour, real and unposed, no text."),
 ("nat-taekwondo","3:4","Authentic documentary photograph, children in white taekwondo uniforms practising in a bright naturally lit studio, candid action moment, true-to-life natural colour, energetic and real, no text."),
 ("nat-art","3:4","Authentic documentary photograph, children painting at easels in a bright colourful art room with natural light, candid and joyful, true-to-life natural colour, real and unposed, no text."),
 ("nat-drama","3:4","Authentic documentary photograph, a children's drama class in a bright studio doing an expressive group activity with natural daylight, candid, true-to-life natural colour, warm and real, no text."),
 ("nat-studio","4:3","Authentic interior architectural photograph of a bright empty dance studio with a ballet barre, large wall mirrors, wooden floor and big windows with soft daylight, clean welcoming and real, true-to-life natural colour, no text."),
]
ok, fail = [], []
for name, ar, prompt in JOBS:
    out = IMG / f"{name}-nat.png"
    try:
        print(f"[gen] {name} ...", flush=True)
        resp = client.models.generate_images(model=MODEL, prompt=prompt,
            config=types.GenerateImagesConfig(number_of_images=1, aspect_ratio=ar))
        imgs = getattr(resp, "generated_images", None) or []
        if not imgs: print(f"   NO IMAGE {name}"); fail.append(name); continue
        imgs[0].image.save(str(out)); print(f"   saved {out.name}"); ok.append(name)
    except Exception as e:
        print(f"   ERROR {name}: {e}"); fail.append(name)
    time.sleep(1)
print("\nOK:", ", ".join(ok) or "none"); print("FAIL:", ", ".join(fail) or "none")
