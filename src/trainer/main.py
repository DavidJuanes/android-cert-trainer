from src.trainer.quiz import new_quiz
from src.trainer.utils import clean_screen


def get_app_version():
    file_object = open("version_no", "r")
    return file_object.readline()


def set_user():
    name = input("Username: ")
    file_object = open("data/current_username", "w")
    file_object.write(name)


def get_user():
    file_object = open("data/current_username", "r")
    return file_object.readline()


def print_menu():
    print("\t1. Start new test")
    print("\t2. Change username")
    print("\t3. Exit")


print("Android Certification Exam Trainer -- v." + get_app_version())
print("===============================================\n")
if get_user() is "":
    print("First of all, specify a username so I can track your progress...")
    set_user()
print("Hi " + get_user() + "!")

while True:
    print_menu()
    option = input("Select an option: ")
    if option == "1":
        result_summary = new_quiz()
        clean_screen()
        print("You answered " + str(result_summary.get_correct_answers_count()) + " correctly out of " + str(result_summary.get_total_count()))
        print("====================================")
    if option == 2:
        set_user()
    if option == 3:
        quit(0)
    clean_screen()













