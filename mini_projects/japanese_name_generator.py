import random

name = ["Yuta", "Yuki", "Yuuichi", "Kento", "Keita"]
surmane = ["Nakamoto", "Ishikawa", "Nakamura", "Yamazaki", "Tsukishima"]

def candidate():
    full_name = random.choice(name) + " " + random.choice(surmane)
    print(full_name)

candidate()

