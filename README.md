# RL-SCS

A simplified implementation of Standard Combat Series (SCS) games for reinforcement learning.

**PettingZoo AEC API Compatible** ✅

## Getting Started

- [Installation](docs/install.md)

## Running the Game

Use the included `run_game.py` script to watch a game with random AI:

```bash
uv sync --group dev
python run_game.py
```

This opens a pygame window and prints step-by-step logs to the terminal. Adjust `STEP_DELAY` at the top of `run_game.py` to control speed (seconds per step).

To use a different map, change the config file name:

```python
config = get_package_root() / "example_configurations" / "solo_soldier_config_5.yml"
```

Available example configs are in `src/rl_scs/example_configurations/`.

## Usage

RL-SCS implements the PettingZoo AEC API, so it works out of the box with any compatible RL library.

Game scenarios are defined in YAML config files.
Several example configs are included in the package at `<PACKAGE_ROOT>/"example_configurations"/`

```python
from rl_scs.SCS_Game import SCS_Game

env = SCS_Game("path/to/config.yml")
env.reset(seed=42)

for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()

    if termination or truncation:
        action = None
    else:
        action_mask = info["action_mask"]
        action = env.action_space(agent).sample(action_mask)

    env.step(action)
```


The observation format and action mask location can be configured at construction time:

```python
env = SCS_Game(
    config_path,
    obs_space_format="channels_first",  # "channels_first" | "channels_last" | "flat"
    action_mask_location="obs",         # "info" (default) | "obs"
)
```
