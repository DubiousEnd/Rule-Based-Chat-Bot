Simple Rule-Based Chatbot

This is a basic, console-based chatbot written in Python. It uses a simple set of regular expression rules to identify user input and provide a corresponsding response.

This project was created as a starting point and includes:
- chatbot.py: The mainPython script for running the chatbot

Features:
- Responds to simple greetingd (hello, hi, hey).

Can answer basic questions ("How are you?", "What is your name?").

Has a "help" command to show available inputs.

Can be exited with "bye" or "exit"

Includes a default fallback response for unrecognized input

How to Run
1. Ensure you have python installed
2. Open your terminal or command prompt.
3. Navigate to directory containing the files.
4.Run the command:
    python chatbot.py
5. The chatbot will greet you, and you can start typing your messages.

How It Works

The chatbot functions using a dictionary of rules defined in chatbot.py.

Each key is a regular expression (regex) pattern that matches potential user inputs.

Each value is the string response the bot will give if that pattern is matched.

The script iterates through this dictionary for every message you send. The first rule that matches your input is used to generate the response.


