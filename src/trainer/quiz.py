from src.trainer.data_reader import read_questions
from random import randint

from src.trainer.utils import clean_screen, Bcolors


def calculate_result(answers):
    correct_answers = 0
    for answer in answers:
        if answer.get_user_answer().upper() == answer.get_right_answer():
            correct_answers += 1
    return ResultSummary(correct_answers, len(answers))


def evaluate(answer):
    if answer.get_user_answer().upper() == answer.get_right_answer():
        print(Bcolors.OKGREEN + "Correct!" + Bcolors.ENDC)
    else:
        print(Bcolors.FAIL + "Incorrect! Correct answer is " + answer.get_right_answer() + Bcolors.ENDC)


def new_quiz():
    quiz_size = 2
    questions = read_questions()
    answered_questions = []  # Used to ensure we don't ask the same question twice
    results = []
    for i in range(quiz_size):
        while True:
            question_id = randint(0, len(questions)-1)
            if question_id not in answered_questions:
                answered_questions.append(question_id)
                break
        question = questions[question_id]
        clean_screen()
        print(Bcolors.BOLD + question["question"] + Bcolors.ENDC)
        for answer in question["answers"]:
            print(answer["id"] + ")" + " " + answer["answer"])
        user_answer = input("Answer: ")
        answer_record = AnswerRecord(question["id"], user_answer, question["correctId"])
        results.append(answer_record)
        evaluate(answer_record)

    return calculate_result(results)


class AnswerRecord:
    def __init__(self, question_id, user_answer, right_answer):
        self.question_id = question_id
        self.user_answer = user_answer
        self.right_answer = right_answer

    def get_user_answer(self):
        return self.user_answer

    def get_right_answer(self):
        return self.right_answer

    def get_question_id(self):
        return self.question_id


class ResultSummary:
    def __init__(self, correct_answers_count, total_count):
        self.correct_answers_count = correct_answers_count
        self.total_count = total_count

    def get_correct_answers_count(self):
        return self.correct_answers_count

    def get_total_count(self):
        return self.total_count