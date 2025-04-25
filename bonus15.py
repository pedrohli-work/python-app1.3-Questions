"""
This module implements a simple quiz application that reads questions and answers from a JSON file,
collects the user's responses, and evaluates them against the correct answers.

The JSON file should contain an array of questions, where each question is a dictionary with the 
following keys:
- "question_text": The text of the question.
- "alternatives": A list of alternative answers.
- "correct_answer": The correct answer index (1-based) for the question.

The script will display each question, allow the user to input their choice, and then show if 
the user's answer was correct or wrong. Finally, it will display the total score out of the 
number of questions.

Usage:
    Ensure the "bonus/questions.json" file is present in the correct directory with the required 
    structure. Then run the script to take the quiz and get a score report.

Example:
    python quiz_script.py
"""

import json

# Open the JSON file "bonus/questions.json" for reading. 
# The 'r' mode opens it in read-only mode.
# The encoding 'utf-8' ensures that the file can handle non-ASCII characters.
with open("bonus/questions.json", 'r', encoding="utf-8") as file:

# Read the contents of the file as a string.
    content = file.read()

# Convert the JSON string to a Python object 
# (in this case, a list of dictionaries)
# 'json.loads()' parses the string content 
# and returns a Python list.
data = json.loads(content)

# Iterate over the list of questions
for question in data:
    # Print the text of the current question
    print(question["question_text"])
    # Iterate over the list of alternatives for the current question
    for index, alternative in enumerate(question["alternatives"]):
        # Print the index (starting at 1) and the alternative answer
        print(index + 1, "-", alternative)

    # Prompt the user to enter their answer as an integer.
    # Convert the user's input to an integer for comparison later.
    user_choice = int(input("Enter your answer:"))

    # Add the user's choice to the current question's dictionary
    question["user_choice"] = user_choice

# Initialize the SCORE variable to keep track of the user's score.
SCORE = 0    

# Parse the data to check the user's answers 
# and compare them with the correct answers
for index, question in enumerate(data):
    # Compare the user's choice with the correct answer
    if question["user_choice"] == question["correct_answer"]:
        # If the answer is correct, increment the score
        SCORE = SCORE +1
        RESULT_MESSAGE = "Correct Answer"
    else:
        # If the answer is wrong, mark it as "Wrong Answer"
        RESULT_MESSAGE = "Wrong Answer"

    # Format the result message to display the question number, 
    # the result, user's answer, and correct answer
    MESSAGE = f"{index +1} {RESULT_MESSAGE} - Your answer: {question['user_choice']}, " \
        f"Correct answer: {question['correct_answer']}"
    # Print the message to show the user the result of each question
    print(MESSAGE)

# Print the user's final score out of the total number of questions
print("Your score is", SCORE, "/", len(data))

