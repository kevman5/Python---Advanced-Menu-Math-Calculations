# -*- coding: utf-8 -*-
"""

@author: kevmm
"""
import random

def intro():
    title = "~ Final Project Quiz ~"
    print(title)

def show_separator():
    print("-" * 24)
    
def main_menu():
    menu_list = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Division", "5. Exit"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])
    print(menu_list[3])
    print(menu_list[4])

def get_user_input():
    user_input = int(input("Enter your choice: "))
    while user_input > 5 or user_input <= 0:
        print("Invalid option.")
        user_input = int(input("Please try again: "))
    else:
        return user_input

def get_user_solution(problem):
    print("Enter your answer")
    print(problem, end="")
    result = int(input(" = "))
    return result

def check_answer(user_solution, solution, count):
    if user_solution == solution:
        count = count + 1
        print("Correct.")
        return count
    else:
        print("Incorrect.")
        return count


def menu_option(index, count):
    number_one = random.randrange(1, 21)
    number_two = random.randrange(1, 21)
    if index is 1:
        problem = str(number_one) + " + " + str(number_two)
        solution = number_one + number_two
        user_solution = get_user_solution(problem)
        count = check_answer(user_solution, solution, count)
        return count
    elif index is 2:
        problem = str(number_one) + " - " + str(number_two)
        solution = number_one - number_two
        user_solution = get_user_solution(problem)
        count = check_answer(user_solution, solution, count)
        return count
    elif index is 3:
        problem = str(number_one) + " * " + str(number_two)
        solution = number_one * number_two
        user_solution = get_user_solution(problem)
        count = check_answer(user_solution, solution, count)
        return count
    else:
        problem = str(number_one) + " // " + str(number_two)
        solution = number_one // number_two
        user_solution = get_user_solution(problem)
        count = check_answer(user_solution, solution, count)
        return count


def result(total, correct):
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    if total == 0:
        percentage = 0
    print("You answered", correct, "correct", "out of", total)
    print("Your score is ", percentage, "%.", sep = "")


def main():
    intro()
    main_menu()
    show_separator()

    option = get_user_input()
    total = 0
    correct = 0
    while option != 5:
        total = total + 1
        correct = menu_option(option, correct)
        option = get_user_input()

    print("Exit.")
    show_separator()
    result(total, correct)

main()