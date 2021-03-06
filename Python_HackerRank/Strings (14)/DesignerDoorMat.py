#Designer Door Mat

# Mr. Vincent works in a door mat manufacturing company. 
# One day, he designed a new door mat with the following specifications: 
'''
    1. Mat size must be N x M. (N is an odd natural number, and M is 3 times N.)
    2. The design should have 'WELCOME' written in the center.
    3. The design pattern should only use |, . and - characters.
'''

# Input
''' 9 27    '''
# Output
''' ------------.|.------------
    ---------.|..|..|.---------
    ------.|..|..|..|..|.------
    ---.|..|..|..|..|..|..|.---
    ----------WELCOME----------
    ---.|..|..|..|..|..|..|.---
    ------.|..|..|..|..|.------
    ---------.|..|..|.---------
    ------------.|.------------ '''

n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]       #.center(m, '-')
#print(pattern)
#print(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1])
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))  #.join()


'''
Sample Designs
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
'''