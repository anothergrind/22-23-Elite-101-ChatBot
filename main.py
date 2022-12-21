# Chatbot introduction 
print("I'm Noel, a chatbot")
print("Feel free to ask me some questions or hold a conversation with me")

print("---------------------------------------------------------------------")
print()

# First question 
# Asks user for a positive odd or even number, if not repeats

starter_input = input("Enter an odd number for a Q/A session and an even number for a conversation: ")
starter = int(starter_input) 

while starter < 1:
	starter_input = input("Odd number for Q/A  and Even number for a convo: ")
	starter = int(starter_input)
print("---------------------------------------------------------------------")
print()

# Q/A Route 
if (starter % 2) == 1: 
	print("Ask any appriopriate question")

# Conversation Route 
if (starter % 2) == 0 :
	world_cup_input = input("What are your thoughts on the world cup")
	
