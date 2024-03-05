"""Restaurant rating lister."""

    
def sort_and_print(dictionary):
    rating_score_items = sorted(dictionary.items())
    
    for key, value in rating_score_items:
        print(f"{key} is rated at {value}")
        
    
def restaurant_rating(text_file):
    text_file = open(text_file)
    rating_score = {}

    for line in text_file:
        words = line.rstrip().split(":") # [name of restaurant, rating]
        rating_score[words[0]] = words[1] # rating_score[name of resaturant (key)] = rating (value) => {name of restaurant: rating}
    
    return rating_score

    
def user_restaurant_input(dictionary):
    user_restaurant = input("Please type a restaurant name")
    user_rating = input("Please add a score")
    dictionary[user_restaurant] = user_rating

    return dictionary
    

        
