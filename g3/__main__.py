"""Run the deterministic two-task demo."""

from __future__ import annotations

import tempfile
from pathlib import Path

from .demo import build_loop


def main() -> None:
    root = Path(tempfile.mkdtemp(prefix="g3_"))
    loop = build_loop(root)
    result = loop.run_stream(["reconcile", "memo"])
    first, second = result.tasks
    print(f"run directory: {root}")
    print(f"rules unchanged: {result.rules_unchanged}")
    print(f"reconcile adopted: {first.adopted_label}")
    print(f"memo started from base: {second.start_tree == loop.base_tree}")
    print(f"memo adopted: {second.adopted_label}")
    print(f"library entries: {', '.join(loop.library.entries())}")
    kept_skill = "skills/reconcile/SKILL.md" in second.final_tree
    print(f"memo inherited the reconcile skill: {kept_skill}")


if __name__ == "__main__":
    main()

