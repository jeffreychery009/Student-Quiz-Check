# Quiz Grading Application

This Python application automatically grades multiple-choice quizzes based on a predefined answer key.

## Assignment Requirements

### Quiz Format
- The quiz consists of 15 multiple-choice questions
- Each answer is a single character (A-D, uppercase)
- Students must correctly answer 11 out of 15 questions to pass

### Answer Key
```
1. A    6. D    11. B
2. C    7. D    12. C
3. A    8. A    13. D
4. B    9. C    14. D
5. B    10. A   15. B
```

### Features
The program will:
1. Store the quiz answer key
2. Prompt for student name and answers file
3. Read student answers from file
4. Compare answers against the key
5. Calculate and display:
   - Number of correct answers
   - Number of incorrect answers
   - Questions incorrectly answered
   - Pass/Fail status
6. Allow grading of multiple students

### Technical Requirements
- Uses functional decomposition
- Implements Exception Handling for file processing
- Handles file errors (IOError, FileNotFoundError, etc.)

### Test Files
The following files are available for testing:
- A001Quiz.txt
- B002Quiz.txt
- C003Quiz.txt

## How to Run

1. Make sure you have Python installed on your computer
2. Open a terminal/command prompt
3. Navigate to the project directory
4. Run the program using:
   ```
   python main.py
   ```
5. Follow the prompts to enter student name and answers file path

## Project Structure

- `main.py`: The main Python script containing the quiz grading logic
- `requirements.txt`: List of project dependencies (currently empty)
- `README.md`: This file, containing project documentation 