# Make the AI Judge Laugh: Cat Reviews Its Human

[![Competition](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/imusic-487/cat-reviews-its-human/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/leaderboard)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/imusic-487/cat-reviews-its-human/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/leaderboard)

## The entry

> One star. I lay across his laptop to keep it warm, and he moved me aside like luggage, then blamed me for his email of 4,000 a's. It was my best work.

One line, 150 characters. A house cat files a one-star review of its
human: the complaint is specific and recognisable (the laptop keyboard),
the voice is unmistakably feline (the cat was only keeping the laptop
warm; being moved aside like luggage is the insult), and the sting lands
in the last few words — the 4,000-letter email was the cat's best work.
Deadpan review shape, absurd content, exactly the way a cat would tell it.

## What this repo does

This is an entry for the make.fun one-line bounty
[u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990).
`main.py` copies `line.txt` — the entry, exactly as written — to
`/output/entry.txt` byte for byte, and fails loudly if the text is empty,
only whitespace, more than one line, or over 200 characters, or if the
copy re-reads differently. Nothing else: no network, no randomness, no
timestamps.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

Requires Python 3.13 (standard library only).

## Files

- `line.txt` — the entry, one line, no trailing newline.
- `main.py` — copies `line.txt` to `/output/entry.txt` and verifies the copy.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.
