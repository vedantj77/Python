def new_game():

    guesses= []
    correct_guesses = 0
    ques_no = 0

    for key in questions:
        print("------------")
        print(key)
        for i in options[ques_no]:
            print(i)
        guess = input("Enter (A, B, C, D) : ").upper()
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key),guess)
        
        ques_no+=1
    display_score(correct_guesses,guesses)

    

def check_answer(answer,guess):
    if answer == guess:
        print("Correct !")
        return 1
    else:
        print("Wrong !")
        return 0
    
def display_score(correct_guesses,guesses):
    print("------------")
    print("Results : ")
    print("------------")
    print("Answers :", end="")
    for i in questions :
        print(questions.get(i),end = "")
    print()

    print("Gusses :", end="")
    for i in guesses :
        print(i,end = "")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Score is : ", score , "%")


questions = {
    "Who created python ? " : "A",
    "What year was Python created ? " : "B",
    "Python is tributed to which comedy group ? " : "C",
    "Is earth round ? "  : "A"
}

options = [["A. Guido van Rossum ", "B. Elon Musk", "C. Bill Gates"],
           ["A. 1989 ", "B. 1991", "C. 2016"],
           ["A. Bocha ", "B. Smosh", "C. Monty Python"],
           ["A. True ", "B. Flase", "C. Flat"]
           ]


new_game()