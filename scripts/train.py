import hydra
from omegaconf import DictConfig


@hydra.main(version_base=None, config_path="../configs", config_name="base")
def main(cfg: DictConfig):
    from yiheng_forge.runner import Runner

    runner = Runner(cfg)
    runner.train()


if __name__ == "__main__":
    main()
