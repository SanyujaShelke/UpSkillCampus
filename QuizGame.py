import random

# Function to load quiz data from a text file
def load_quiz_data(file_path):
    quiz_data = []
    with open(file_path, 'r') as file:
        for line in file:
            question, answer = line.strip().split(',')
            quiz_data.append({'question': question, 'answer': answer})
    return quiz_data

# Function to present a question to the user and check the answer
def present_question(question):
    print(question['question'])
    user_answer = input("Your answer: ").strip().lower()
    return user_answer == question['answer'].lower()

# Function to run the quiz
def run_quiz(quiz_data):
    score = 0
    random.shuffle(quiz_data)  # Shuffle the questions
    for question in quiz_data:
        if present_question(question):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    print("Quiz complete! Your score is {}/{}".format(score, len(quiz_data)))

# Main function
def main():
    file_path = 'quiz_questions.txt'  # Path to the quiz data file
    quiz_data = load_quiz_data(file_path)
    run_quiz(quiz_data)

if __name__ == "__main__":
    main()
