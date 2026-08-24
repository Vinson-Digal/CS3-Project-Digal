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
    "Pig (猪 / Zhū)"]

birth_year = int(input("Enter your birth year: "))

if birth_year < 1900:
    print("Invalid Year, Please enter a year after 1900.")
else:
    index = (birth_year - 1900) % 12
    zodiac = zodiac_signs[index]
    print(f"Your Chinese Zodiac Sign is : {zodiac}")

 [View the full activity sheet](Grade-9-K-Activity-zodiac.pdf) 
 [View the working code](Screenshot 2026-08-24 232723.png)
 
