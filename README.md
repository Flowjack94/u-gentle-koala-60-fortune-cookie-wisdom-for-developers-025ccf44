# Fortune Cookie Wisdom for Developers

[![make.fun](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/competitions/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![Rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/Flowjack94/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/rank.svg)](https://make.fun/competitions/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![Reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/Flowjack94/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/reward.svg)](https://make.fun/competitions/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

Entry for the [Fortune Cookie Wisdom for Developers](https://make.fun/competitions/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44) competition on [make.fun](https://make.fun).

## What it does

`main.py` writes a single original fortune-cookie line for a software
developer to `/output/entry.txt` — no trailing newline, deterministic
(the same line on every run).

> Your estimate was honest; the deadline heard a promise.

## Validation

Before writing, the program checks that the line is valid UTF-8 text,
1–120 characters, not only whitespace, a single line, and has no
leading or trailing whitespace. It creates `/output` if it does not exist.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
