# Program 4
# Deanna Deylami & Lucas Geiger
# 11/21/25
# Hard-coded State Machines
import random

# Define States
FOLLOW = 0
PULL_OUT = 1
ACCELERATE = 2
PULL_IN_AHEAD = 3
PULL_IN_BEHIND = 4
DECELERATE = 5
DONE = 6

# Define counting arrays
state_count = [0] * 7
transition_count = [0] * 9

# Implement actions
def follow(file):
    if(trace):
        file.write("State= 1 Follow\n")
    state_count[FOLLOW] += 1 # Increment count for state

def pull_out(file):
    if(trace):
        file.write("State= 2 Pull Out\n")
    state_count[PULL_OUT] += 1 # Increment count for state

def accelerate(file):
    if(trace):
        file.write("State= 3 Accelerate\n")
    state_count[ACCELERATE] += 1 # Increment count for state

def pull_in_ahead(file):
    if(trace):
        file.write("State= 4 Pull In Ahead\n")
    state_count[PULL_IN_AHEAD] += 1 # Increment count for state

def pull_in_behind(file):
    if(trace):
        file.write("State= 5 Pull In Behind\n")
    state_count[PULL_IN_BEHIND] += 1 # Increment count for state

def decelerate(file):
    if(trace):
        file.write("State= 6 Decelerate\n")
    state_count[DECELERATE] += 1 # Increment count for state

def done(file):
    if(trace):
        file.write("State= 7 Done\n")
    state_count[DONE] += 1 # Increment count for state


# Determine transitions
def transition(scenario, transition_prob, scenario_num):
    if scenario_num == "1":
        file = open("Scenario1.txt", "w")
    else:
        file = open("Scenario2.txt", "w")
    for i in range(0,scenario):
        if(trace):
            file.write(f"\nIteration = {i}\n")
        
        state = FOLLOW
        follow(file)

        while state != DONE:
            # Get random number between 0 and 1
            random_num = random.random()

            # Check transitions
            if(state == FOLLOW):
                # Transition 1: Close to car to pass and no oncoming traffic
                if(random_num < transition_prob[0]): 
                    transition_count[0] += 1
                    state = PULL_OUT
                    pull_out(file)
                else:
                    state = FOLLOW
                    follow(file)
            elif(state == PULL_OUT):
                # Transition 2: No oncoming traffic and in passing lane
                if(random_num < transition_prob[1]):
                    transition_count[1] += 1
                    state = ACCELERATE
                    accelerate(file)
                # Transition 4: Oncoming traffic
                elif(random_num >= transition_prob[1] and random_num < 0.8):
                    transition_count[3] += 1
                    state = PULL_IN_BEHIND
                    pull_in_behind(file)
                else:
                    state = PULL_OUT
                    pull_out(file)
            elif(state == ACCELERATE):
                # Transition 3: In front of car to pass
                if(random_num < transition_prob[2]):
                    transition_count[2] += 1
                    state = PULL_IN_AHEAD
                    pull_in_ahead(file)
                # Transition 5: Oncoming traffic and behind car to pass
                elif(random_num >= transition_prob[2] and random_num < trans_limit):
                    transition_count[4] += 1
                    state = PULL_IN_BEHIND
                    pull_in_behind(file)
                # Transition 6: Oncoming traffic and alongside car to pass
                elif(random_num >= trans_limit and random_num < 0.9):
                    transition_count[5] += 1
                    state = DECELERATE
                    decelerate(file)
                else:
                    state = ACCELERATE
                    accelerate(file)
            elif(state == PULL_IN_AHEAD):
                # Transition 9: In travel lane
                if(random_num < transition_prob[8]):
                    transition_count[8] += 1
                    state = DONE
                    done(file)
                else:
                    state = PULL_IN_AHEAD
                    pull_in_ahead(file)
            elif(state == PULL_IN_BEHIND):
                # Transition 7: Done pulling in behind
                if(random_num < transition_prob[6]):
                    transition_count[6] += 1
                    state = FOLLOW
                    follow(file)
                else:
                    state = PULL_IN_BEHIND
                    pull_in_behind(file)
            elif(state == DECELERATE):
                # Transition 8: Behind car to pass
                if(random_num < transition_prob[7]):
                    transition_count[7] += 1
                    state = PULL_IN_BEHIND
                    pull_in_behind(file)
                else:
                    state = DECELERATE
                    decelerate(file)
            elif(state == DONE):
                print("Unexpected state value= ", state)
                break
            else:
                print("Unexpected state value= ", state)
                break
    
    file.write("\n")
    return file

def final_setup(scenario, file, iterations, transition_prob):
    # Calculate stats 
    transition_frequency = []
    for trans in transition_count:
        result = round(trans / sum(transition_count), 3)
        transition_frequency.append(result)

    state_frequency = []
    for state in state_count:
        result = round(state / sum(state_count), 3)
        state_frequency.append(result)
    
    # Print stats for scenarios w/ calculated stats.
    file.write(f"scenario                = {scenario}\n")
    file.write(f"trace                   = {trace}\n")
    file.write(f"iterations              = {iterations}\n")
    file.write(f"transition probabilities= {transition_prob}\n")
    file.write(f"state counts            = {state_count}\n")
    file.write(f"state frequencies       = {state_frequency}\n")
    file.write(f"transition counts       = {transition_count}\n")
    file.write(f"transition frequencies  = {transition_frequency}\n")

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

transition1 = transition(SCENARIO1,transition_prob1, "1")
final_setup("1", transition1, SCENARIO1, transition_prob1)

# Clean up stats after 1st iteration
state_count = [0] * 7
transition_count = [0] * 9

trace = False # No tracing in scenario 2
transition2 = transition(SCENARIO2, transition_prob2, "2")
final_setup("2", transition2, SCENARIO2, transition_prob2)
