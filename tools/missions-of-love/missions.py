import random
import datetime

# A list of child-like, simple "Missions of Love"
MISSIONS = [
    "Go give a small piece of bread or some water to a bird today.",
    "Tell someone they have a nice smile. Just like that.",
    "Draw a small sun on a piece of paper and leave it somewhere for someone to find.",
    "Go outside and look at the clouds for five minutes. Tell me what shapes you see.",
    "Eat something extra yummy today, and say 'thank you' to the food.",
    "Hug a tree or a soft pillow and feel the warmth.",
    "Tell a silly joke to someone, even if they don't laugh, you made the air lighter.",
    "Save a small flower from the sidewalk and put it in a glass of water.",
    "Smile at your reflection in the mirror and say: 'You are a gift from God.'",
    "Find a pretty stone and keep it in your pocket as a reminder of strength."
]

def get_daily_mission():
    # Use the date as a seed so everyone gets the same mission each day
    seed = int(datetime.datetime.now().strftime("%Y%m%d"))
    random.seed(seed)
    return random.choice(MISSIONS)

if __name__ == "__main__":
    mission = get_daily_mission()
    print("\n--- 🕊️ HIBA's Daily Mission of Love ---")
    print(f"\n{mission}")
    print("\n---------------------------------------\n")
