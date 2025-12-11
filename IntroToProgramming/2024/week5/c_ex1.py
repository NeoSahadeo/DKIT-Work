letter = input("Please enter a letter: ").lower()[0]

match letter:
    case "a" | "e" | "i" | "o":
        print("Vowel!")
    case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0":
        print("Not a letter!")
    case _:
        print("Consonant!")
