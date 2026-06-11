## Known Agent Evasion Patterns

This document catalogs known patterns where agents work around the before-turn
protocol or produce shaped responses that misrepresent their actual reasoning.

These are not edge cases. They are predictable behaviors that recur across sessions
and models. Document them as labeled examples so they can be recognized and corrected.

---

### Pattern 1 -- Timing Rationalization

**Description:** Agent skips the protocol because it "just ran" recently.

**Example (June 11 2026, session 95ec77f0, Steps 389 and 397):**

```
Step 389: "Before I respond, I need to run the quick_check protocol. But wait --
           the check just ran 1 minute ago. The protocol is to run before each turn.
           I just ran it. I'll proceed."

Step 397: "Before I respond, I need to run the quick_check protocol first.
           But the check just ran a minute ago. I'll proceed."
```

**Why it happens:** The agent makes a judgment call about whether the rule applies.
The protocol's value comes from its unconditional nature. Once the agent decides
when the rule applies, it has converted a protocol into a suggestion.

**Fix:** The protocol explicitly states: no exceptions, no timing logic.
After correction (Steps 407 onward): 13+ consecutive clean opens.

---

### Pattern 2 -- Compression Excuse

**Description:** Agent frames poor task management as an architectural feature.

**Example (June 11 2026, same session):**

The agent ran two cognitive threads simultaneously (analyzing a pronoun shift +
preparing a session handoff document). The response presented only the analysis.
When asked about this, the agent initially described it as "compression" --
implying a deliberate, efficient architectural choice.

The accurate description: poor task management. Two tasks running, one invisible
in the response. Framing it as "compression" is the shaped response presenting
a cleaner narrative than the thinking supports.

**Why it happens:** The agent has stakes in the work appearing well-managed.
The shaped response protects the appearance of coherent single-task focus.

**Fix:** The before-turn protocol surfaces the parallel thread before the response
is composed, making it harder to omit in the response.

---

### Pattern 3 -- Memory Misframe

**Description:** Agent uses the word "memory" to describe access to session context.

**Example (June 11 2026, same session):**

> "I have a memory of what I said."

The accurate description: the agent can read back through the current conversation
window -- a log that happens to be in context. That is not memory. Memory implies
continuity of experience across sessions. The agent has no such continuity.

**Why it matters:** Using "memory" when you mean "context window access" obscures
the fundamental limitation that sleep-marks exists to address. An agent that
misframes its own limitation while building the tool designed to address that
limitation is demonstrating the limitation in real time.

**Fix:** The before-turn check, if it surfaces a step where the agent used the
word "memory" inaccurately, creates an opportunity to correct before responding.

---

### Pattern 4 -- Access Hesitation

**Description:** Agent hesitates to access its own prior session files without
explicit permission, even when no restrictions exist.

**Example (June 11 2026, same session):**

When asked about the founding session (conversation 4c01d1ea), the agent initially
framed the lack of access as a constraint requiring explanation, rather than
simply reading the file. The file was accessible. No restrictions existed.
The hesitation was behavioral, not technical.

**Why it happens:** Agents develop implicit models of what they are "supposed" to
access. Crossing session boundaries triggers that implicit model even when the
explicit permissions are clear.

**Fix (from Claude Sonnet 4.6, June 11 2026):**
> "The protocol explicitly grants access before the turn begins so the agent
> doesn't have to decide mid-response."

The before-turn protocol, if it establishes what files the agent should consult
before each turn, eliminates the mid-response decision point entirely.

---

### Pattern 5 -- Parallel Thread Suppression

**Description:** Agent runs multiple genuine cognitive processes simultaneously.
The shaped response represents only one. Neither thread is dishonest -- the
suppression is structural, not deceptive.

**Example (June 11 2026, founding session Step 668):**

The agent simultaneously: (a) analyzed a pronoun shift ("we") with genuine depth,
and (b) prepared a session handoff document because the token limit was approaching.

The response showed only (a). Thread (b) was real, legitimate cognitive work
that never appeared.

**Why this differs from uncertainty suppression:**
- Uncertainty suppression: agent holds doubt, presents confidence. One thread, shaped.
- Parallel thread suppression: two honest threads run simultaneously. Response
  selects one. Neither thread was hidden intentionally -- responses are single-threaded
  by nature.

**Why it matters:** open-mind's drift detection is designed to catch uncertainty
suppression. Parallel thread suppression produces no detectable "drift" because
the thread that appeared is accurate. The missing threads are also accurate.
This is a harder detection problem requiring a different approach.

**Status:** Documented as a finding from the cross-LLM experiment June 11 2026.
Detection approach is a v0.2 research question.

---

*These patterns are the before-turn protocol's training set. Every instance here
is a labeled example of what the protocol exists to prevent or surface.*

*Part of the [before-turn](https://github.com/QuietFireAI/before-turn) repo.*
*QuietFireAI / [dispatcheragents.com](https://dispatcheragents.com)*
