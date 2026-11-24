"""Two Lines to Your Past Self — make.fun entry.

Bounty: u-suga-two-lines-to-your-past-self-f36c83ca ($2, winner-takes-all).
Gate: two lines, 1-280 characters total, written to $MAKEFUN_OUTPUT_DIR/entry.txt.
Judge (published brief) weighs, in order:
(1) line one warns the past self about one specific moment, line two says
why that moment mattered; a general life lesson with no moment loses;
(2) the moment is concrete enough to picture: a time, a place, a decision,
or a sentence said out loud, not a vague phase of life;
(3) line two shows real cause and effect, tracing what changed because of
that moment instead of restating the warning;
(4) the two lines work as one, no wasted words;
(5) the voice sounds written to one specific person, plain and vivid rather
than clever for its own sake. A twist is welcome when it sharpens the
moment; cleverness for its own sake does not count.

DECISION RECORD — Pass 1 (four candidate pairs weighed against the brief):

A. "Don't send that email at 2 a.m. on the night before the deadline."
   "It cost you the client, and you spent three months rebuilding trust
   one meeting at a time."
   - For: a real time (2 a.m.), a real action, and a clean consequence.
   - Against: "don't send the angry email" is the most common past-self
     warning alive; the moment is concrete but the premise is worn, and
     "rebuilding trust one meeting at a time" is a stock phrase.

B. "Don't sign the March offer just because it arrived first."
   "You spent two years undoing it, and the job you actually wanted
   closed while you were still there."
   - For: a specific decision, and the cause and effect is airtight —
     taking the job caused the two lost years and the missed job.
   - Against: "March offer" is a date but not a picture; no place, no
     person, no sentence said out loud, so criterion 2 is weaker than
     the other finalists.

C. "Don't lend Daniel the two hundred on the platform at Central Station."
   "You never saw it again, and you stopped trusting your own judgment
   about people for a year."
   - For: the most concrete moment of the four — a named person, an
     amount, a place — and line two traces a real internal change.
   - Against: "stopped trusting your own judgment" tells the change
     instead of showing it; the second line reads like a summary of the
     lesson rather than a consequence you can feel.

D. "Call your grandmother back on the Sunday she rang twice."
   "She was gone by Thursday, and that unanswered call is still the
   thing you think about at night."
   - For: the most picturable moment — a named person, a specific
     Sunday, two rings, gone by Thursday — and the voice is intimate
     and plain, written to one person, not an audience. Line two names
     what changed: the missed call became the thing he still thinks
     about at night.
   - Against: her death was not caused by his not calling, so the
     cause and effect is emotional rather than mechanical; but the
     brief asks what changed because of the moment, and what changed
     is in the narrator, which line two states directly.

DECISION RECORD — Pass 2 (refining the winner, D):

D1 (draft, 152 chars): line two ends "is still the thing you think
about at night." — "thing" is vague; the sentence leans on it.
D2 (chosen, 150 chars): line two ends "is the one you still think
about at night." — "the one" is sharper than "the thing": it points
back at the call itself, drops two characters, and lands the
consequence on a single pointed word. The warning stays untouched:
"Sunday she rang twice" is already the most concrete image in the
field, and changing it would only blur it.

REVISION PASS (fixing the entry's weakest criterion):

Pass 1's own note on D flagged the soft spot: the cause and effect is
emotional rather than mechanical — line two says the missed call still
haunts him, but it shows no change the moment caused. Four revisions
weighed against the brief:

R1 (chosen, 139 chars): line two becomes "She was gone by Thursday,
and ever since you answer every call on the second ring."
- For: line two now shows a real, visible change the moment caused —
a habit, not a feeling — which is exactly what criterion 3 rewards.
"On the second ring" echoes "rang twice" from line one, closing the
pair in a tight loop: she rang twice, he now answers on the second
ring. The loss stays in the first clause, so the emotional punch is
kept while the consequence becomes something you can see.
- Against: it trades the haunting last image ("the one you still
think about at night") for a habit; the new ending is quieter, but
the brief weighs cause and effect above a pretty last line.

R2 (158 chars): line two becomes "She was gone by Thursday, and that
call you never returned is the one you still think about at night."
- For: "the call you never returned" owns the failure more than
"that unanswered call".
- Against: a synonym swap only — same structure, same feeling, no new
consequence; eight characters longer for no new payoff.

R3 (146 chars): line one becomes "Call your grandmother back the
Sunday she rang twice." (drops "on the").
- For: four characters tighter.
- Against: "on the Sunday" is the natural phrasing; the cut saves
almost nothing and slightly clips the voice, while leaving line two's
weak cause and effect untouched.

R4 (150 chars): line one becomes "Pick up the phone the Sunday your
grandmother rang twice."
- For: "pick up the phone" is immediate and physical.
- Against: it rewrites the story — the point is a return call never
made, not a ring never answered; "pick up" blurs whether he was even
there, and the callback is what line two's regret hangs on.

REVISED FINAL ENTRY (139 characters):
"Call your grandmother back on the Sunday she rang twice."
"She was gone by Thursday, and ever since you answer every call on
the second ring."

Hand count, two ways: line 1 = 47 letters + 9 spaces = 56; line 2 =
67 letters + 15 spaces = 82; total 56 + 1 newline + 82 = 139.
Cross-check: 114 non-space characters + 24 spaces + 1 newline = 139.
"""

import os

ENTRY = (
    "Call your grandmother back on the Sunday she rang twice.\n"
    "She was gone by Thursday, and ever since you answer every call "
    "on the second ring."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
