import sys
import json

def main():
    tweet_file = open(sys.argv[1])

    # Build up term dictionary
    terms = {}
    # total number of words
    total_words = 0.0
    
    # Parse the data in output.txt
    for line in tweet_file:
        tweet = json.loads(line, encoding="utf-8") # tweet is a dict
        text_info = tweet.get("text") # type() == 'unicode'
        text_lang = tweet.get("lang")
        # For each tweet
        if text_info and text_lang == "en": # if has text and is English
            text_info = text_info.encode("utf-8") # type() == 'str'
            text_word_list = text_info.split() # Change to word sequence rather than byte

            num_word = 0
            while num_word < len(text_word_list):
                # Remove common punctuations
                if text_word_list[num_word][-1] in "\'\"!()-[]{};:\,<>./?@#$%^&*_~":
                    text_word_list[num_word] = text_word_list[num_word][0:-1]
                elif text_word_list[num_word][0] in "\'\"!()-[]{};:\,<>./?@#$%^&*_~":
                    text_word_list[num_word] = text_word_list[num_word][1:]
                word = text_word_list[num_word]
                # print word

                # if words not in sentiment, add to terms
            	if not terms.get(word):
            		terms[word] = 1
                else:
                    terms[word] = terms[word] + 1

            	# Next word
                total_words += 1
                num_word += 1

        else: # if empty text or not English
            pass

    # Generate results for each term
    results = terms.items()
    # print results
    num_term = 0
    while num_term < len(results):
    	keyword = results[num_term][0]
    	freq = results[num_term][1] / total_words
    	print keyword, freq
    	num_term += 1

if __name__ == '__main__':
    main()
