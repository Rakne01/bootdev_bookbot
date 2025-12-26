from collections import Counter

def count_words(text):
	split_words = text.split()
	return len(split_words)

def count_characters(text):
	lower_text = text.lower()
	return Counter(lower_text)

def sort_on(items):
    return items["num"]

def sort_characters(char_text):
	new_list = []
	for key in char_text:
		new_dict = {}
		new_dict["char"] = key
		new_dict["num"] = char_text[key]
		new_list.append(new_dict)
	
	new_list.sort(reverse=True, key=sort_on)
	return new_list



# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries


# vehicles = [
#     {"name": "car", "num": 7},
#     {"name": "plane", "num": 10},
#     {"name": "boat", "num": 2}
# ]
# vehicles.sort(reverse=True, key=sort_on)
# print(vehicles)
# [{'name': 'plane', 'num': 10}, {'name': 'car', 'num': 7}, {'name': 'boat', 'num': 2}]
