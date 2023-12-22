#---------------------------TASK 1-----------------------------

# Make a program that has some sentence (a string) on input and returns a dict containing
# all unique words as keys and the number of occurrences as values. 

sentence = input("Shkruani një fjalë: ")

word = sentence.lower().split()

word_dictionary = {}

for i in word:
    word = ''.join(e for e in word if e.isalnum()) #It's used to clean the word from special characters and punctuation marks

    if i:  #to prevent the processing of empty or whitespace characters within the 'word' variable.
        if i in word_dictionary:
            word_dictionary[i] += 1
        else:
            word_dictionary[i] = 1

print("Numërimi i fjalëve:", word_dictionary)



#---------------------------TASK 2-----------------------------
# Input data:

# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# Create a function which takes as input two dicts with structure mentioned above, then computes
# and returns the total price of stock.

def calculate_total_price(stock, prices):
    total_price = 0

#This line unpacks each tuple from the list and assigns the first element to the 'item'
# variable and the second element to the 'quantity' variable.
    for item, quantity in stock.items(): 
        if item in prices:
            total_price += prices[item] * quantity

    return total_price

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = calculate_total_price(stock, prices)
print("Total price of stock: $", total_price)




#---------------------------TASK 3-----------------------------
# List comprehension exercise

# Use a list comprehension to make a list containing tuples (i, j) where i goes from 1 to 10 and j
# is corresponding to i squared.

result = [(i, i**2) for i in range(1, 11)]
print(result)