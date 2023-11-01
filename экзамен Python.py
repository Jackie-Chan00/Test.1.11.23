def capitalize_first_letter(words):
    capitalized_words = [word.capitalize() for word in words]
    return capitalized_words
input_words = ['bin', 'wheel', 'shadow']
result = capitalize_first_letter(input_words)
print(result)


#Ex-2

l = [1, 2, 3, 6, 12, 14, 21]
divisible_by_7 = []

for i in l:
    if (i%7==0):
        divisible_by_7.append(i)
print(divisible_by_7)

#Ex-3

def square_number(x):
    return x**2

def square_of_integers(numbers):
    squared_numbers = list(map(square_number, numbers))
    return squared_numbers

input_numbers = [2, 55, 876]
result = square_of_integers(input_numbers)
print(result)
