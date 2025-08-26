# if...elif..else statement

# grade 0--->40->E
# 41  ----> 50 -> D
# 51  ----> 60 -> C
# 61  ----> 70  -> B
# 71 -----> 80  -> A


grade = int(input("Enter the score of a person "))

if grade >0 and grade<=40:
    print("You got an E.Improve next time")
elif grade >41 and grade <= 50:
    print("You Got D. Try Your level best next time")
elif grade > 51 and grade <= 60:
    print("You got a C.You can do better than this")
elif grade > 61 and grade <= 70:
    print("you got a B . The sky is the limit ")
elif grade > 71 and grade <=100:
    print("You got an A.That's wonderful. Maintain") 

else:
    print("invalid Score/grade.please try again")   
