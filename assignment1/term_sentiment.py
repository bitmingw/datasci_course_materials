import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1]) # Not in AFINN-111.txt
    tweet_file = open(sys.argv[2])
    # hw()
    # lines(sent_file)
    # lines(tweet_file)

    # Build up the sentiment dictionary
    std_scores = {} # empty dictionary
    for line in sent_file:
        term, score = line.split("\t")
        std_scores[term] = int(score) # Convert to int

    # Build up the non-sentiment dictionary
    non_scores = {}
    
    # Parse the data in output.txt
    for line in tweet_file:
        tweet = json.loads(line, encoding="utf-8") # tweet is a dict
        text_info = tweet.get("text") # type() == 'unicode'
        text_lang = tweet.get("lang")
        # For each tweet
        if text_info and text_lang == "en": # if has text and is English
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
                if std_scores.get(word):
                	word_value = std_scores.get(word)
                	if word_value > 0:
                		pos_score += word_value
                	elif word_value < 0:
                		neg_score -= word_value
                # if words not in sentiment, add to terms
            	elif not non_scores.get(word):
            		non_scores[word] = [0, 0]

            	# Next word
                num_word += 1
            
            # Eval non-sentiment word in the tweet
            num_word = 0
            while num_word < len(text_word_list):
            	word = text_word_list[num_word]
            	if non_scores.get(word):
            		non_scores[word][0] += pos_score
            		non_scores[word][1] += neg_score
            	num_word += 1

        else: # if empty text or not English
            pass

    # Generate results for non-sentiment words
    non_sent_results = non_scores.items()
    # print non_sent_results
    num_word = 0
    while num_word < len(non_sent_results):
    	keyword = non_sent_results[num_word][0]
    	# Avoid divided by 0
    	pos_score = 0.5 if not non_sent_results[num_word][1][0] else non_sent_results[num_word][1][0]
    	neg_score = 0.5 if not non_sent_results[num_word][1][1] else non_sent_results[num_word][1][1]
    	score = pos_score / float(neg_score)
    	print keyword, score
    	num_word += 1

if __name__ == '__main__':
    main()
