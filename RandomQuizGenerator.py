#! python3
# RandomQuizGenerator.py - Creates quizzes with questions and answers in random order,
#  along with the answer key.

import random
import os

# set the list of capitals for the quizzes:

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New \
   Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West \
   Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# create directory for the files if it doesn't already exist and navigate to it

desired_dir = os.path.join(os.getcwd(), 'GeneratedQuizzes')

if not os.path.isdir(desired_dir):
    os.makedirs(desired_dir)

os.chdir(desired_dir)

# generate 35 quiz files

for quizNum in range(35):
    # create the quiz and answer key files
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(('' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # write out the header for the answer key
    answerFile.write('Answer key for State Capitals Quiz (Form %s)' % (quizNum + 1))
    answerFile.write('\n\n')

    # shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # loop through all 50 states, making a question and answer
    for st in states:
        quizFile.write('What is the capital of %s?\n' % st)
        answerFile.write('The capital of %s is %s.\n' % (st, capitals[st]))

    # close the files
    quizFile.close()
    answerFile.close()
