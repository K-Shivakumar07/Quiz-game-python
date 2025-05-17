# Python quiz game

questions = ("How many elements are in the periodic table?:",
             "Which animal lays the largest egg?:",
             "What is the abundant gas in the atmosphere?:",
             "How many bones does a human have?:",
             "Which planet in the solar system is the hottest?:")

options = (("A. 116","B. 118","C. 120","D. 122"),
           ("A. Ostrich","B. Cassowary","C. Emu","D. Kiwi"),
           ("A. Oxygen","B. Nitrogen","C. Carbon Dioxide","D. Helium"),
           ("A. 206","B. 207","C. 208","D. 210"),
           ("A. Mercury","B. Venus","C. Mars","D. Jupiter"))

answers = ("B","A","B","A","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------")
    print(question)
    for option in options[question_num]:
        print(option)
     
    guess = input("Enter (A,B,C,D):").upper() 
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT. The correct answer is", answers[question_num])
    question_num += 1
    
    
print("-----------------------")
print("    RESULTS    ")
print("-----------------------")

print("Answers:", end= "")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses:", end= "")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/ len(questions)*100)
print("Your score is:", score, "%")

print("***** QUIZ OVER *****")
print("***** THANK YOU FOR PLAYING *****")