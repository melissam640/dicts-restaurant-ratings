"""Restaurant rating lister."""


def restaurant_rating(text_file):
    
    text_file = open(text_file)
    rating_score = {}

    for line in text_file:
        words = line.rstrip().split(":") # [name of restaurant, rating]
        rating_score[words[0]] = words[1] # rating_score[name of resaturant (key)] = rating (value) => {name of restaurant: rating}
    rating_score_items = sorted(rating_score.items()) # {[(key, value), (key, value), (key, value)]}

    for key, value in rating_score_items:
        print(f"{key} {value}")
    

        
