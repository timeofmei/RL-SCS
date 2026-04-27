# RL-SCS Project Notes

## Setup

```bash
uv sync --group dev
python run_game.py
```

## Project Structure

- `src/rl_scs/SCS_Game.py` — main game environment (PettingZoo AEC API)
- `src/rl_scs/render/SCS_Renderer.py` — pygame renderer
- `src/rl_scs/render/CounterCreator.py` — generates unit counter images
- `src/rl_scs/render/fonts.py` — cross-platform font selection (`FONT_SANS`, `FONT_MONO`)
- `src/rl_scs/render/Color.py` — color enum
- `src/rl_scs/example_configurations/` — YAML scenario configs
- `src/rl_scs/assets/` — unit and terrain images
- `run_game.py` — script to run a game with random AI and pygame rendering

## Key Conventions

**Players**: internally indexed 0 and 1. Config files use `p1`/`p2`. Asset files follow the `p{player+1}_` prefix (e.g., `p1_soldier.png` = player 0, `p2_soldier.png` = player 1).

**Actions**: the action space is `Discrete` (flat integer). Use `env.get_action_coords(action)` to convert to a 3D coordinate tuple before passing to `env.string_action()`.

**Fonts**: all font usage goes through `FONT_SANS` and `FONT_MONO` constants from `render/fonts.py`. Do not hardcode font names elsewhere — the constants pick the best available font on the current OS.

**Terrain images**: config files may contain legacy relative paths like `Games/SCS/Images/plains.jpg`. These are resolved in `SCS_Game.py` by taking the filename and looking it up in `assets/`.

## Running Tests

```bash
uv run pytest test/ -v -m "not stress"
uv run pytest test/ -v -m stress
```

## Original Repository

This project is derived from [NuZero](https://github.com/guilherme439/NuZero).
