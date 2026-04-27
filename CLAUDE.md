# RL-SCS

## Setup

```bash
uv sync --group dev
python run_game.py
```

## Running Tests

```bash
uv run pytest test/ -v -m "not stress"
uv run pytest test/ -v -m stress
```

## Tech Stack

- **RL 框架**：PettingZoo AEC API
- **渲染**：pygame
- **包管理**：uv
- **规则参考**：庙算·陆战指挥官（`docs/miaosuan/`，自行实现，不依赖庙算 SDK）

## Project Structure

```
src/rl_scs/
├── SCS_Game.py          # 环境核心（setup / step / reset）
├── map.py               # HexMap：路径规划、通视、格距
├── weapons.py           # 武器 ID 具名常量
├── actions.py           # 动作构造函数 + 验证器
└── render/
    ├── SCS_Renderer.py
    ├── CounterCreator.py
    ├── fonts.py         # FONT_SANS / FONT_MONO（跨平台）
    └── Color.py
data/                    # 不纳入 git
├── maps/<map_id>/basic.json, cost.json
└── scenarios/<id>.json
```

## Key Conventions

**阵营**：红方 `color=0`，蓝方 `color=1`。配置文件沿用 `p1`/`p2`，资源文件前缀 `p1_`/`p2_`。

**动作**：结构化字典，`type` 字段区分种类（1 机动 / 2 打击 / 5 夺控 / 333 结束部署…）。详见 [docs/api-spec.md](docs/api-spec.md)。

**推演节奏**：回合制。每回合双方同时提交动作列表，环境裁决一次。不引入实时帧推进。

**字体**：所有字体使用通过 `render/fonts.py` 中的 `FONT_SANS`/`FONT_MONO`，不硬编码字体名。

**地形图片**：配置文件中的旧相对路径（如 `Games/SCS/Images/plains.jpg`）由 `SCS_Game.py` 取文件名后在 `assets/` 中查找。

**武器 ID**：用 `weapons.py` 中的具名常量，不用魔数。

## Documentation

| 文档 | 内容 |
|------|------|
| [docs/goals.md](docs/goals.md) | 项目目标、核心约束、与庙算的差异对比 |
| [docs/architecture.md](docs/architecture.md) | 详细架构、模块职责、裁决流程、数据格式 |
| [docs/api-spec.md](docs/api-spec.md) | 观察/动作结构、武器 ID 表、规则约束摘要 |
| [docs/implementation-plan.md](docs/implementation-plan.md) | 带复选框的实现任务清单 |
| [docs/miaosuan/](docs/miaosuan/) | 庙算平台原始文档（规则参考，不直接使用其 SDK） |

## Original Repository

Derived from [NuZero](https://github.com/guilherme439/NuZero).
