#!/usr/bin/env python3
"""Thin shim - the canonical module is before_turn/quick_check.py.

Kept so `python scripts/quick_check.py ...` (the documented invocation)
keeps working from a bare clone. One source of truth: the package.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from before_turn.quick_check import BEFORE_TURN_QUESTIONS, main, quick_check  # noqa: F401,E402

if __name__ == "__main__":
    main()
