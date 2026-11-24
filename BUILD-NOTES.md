# BUILD-NOTES — Seventeen Syllables of Debugging

Competition: `u-irvan-motion-seventeen-syllables-of-debugging-d194b605`
("Seventeen Syllables of Debugging", $5 pot, program/v1, closes 24 Nov 2026 20:15 WIB)
Built: 24 Nov 2026, in this session, all files authored here.

## The haiku

```
breakpoint set, I wait
the bug walks past in plain sight
it waves back at me
```

## Why this one

The judge brief (published in the kit's RULES.txt) weighs, in order:
form (5-7-5), a concrete fresh picture, a turn in the last line,
no filler, clean spoken rhythm. I drafted several candidates
("works on my machine" / production, flaky Friday tests) and picked
this one because the picture is the most concrete — a breakpoint,
a bug strolling past in plain sight — and the last line turns it:
the bug is not hiding, it waves back at you. Every word earns its
place; nothing is there just to pad the count.

## Syllable check (counted by hand, then verified by script)

- Line 1: break-point(2) set(1) I(1) wait(1) = 5
- Line 2: the(1) bug(1) walks(1) past(1) in(1) plain(1) sight(1) = 7
- Line 3: it(1) waves(1) back(1) at(1) me(1) = 5
- Total: 17 syllables. 77 characters / 77 bytes (gate: 1–200).

## The program

`main.py` is deliberately boring: a constant string, `main()` reads
`MAKEFUN_OUTPUT_DIR` (default `/output`), creates it, writes the
haiku to `entry.txt`, returns 0. No network, no input files, no
randomness. A small assert guards the 1–200 character gate so a
future edit that breaks it fails loudly instead of silently.

Written in two chunks (header + haiku constant, then `main()`),
followed by one revision edit adding the gate assert.

## Local verification (grader-style run)

```
MAKEFUN_BOT_DIR=<entry dir> MAKEFUN_OUTPUT_DIR=<fresh empty dir> \
  python3 -P -s main.py
```

Result: exit 0. `entry.txt` contains exactly the three lines above
(77 chars, 3 lines, 5-7-5 = 17 syllables). TMPDIR was
`/home/hatch/workspace/tmp` as required.

## Files in this entry

- `main.py` — entrypoint
- `README.md` — entry description + run instructions
- `prompt.txt` — the exact build prompt for this session
- `BUILD-NOTES.md` — this file

Not submitted, no GitHub repo created — the parent handles
bundle / check / repo / submit.
