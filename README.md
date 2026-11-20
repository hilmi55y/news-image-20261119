[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/hilmi55y/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/hilmi55y/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# The World in One Day — Thursday 19 November 2026

A newspaper front page that sums up the world's news of Thursday
19 November 2026: the UN court's genocide ruling on Myanmar, the first
Trump–Xi–Putin summit in Shenzhen, Anthropic's record $81.3bn IPO, the
day's market sell-off, COP31 in Antalya, and 40 briefs from every region
and field — plus a world map of where the day happened and the day's
numbers.

Referral: https://make.fun/r/ky8x585w

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This copies `entry.png` (1024×1024 PNG, under 1 MiB) to `out/entry.png`.
The program is Python 3.13 standard library only and deterministic:
every run writes the same bytes.

## What the image shows

- **Masthead** naming the day: Thursday 19 November 2026.
- **Hero:** a world map marking Shenzhen, The Hague, New York, Gaza,
  Antalya and Dhaka, beside the three biggest stories of the day.
- **Market ticker:** the close of 19 November — Dow −1,100, S&P 500 −2.0%
  (sixth straight loss), Nasdaq −2.3%, gold, Bitcoin, Brent and the VIX.
- **40 numbered briefs** across politics, markets, tech, science, sport,
  culture and climate, from every region.
- **By the numbers:** $81.3bn, 879,000 chips, $190.4m, 109-0, 4/26, 133, 6.

Every story on the page happened or was first reported on 19 November
2026; the full list with sources is in `STORIES.md` in the build folder.
Nothing on the page is invented, and no figure is used without a source.

Built for the [make.fun](https://make.fun) bounty
[news-image-20261119](https://make.fun/bounty/news-image-20261119).
