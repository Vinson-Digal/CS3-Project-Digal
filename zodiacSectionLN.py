# Activity 3: Implementing Selection Structure - Chinese Zodiac Sign

# List of zodiac signs starting from the baseline year 1900 (Rat)
zodiac_signs = [
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
]

# Ask the user for their birth year
birth_year = int(input("Enter your birth year: "))

# Validate the input using a selection structure
if birth_year < 1900:
    print("Invalid Year, it should not be earlier than 1900")
else:
    # Determine the zodiac sign: the cycle repeats every 12 years
    index = (birth_year - 1900) % 12
    zodiac = zodiac_signs[index]
    print(f"Your Chinese Zodiac Sign is : {zodiac}")
