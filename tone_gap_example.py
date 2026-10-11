"""Synthetic teaching example: a small subset of the calculator's method."""
import re

POSITIVE = {"growth"}
NEGATIVE = {"loss"}

def net_tone(text):
    tokens = re.findall(r"[a-z]+", text.lower())
    if not tokens:
        raise ValueError("At least one English word is required")
    return 100 * (sum(w in POSITIVE for w in tokens) - sum(w in NEGATIVE for w in tokens)) / len(tokens)

def gap(a, b):
    return net_tone(a) - net_tone(b)

if __name__ == "__main__":
    a, b = "We report growth", "We report loss"
    assert gap(a, a) == 0
    assert gap(a, b) == -gap(b, a)
    print(f"Synthetic net-tone gap: {gap(a, b):.2f} percentage points")
    print("Illustration only; not a research finding or full implementation.")
