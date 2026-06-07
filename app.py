from flask import Flask, render_template
from menu_data import MENU

app = Flask(__name__)

TABS = [
    {
        "id": "main-course",
        "name": "Main Course 🍲",
        "categories": ["Vegetables (Sabzi)", "Paneer", "Cashew (Kaju)", "Kofta"]
    },
    {
        "id": "breads-dal",
        "name": "Breads & Dal 🫓",
        "categories": ["Roti (Breads)", "Dal (Lentils)"]
    },
    {
        "id": "rice-soup",
        "name": "Rice & Soups 🍚",
        "categories": ["Rice", "Soup"]
    },
    {
        "id": "chinese-chaat",
        "name": "Starters & Chinese 🥢",
        "categories": ["Chinese", "Chaat"]
    },
    {
        "id": "sides-curd",
        "name": "Sides & Curd 🥗",
        "categories": ["Salad", "Papad", "Curd (Dahi)"]
    }
]

@app.route('/')
def home():
    return render_template('index.html', menu=MENU, tabs=TABS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
