# Sentiment Analysis Flask App

This is a simple web app that uses a HuggingFace model to analyze the sentiment of user reviews.

## Features
- Input a review in a web form
- Get sentiment label and score using a multilingual HuggingFace model

## Setup

1. **Clone the repository** (if not already):
   ```bash
   git clone <repo-url>
   cd HF-Sentiment
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   python app.py
   ```

4. **Open your browser** and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Notes
- The first run may take a while as the model downloads.
- Requires Python 3.7 or higher. 