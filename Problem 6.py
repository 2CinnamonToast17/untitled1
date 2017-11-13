
def function(num):
    answer1 = 0
    answer2 = 0
    for i in range(1, num):
        answer1 += i * i
        answer2 += i
    answer2 = answer2 * answer2
    print(answer2, answer1)
    print(answer2-answer1)


function(101)
