apple = []
'''
def maximum (inputlist):
    maxi = inputlist[0]
    for b in inputlist:
        if b > maxi:
            maxi = b
    return maxi
def minimum (inputlist):
    mini = inputlist[0]
    for d in inputlist:
        if d < mini:
            mini = d
    return mini
'''
def maximum (inputlist):
    inputlist.sort()
    return inputlist[-1]

def minimum (inputlist):
    inputlist.sort()
    return inputlist[0]

counter = True
while counter == True:
    number = float(input("Please enter a number"))
    apple.append(number)
    end_loop = input("Would you like to continue?(Y/N)")
    if end_loop == "N" or end_loop == "n":
        counter = False
print (apple)
print (maximum(apple), minimum(apple))