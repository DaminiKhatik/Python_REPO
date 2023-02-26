#Creating a random user password
import random
from string import punctuation, ascii_letters, digits
symbols = ascii_letters + digits + punctuation
secure_random = random.SystemRandom() 
password = "".join(secure_random.choice(symbols)for i in range(10)) 
print(password)


#Create cryptographically secure random numbers
from random import SystemRandom
secure_rand_gen = SystemRandom()
print(secure_rand_gen.randint(0, 20)) 


#Random and sequences: shue, choice and sample
import random 
from random import shuffle
laughs = ["Hi", "Ho", "He"]
random.shuffle(laughs)  
print(laughs)

#Creating random integers and ﬂoats: randint, randrange, random, and uniform
import random 
from random import randint
a=random.randrange(1000)
print(a)




