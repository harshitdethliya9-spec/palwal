# Shree Palwal Food Hub

A beautiful, fast, and interactive website for **Shree Palwal Food Hub** restaurant built using Python (Flask), HTML, and CSS. It showcases the complete menu with interactive tabs, pricing details (Half & Full portions), maps location, and contact details.

## Features

- **Interactive Tabbed Menu**: Seamless navigation between different food categories like Main Course, Breads, Rice, Chinese, etc.
- **Dynamic Pricing**: Shows portion-based pricing (Half/Full) for Vegetables and Paneer items.
- **Embedded Location Map**: Live map navigation directly pointing to the restaurant location in Maksi, MP.
- **Responsive Design**: Mobile-friendly UI that adapts beautifully to phones and tablets.
- **Dine-in Focus**: Showcases fresh food options without online delivery constraints.

## Tech Stack

- **Backend**: Python 3 (Flask Framework)
- **Frontend**: HTML5, Vanilla CSS3 (with responsive layout, CSS variables, and slide-in animations)
- **Production Server**: Gunicorn (for production/Render deployment)

## How to Run Locally

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Server**:
   ```bash
   python app.py
   ```

3. **Open Website**:
   Open your browser and navigate to: https://palwal.onrender.com/

## Deployment on Render

This project is pre-configured for deployment on Render.

- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
