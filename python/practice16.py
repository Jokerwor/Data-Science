# Greatest of four numbers
sub1 = int(input("Enter the value of a:"))
sub2 = int(input("Enter the value of b:"))
sub3 = int(input("Enter the value of c:"))
total_percentage = (sub1 + sub2 + sub3)/300*100
if(total_percentage>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("pass",total_percentage)
else:
    print("fail",total_percentage)
