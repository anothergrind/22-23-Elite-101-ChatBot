# Chatbot introduction
print("I'm Noel, a chatbot")
print("Feel free to ask me some questions or hold a conversation with me")

print("---------------------------------------------------------------------")
print()

# First question
# Asks user for a positive odd or even number, if not repeats
def main_question(): 
    starter_input = input("Enter an even number for a topic: ")
    starter = int(starter_input)
    print("---------------------------------------------------------------------")
    print()
    if (starter % 2 == 0):
        topic_route()
    else:
        main_question()

# Main topics and subtopics
topics = {
    "entertainment": ["soccer", "basketball", "football", "movies", "anime"],
    "school": ["tuition", "grades", "studying", "stem", "humanities", "admission"],
    "health": ["vaping", "smoking", "staying healthy", "habits"],
    "technology": ["artificial intelligence", "machine learning", "chatgpt", "deep learning", "natural language processing"],
    "business": ["nft", "affiliate marketing", "content creation", "tutoring", "online company"],
    "food": ["asian", "italian", "diets", "mexican"],
	"holiday": ["christmas", "mother's day", "thanksgiving", "memorial day", "new years"],
	"games": ["roblox", "minecraft", "call of duty", "fortnite", "overwatch 2"]
}

def topic_route():
    first_topic = input("What main topic do you want to talk about? " + str(list(topics.keys())))
    if first_topic in topics:
        sub_topic_route(first_topic)
    else:
        print("Sorry, I don't understand your input. Please choose a topic from the list.")
        topic_route()

def sub_topic_route(main_topic):
    print("Here are the subtopics for " + main_topic + ": " + str(topics[main_topic]))
    sub_topic = input("Which subtopic would you like to discuss? ")
    if sub_topic in topics[main_topic]:
        print("Let's talk about " + sub_topic + "!")
    else:
        print("Sorry, I don't understand your input. Please choose a subtopic from the list.")
        sub_topic_route(main_topic)

# Main loop that controls the chatbot
want_to_exit = ''
while want_to_exit != "Y": 
    main_question()
    want_to_exit = input("Do you want to exit the chatbot? (Y/N)")
