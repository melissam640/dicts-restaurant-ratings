"""Restaurant rating lister."""


def restaurant_rating(text_file):
    
    text_file = open(text_file)
    rating_score = {}

    for line in text_file:
        words = line.rstrip().split(":") # [name of restaurant, rating]
        rating_score[words[0]] = words[1] # rating_score[name of resaturant (key)] = rating (value) => {name of restaurant: rating}
    rating_score_items = sorted(rating_score.items()) # {[(key, value), (key, value), (key, value)]}
    print(rating_score_items)
    # for key, vaue in rating_score.items():
    #     print(restaurant_rating(f"{key} {vaue}"))
    

        
