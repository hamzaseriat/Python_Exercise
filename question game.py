import random

quiz_data = [
    {
        "question": "How many elements are in the periodic table?",
        "options": ("A) 118", "B) 119", "C) 120", "D) 121"),
        "answer": "A"
    },
    {
        "question": "Which animal lays the largest eggs?",
        "options": ("A) Whale", "B) Elephant", "C) Ostrich", "D) Crocodile"),
        "answer": "C"
    },
    {
        "question": "What is the atomic number of oxygen?",
        "options": ("A) 8", "B) 16", "C) 32", "D) 64"),
        "answer": "A"
    },
    {
        "question": "Which element has the highest melting point?",
        "options": ("A) Gold", "B) Carbon", "C) Tungsten", "D) Platinum"),
        "answer": "C"
    },
    {
        "question": "What is the most abundant gas in Earth's atmosphere?",
        "options": ("A) Nitrogen", "B) Oxygen", "C) Argon", "D) Carbon Dioxide"),
        "answer": "A"
    },
    {
        "question": "What is the capital of France?",
        "options": ("A) London", "B) Paris", "C) Berlin", "D) Rome"),
        "answer": "B"
    },
    {
        "question": "Which country has the largest population?",
        "options": ("A) China", "B) India", "C) United States", "D) Indonesia"),
        "answer": "B" # Güncel bilgiye göre Hindistan (B) veya Çin (A) seçilebilir.
    },
    {
        "question": "Which is the largest ocean in the world?",
        "options": ("A) Arctic Ocean", "B) Atlantic Ocean", "C) Indian Ocean", "D) Pacific Ocean"),
        "answer": "D"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ("A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"),
        "answer": "B"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ("A) Diamond", "B) Graphite", "C) Quartz", "D) Emerald"),
        "answer": "A"
    }
]

# Soruları her seferinde farklı sırada getirmek için karıştırıyoruz
random.shuffle(quiz_data)

guesses = []
score = 0
correct_answers_count = 0

print("=========================================")
print("      WELCOME TO THE TRIVIA QUIZ!        ")
print("=========================================")

for index, item in enumerate(quiz_data):
    print(f"\nQuestion {index + 1}: {item['question']}")
    for option in item['options']:
        print(option)
    
    # Kullanıcı geçerli bir şık girene kadar döngü çalışır
    while True:
        guess = input("Enter (A, B, C, or D): ").upper().strip()
        if guess in ("A", "B", "C", "D"):
            break
        print("Invalid choice! Please enter A, B, C, or D.")

    guesses.append(guess)
    
    if guess == item['answer']:
        score += 10
        correct_answers_count += 1
        print("⭐ Correct!!")
    else:
        print("❌ Wrong!!")
        print(f"The correct answer was: {item['answer']}")
    
    print("-" * 30)

# --- OYUN SONU RAPORU ---
total_questions = len(quiz_data)
success_rate = (correct_answers_count / total_questions) * 100

print("\n=========================================")
print("               GAME OVER                 ")
print("=========================================")
print(f"Your Score      : {score} / {total_questions * 10}")
print(f"Correct Answers : {correct_answers_count} out of {total_questions}")
print(f"Success Rate    : {success_rate:.1f}%")
print("=========================================")