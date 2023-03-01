# ********** list not mutable if re-assigned **********
# first_list = ["Awni", "Ahmed", "Yumna"]
# second_list = first_list
#
# print(second_list, "Before")
#
# first_list = ["Mariam"]
# print(second_list, "After")
# **********************************************************************************************************************
# *************************************** Total sum in list ***************************************
# price = [10, 20, 30]
# i = 0
# result = 0
# while i < len(price):
#     result = result + price[i]
#     i+=1
# print(result)
# ********** Another Total sum in list **********
# prices = [10, 20, 30, 40]
# result = 0
# for one_price in prices:
#     result += one_price
# print(f"The sum of the prices = {result}")
# **********************************************************************************************************************
# *************************************** find Max and Min in a list ***************************************
# list_of_numbers = [10, 3, 5, 76, 324,-545645, 656]
# maximum = list_of_numbers[0]
# minimum = list_of_numbers[0]
# for number in list_of_numbers:
#     if maximum < number:
#         maximum = number
#     if minimum > number
#         minimum = number
# print(f"Maximum = {maximum}")
# print(f"Minimum = {minimum}")
# **********************************************************************************************************************
# *************************************** Prime numbers in a list ***************************************
# numbers = []
# for x in range(1, 600):
#     numbers.append(x)
# print(numbers)
# prime_numbers = []
# for x in numbers:
#     flag = 0
#     for y in range(1, x):
#         if x % y == 0:
#             flag += 1
#     if flag == 1:
#         prime_numbers.append(x)
# print(prime_numbers)
# *************************************** Prime numbers in a list another way ***************************************
# numbers = []
# for x in range(1, 600):
#     numbers.append(x)
# print(numbers)
# prime_numbers = []
# for x in numbers:
#     if x > 1:
#         for i in range(2, x):
#             if (x % i) == 0:
#                 break
#         else:
#             prime_numbers.append(x)
# print(prime_numbers)
# **********************************************************************************************************************
# *************************************** Car Engine ***************************************
# car_status = False
# user_input = input("Enter Your Command to The Car: ")
# while user_input != "QUIT":
#     if user_input == "START":
#         if car_status:
#             print("Car is Already Started")
#         else:
#             print("Car is Starting")
#             car_status = True
#     elif user_input == "STOP":
#         if not car_status:
#             print("Car Already Stopped")
#         else:
#             print("Car is Stopping")
#             car_status = False
#     elif user_input == "HELP":
#         print("START: Starts the car engine!\n"
#               "STOP: stops the car engine\n"
#               "QUIT: to QUIT the app")
#     else:
#         print("Invalid Command")
#     user_input = input("Enter your command: ")
# else:
#     print("The Car is Quitting life and is going to die and rest in peace!!!!!\n"
#           "Goodbye Cruel world.\n"
#           "I'm Heading to the Spring")
#     exit()
# **********************************************************************************************************************
# *************************************** change text to emojies ***************************************
# emojies = {
#     "happy": ":)",
#     "sad": ":("
# }
# user_input = input("Enter your status:> ")
# statement = user_input.split(" ")
#
#
# def change(any_list, any_dictionary):
#     result = ""
#     for words in any_list:
#         result += any_dictionary.get(words, words) + " "
#     print(result)
#
#
# change(statement, emojies)
# *************************************** numbers to text ***************************************
# number_in_words = {
#     "0": "Zero",
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine"
# }
# numbers = input("Enter Your numbers")
# digits = numbers.split(" ")
# result = ''
# for digit in digits:
#     result += number_in_words.get(digit, digit) + ' '
# print(result)
# **********************************************************************************************************************
# *************************************** Trying functions ***************************************
# def whatever(x, y, z):
#     print(x, y, z)
#
#
# whatever(3, y=7, z=9)
# **********************************************************************************************************************
# *************************************** infinite arguments ***************************************
# def compare_numbers(limit, added_value, *numbers):
#     for number in numbers:
#         if number > limit:
#             print(number)
#         if number < limit:
#             print(number + added_value)
#
#
# compare_numbers(5, 3, 1, 10, 9, 60)
# **********************************************************************************************************************
# *************************************** class explanation ***************************************
# class Shape:
#     def __init__(self, type_of_shape, color_of_shape):
#         self.type_of_shape = type_of_shape
#         self.color_of_shape = type_of_shape
#
#     def display_type_color(self):
#         print(f"This shape is {self.type_of_shape} and its color is {self.color_of_shape}")
#
#
# shape_one = Shape("Square", "Blue")
# shape_one.display_type_color()
# **********************************************************************************************************************
# *************************************** vowels in string ***************************************
# def spot_vowels(txt):
#     i = 0
#     characters = [*txt]
#     vowels_characters = ["a", "e", "i", "o", "u"]
#     vowels_list = []
#     for character in characters:
#         if character in vowels_characters:
#             vowels_list.append(character)
#     print(vowels_list)
#
#
# spot_vowels("Me and the boys running after a cat")
# **********************************************************************************************************************
# *************************************** convert to roman numeral ***************************************
# def convert_to_roman(num):
#     if num < 1 or num > 1000:
#         print("Number out of range!")
#     else:
#         con = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
#         rom = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
#         result = ""
#         for i in range(0, len(con)):
#             while num >= con[i]:
#                 num -= con[i]
#                 result += rom[i]
#         print(result)
#
#
# number = int(input("Enter the Number you want to convert to Roman numeral:> "))
# convert_to_roman(number)
# **********************************************************************************************************************
# *************************************** check if text is palindrome ***************************************
# def check_text_is_palindrome(txt):
#     characters = [*txt]
#     characters_number = len(characters)
#     i = 0
#     while i <= characters_number/2:
#         if characters[i] == characters[-1-i]:
#             i += 1
#             continue
#         else:
#             print("The text is not Palindrome")
#             break
#     else:
#         print("The text is Palindrome")
#
#
# text = input("Enter the text to check if it is Palindrome or not:> ")
# check_text_is_palindrome(text)
# **********************************************************************************************************************
# *************************************** Draw a donut using turtle library ***************************************
# import turtle
# tr = turtle.Screen()
# tr.title("Draw a Donut")
# turtle.bgcolor("black")
# pen = turtle.Turtle()
# pen.color("pink")
# pen.pensize(3)
# pen.speed(9)
# pen.up()
# pen.forward(-50)
# pen.left(90)
# pen.down()
# for a in range(30):
#     for b in range(3):
#         pen.forward(10)
#         pen.left(30)
#
#     for c in range(10):
#         pen.right(15)
#         pen.forward(10)
#
#     pen.right(29)
#
#     for d in range(5):
#         pen.forward(10)
#
#     for e in range(5):
#         pen.right(12)
#         pen.forward(10)
#
#     for f in range(8):
#         pen.forward(10)
# turtle.done
print("This is just for testing the git push and the git pull")
