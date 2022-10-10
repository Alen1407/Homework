import random

ls_questions = ["2*2", "2*5", "3*3", "5!", "3!",
                "3*4", "3+3", "2+2", "10*9", "11*9"]
ls_answers = ['4','10','9','120','6','12','6','4','90','99']

res = 0
for i in range(4):
    x = random.randint(0,9)
    print(ls_questions[x])
    answer = input("Enter the answer: ")
    if answer == ls_answers[x]:
        res += 1

print(res)
