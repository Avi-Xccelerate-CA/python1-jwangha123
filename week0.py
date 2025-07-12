# week 0 problem 1
# create a function that returns a list of (vitamins,injections) tuples for each attribute that they need.
# Complete problem statement in README.mds


# your input type should be a list,
# output should also be a list containing tuples
# Example:
# input: [250, 0, 250, 0, 0, 0]
# expected output: [(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
# input: [500, 1, 2, 3, 4, 5]
#expected output: "No medicine given"
# HINT: using % operator to find remainder may be helpful
def dose(needs):
    #YOUR SOLUTION STARTS HERE
    if any(need > 250 for need in needs) or sum(needs) > 500:
        return "No medicine given"
    
    treatment = []
    for need in needs:
        vitamins = need // 10
        remainder = need % 10
        if remainder == 0:
            injections = 0
        else:
            vitamins += 1
            injections = 10 - remainder
        treatment.append((vitamins, injections))
    
    return treatment
    #YOUR SOLUTION ENDS HERE

