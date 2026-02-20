import random

def generate_autobiography(name, age, profession):
    traits = [
        "hard-working",
        "curious",
        "ambitious",
        "creative",
        "resilient",
        "focused",
        "optimistic"
    ]

    probabilities = [0.15, 0.15, 0.20, 0.10, 0.15, 0.15, 0.10]
    selected_traits = random.choices(traits, probabilities, k=3)

    story = (
        f"My name is {name}. I am {age} years old and currently a {profession}. "
        f"I am known to be {selected_traits[0]}, {selected_traits[1]}, and {selected_traits[2]}. "
        f"My journey is shaped by probability, choices, and consistent effort. "
        f"I believe my future is built through learning, discipline, and adaptability."
    )

    return story
