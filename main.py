import random

#declaring the questions and answers
jokeQuestions = [ "Largest planet ? ", "Worse song ever ? ", "Capital of Peru?", "Roman god of War ?" ]
jokeAnswers = [ "Jupiter", "Castles in the Sky", "Lima", "Mars" ]

score = 0

start = str(input("Would you like to do our joke quiz? Y or N"))
if (start == "n") or (start == "N"):

    quit()
else:

    pass

for a in range(len(jokeQuestions) + 10):

    i = random.randrange(0, len(jokeQuestions))
    query = input(jokeQuestions[i])
    if (query.lower() == jokeAnswers[i].lower()):

        print("Correct!")
        score += 1
    else:

        print("Wrong!")

    YN = input("Would you like to continue Y or N?")
    if (YN.lower() == "Y"):

        pass
    elif (YN.lower() == "N"):

        quit()
    else:

        print(f"I said Y OR N not {YN}")

print(f"The final score is {score}")