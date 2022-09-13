#MB
#03062022
#103
#RandomPasswordGen

import random
#defines password
def password():
#word accumulator
    word = ""
#goes through random in the range of 8-16
    for x in range(random.randint(8,16)):
 #random number generator for the ascii code
        val = random.randint(33,126)
       #accumulates, and gives the random number a value
        word = word + chr(val)
    #returns word
    return word 
#runs function
def main():
#prints outcome of function
    print(password())
#runs function
    password()
main()
