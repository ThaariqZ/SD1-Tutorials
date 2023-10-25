total = 0 # sum of scores
count = 0 #number of scores entered 

# get one score & convert string to integer


while True: 

    score = int(input("Enter score, (Enter -9 to end): ") )

    if score != 9: 
        total = total + score
        count = count + 1

    elif score == -9 :
        break


#print average of scores entered
average = float( total ) / count
print("Class average is", average)
