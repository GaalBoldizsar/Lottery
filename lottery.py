# -*- coding: utf-8 -*-
import random

lottery_list = []
count = 0


# --- Sorsolas ---------------------------------
def sorsolas(lottery_list, count):

    allNumbers = 0
    pull = 99999999

    # - Numbers Variation + Validation
    while allNumbers < 10:
        allNumbers = int(raw_input("Variation of numbers (more than 10): "))

    # - Pulls Number + Validation
    while pull > allNumbers:
        pull = int(raw_input("Pulls number (less than variation): "))

    while count < pull:
        addNumber = random.randint(1, allNumbers)

        # --- If already pulled Pass it --
        if addNumber in lottery_list:
            pass
        else:
            lottery_list.append(addNumber)
            count += 1


# --- Numbers to ascending order --------------
def sorbarendezes(numbers):
    print(sorted(numbers, key=int))


# --- Main Function ---------------------------
def main(lottery_list):
    sorsolas(lottery_list, count)
    sorbarendezes(lottery_list)


if __name__ == "__main__":
    main(lottery_list)