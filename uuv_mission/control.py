#Arnav Joshi:Control Engineer 
#College: LMH
#Date:20/10/26
#The purpose of this file is to have a control action on the submarine by taking target depth and current depth into consideration.

## Implementing PD Controller as a class
class PDController:

    #initializing error
    def __init__(self):
        self.previous_error = 0.0

    #implementing the PD formula
    def step(self, reference, depth):
        error = reference - depth
        action = 0.15 * error + 0.6 * (error - self.previous_error)
        self.previous_error = error
        return action
