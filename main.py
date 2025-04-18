"""
Name: Jeffrey Chery
Date: 04/17/2025
Purpose: This program will grade a quiz for a few select students and will display the results whether they 
passed or failed.
IPO Chart
    Input: The name of the student and the name of the file that where the student's answers are stored.
    Process: The program will read the file and compare the answers to the correct answers.
    Output: The program will display whether the student passed or failed.
"""

def main():
    print("Quiz Grading App...")
    name, filename = get_file_name()
    if name and filename:
        display_results(name, filename)
    


def get_file_name():
    # Get the student's name and the file name
    name = input("\nEnter name of student: ")
    filename = input("\t quiz answers file: ")

    try:
        open(filename, "r")
    except FileNotFoundError:
        print(f"\nError ... could not find {filename}.")
        user_choice = input("Do you have another student (y/n): ")
        if user_choice != "y":
            return None, None
        else:
            return get_file_name()
        
    return name, filename

def display_results(name, filename):
    ANSWER_KEY = ["A", "C", "A", "B", "B", "D", "D", "A", "C", "A", "B", "C", "D", "D", "B"]
    answers_correct = 0
    answers_incorrect = 0
    incorrect_answers_list = []

    with open(filename, "r") as file:
        for question, line in enumerate(file, 1):
            answer = line.strip()

            correct_answer = ANSWER_KEY[question - 1]

            if answer == correct_answer:
                answers_correct += 1
            else:
                answers_incorrect += 1
                incorrect_answers_list.append(question)

            
                
    print(f"\nCorrect answers: {answers_correct}")
    print(f"Incorrect answers: {answers_incorrect}", end="")
    if len(incorrect_answers_list) > 0:
        print(f" ({', '.join(map(str, incorrect_answers_list))})")
    else:
        print()

    if answers_correct >= 11:
        print(f"\n{name} ... you passed the quiz!")
    else:
        print(f"\n{name} ... you failed the quiz.")
    
    
    









if __name__ == "__main__":
    main()

