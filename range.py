

#Let's assume I have need a number 
#From 1 - 10
# I can use range to fix this. 

for number in range(1,10):
    print(number)
#something to note is that, because 10 is specified doesn't mean it prints it to the last number
#so we change it to 11
for number in range(1,11):
    print(number)
#if I want to put this number's in a list then .# 
def list_range():
    numbers = list(range(1,11))
    print(numbers)
list_range()
#adding a third argument to range, to skip numbers 
for even_number in range(0,6,2):
    print(even_number)
list_item= []
for even_number in range(1,10):
    list_item.append(even_number)
list_item_= []
for item in list_item:
    list_item_.append(item + item + 1)

print(list_item_)



