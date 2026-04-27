import time
from rl_scs.SCS_Game import SCS_Game
from rl_scs.utils.package_utils import get_package_root

STEP_DELAY = 0.5  # seconds between steps

config = get_package_root() / "example_configurations" / "mirrored_config_5.yml"
env = SCS_Game(config)
env.reset(seed=42)

step = 0
for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()

    if termination or truncation:
        action = None
        print(f"[Turn {env.current_turn}] {agent} 结束 (reward={reward:.2f})")
    else:
        action_mask = info["action_mask"]
        action = env.action_space(agent).sample(action_mask)
        action_str = env.string_action(env.get_action_coords(action))
        print(f"[Turn {env.current_turn}] Step {step:>4} | {agent} | {action_str}")

    env.step(action)
    env.render("human")
    step += 1
    time.sleep(STEP_DELAY)

env.close()
