"""Closed RSI loop on top of Harness².

Reuses Harness² component trees, evidence-gated library, blind selection ids,
and rollout ledger. Adds the acceptance gates those pieces do not enforce:
one edit per probe, re-execution before adoption, no cross-task inheritance of
a fused harness, and library updates that can be revoked.
"""

from .loop import ClosedLoop, StreamResult

__all__ = ["ClosedLoop", "StreamResult"]
