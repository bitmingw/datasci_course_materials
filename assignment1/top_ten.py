import sys
import json

def main():
    tweet_file = open(sys.argv[1])

    # Build up hashtags dictionary
    tags = {}
    # Total number of tags
    total_tags = 0.0
    
    # Parse the data in output.txt
    for line in tweet_file:
        tweet = json.loads(line, encoding="utf-8") # tweet is a dict
        text_info = tweet.get("text") # type() == 'unicode'
        text_lang = tweet.get("lang")
        entities = tweet.get("entities")

        # For each tweet
        if text_info and text_lang == "en" and entities: # if has text and is English and has tags
            hashtags = entities["hashtags"]

            if hashtags:
                # print hashtags
                for eachtag in hashtags:
                    one_tag = eachtag["text"]
                    if not tags.get(one_tag):
                        tags[one_tag] = 1
                    else:
                        tags[one_tag] += 1
                    total_tags += 1

        else: # if empty text or not English
            pass

    # Generate results for each term
    results = list(tags.items())
    # Calculate frequency
    num_tags = 0
    while num_tags < len(results):
    	one_tag = results[num_tags][0]
    	freq = results[num_tags][1] / total_tags
    	num_tags += 1
    results = sorted(results, key = lambda x:x[1], reverse = True) # Reverse sort by second element
    # Print top 10
    for num in range(10):
        print results[num][0], results[num][1]

if __name__ == '__main__':
    main()
