# week 3 stuff\

name = input("what is your name?")
print(name)

age = (input('how old are you?'))

while not isinstance(age, int):
    try:
        age = int(age)
        age +=1
        print("Next year you will be", age)
    except ValueError:
        print('You must enter a number')
        age = input('How old are you?')

print('arg1','arg2', end =",", sep=',')
print('arg3', 'arg4', sep=",'")

file = open('top_ten_movies.txt')
text = file.read()
print(text)

with open('top_ten_movies.txt') as file:
    for line in file:
        print(line.rstrip()) #rstrip gets rid of the extra spaces

movies = []
with open('top_ten_movies.txt') as file:
    for line in file:
        movies.append(line.rstrip())
print(movies)

data = 'jose lopez 60'
new_data = data.split()
print(new_data)
name = new_data[0] + " " +new_data[1]
height = int(new_data[2])
print(name)
print(height)

names_and_heights = {}
with open('heights.txt') as file:
    for line in file:
        split_line = line.split()
        names_and_heights[split_line[0] + " " + split_line[1]] = int(split_line[2])
print(names_and_heights)

