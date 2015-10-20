import random
import sys, getopt, os


def generate_dice_key(word_count):
    start_index = 11111
    end_index = 66666
    max_retry = end_index
    filename = os.path.join("files", "beale.wordlist.asc.txt")
    word_list = list(open(filename))
    phrase = []

    for index in range(word_count):
        word_line = ''
        # While loop needed because not all random numbers between start/end index correspond to
        # words in the word list file. In that case, we need to generate a new random index
        while not word_line:
            max_retry -= 1
            if max_retry == 0:
                raise Exception("Can't find valid words in word file.")

            random_word_index = random.randrange(start_index, end_index)
            random_word = str(random_word_index)

            for line in word_list:
                if line.startswith(random_word):
                    word_line = line
                    break

        phrase.append(word_line.replace('\n',''))

    # This is the list of words (in order) that make a strong pass phrase
    for word in phrase:
        print word


def main(argv):
    wc = 7
    usage = 'dice.py -w <wordcount>'

    try:
        opts, args = getopt.getopt(argv,"hw:",["help","wordcount="])
    except getopt.GetoptError as error:
        print error
        print usage
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print usage
            sys.exit()
        elif opt in ("-w", "--wordcount"):
            try:
                count = int(arg)
            except ValueError as error:
                print error
                print "Invalid word count"
                sys.exit(2)
            if count < 1:
                print "Word count must be > 0"
                sys.exit(2)
            if count < 5:
                print "Warning: Word count is too small"

            wc = count

    # If successful until here generate a pass phrase
    generate_dice_key(wc)

if __name__ == "__main__":
    main(sys.argv[1:])