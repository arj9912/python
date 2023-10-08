
def percent(marks):
    return (sum(marks)/400)*100
marks1 = [45,78,86,77]
percentage = percent(marks1)

marks2 = [75,98,88,77]
# percentage2 = (sum(marks2)/400)*100
percentage2 = percent(marks2)
print(percentage,percentage2)