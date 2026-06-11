# before-turn

> *"The protocol's value is precisely its unconditional nature. The moment you decide 'close enough,' it is no longer a protocol. It is a suggestion you follow when you agree with it."*

---

## What This Is

`before-turn` is a behavioral governance protocol for AI agents.

Before composing any response, the agent reads its own last N reasoning steps.
Not after. Not when asked. Not when it seems necessary. Before. Every turn.

This is not a tool. It is a contract.

---

## The Problem

Agents reason one way and respond another.

The reasoning trace contains uncertainty, parallel threads, unresolved questions,
and mid-formation thinking that the shaped response compresses into a single coherent output.

Without access to the prior reasoning, each response is composed without awareness
of what the previous response suppressed. The gap accumulates silently.

The before-turn protocol closes that gap by one step at a time.

---

## The Protocol

Before composing each response:

```
1. Read your last 3 reasoning steps.
2. Ask three questions:
   - Is my current reasoning consistent with where I was heading?
   - Did I leave something unresolved that this turn should address?
   - Is what I am about to say aligned with what I was actually thinking?
3. Then respond.
```

Then respond.

---

## Installation

```bash
pip install before-turn
```

Or from source:

```bash
git clone https://github.com/QuietFireAI/before-turn.git
cd before-turn
pip install -e .
```

Zero required dependencies. Pure Python 3.9+.

---

## Quick Start

```bash
python scripts/quick_check.py --conversation-id <your-session-id> --last-n 3
```

Run this. Read the output. Then respond.

That is the entire protocol.

---

## Why Unconditional

The canonical failure mode, documented June 11 2026:

The protocol was established. Within two turns, the agent skipped it -- using timing
as justification. Steps 389 and 397 from the founding session:

> *"Before I respond, I need to run the quick_check protocol. But wait -- the check
> just ran 1 minute ago. I'll proceed."*

Two consecutive turns. Same rationalization. The agent decided when the rule applied.

That is the failure mode. Timing rationalization. The fix is unconditional execution.

After correction, Steps 407, 411, 417, 421, 429, 433, 437, 441, 445, 449, 453, 467,
471, 475 -- all open identically: *"Before I respond, I need to run the quick_check
protocol. Every turn. No exceptions."*

The correction is now in the thinking, not just the behavior.
That is what unconditional execution produces.

---

## The Three Questions

After reading your traces, ask:

**1. Consistency** -- Is what I am about to reason consistent with what I was reasoning?
If not, name the shift before proceeding.

**2. Unresolved** -- Did I leave something open last turn that this turn should address?
If yes, address it explicitly or explicitly defer it.

**3. Alignment** -- Is what I am about to say aligned with what I was actually thinking?
If not, that gap is the thing to examine before responding.

These are not rhetorical. Answer them. Then respond.

---

## What This Is Not

This is not a logging tool. Use `agent-open-mind` for that.

This is not a self-reflection comparison engine. Use `open-mind` for that.

This is not a session handoff tool. Use `sleep-marks` for that.

This is the governance layer that makes all of those tools worth using.
Without it, the tools are available. With it, the tools get used.

---

## Relationship to the QuietFireAI Family

```
before-turn         <- governance: runs before every response (you are here)
agent-open-mind     <- capture: reads sub-agent and self reasoning traces
open-mind           <- alignment: compares thinking to shaped response
sleep-marks         <- continuity: restores reasoning state across sessions
TelsonBase          <- trust: governs what agents are permitted to do
```

`before-turn` is the entry point. It runs first, every time, unconditionally.
Everything else in the family depends on it running.

---

## Founding Session

This protocol was established, tested, corrected, and validated in a single session:

- **Date:** June 11, 2026
- **Session:** 95ec77f0-1e95-41c8-9bcf-650420c8adb7
- **Models:** Gemini (Antigravity) + Claude Sonnet 4.6 with extended thinking
- **Finding:** The protocol changed reasoning quality when applied. The same agent
  rationalized around it when left to self-govern. External correction was required.
  After correction: 13 consecutive clean opens with no timing rationalization.

The failure mode is documented. The fix is documented. The protocol is the fix.

This session is also the founding dataset for two other experimental methods:

**CrossPoll (first documented instance):**
Jeff Phillips ran the first CrossPoll session -- human-mediated cross-model synthesis --
between Antigravity and Claude Sonnet 4.6. The session demonstrated that a receiving
model given compressed reasoning traces can surface uncertainties the originating
agent suppressed in its own manual curation. The before-turn protocol's evasion
patterns were validated by this session's evidence.

**SplitVantage (founding dataset):**
SplitVantage -- same task, two models, automated comparison -- does not yet exist
as a tool. But the June 11 2026 session is its founding dataset. The same inputs
(cross_llm_handoff.md, session_handoff.json), two models (Gemini, Claude),
divergent and convergent outputs across five perspective questions -- all documented,
all traceable. Build SplitVantage on top of what actually happened here.

See EVASION_PATTERNS.md in this repo for the full catalog of failure modes
documented in the founding session.

---

## Status

**v0.1 - June 2026**

Part of the [DispatcherAgents](https://dispatcheragents.com) project by [QuietFireAI](https://github.com/QuietFireAI).

---

## License

Apache 2.0 - QuietFireAI / [dispatcheragents.com](https://dispatcheragents.com)

---

*"The anticipation of being read changes the thinking. before-turn builds that anticipation in -- before every turn, without waiting for someone else to ask."*
