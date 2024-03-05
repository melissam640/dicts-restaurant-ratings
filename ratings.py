"""Restaurant rating lister."""


def restaurant_rating(text_file):
    
    def sort_and_print(dictionary):
        rating_score_items = sorted(dictionary.items())
    
        for key, value in rating_score_items:
            print(f"{key} is rated at {value}")
    
    text_file = open(text_file)
    rating_score = {}

    for line in text_file:
        words = line.rstrip().split(":") # [name of restaurant, rating]
        rating_score[words[0]] = words[1] # rating_score[name of resaturant (key)] = rating (value) => {name of restaurant: rating}
    
    sort_and_print(rating_score)
    
    user_restaurant = input("Please type a restaurant name")
    user_rating = input("Please add a score")
    rating_score[user_restaurant] = user_rating

    sort_and_print(rating_score)
    

        
