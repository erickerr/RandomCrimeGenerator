#! python3

__author__ = "Eric Kerr"
__copyright__ = "Copyright (C) 2017 Eric Kerr"
__license__ = "Creative Commons Attribution-NonCommercial 3.0 Unported License"
__version__ = "1.0"

#imports
import random
import fileinput
import sys
import time
from random import randint

#introduction
    
print("\n")
print("Welcome to the Random Crime Generator.")
print("\n")

#main loop

trial = 'Yes'
while trial == 'Yes' or 'yes' or 'Y' or 'y' or 'ok' or 'Okay' or 'OK':

    #define random name, random verb, and random noun

    def random_name():
        line_num = 0
        selected_line = ''
        with open('names.txt') as f:
            for line in f:
                line = f.readline()
                if not line: break
                line_num += 1
                if random.uniform(0, line_num) < 1:
                    selected_line = line
        return selected_line.strip()

    def random_verb():
        line_num = 0
        selected_line = ''
        with open('verbs.txt') as f:
            for line in f:
                line = f.readline()
                if not line: break
                line_num += 1
                if random.uniform(0, line_num) < 1:
                    selected_line = line
        return selected_line.strip()

    def random_noun():
        line_num = 0
        selected_line = ''
        with open('nouns.txt') as f:
            for line in f:
                line = f.readline()
                if not line: break
                line_num += 1
                if random.uniform(0, line_num) < 1:
                    selected_line = line
        return selected_line.strip()

    sample_name = random_name()
    sample_verb = random_verb()
    sample_noun = random_noun()
    sample_verb2 = random_verb()

    number = randint(1,40)
    years = str(number)

    #make sentence by combining name, verb, noun, and second verb
            
    def MakeSentence():

        x = sample_name + " stands accused of " + sample_verb + " " + sample_noun + " while " + sample_verb2 + "." #initialize sentence as such
        return x
    
    sample_sentence = MakeSentence()
    answers = [sample_name + " is guilty and has been sentenced to " + years + " years hard labour for " + sample_verb + " " + sample_noun + " while " + sample_verb2 + ".\n", sample_name + "'s crime has been judged not proven. The court will reassess the case once more evidence has been found.\n"]

    #judgment

    trial = input("The next accused awaits sentencing. Shall we begin the trial?\n") #continue playing?
    if trial in ('Yes', 'yes', 'Y', 'y', 'ok', 'Okay', 'OK'):
        print("\n")
        print("Bring in the accused!")
        print("\n")
        print(sample_sentence)
        print("\n")

        response = input("Is " + sample_name + " guilty?\n")
        if response in ('Yes', 'yes', 'Y', 'y', 'ok', 'Okay', 'OK'):
            print(random.choice(answers))
        else:
            print(random.choice(answers))

    else:
        print("Court is closed for today.")
        time.sleep(5)
        sys.exit(0)
     
else:
    print("Court is closed for today.")
    time.sleep(5)
    sys.exit(0)

#end execution
