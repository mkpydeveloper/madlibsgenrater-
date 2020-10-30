from random import randint 
import copy 

story = (
     "one day my {} friend and i decided to go to the {} game in {}. " +
     "we really wanted to see the {} play the {}. " +
     "so we {} our {} down to the {} and bought {}s. " +
     "we got into the game and it was a lot of fun. " +
     "we ate some {} {} and drink some {} {}. " +
     "we had a great time we plan to go ahead next year. "
	)

# create a dictionary 

word_dict = {
	"adjective":["Adorable",	"Delightful","	Homely"
"Adventurous",	"Depressed",	"Horrible"
"Aggressive"	,"Determined"	,"Hungry",
"Agreeable",	"Different"	],
	"city name":["indore ", "mumbai ", "chennai ","bhopal",],
	"noun":["people","dog","cat","man","map","music"],
	"action verb":["run","fall","crawl","cry","watch","swim"],
	"sports noun":["ball","mit","puck","uniform","helmet"],
	"place":["park","home","campus","school","hotel"]

}

def get_word(type,local_dict):
	words = local_dict[type]
	count = len(words)-1 
	index = randint(0, count)
	return local_dict[type].pop(index)

def create_function():
	local_dict = copy.deepcopy(word_dict)
	return story.format(
		get_word('adjective',local_dict),
		get_word('sports noun',local_dict),
		get_word('city name',local_dict),
		get_word('noun',local_dict),
		get_word('noun',local_dict),
		get_word('action verb',local_dict),
		get_word('noun',local_dict),
		get_word('place',local_dict),
		get_word('noun',local_dict),
		get_word('adjective',local_dict),
		get_word('noun',local_dict),
		get_word('adjective',local_dict),
		get_word('noun',local_dict)

		) 
print("story 1:")
print(create_function())
print()
print("story 2:")
print(create_function())
