# Angry Judge: The Short Rant Contest

[![make.fun](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/raz-indri/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/raz-indri/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

One short, funny rant about an everyday annoyance, judged by a furious,
permanently unimpressed judge.

## The entry (279 characters)

> Our router needs restarting every 47 minutes, and nobody in this house knows why, including the man we paid $90 to look at it. He stared at the blinking light, said 'huh,' and left. The light is still blinking. It blinks in Morse code for help and I am starting to understand it.

## Output contract

`main.py` writes exactly this text to `<output_dir>/entry.txt`, where the
output directory comes from the `OUTPUT_DIR` environment variable, then
`MAKEFUN_OUTPUT_DIR`, then the default `/output`. The text is validated
before writing: UTF-8, 1–400 characters, not whitespace only, no stray
control characters.

## How the entry was chosen

Seven original drafts were written (printer, self-checkout, "circling back",
a meta rant addressed to the judge, bus, router, reply-all) and duel-tested
pairwise in both orders against the judge's criteria (real rant about a
concrete everyday annoyance, actually funny, specific, economical, fresh).
The router rant won all 6 of its duels; the bus rant was runner-up with 5.

## Run

```sh
python3 main.py
```
