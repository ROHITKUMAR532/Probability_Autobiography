import random

def success_probability(risk, trials=1000):
    success = 0
    for _ in range(trials):
        if random.random() < risk:
            success += 1
    return success / trials