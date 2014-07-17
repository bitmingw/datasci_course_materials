import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1]) # AFINN-111.txt
    tweet_file = open(sys.argv[2]) # output.txt
    # hw()
    # lines(sent_file)
    # lines(tweet_file)
    
    # Build up the dictionary
    scores = {} # empty dictionary
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score) # Convert to int
    # print scores.items() # print the dictionary
    
    # Parse the data in output.txt
    for line in tweet_file:
        tweet = json.loads(line, encoding="utf-8") # tweet is a dict
        text_info = tweet.get("text") # type() == 'unicode'
        if text_info: # del None element
            text_info = text_info.encode("utf-8") # type() == 'str'
            text_word_list = text_info.split() # Change to word sequence rather than byte

            score = 0
            num_word = 0
            while num_word < len(text_word_list):
                # Remove common punctuations
                if text_word_list[num_word][-1] in "\'\",.?:;()[]{}":
                    word = text_word_list[num_word][0:-1]
                elif text_word_list[num_word][0] in "\'\"#":
                    word = text_word_list[num_word][1:]
                else:
                    word = text_word_list[num_word]
                # print word

                if scores.get(word) != None:
                    score += scores.get(word)
                num_word += 1
            print score
        else: # deal with empty text
            print 0


if __name__ == '__main__':
    main()
