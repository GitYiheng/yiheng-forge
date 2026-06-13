from __future__ import annotations

import random
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from omegaconf import DictConfig


def _get(cfg: Any, key: str, default: Any = None) -> Any:
    if cfg is None:
        return default
    if isinstance(cfg, dict):
        return cfg.get(key, default)
    return getattr(cfg, key, default)


class Runner:
    def __init__(self, cfg: "DictConfig"):
        self.cfg = cfg
        self.seed = int(_get(cfg, "seed", 42))
        runner_cfg = _get(cfg, "runner", {})
        self.output_dir = Path(_get(runner_cfg, "output_dir", "outputs"))

    def setup(self) -> None:
        random.seed(self.seed)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def train(self) -> None:
        self.setup()
        trainer_cfg = _get(self.cfg, "trainer", {})
        max_steps = int(_get(trainer_cfg, "max_steps", 1))

        print(f"Starting training: max_steps={max_steps}, seed={self.seed}")
        for step in range(1, max_steps + 1):
            print(f"train step {step}/{max_steps}")
        print(f"Training finished. Outputs: {self.output_dir}")
