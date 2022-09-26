def get_grade(score):
    if score > 90 and score <= 100:
        return 'A'
    elif score > 80 and score <= 90:
        return 'B'
    elif score > 70 and score <= 80:
        return 'C'
    else:
        return 'F'
    

score = int(input())
grade = get_grade(score)
print(grade) # A ~ F