# Problem Set 4A
# Name: <Elizaveta Latash>
# Collaborators: None
# Time Spent: Couple of hours


# Permutations
#######################################################################
# From the MIT Introduction to Computer Science and Programming in Python Course
# Instructions in double quotes are from the course



def toString(List):
    return ''.join(List)

def get_permutations(sequence, start, end):
    # start = 0
    # end = N-1
    SEQ=sequence
    
    
    if start == end:
        print(toString(sequence))
    else:
        for i in range(start, end + 1):
            SEQ[start], SEQ[i] = SEQ[i], SEQ[start]
            get_permutations(SEQ, start + 1, end)
            SEQ[start], SEQ[i] = SEQ[i], SEQ[start] # backtrack


    
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''


if __name__ == '__main__':
    
    print('Please choose a word to permute.')
    Word = input('Enter your word: ')
    Word_list = list(Word)
    N = len(Word_list) - 1
    print("These are the permutations of", Word, ".")
    get_permutations(Word_list, 0, N)
    


