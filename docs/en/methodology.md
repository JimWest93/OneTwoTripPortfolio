[RU](../ru/methodology.md) · [Language selection](../../README.md)

# How to read the portfolio metrics

This portfolio describes my experience through tasks and engineering decisions. Statistics provide context; the substance of the work is explained in the [cases](cases/index.md) and [practical examples](archive/index.md).

## Period and counting units

The analysis covers **December 22, 2021–September 28, 2026**. The start is the first identified authored change, not a verified employment date. The first and last years are partial and marked on the charts.

| Metric | What is counted | Interpretation |
| --- | --- | --- |
| 4,046 non-merge commits | Unique authored change records in the available Git history | One outcome may involve multiple commits, backports or fixes |
| 831 work items | Unique tasks matched to my code changes and checked against the work history | Includes different task states; not a count of released features |
| 342 merged PRs | Authored changes accepted through pull requests in available history since November 2024 | A shorter period than the full work history; PRs and commits are not added together |
| 788 commits touching tests | Changes affecting unit, snapshot or UI tests, or their resources | Includes additions, fixes and removals; not code coverage |
| 84 catalog examples | Selected scenarios from 21 case studies | Examples overlap and introduce the experience rather than count features |

## How the charts work

A task belongs to the year of its first authored code change, even if work continued later. Each identifier was counted once in the underlying analysis. Ambiguous matches were checked separately; one unverified record was excluded from the total of 831.

Domains and types of work were classified for this portfolio based on task content. Each task has one category on the relevant chart. Cases are organized differently: eSIM payment may illustrate product development, payment integration and automated checks at the same time.

Change counts do not measure task difficulty, working hours or developer effectiveness. Gaps in Git do not mean no work happened: requirements analysis, decision discussions and diagnosis do not always produce commits.

## Basis of the experience descriptions

Preparation cross-checked authored changes, tasks, reviews, technical documentation and current module structure. Historical task assignment alone is not treated as proof of personal implementation. The reader-facing version uses self-contained descriptions without internal identifiers or corporate-system links.

The architecture, design and overall product were created by the team. The technology matrix covers tools in areas I contributed to; a library's presence does not mean I first introduced it into the app.

Professional growth is described through expanding tasks and engineering practices. Formal promotions, management positions and business results are not claimed without additional evidence. Some infrastructure solutions involved substantial AI assistance; the relevant cases explain my role and verification approach.

## Images and reproducibility

The gallery contains unchanged snapshot-test baselines using prepared data. Captions explain the UI state and source type. Test amounts and masked card numbers are fixtures. The images show product areas; the case text defines my contribution.

The `data/` directory holds case text and aggregates sufficient to rebuild the portfolio. `build_charts.py` reproduces charts; `build_portfolio.py` builds documents and the website. `validate.py` checks totals, section links, language parity and the absence of private links and identifiers in reader-facing materials.
