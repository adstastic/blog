"""Record intrinsic dimensions of static images so the image render hook can
emit width/height and reserve space, which lazy loading otherwise costs in CLS.
Re-run after adding images:  uv run scripts/image-dims.py"""
import json, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[1] if "scripts" in __file__ else pathlib.Path(".")
assets = ROOT / "static" / "assets"
out = {}
for f in sorted(assets.rglob("*")):
    if f.suffix.lower() not in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
        continue
    r = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(f)],
                       capture_output=True, text=True)
    w = h = None
    for line in r.stdout.splitlines():
        if "pixelWidth:" in line:  w = int(line.split()[-1])
        if "pixelHeight:" in line: h = int(line.split()[-1])
    if w and h:
        out["/assets/" + str(f.relative_to(assets))] = {"w": w, "h": h}
dest = ROOT / "data" / "imagedims.json"
dest.write_text(json.dumps(out, indent=0, sort_keys=True, ensure_ascii=False))
print(f"recorded {len(out)} images -> {dest}")
