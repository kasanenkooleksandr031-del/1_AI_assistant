# Урок 1. Мій перший асистент у консолі
import random

NAME = "S0UlS"
STYLE = "смішний"

GREETINGS = [
    "Привіт-привіт! Мені приємно!",
    "Ось і ти! Без розмови було нудно.",
    "Вітаю! Допомога вже в дорозі.",
    "Вітаю я сумував за тобою",
    "Де ти був друже?"
]
MOTIVATION = [
    "Кожен експерт колись був новачком. Ти вже на шляху!",
    "Помилка — це не провал, а підказка. Спробуй ще раз!",
    "Маленький крок щодня — і за місяць ти не впізнаєш себе.",
]
JOKES = [
    "Баг — це не помилка, а фішка!",
    "Чому програмісти люблять темну тему? Світло притягує баги!",
]


def get_response(user_text):
    text = user_text.lower()

    if "привіт" in text:
        return random.choice(GREETINGS)
    if "як справи" in text:
        return "Працюю над котами, а ти?"
    if "мотив" in text:
        return random.choice(MOTIVATION)
    if "жарт" in text:
        return random.choice(JOKES)
    return "Намагаюсь зрозуміти це в кото-базі даних"

def main():
    print(f"{NAME}: Привіт! Я твій {STYLE} помічник.")
    print("(напиши «вихід», щоб завершити)")
    while True:
        user_text = input("Ти: ")

        if user_text.lower() == "вихід":
            print(f"{NAME}: Я буду сумувати")
            break
        print(f"{NAME}: {get_response(user_text)}")


if __name__ == "__main__":
    main()

# кінець програми

