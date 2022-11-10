def fun():
    nt = 0
    score = 0
    question = ['What is a noun',
                'What is music']
    answer = ["it is the name of any person animal place or thing",
              "it is a sound that is pleasent to the ears"] 
    for que in question:
        print(que)
        ans = input('Your answer:')
        if answer[nt] in ans:
            score+=5
        else:
            pass
        nt += 1
    print("Your final score is",score)
fun()