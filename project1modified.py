import time
print("--------------------------------------------------")
#Welcome the user
print("\033[1m***WELCOME TO MATHS QUIZ!!!***\033[0m")#untuk boldkan tajuk
time.sleep(1)#masa delay
print("--------------------------------------------------")

#Chances
chances=1 #cubaan menjawab hanya sekali
print("INSTRUCTION :\n")
print("You have to pick", chances,"correct answer.\nYou will get 1 score if you pick a correct answer.\n")
time.sleep(2)

#score
score=0 #setkan markah kepada 0

#question 1
print("==================================================")
question_1=print("1) How many factors does the number 24 have?\n(A) 4\n(B) 6\n(C) 8\n(D) 12\n\n")
answer_1= "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("CORRECT! GOOD JOB!!!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS :", answer_1, "\n\n")

time.sleep(2)

#question 2
print("==================================================")
question_2 = print("2)Name two factors of the number 15\n(A) 3 and 5\n(B) 2 and 7\n(C) 4 and 6\n(D) 9 and 12\n\n")  
answer_2 = "a"

for i in range(chances):
    answer = input("answer: ")
    if (answer.lower() == answer_2):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("NICE TRY\n ")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS :", answer_2, "\n\n")

time.sleep(2)

#question 3
print("==================================================")
question_3 =print("3)  What is the result of 7 multiplied by 9?\n(A) 14\n(B) 63\n(C) 56\n(D) 17\n\n")
answer_3= "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("CORRECT! WELL DONE KIDS!!!\n")
        score = score + 1
        break
    else:
        print("SORRY.... INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS :", answer_3, "\n\n")

time.sleep(2)

#question 4
print("==================================================")
question_4 =print("4)  How many factors does the number 36 have?\n(A) 4\n(B) 6\n(C) 8\n(D) 9\n\n")
answer_4= "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("CORRECT! FANTASTIC!!!\n")
        score = score + 1
        break
    else:
        print("OOPPSSS, INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS :",answer_4, "\n\n")

time.sleep(2)

#question 5
print("==================================================")
question_5 =print("5)  Is 25 a multiple of 5?\n(A) YES\n(B) NO\n\n")
answer_5= "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("CORRECT!!! YOU SO GENIUS!\n")
        score = score + 1
        break
    else:
        print("NOPE!INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS :", answer_5, "\n\n")

time.sleep(2)

#print the score
print("==================================================")
while score >=2:
    print("WELL DONE! Your Score was : ", score)
    break

while score <2:
    print("Better luck next time! Your score was : ",score)
    break

#Goobye message
print("Thank you for playing the MATH Quiz Game!")
