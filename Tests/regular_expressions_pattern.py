import re

def multi_find_re (test_patterns, test_phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for test_pattern in test_patterns:
        print(f'Searching using: {test_pattern}')
        print(re.findall(test_pattern, test_phrase))
        print('\n')

### PATTERN REPETITION SYNTAX

print ('\nSEARCHING USING REPETITION SYNTAX\n')

test_phrase = 'sdds dsdssd ds dsdsds ds ds d d s ds dsdsdsdsdsdssss ddddssds ddss ssddsddd'

test_patterns = [ 'sd*',     	# s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]
multi_find_re(test_patterns, test_phrase)


### CHARACTER SETS

print ('\nSEARCHING USING CHARACTER SETS\n')

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['[sd]',    # either s or d
                's[sd]+']   # s followed by one or more s or d

multi_find_re(test_patterns,test_phrase)

### EXCLUSION

print ('\nSEARCHING USING EXCLUSION\n')

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

test_patterns = ['[^!.? ]+']

multi_find_re(test_patterns, test_phrase)

### CHARACTER RANGES

print ('\nSEARCHING USING CHARACTER RANGES\n')

test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns=['[a-z]+',      # sequences of lower case letters
               '[A-Z]+',      # sequences of upper case letters
               '[a-zA-Z]+',   # sequences of lower or upper case letters
               '[A-Z][a-z]+'] # one upper case letter followed by lower case letters
                
multi_find_re(test_patterns,test_phrase)


### ESCAPE CODES

print ('\nSEARCHING USING ESCAPE CODES\n')

test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]

multi_find_re(test_patterns,test_phrase)