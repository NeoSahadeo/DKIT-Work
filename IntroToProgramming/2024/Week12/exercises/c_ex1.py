oxpork = ["eloquent",
          "benevolent",
          "ephemeral",
          "serendipity",
          "ubiquitous",
          "meticulous",
          "cacophony",
          "quintessential",
          "nostalgia",
          "ambiguous"]

print("OxPork Dictionary:")
for word in oxpork:
    print(word)

user_input = input("Enter a word you would like to delete: ").strip().lower()

if oxpork.__contains__(user_input):
    oxpork.remove(user_input)


print("OxPork Dictionary:")
for word in oxpork:
    print(word)
