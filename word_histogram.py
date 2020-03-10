"""
SYSC 1005 A Fall 2018 - Using a Dictionary to Implement a Histogram
"""
import string

# For information about the string module, type help(string) at the shell 
# prompt, or browse "The Python Standard Library", Section "Built-in Types",
# Subsection "Text Sequence Type - str" in the Python 3.7 documentation
# (available @ python.org).

def build_histogram(filename):
    """ (str) -> dict of str, int pairs
    
    Return a histogram of the words in the specified file.
    (A histogram is a set of counters. In this example, each counter
    keeps track of the number of occurrences of one word.)
     
    >>> hist = build_histogram('sons_of_martha.txt')
    >>> hist
    >>> len(hist)  # How many different words are in the file?
    >>> most_frequent_word(hist)  # Which word occurs most often?
    """

    infile = open(filename, "r")
    hist = {}

    for line in infile:

        # Split each line into a list of words.
        # The split method removes the whitespace from around each word.
        
        word_list = line.split()

        # For each word, remove any punctuation marks immediately
        # before and after the word, then convert it to lower case.
        
        for word in word_list:
            word = word.strip(string.punctuation).lower()
            
            # or, 
            # word = word.strip(string.punctuation)
            # word = word.lower()

            # Don't count any empty strings created when the punctuation marks
            # are removed. For example, if word is bound to a hyphen, '-',
            # word.strip(string.punctuation) yields the empty string, ''.
            
            if word != '':
                count = hist.get(word, 0)  # get returns the current count of
                                           # the number of occurrences of word, 
                                           # or 0 if word is not yet in the 
                                           # dictionary.
                hist[word] = count + 1

            # or simply,
            # hist[word] = hist.get(word, 0) + 1

    return hist


def most_frequent_word(hist):
    """ (dict of str, int pairs) -> tuple of str, int
    
    Return a tuple containing the most frequently occurring word in the 
    specified histogram (a dictionary of word/frequency pairs), along with its 
    frequency.
    
    >>> hist = build_histogram('sons_of_martha.txt')
    >>> hist
    >>> len(hist)  # How many different words are in the file?
    >>> most_frequent_word(hist)  # Which word occurs most often?    
    """
    max_frequency = -1
    for word in hist:
        if hist[word] > max_frequency:
            max_frequency = hist[word]
            most_frequent = word
    
    return (most_frequent, max_frequency)
def words_with_frequency(hist, n):
    """ (dict of str, int pairs; int) -> list of str
    Returns a list of all words in dictionary hist that occur
    with frequency n. The list is sorted in ascending order.
    >>> hist = build_histogram('sons_of_martha.txt')
    >>> words_with_frequency(hist, 1) # Which words occur once
    # in the file?
    >>> words_with_frequency(hist, 5) # Which words occur five
    # times?
    """
    list_string = []
    for word in hist:
        if hist[word] == n:
            list_string.append(word)
    return list_string
            
def build_concordance(filename):
    """ (str) -> dict of str, list pairs
    Return a dictionary in which the keys are the words in the
    specified file. The value associated with each key is a list
    containing the line numbers of all the lines in which each word
    occurs.
    >>> concordance = build_concordance('sons_of_martha.txt')
    """
    infile = open(filename, "r")
    concordance = {}
    word_set =set()
    line_number = 1
    for line in infile:
        word_list = line.split()
        for every_word in word_list:
            every_word = every_word.strip(string.punctuation).lower()
            if every_word != '':
                word_set.add(every_word)
        list_of_words = list(word_set)
        for item in list_of_words:
            if item not in concordance:
                concordance[item] = [line_number]
            else:
                list_of_line = concordance.get(item)
                list_of_line.append(line_number)
                concordance[item] = list_of_line                
        line_number = line_number + 1
        word_set=set()
    return concordance


if __name__ == '__main__':
    # Build and display a histogram of the distinct words in a file
    hist = build_histogram('sons_of_martha.txt')
    print(hist)
    most_occurent = most_frequent_word(hist)
    print('The most frequently occuring word is: '+str(most_occurent[0]))
    print('The number of occurrences: '+str(most_occurent[1]))
    # The most frequent word is "the" and it occur 42 time
    file_name = input('Enter the name of your file: ')
    concordance = build_concordance(file_name)    
    key_words = concordance.keys()
    word_list = []
    for word in key_words:
        word_list.append(word)
        word_list.sort()
    for unique_words in word_list:
        print(unique_words+': '+str(concordance[unique_words]))

