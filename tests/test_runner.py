from pathlib import Path

from yiheng_forge import Runner


def test_runner_initializes_with_dict_config(tmp_path):
    cfg = {
        "seed": 123,
        "runner": {"output_dir": str(tmp_path / "outputs")},
        "trainer": {"max_steps": 1},
    }

    runner = Runner(cfg)

    assert runner.seed == 123
    assert runner.output_dir == Path(tmp_path / "outputs")


def test_runner_train_smoke(tmp_path):
    cfg = {
        "seed": 42,
        "runner": {"output_dir": str(tmp_path / "outputs")},
        "trainer": {"max_steps": 1},
    }

    Runner(cfg).train()

    assert (tmp_path / "outputs").is_dir()
