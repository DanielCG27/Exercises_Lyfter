def verify_positives(list):
    count_negatives= 0
    for num in list:
        if num <= 0:
            count_negatives += 1
    if count_negatives == 0:
        return True
    else:
        return count_negatives
list= [25, 5, -85, 98, -2, 74, 2, 9]
result= verify_positives(list)
if result is True:
    print("All elements of the list are positives")
else:
    print(f"There is at list one negative number. Count of negative numbers {result}")