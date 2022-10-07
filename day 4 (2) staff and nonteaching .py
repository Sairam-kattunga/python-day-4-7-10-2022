total_users=int(input("Enter Total Users: "))
staff_users=int(input("Enter Staff Users: "))
non_teaching=staff_users//3
staff_users=staff_users+non_teaching
student_users=total_users-staff_users
if (total_users>staff_users and total_users>0 and staff_users>0):
    print("Student Users= ",student_users)
elif ((total_users<staff_users) or (total_users is staff_users)):
    print("enter a valid input")
else:
    print("invalid")
