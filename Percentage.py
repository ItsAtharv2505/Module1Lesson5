print("Enter the obtained marks:")

math = int(input("Enter the math marks:"))
english = int(input("Enter the english marks:"))
science = int(input("Enter the science marks:"))
hindi = int(input("Enter the hindi marks:"))

sum = math+english+science+hindi
print(sum)
perc = (sum/400)*100
print("The total percentage of Raj is:", perc)
