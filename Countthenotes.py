amount = int(input("How much would you like to withdraw:"))

note1 = amount//100
note2 = (amount%100)//50
note3 = ((amount%100)%50)//10

print(note1)
print(note2)
print(note3)