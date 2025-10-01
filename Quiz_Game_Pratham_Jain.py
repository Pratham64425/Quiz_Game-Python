import random

def run_quiz(player_name, questions, is_computer=False):
    print(f"\n👤 {player_name}, it's your turn!\n")
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for opt in q["options"]:
            print(opt)

        if is_computer:
            ans = random.choice(['a', 'b', 'c', 'd'])
            print(f"Computer chooses: {ans}")
        else:
            while True:
                ans = input("Your answer (a/b/c/d): ").lower()
                if ans in ['a', 'b', 'c', 'd']:
                    break
                else:
                    print("⚠️ Please enter a valid option: a, b, c, or d.")

        if ans == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. Correct answer: {q['answer']})")

    return score

def display_results(results, total_questions):
    print("\n🎯 Final Results:")
    max_score = 0
    winners = []

    for name, score in results.items():
        percent = (score / total_questions) * 100
        print(f"{name} Score: {score}/{total_questions} ({percent:.2f}%)")

        if score > max_score:
            max_score = score
            winners = [name]
        elif score == max_score:
            winners.append(name)

    if len(winners) == 1:
        print(f"\n🏆 Winner: {winners[0]}!")
    else:
        print(f"\n🤝 It's a tie between: {', '.join(winners)}")

def start_quiz():
    print("🎮 Welcome to the Python Quiz Game!")
    start = input("Type 'start' to begin or 'q' to quit: ").lower()
    if start == 'q':
        print("Quiz exited.")
        return

    questions = [
        {
            "question": "1. What is the output of: print(2 ** 3)?",
            "options": ["a) 6", "b) 8", "c) 9", "d) 5"],
            "answer": "b"
        },
        {
            "question": "2. Which of the following is a valid variable name?",
            "options": ["a) 2name", "b) name_2", "c) @name", "d) name-2"],
            "answer": "b"
        },
        {
            "question": "3. What is the data type of: print(type(3.0))?",
            "options": ["a) int", "b) float", "c) double", "d) decimal"],
            "answer": "b"
        },
        {
            "question": "4. What does the 'len()' function do in Python?",
            "options": ["a) Converts type", "b) Loops", "c) Counts elements", "d) None"],
            "answer": "c"
        },
        {
            "question": "5. Which keyword is used to handle exceptions in Python?",
            "options": ["a) try", "b) handle", "c) exception", "d) check"],
            "answer": "a"
        },
        {
            "question": "6. What is the output of: bool('False')?",
            "options": ["a) False", "b) True", "c) Error", "d) None"],
            "answer": "b"
        },
        {
            "question": "7. Which of the following is immutable?",
            "options": ["a) List", "b) Dictionary", "c) Set", "d) Tuple"],
            "answer": "d"
        },
        {
            "question": "8. How do you start a function in Python?",
            "options": ["a) function", "b) start", "c) def", "d) func"],
            "answer": "c"
        },
        {
            "question": "9. Which operator is used for floor division?",
            "options": ["a) /", "b) //", "c) %", "d) **"],
            "answer": "b"
        },
        {
            "question": "10. What will 'list(range(3))' return?",
            "options": ["a) [0, 1, 2]", "b) [1, 2, 3]", "c) [0, 1, 2, 3]", "d) [1, 2]"],
            "answer": "a"
        }
    ]

    print("\nChoose Mode:")
    print("1. Play against Computer")
    print("2. Multiplayer Mode")
    mode = input("Enter 1 or 2: ")

    total_questions = len(questions)
    results = {}

    if mode == "1":
        player_name = input("Enter your name: ")
        player_score = run_quiz(player_name, questions)
        computer_score = run_quiz("Computer", questions, is_computer=True)
        results[player_name] = player_score
        results["Computer"] = computer_score

    elif mode == "2":
        num = int(input("Enter number of players: "))
        for i in range(num):
            name = input(f"Enter name of Player {i+1}: ")
            score = run_quiz(name, questions)
            results[name] = score
    else:
        print("Invalid choice.")
        return

    display_results(results, total_questions)


start_quiz()
