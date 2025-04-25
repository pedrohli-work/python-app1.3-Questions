# Quiz Application

## Description
This project implements a simple quiz application that loads questions from a JSON file, collects the user's answers, and calculates the final score. The application displays the questions, allows the user to choose an alternative, and provides feedback on whether the answer is correct or incorrect.

## JSON Structure
The JSON file that stores the questions should follow this structure:

```json
[
  {
    "question_text": "Question 1?",
    "alternatives": ["Alternative 1", "Alternative 2", "Alternative 3", "Alternative 4"],
    "correct_answer": 1
  },
  {
    "question_text": "Question 2?",
    "alternatives": ["Alternative 1", "Alternative 2", "Alternative 3", "Alternative 4"],
    "correct_answer": 2
  }
]
