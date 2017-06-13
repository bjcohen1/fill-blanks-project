#Store questions and answers here
easy_string = '''1 is the major language of the internet. 2 is a way we can give style to our webpages. When writing programs we use 3 to minimize repetition.
We can use 4 to convert inputs and outputs.'''
easy_answers = ["place_holder","html","css","loops","functions"]

medium_string = '''A 1 loop usually requires a counter, whereas a 2 loop does not. The 3 function can exchange one word in a string for another.
Every item on a list has an 4 that corresponds to its 5 in the list.'''
medium_answers = ["place_holder", "while", "for", "replace", "index", "position"]

hard_string = '''We can break strings into lists using the 1 function and put them back together using the 2 function.  The 3 function will provide all of the
numbers from x to x-1.  We can request user input using the 4 function and generate random numbers using the 5 function. Coding is a 6 way to spend your vacation!'''
hard_answers = ["place holder", "split", "join", "range", "raw_input", "randint", "great"]

print "Welcome to the quiz!"

#function that takes in the string until this point and replaces a blank with a correct answer
def print_with_new(string, old, new):
	string = " ".join(string)
	string = string.replace(old,new)
	print string
	string = string.split(" ")
	return string
#function containing the loops for multiple tries for incorrect responses--takes user guess as input and outputs the correct answer in place in the quiz if correct, if
    #incorrect, give user another chance until out of chances
def try_again(string, blank_evaluated, answer):
    try_counter = 3
    no_more_chances = 0
    print "Try again " + str(try_counter) + " chances remaining"
    while try_counter > no_more_chances:
        user_input = raw_input("Answer " + blank_evaluated + ":").lower()
        if user_input == answer[int(blank_evaluated)]:
            print "Correct!"
            string = print_with_new(string, blank_evaluated, user_input)
            try_counter = 0
        else:
            try_counter -= 1
            if try_counter == no_more_chances:
                print "No Chances Remaining!"
                return string, try_counter
            else:
                print "Try again " + str(try_counter) + " chances remaining"
    return (string, try_counter)

#function to play the game--inputs are the unfilled in quiz, the answer key, and the number of blanks in the quiz and the outputs are either the filled in quiz if the
    #players gets the answers correct or a prompt to try again if incorrect with number of tries remaining

def fill_the_quiz(string_1, answer_key, number_of_blanks):
    print string_1
    string_1 = string_1.split()
    for word in string_1:
        if word in str(range(number_of_blanks+1)):
            user_input = raw_input("Answer " + word + ":").lower()
            if user_input == answer_key[int(word)]:
                print "Correct!"
                string_1 = print_with_new(string_1, word, user_input)
            else:
                string_1 = try_again(string_1 ,word, answer_key)
                if string_1[1] == 0:
                    return "Game over, you lose!"
    return "You Win!"

#Have user input the difficulty level to determine which quiz will be presented, use the outputs of that input to serve as the the quiz questions, answer set,
    #and number of blanks in the quiz.
def choose_difficulty():
    difficulty = raw_input("Would you like to play Easy, Medium, or Hard?").lower()
    if difficulty == "easy":
        test_string = easy_string
        answer_key = easy_answers
        number_of_blanks = 4
    elif difficulty == "medium":
        test_string = medium_string
        answer_key = medium_answers
        number_of_blanks = 5
    elif difficulty == "hard":
        test_string = hard_string
        answer_key = hard_answers
        number_of_blanks = 6
    else:
        choose_difficulty()
    print fill_the_quiz(test_string, answer_key, number_of_blanks)

choose_difficulty()

