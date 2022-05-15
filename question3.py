import json
d = { }
#define a variable for the score
right_answer = 0
#define the question number
number=1
#loading question to the program
f = open("ques.txt",'r')
d = json.load(f)
f.close()

name = input("Enter your full name: ")
for q in d.keys():
    print("Question",number,": ", q)
    ans = input("The answer is ")
    #testing the result
    if ans.lower() == d[q].lower():
        right_answer = right_answer + 1
        print("Correct ")
    else:
        print ("Wrong")
    number = number + 1

#write the name and the score is a separate file
result={name:right_answer}
m = open("score.txt",'w')
result = json.dump(result,m)
m.close()
    

