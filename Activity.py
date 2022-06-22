
###################### Question 1 ######################

def funcAverage2(scoreList):
    sum = 0
    for score in scoreList:
        sum = sum + score

    return sum / len(scoreList)

scoreList =[]

for i in range(6):
    # print("Insert course score: ")
    scoreList.append(int(input(f"Insert course Score {i+1} : ")))

print("Your Average is : " ,round(funcAverage2(scoreList)))

###################### Question 2 ######################

def funcfuncAvg(a,b,c,d,e,f):
    print(round((a+b+c+d+e+f)/6))

funcfuncAvg(3,4,2,5,6,12)

###################### Question 3 ######################

def funcArbit(*scores):
    sum = 0
    for score in scores:
        sum = sum+score

    return sum/len(scores)

print("Average using Arbitrary Arguments is: ",round(funcArbit(2,45,6,4,8,54)))

###################### Question 4 ######################

marksDict = {}
#
keys = ['AML_1413', 'CBD_2214', 'COM_3013', 'AML_1301','COM_1114','AML_1214']
values = scoreList

for key, value in zip(keys, values):
    marksDict[key] = value

for k, v in marksDict.items():
    print(k, v)

###################### Question 5 ######################

def keyArg(**kwargs):

    print(sum(kwargs.values())/len(kwargs))

keyArg(**marksDict)


def fun(a, b = 2, c = 3):
    print("Hello")

