'''

ID : C0860583
Name : Praveen Mahaulpatha

'''



print("\n############################ Question 4.1 ############################\n")

myPizza = ["BBQ Chicken", "Pepperoni","Thin Crust"]

for i in range(len(myPizza)):
    print(f"I like {myPizza[i]}")

print(f"\nI like different pizzas.\nMy most favourits are {myPizza}\nAt one time I had too much of it."
      f"\nSo now I don't love em anymore. ")

print("\n############################ Question 4.2 ############################\n")
animalList = ["Lion","Tiger","Cougar"]

for animal in animalList:
    print(f"A {animal} would make a great pet. Only for a Circus.")

print("\nAll these animnals are like your cat at home but about might eat you for lunch ")

print("\n############################ Question 4.3 ############################\n")
for i in range(20):
    print(i+1)

print("\n############################ Question 4.4 ############################\n")
millionList = range(1,1000001)

# for i in millionList:
#     print(i)



print("\n############################ Question 4.5 ############################\n")
from datetime import datetime
print(min(millionList), max(millionList))
start_time = datetime.now()
print("Sum: ",format(sum(millionList),","))
end_time = datetime.now()
print('Time taken to sum 1 million: {}'.format(end_time - start_time))


print("\n############################ Question 4.6 ############################\n")
oddList =[]
for num in range(1,20,2):
    oddList.append(num)

for i in oddList:
    print(i)

print("\n############################ Question 4.13 ############################\n")

buffet = ('Biscuit', 'watermelon','onion','Boiled Eggs','Sushi')

for fd in buffet:
    print(fd)

try :
    buffet[0] = 'Water'
except TypeError:
    print("\nTypeError: 'tuple' object does not support item assignment\n")

buffet = ('Donut','Bagel','Biscuit','onion','Boiled Eggs')

for fd in buffet:
    print(fd)

print("\n############################ Question 8.3 ############################\n")

def make_shirt(size='Large',text="I love Python"):
    print(f"The size of the shirt is {size} and the printed message is \"{text}\"")

make_shirt('XXL', "Yes, I like piña coladas")

print("\n############################ Question 8.4 ############################\n")

make_shirt('large')
make_shirt('Medium')
make_shirt('XS',"I believe I can Fly")

print("\n############################ Question 8.5 ############################\n")

def describe_city(city,country='Sri Lanka'):
    print(f"{city} is in {country}")

describe_city('Colombo')
describe_city('Negombo')
describe_city('Zarragoza','Spain')


print("\n############################ Question 8.6 ############################\n")

def city_country(city,country):
    print(f"{city}, {country}")

city_country('Colombo','Sri Lanka')
city_country('Moscow','Russia')
city_country('Rome','Italy')

print("\n############################ Question 8.7 ############################\n")

def make_album(name,title,Num=None):
    desc = {'Artist Name':name,'Album name':title,'Number of Songs':Num}
    return desc

album1 = make_album('John Lennon','Imagine',5)
album2 = make_album('Guns and Roses','Bad Obsession',10)
album3 = make_album('Live','Police')

print(album1,album2,album3)

print("\n############################ Question 8.8 ############################\n")

val = 0

while val<3:
    artName = input("Please enter Artist Name: ")
    albumName = input("Please enter Album Name: ")
    numofSongs = int(input("Please enter number of Songs: "))

    print(make_album(artName,albumName,numofSongs))

