math=int(input("please enter your math grades."))
science=int(input("please enter your science grades."))
history=int(input("please enter your history grades."))
social_studys=int(input("please enter your social_studys grades"))
ela=int(input("please enter your ela grades"))
total=math+science+history+social_studys+ela
print("total", total)
average=total/5
print("average", average)
if average>=91 and average<=100:
    print("your grade is a1")
elif average>=81 and average<=91: 
    print("your grade is a2")
elif average>=71 and average<81: 
    print("your grade is b1")
