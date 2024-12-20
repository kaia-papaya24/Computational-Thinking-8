# Beginning:
messy_points = 0
notmessy_points = 0

# Middle:
answer = input ("If you got your man taken, would you rather A) leave him and mind your buisness, or B)beat up/ yell at the girl he left you for?\n")
if answer == "A":
    notmessy_points += 1
elif answer == "B":
    messy_points += 1


answer = input ("If someone was talking bad about you at school, would you A) curse her out and possibly fight her, or B) have a calm conversation with her?\n")
if answer == "B":
    notmessy_points += 1
elif answer == "A":
    messy_points += 1


answer = input ("If your friend confided in you and told you she cheated on her bf, do you A) leave it alone, or B) tell him about it?\n")
if answer == "A":
    notmessy_points += 1
elif answer == "B":
    messy_points += 1


answer = input ("If someone posted something mean about you online, would you A) ask them to take it down or,B) post blackmail on them?\n")
if answer == "A":
    notmessy_points += 1
elif answer == "B":
    messy_points += 1


    answer = input ("If you were talking bad about your friend and they were standing behind you the whole time would you A)deny it and gaslight them or, B)have a conversation with them and apologize?\n")
if answer == "A":
    messy_points += 1
elif answer == "B":
    notmessy_points += 1
#End:

if messy_points > notmessy_points:
    print("You are a messy gyal")
elif notmessy_points > messy_points: 
    print("You are not a messy gyal")
elif messy_points == notmessy_points:
    print("You are kind of a messy gyal")