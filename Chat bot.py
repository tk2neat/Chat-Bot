#Lots of websites use chatbots to interact with their customers.  These chatbots are often very sophisticated and use AI to learn and adapt to the user.  Our chat bot is going to be a bit simpler.

#The chatbot should work like this:

#Ask the user their name and store it in a variable.
name = input("What is your name? \n")
#Greet the user by name.
print("Hello " + name)
#Ask the user three questions about themselves and store their responses in three different suitably named variables.
colour = input("What is your favourite colour? \n")
animal = input("What is your favourite animal? \n")
food = input("what is your favourite food? \n")

#Respond to each of the questions one by one, using the user’s name in the response.
print("your favourite colour is " + colour + "? I like that colour too " + name + "\n")
print("your favourite animal is " + animal + "? thats so cool " + name + "\n")
print("your favourite food is " + food + "? I like spicy food " + name + "\n")
#Output a summary of all of the user’s answers in a single sentence.
print("So your favourite colour is " + colour + " your favourite animal is a " + animal + " and your favourite food is " + food + " thats so unique!")