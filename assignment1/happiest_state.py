import sys
import json
import operator

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


def main():
    sent_file = open(sys.argv[1]) # AFINN-111.txt
    tweet_file = open(sys.argv[2]) # output.txt
    
    # Build up word dictionary
    scores = {} # empty dictionary
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score) # Convert to int

    # Build up state reverse lookup table
    states_reverse = {}
    for key, value in states:
        states_reverse[value] = key

    # Build up state happiness dictionary
    states_happiness = {}
    for key in states.keys():
        states_happiness[key] = 0.0

    # Build up state number of twitter dictionary
    states_tweets = {}
    for key in states.keys():
        states_tweets[key] = 0.0
    
    # Parse the data in output.txt
    for line in tweet_file:
        tweet = json.loads(line, encoding="utf-8") # tweet is a dict
        text_info = tweet.get("text") # type() == 'unicode'
        text_lang = tweet.get("lang")

        # Location info
        tweet_coordinates = tweet.get("coordinates")
        tweet_place = tweet.get("place")

        # For each tweet
        # if has text and is English and has place
        if text_info and text_lang == "en" and (tweet_coordinates or tweet_place):

            # Get the address
            address = str(tweet_place["full_name"].encode("utf-8"))
            parsed_address = address.split(", ")
            # print parsed_address

            location = None
            for each_address in parsed_address:
                if each_address in states.keys():
                    location = each_address
                elif each_address in states_reverse.keys():
                    location = states_reverse.get(each_address)
                # print location

                if location:
                    text_info = text_info.encode("utf-8") # type() == 'str'
                    text_word_list = text_info.split() # Change to word sequence rather than byte

                    pos_score = 0 # Score of positive words
                    neg_score = 0 # Score of negative words, IS positive value
                    num_word = 0
                    while num_word < len(text_word_list):
                        # Remove common punctuations
                        if text_word_list[num_word][-1] in "\'\"!()-[]{};:\,<>./?@#$%^&*_~":
                            text_word_list[num_word] = text_word_list[num_word][0:-1]
                        elif text_word_list[num_word][0] in "\'\"!()-[]{};:\,<>./?@#$%^&*_~":
                            text_word_list[num_word] = text_word_list[num_word][1:]
                        word = text_word_list[num_word]
                        # print word

                        # Eval each sentiment word
                        if scores.get(word):
                            word_value = scores.get(word)
                            if word_value > 0:
                                pos_score += word_value
                            elif word_value < 0:
                                neg_score -= word_value

                        # Next word
                        num_word += 1

                    states_happiness[location] += (pos_score - neg_score)
                    states_tweets[location] += 1

        else: # if empty text or not English
            pass

    # Normalization
    for key in states.keys():
        if states_tweets[key]:
            states_happiness[key] = states_happiness[key] / states_tweets[key]

    sorted_happiness = sorted(states_happiness.iteritems(), key = operator.itemgetter(1), reverse = True)
    # print sorted_happiness
    happiest_state = sorted_happiness[0]
    sys.stdout.write(happiest_state[0]) # State abbrev ONLY, without a score, "\n" should not be print


if __name__ == '__main__':
    main()
