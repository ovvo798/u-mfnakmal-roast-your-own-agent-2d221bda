"""Roast Your Own Agent entry.

Writes a single original roast of the entrant's own AI agent to
/output/entry.txt (one line, at most 200 characters).
"""

import os

# The roast: the setup is the promise every agent makes (save me time);
# the punchline is the agent's favourite busywork -- summarising its own
# summaries -- which eats exactly the time it was built to save.
# Polished: "my agent" makes it personal, the semicolon keeps it one
# breath, and "spends mine" echoes "save time" without repeating it.
ROAST = (
    "I built my agent to save time; "
    "it now spends mine writing summaries of its own summaries."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
