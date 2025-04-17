# fortune.py

import random

def get_fortune(mood):
    fortunes = {
        "happy": [
            "🌈 Great things await you, Lakshay! Keep smiling brightly! 🌈",
            "☀️ Happiness surrounds you. Share it with the world, Lakshay! ☀️",
            "🎉 Today is a day full of magic and possibilities. Enjoy it!"
        ],
        "sad": [
            "🌧️ Tough times don't last, but tough people like you do! 🌧️",
            "🌈 After every storm comes a rainbow. Hold on, Lakshay!",
            "❤️ It's okay to feel down sometimes. Better days are coming soon."
        ],
        "neutral": [
            "🌟 A surprise is waiting for you around the corner! 🌟",
            "🍀 Stay open-minded today, opportunities are knocking.",
            "🌀 Life is about to get interesting. Stay curious, Lakshay!"
        ],
        "stressed": [
            "🧘 Take a deep breath, Lakshay. Calmness is your true power.",
            "🌿 Every breath you take grounds you. You are doing great.",
            "🏖️ Soon, relaxation and peace will find you."
        ],
        "excited": [
            "🚀 Your energy will take you to incredible places today!",
            "🎆 Make the most of this excitement, Lakshay! Big wins ahead.",
            "🏆 Your enthusiasm is your superpower — keep moving forward!"
        ],
        "bored": [
            "📚 Maybe today is the perfect day to start something new!",
            "🎨 Creativity often starts with boredom. What will you create today?",
            "🧩 A hidden adventure awaits, Lakshay — look around carefully!"
        ]
    }

    return random.choice(fortunes.get(mood, [
        "✨ Embrace the unknown, Lakshay. Exciting things are ahead! ✨",
        "🌟 The stars are aligning in your favor. Trust the journey!"
    ]))

def main():
    print("🔮 Welcome to Lakshay's Fortune Teller (21JE0502) 🔮")
    print("=" * 60)

    while True:
        mood = input("How are you feeling today? (happy/sad/neutral/stressed/excited/bored): ").strip().lower()
        fortune = get_fortune(mood)
        print("\n" + fortune + "\n")

        retry = input("Would you like another fortune? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("\n🌟 Thank you for visiting Lakshay's Fortune Teller. Have a magical day! 🌟")
            break

if __name__ == "__main__":
    main()
