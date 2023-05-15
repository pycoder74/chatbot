import numpy as np
greetings = np.array(["Hello.", "Hi!", "Hey!", "Hey there!"])
questions = np.array(["How can I help?", "What can I do for you?", "What do you need help with?"])
Hellos = np.concatenate((greetings, questions))
