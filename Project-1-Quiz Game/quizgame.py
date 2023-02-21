print("WELCOME TO THE CRICKET QUIZ !") 

playing = input("Do you want to play? ")

# reason to write != is if user type other words except yes it will quit 
if playing.lower() != "yes":
# if playing.upper() != "YES":
    quit() 
    
print("Okay ! Lets play ")
score = 0


answer = input("Which was the year in which India won the world cup? ")
# we can use upper lower wala function for answer 
if answer.lower() == "2011":
    print('Correct!') 
    # score = score +1
    score += 1
else:
    print('Incorrect')
    


answer = input("Who scored the most runs in ICC Mens World cup 2011? ")
if answer.lower() == "Tm Dilshan":
    print('Correct!')
    score += 1
else:
    print('Incorrect')
    


answer = input("Who took the most wickets in ICC Mens World cup 2011? ")
# we can use upper lower wala function for answer 
if answer.lower() == "Shahid Afridi":
    print('Correct!')
    score += 1
else:
    print('Incorrect')
    


answer = input("Which player has the highest individual score in ICC Mens World cup 2011? ")
# we can use upper lower wala function for answer 
if answer.lower() == "Australia":
    print('Correct!')
    score += 1
else:
    print('Incorrect')
    


answer = input("Who captained India in 2011 World Cup? ")
# we can use upper lower wala function for answer 
if answer.lower() == "Ms dhoni":
    print('Correct!')
    score += 1
else:
    print('Incorrect')
    

# concatination property of strings - adding two or more substrings to form single string 

print("Yot have got " + str(score) + " questions correct !!!")

print("Yot have got " + str((score/5) * 100 ) + " % !!!")

# "sharan " + 1(int) --> #does not make any sense 
# "sharan " + '1'(string)  --> "sharan1' 

