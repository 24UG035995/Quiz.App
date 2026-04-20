# Python Quiz App

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language is used for AI?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. Paint"],
        "answer": "A"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["A. 3", "B. 5", "C. 4", "D. 6"],
        "answer": "C"
    }
]

score = 0

print("🎯 Welcome to Python Quiz App")
print("---------------------------")

for q in questions:
    print("\n" + q["question"])
    
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong Answer")

print("\n📊 Quiz Finished")
print("Your Score:", score, "/", len(questions))
