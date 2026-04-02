import art
print(art.logo)

bid={}

flag="yes"
while flag=="yes" :
    key=input("What is your name?")
    value=int(input("What is your bid? $"))
    bid[key]=value
    flag=input("Are there any other bidders? Type 'yes or 'no'.")

max=0
max_name=""
for thing in bid:
    if max<bid[thing]:
        max=bid[thing]
        max_name=thing

print(f"The winner is {max_name} with a bid of ${max}.")