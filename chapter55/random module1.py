# Reproducible random numbers: Seed and State
import random
random.seed(5)                   
print(random.randrange(0, 10)) 
print(random.randrange(0, 10))

save_state = random.getstate()  # Get the current state 
print(random.randrange(0, 10)) 
print(random.randrange(0, 10)) 


# Random Binary Decision
import random
probability = 0.3
if random.random() < probability:  
    print("Decision with probability 0.3") 
else:    
    print("Decision with probability 0.7")