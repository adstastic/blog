#!/usr/bin/env python3
"""Assert every legal fg/bg token pair in main.css clears WCAG AA (4.5:1).

Run before committing CSS:  uv run contrast.py

Role tokens reference palette tokens (--text: var(--base02)), so one level of
var() indirection is resolved. --code-dim is deliberately excluded: inside a
code block dimness encodes "subordinate", and the text is not prose.
"""

import re
import sys
import pathlib

CSS = pathlib.Path(__file__).parent / "static/css/main.css"
FG = ["text", "text-2", "link", "link-hover"]
BG = ["bg", "bg-panel"]
MIN = 4.5


def ratio(a, b):
    def lum(h):
        ch = [int(h.lstrip("#")[i : i + 2], 16) / 255 for i in (0, 2, 4)]
        ch = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in ch]
        return 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2]

    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def declarations(src, selector):
    m = re.search(re.escape(selector) + r"\s*\{(.*?)\n\}", src, re.S)
    assert m, f"no {selector!r} block in {CSS}"
    return dict(re.findall(r"--([\w-]+):\s*([^;]+);", m.group(1)))


def resolve(tokens, palette, name):
    """Follow at most one var() hop to a literal hex."""
    raw = tokens[name].strip()
    if raw.startswith("#"):
        return raw
    ref = re.fullmatch(r"var\(--([\w-]+)\)", raw)
    assert ref, f"--{name} is neither a hex nor a single var(): {raw!r}"
    target = ref.group(1)
    assert target in palette, f"--{name} points at unknown --{target}"
    return palette[target].strip()


def main():
    src = CSS.read_text()
    palette = declarations(src, ":root")
    dark_over = declarations(src, ".dark, .dark-theme")
    fail = []
    report = []

    for scheme, tokens in (("light", palette), ("dark", {**palette, **dark_over})):
        missing = [k for k in FG + BG if k not in tokens]
        assert not missing, f"{scheme}: missing tokens {missing}"
        hexes = {k: resolve(tokens, palette, k) for k in FG + BG}
        for fg in FG:
            for bg in BG:
                r = ratio(hexes[fg], hexes[bg])
                if r < MIN:
                    fail.append(
                        f"{scheme}: --{fg} {hexes[fg]} on --{bg} {hexes[bg]} = {r:.2f} (need {MIN})"
                    )
        report.append(
            f"  {scheme:5s} "
            + "  ".join(f"{fg}/{bg} {ratio(hexes[fg], hexes[bg]):.2f}" for fg in FG for bg in BG)
        )

    # both schemes must declare the same role names, or dark mode silently drifts
    roles = set(FG + BG) | {"rule", "focus", "code-dim"}
    only_dark = sorted(set(dark_over) - roles - {"color-scheme"})
    if only_dark:
        fail.append(f"roles declared only in dark: {only_dark}")
    missing_dark = sorted(r for r in FG + BG + ["rule", "code-dim"] if r not in dark_over)
    if missing_dark:
        fail.append(f"roles not overridden for dark: {missing_dark}")

    if fail:
        print("\n".join(fail))
        return 1

    print("\n".join(report))
    print(f"contrast OK: all {len(FG) * len(BG) * 2} token pairs >= {MIN}:1")
    return 0


if __name__ == "__main__":
    sys.exit(main())
