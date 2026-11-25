# The Funniest One-Line Resignation Letter

[![make.fun](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/freysiatiara/resignation-line-20261125/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/freysiatiara/resignation-line-20261125/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

Entry for the [make.fun bounty](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947): the one-line resignation letter of a cron job that has fired every minute since March.

## The line

> I resign effective immediately — the first thing here to run on schedule since March.

85 characters, one line, no trailing newline.

## How it works

`main.py` (Python stdlib only) writes the line to `/output/entry.txt` with
plain `open`/`write` and sets mode `0644`. A guard refuses to write if the
line is empty, longer than 140 characters, or spans more than one line.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
