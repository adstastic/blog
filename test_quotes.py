"""Self-check for highlight filtering. Run: uv run test_quotes.py"""

from fetch_and_generate_quotes import HighlightItem, is_real_highlight


def h(text):
    return HighlightItem(id=1, text=text)


def test_placeholder_is_not_a_highlight():
    # Snipd sends this literal string instead of the snippet. 14 Readwise
    # sources contain nothing else, which is how 8 posts shipped with a body
    # that read only "> 1min Snip".
    assert not is_real_highlight(h("1min Snip"))
    assert not is_real_highlight(h("  1min snip  "))
    assert not is_real_highlight(h("1MIN SNIP"))


def test_blank_is_not_a_highlight():
    # Whitespace-only highlights produced bare "> " lines and stray empty
    # blockquote paragraphs in derren-brown.md and remarks-on-ai-from-nz.md.
    assert not is_real_highlight(h(""))
    assert not is_real_highlight(h("   \n  "))
    # None is not tested: text is a required str, so Pydantic rejects it at the
    # API boundary before this function is ever reached.


def test_real_text_survives():
    assert is_real_highlight(h("**Garbage Truck**"))
    assert is_real_highlight(h("Rendering the first frame of DOOM took 12 days."))
    # Not over-eager: only the exact placeholder is filtered, not text about it.
    assert is_real_highlight(h("1min Snip was the placeholder we kept seeing"))


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn()
            print(f"ok  {name}")
    print("all checks passed")
