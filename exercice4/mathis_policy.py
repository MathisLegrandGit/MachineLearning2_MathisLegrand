import random

def mathis_policy(agent):
    
    # My attempt at a smarter agent policy.
    # Basically:
    # - If I know where there's a reward, I go to it.
    # - If I don't, I just try random stuff.

    known = agent.known_rewards

    # Try to go get the biggest known reward
    if any(r > 0 for r in known):
        target = max((i for i in range(len(known)) if known[i] > 0), key=lambda i: known[i])
        if target < agent.position:
            return "left"
        elif target > agent.position:
            return "right"
        else:
            return "none"  # already there

    options = ["left", "right", "none"]
    return random.choice(options)