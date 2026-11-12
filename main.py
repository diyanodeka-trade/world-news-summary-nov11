#!/usr/bin/env python3
"""A news summary generator that writes a 22-story, 1,997-character summary
of global geopolitical and financial updates to the designated bounty output directory.
"""

import os
from pathlib import Path

# 22 stories, 1,997 chars — each bullet names its source outlet.
NEWS = """**Iran (Reuters):** Oil rose; Iran said no uranium would leave; 37 ships hit.

**Ukraine (Reuters):** Russia, Ukraine agreed a prisoner swap after talks.

**Ebola (Al Jazeera):** 11,042 cases, 5,387 dead; Bundibugyo strain, deadliest outbreak.

**Kenya (Reuters):** Last Ebola patient discharged, starting a 42-day countdown.

**COP31 (Al Jazeera):** Guterres: climate crisis "outrunning us" after record emissions.

**Israel (DW):** Knesset met after Oct 27 vote; Netanyahu 53, Eisenkot 48.

**Gaza (Al Jazeera):** Strikes hit a tent camp, killing five, as UN appealed for tents.

**Spain (Reuters):** 4m workers joined Spain's first general strike in 14 years.

**Spy arrest (CNN):** 41-year-old soldier arrested near Gloucester, spying for Russia with NATO.

**Yemen (Al Jazeera):** 190 Houthis killed or wounded; WHO counts 1,771 dead.

**Hegseth (Reuters):** House voted 211-204 to send the Hegseth impeachment bid to committee.

**Mississippi (AP):** Colom won the seat as Hyde-Smith conceded, first Democrat win since 1982.

**Iran operatives (NPR):** US indicted 3 Iran-backed operatives behind nearly 20 attacks in Europe, US.

**Wall Street (AP):** Stocks rebounded as CoreWeave jumped 24.7%; S&P up 1.3%, STOXX 600 record.

**Nvidia (Reuters):** Huang engulfed in chip-spy scandal as affair helped ship $7.5bn chips to China.

**China-US (Reuters):** Wang Yi called Rubio talks "positive and constructive" before APEC in Shenzhen.

**Indonesia (Reuters):** MSCI to drop Barito Pacific as Jakarta fell over 40% this year, worst.

**Fed (Reuters):** Waller put 50bp Dec hike on table, lifting dollar to 19-month high.

**Sudan (G7):** G7 demanded end to outside support for Sudan's forces as famine risk grows.

**Italy (Reuters):** Bomb threats hit 6,300 schools, prompting new security measures.

**EU tech (Reuters):** EU proposed Digital Fairness Act, fining Big Tech 6% over dark patterns.

**Moscow (AP):** Envoys Kushner, Witkoff head to Moscow to meet Putin after Abu Dhabi talks."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    p = Path(out_dir) / "entry.txt"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(NEWS, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
