#завдання 1
x=10
print(x)
#завдання 2
a=5
b=3
arrea=a*b
print("Площа трикутника", arrea)
#Завдання 3
string='Hello,world!'
print(string)
#завдання 4
fruits=["apple","banana","orange"]
print(fruits)
#task 5
age={"john":25, 'Alice':30}
print("Age Alice", age["Alice"])
#task 6
my_tuple=(1,2,3)
if 2 in my_tuple:
    print ("number 2 found")
else:
    print("No found this number")
#task 7
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("united union",union_set)
#task8
with open("example.txt", "w") as file:
    file.write("Hello,world. \n")
    file.write("My name is Chikatillo.\n")
    file.write("Good by world")
with open("example.txt","r") as file:
    content=file.read()
    print(content)
#task9
names=["John","Alice","Bob"]
with open("names.txt","w") as file:
    for name in names:
       file.write(name + "\n")

#task 10

sum_of_numbers = 0

for num in range(1, 11):
    sum_of_numbers += num

print("Сума чисел від 1 до 10:", sum_of_numbers)

#task 11

string = "Hello, world!"
print(string[:5])
#task 12

numbers = [1, 2, 3, 4, 5]

numbers.append(6)

del numbers[0]

print(numbers)
#task 13
grades={"Math":90, "History":85}
if "Sciense" in grades:
    print("Key 'sciense'found in this dict")
else:
    print("No found this key")
#task 14
numbers=[1,2,3,4,5,6,7,8,9,10]
if 8 in numbers:
    print("Yes")
else:
    print("no")

numbers = [96, 69, 3, 54, 19]


with open("data.txt", "w") as file:

    for number in numbers:
        file.write(str(number) + "\n")


total_sum = 0
count = 0


with open("data.txt", "r") as file:

    for line in file:

        number = int(line.strip())
        total_sum += number
        count += 1


if count > 0:
    average = total_sum / count
else:
    average = 0

print("average:", average)
#task14
