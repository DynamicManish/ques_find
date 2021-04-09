#Hi, This is a question finder
#It will take inputs, will check if it is an interrogative user_input, will make it capitalized cased and will arrange it in the form of a sentence

def question_finder(sentence):
    sentence = sentence.capitalize()
    if sentence.startswith(('What','When','How','Is','Whom','Why','Whose','Howdy')):
        return "{}?".format(sentence)
    else:
        return "{}.".format(sentence)

user_data = []

while True:
    user_input = input("Type a sentence: ").strip()
    Stop = user_input.lower()
    if Stop == 'stop':
        break
    else:
        user_data.append(question_finder(user_input))

        
# print(" ".join((user_data))),this line of command can be used also
for inputs in user_data: #at this time, I am using this one :)
    print(inputs,end=" ")
