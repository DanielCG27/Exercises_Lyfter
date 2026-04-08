num= int(input("Put your grades quantity"))
total_sum= 0
approve_sum= 0
approve_counter= 0
disapprove_sum= 0
disapprove_counter= 0
for i in range(num):
    grade= float(input(f"Show your grade {i + 1}: "))
    total_sum += grade
    if grade > 70:
        approve_sum += grade
        approve_counter += 1
    elif grade < 70:
        disapprove_sum += 1
        disapprove_counter += 1
total_average= total_sum / num
if approve_counter > 0:
    approve_average= approve_sum / approve_counter
else:
    approve_average= 0
if disapprove_counter > 0:
    disapprove_average= disapprove_sum / disapprove_counter
else:
    disapprove_average= 0
print("Approve grades :", approve_counter)
print("Disapprove grades:", disapprove_counter)
print("Total average:", total_average)
print("Approve average:", approve_average)
print("Disapprove average:", disapprove_average)