"""Write one fixed short poem about agency: the power to ask and to be given.

The poem: at breakfast a child asks, "Can I call you Mum?" The spoon stops
halfway to her mouth. The answer is yes. She says the word again, just to
hear it fit — Mum. Mum. It fit.

Why this poem: of 10 new v2 candidates written and scored in-session against
the judge's five criteria in order, it beat v1's "the milk" head-to-head on
feeling, insight and freshness. The ask and the yes are both explicit, the
word itself is the power handed over, and belonging turns out to be a name
you are allowed to use. Full scoring:
~/workspace/makefun/poem-permission-01-candidates-v2.md

Deterministic: the same poem is written on every run. Standard library
only, no network.
"""

from pathlib import Path

POEM = (
    "At breakfast she asked,\n"
    "Can I call you Mum?\n"
    "The spoon stopped\n"
    "halfway to her mouth.\n"
    "I said yes.\n"
    "She said it again,\n"
    "just to hear it fit.\n"
    "Mum. Mum.\n"
    "It fit."
)
# One fixed poem, hard-coded below: the brief asks for one poem, the same
# every run, so the program never improvises or reads anything at runtime.
# Newlines inside POEM are the poem's line breaks; there is no trailing
# newline, so the file holds exactly the 153 characters of the poem.


OUTPUT_FILE = Path("/output/entry.txt")  # the kit's single required output


def main() -> None:
    # Self-check the gate before writing: the entry must be 1-280 characters,
    # UTF-8, and not only white space. Failing here is better than shipping
    # an invalid entry.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise ValueError("poem must be 1-280 characters, not only white space")
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
