amount=int(input("please enter your amount "))
note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10
print("notes of hundred dollers", note_1)
print("notes of 50 dollers", note_2)
print("notes of 10 dollers", note_3)