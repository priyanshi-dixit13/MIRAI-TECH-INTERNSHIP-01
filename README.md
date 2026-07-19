# Assignment 1: Echo Interface & Basic Calculator

**Mirai School of Technology — Internship**
**Author:** Priyanshi Dixit

## Overview
Two beginner Python tasks: an **Echo Interface** (returns user input as output) and a **Basic Calculator** (add, subtract, multiply, divide).

## Tech Stack
Python

## Project Structure

assignment-1/
├── echo_interface.py
├── calculator.py
└── README.md


## How to Run
bash
python echo_interface.py
python calculator.py

## Features
- **Echo Interface:** takes text input, returns it as-is
- **Calculator:** four basic operations, handles invalid input & division by zero

## Screenshots


# Assignment 2: Upgrading the AI Multiverse


## Overview
A multi-personality AI chatbot built with Streamlit and the Google Gemini API. Users switch between AI personalities, each with a distinct tone.

## Tech Stack
Python · Streamlit · Google Gemini API

## Project Structure

assignment-2/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md


## Setup & Run
bash
pip install -r requirements.txt

Add your key to .env:

GEMINI_API_KEY=your_api_key_here

bash
streamlit run app.py

## Features
- Multiple selectable AI personalities
- Real-time chat interface
- API key secured via .env (git-ignored)

## Screenshot
