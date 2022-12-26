# Chatbot introduction
print("I'm Noel, a chatbot")
print("Feel free to ask me some questions or hold a conversation with me")

print("---------------------------------------------------------------------")
print()

# First question
# Asks user for a positive odd or even number, if not repeats
def main_question(): 
	starter_input = input("Enter an odd number for Q/A and an even number for a topic: ")
	starter = int(starter_input)
	print("---------------------------------------------------------------------")
	print()
	if (starter % 2 == 0):
		topic_route()
	elif (starter % 2 == 1): 
		question_answer_route()
	else:
		main_question()

def question_answer_route(): 
	first_qa = input("What are your thoughts on the world cup")
	print("That's great, I thought the world cup was amazing in my opinion")

def topic_route():
	first_topic = input("What main topic do you want to talk about? [entertainment, school, heath, technology, business, & food]")

main_topic = [
 "entertainment", "school", "health", "technology", "business", "food"
]

#Subtopics for each main topic
entertainment_sub_topics = [
 "soccer", "basketball", "football", "movies", "anime"
]
school_sub_topics = [
 "tuition", "grades", "studying", "stem", "humanities", "admission"
]
health_sub_topics = ["vaping", "smoking", "staying healthy", "habits"]
technology_sub_topics = [
 "artificial intelligence", "machine learning", "chatgpt", "deep learning",
 "natural language processing"
]
business_sub_topics = [
 "nft", "affiliate marketing", "content creation", "tutoring", "online company"
]
food_sub_topics = [
 "asian",
 "italian",
 "diets",
 "mexican",
]

# Main loop that controls the chatbot
want_to_exit = ''; 
while want_to_exit != "Y": 
	main_question()
	want_to_exit = input("Do you want to exit the chatbot? (Y/N)")		

# Topic Based Route
# Ask about a main topic

