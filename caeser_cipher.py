LT2IN = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
IN2LT = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

key = int(input("Enter the key: "))


plain = input("enter password: ").upper()
converted = ""

for i in plain:
    if i.isalpha():converted = converted + IN2LT[(LT2IN[i]+key)%26]
print(converted)

converted2 = ""
for s in converted:
    converted2 = converted2 + IN2LT[(LT2IN[s]-key)%26]
print(converted2)
