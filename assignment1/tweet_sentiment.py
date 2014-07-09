import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # hw()
    # lines(sent_file)
    # lines(tweet_file)
    
    # Build up the dictionary
    # sent_file = open("AFINN-111.txt") # For test
    scores = {} # empty dictionary
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score) # Convert to int
    # print scores.items() # print the dictionary
    
    # Parse the data in output.txt
    # tweet_file = open("problem_1_submission.txt") # For test
    # tweet_file = open("output.txt") # For test
    for line in tweet_file:
        tweet = json.loads(line, encoding="utf-8") # tweet is a dict
        # print tweet.keys()
        # print tweet.values()
        score = 0
        for word in tweet.keys():
            if scores.get(word) != None:
                score += scores.get(word)
        print score

if __name__ == '__main__':
    main()
