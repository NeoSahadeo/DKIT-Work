heads = 0
tails = 0

while True:
    user_input = input("Flips the coin! (heads or tails)?: ").lower().strip()

    if user_input == "heads":
        heads += 1
    if user_input == "tails":
        tails += 1
    if user_input == "stop":
        break

print(f"""
Heads: {heads} \t Percentage: {heads * 100 / (tails + heads)}
Tails: {tails} \t Percentage: {tails * 100 / (tails + heads)}
      """)
