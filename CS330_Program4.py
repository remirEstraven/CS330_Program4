# Program 4
# Deanna Deylami & Lucas Geiger
# 11/21/25
# Hard-coded State Machines
import random

# Define States
FOLLOW = 1
PULL_OUT = 2
ACCELERATE = 3
PULL_IN_AHEAD = 4
PULL_IN_BEHIND = 5
DECELERATE = 6
DONE = 7

# Define counting arrays
state_count = [0] * 7
transition_count = [0] * 9

# Implement actions
def follow():
    if(trace):
        # Write to file 'State= 1 Follow'
        pass
    state_count[FOLLOW] += 1 # Increment count for state

def pull_out():
    if(trace):
        # Write to file 'State= 2 Pull Out'
        pass
    state_count[PULL_OUT] += 1 # Increment count for state

def accelerate():
    if(trace):
        # Write to file 'State= 3 Accelerate'
        pass
    state_count[ACCELERATE] += 1 # Increment count for state

def pull_in_ahead():
    if(trace):
        # Write to file 'State= 4 Pull In Ahead'
        pass
    state_count[PULL_IN_AHEAD] += 1 # Increment count for state

def pull_in_behind():
    if(trace):
        # Write to file 'State= 5 Pull In Behind'
        pass
    state_count[PULL_IN_BEHIND] += 1 # Increment count for state

def decelerate():
    if(trace):
        # Write to file 'State= 6 Decelerate'
        pass
    state_count[DECELERATE] += 1 # Increment count for state

def done():
    if(trace):
        # Write to file 'State= 7 Done'
        pass
    state_count[DONE] += 1 # Increment count for state


# Determine transitions
def transition(scenario, transition_prob):
    for i in range(0,scenario):
        if(trace):
            pass
            # Write to file 'Iteration= i'

        state = FOLLOW
        follow()

        while state != DONE:
            # Get random number between 0 and 1
            random_num = random.random()

            # Check transitions
            if(state == FOLLOW):
                # Transition 1: Close to car to pass and no oncoming traffic
                if(random_num < transition_prob[0]): 
                    transition_count[0] += 1
                    state = PULL_OUT
                    pull_out()
                else:
                    state = FOLLOW
                    follow()
            elif(state == PULL_OUT):
                # Transition 2: No oncoming traffic and in passing lane
                if(random_num < transition_prob[1]):
                    transition_count[1] += 1
                    state = ACCELERATE
                    accelerate()
                # Transition 4: Oncoming traffic
                elif(random_num >= transition_prob[1] and random_num < 0.8):
                    transition_count[3] += 1
                    state = PULL_IN_BEHIND
                    pull_in_behind()
                else:
                    state = PULL_OUT
                    pull_out()
            elif(state == ACCELERATE):
                # Transition 3: In front of car to pass
                if(random_num < transition_prob[2]):
                    transition_count[2] += 1
                    state = PULL_IN_AHEAD
                    pull_in_ahead()
                # Transition 5: Oncoming traffic and behind car to pass
                elif(random_num >= transition_prob[2] and random_num < trans_limit):
                    transition_count[4] += 1
                    state = PULL_IN_BEHIND
                    pull_in_behind()
                # Transition 6: Oncoming traffic and alongside car to pass
                elif(random_num >= trans_limit and random_num < 0.9):
                    transition_count[5] += 1
                    state = DECELERATE
                    decelerate()
                else:
                    state = ACCELERATE
                    accelerate()
            elif(state == PULL_IN_AHEAD):
                # Transition 9: In travel lane
                if(random_num < transition_prob[8]):
                    transition_count[8] += 1
                    state = DONE
                    done()
                else:
                    state = PULL_IN_AHEAD
                    pull_in_ahead()
            elif(state == PULL_IN_BEHIND):
                # Transition 7: Done pulling in behind
                if(random_num < transition_prob[6]):
                    transition_count[6] += 1
                    state = FOLLOW
                    follow()
                else:
                    state = PULL_IN_BEHIND
                    pull_in_behind()
            elif(state == DECELERATE):
                # Transition 8: Behind car to pass
                if(random_num < transition_prob[7]):
                    transition_count[7] += 1
                    state = PULL_IN_BEHIND
                    pull_in_behind()
                else:
                    state = DECELERATE
                    decelerate()
            elif(state == DONE):
                print("Unexpected state value= ", state)
                break
            else:
                print("Unexpected state value= ", state)
                break

# Transition probabilities for each scenario
transition_prob1 = [0.8, 0.4, 0.3, 0.4, 0.3, 0.3, 0.8, 0.8, 0.8]
transition_prob2 = [0.9, 0.6, 0.3, 0.2, 0.2, 0.4, 0.7, 0.9, 0.7]

trace = True # Start with true for Scenario 1

# For Accelerate transitions cause its weird
if(trace):
    trans_limit = 0.6
else:
    trans_limit = 0.5

# Number of iterations for scenarios 1 and 2 
SCENARIO1 = 100
SCENARIO2 = 1000000

transition(SCENARIO1,transition_prob1)

trace = False # No tracing in scenario 2
transition(SCENARIO2, transition_prob2)

# Calculate stats 

# Print stats for scenarios 1 and 2 in different files