#auto comment program using python 
import pyautogui
from time import sleep

comments=[  "Amazing",
            "Beautiful",
            "Kind",
            "Inspiring",
            "Brilliant",
            "Wonderful",
            "Fantastic",
            "Magnificent",
            "Generous",
            "Positive",
            "Courageous",
            "Supportive",
            "Loyal",
            "Authentic",
            "Caring",
            "Humble",
            "Creative",
            "Friendly",
            "Adventurous",
            "Thoughtful",
            "Cheerful",
            "Compassionate",
            "Dedicated",
            "Energetic",
            "Gracious",
            "Helpful",
            "Impressive",
            "Innovative",
            "Kindhearted",
            "Optimistic",
            "Patient",
            "Reliable",
            "Resourceful",
            "Respectful",
            "Sincere",
            "Talented",
            "Trustworthy",
            "Understanding",
            "Valiant",
            "Vibrant",
            "Wise",
            "Zestful",
            "Charming",
            "Considerate",
            "Diligent",
            "Empathetic",
            "Encouraging",
            "Faithful",
            "Forgiving",
            "Gentle",
            "Grateful",
            "Hardworking",
            "Hopeful",
            "Innovative",
            "Joyful",
            "Modest",
            "Observant",
            "Passionate",
            "Perceptive",
            "Persevering",
            "Radiant",
            "Resilient",
            "Responsible",
            "Selfless",
            "Sensible",
            "Skillful",
            "Sociable",
            "Spirited",
            "Strong",
            "Supportive",
            "Tactful",
            "Trusting",
            "Uplifting",
            "Versatile",
            "Warm",
            "Welcoming",
            "Witty",
            "Zealous",
            "Adaptable",
            "Brave",
            "Calm",
            "Determined",
            "Eager",
            "Efficient",
            "Flexible",
            "Focused",
            "Genuine",
            "Honest",
            "Innovative",
            "Logical",
            "Motivated",
            "Organized",
            "Persistent",
            "Proactive",
            "Punctual",
            "Resourceful",
            "Steadfast",
            "Tenacious"]

sleep(5)

for i in range(100):
    pyautogui.typewrite(comments[i])
    pyautogui.typewrite("\n")
    sleep(2)

