# In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'.
# If there are one or two good ideas, return 'Publish'.
# If there are more than two good ideas, return ' I smell a series'.
# If there are no good ideas, as is often the case, return 'Fail'.
# A list set to variable x containing ideas
x = []

# A function to evaluate the list
def find_good_ideas(x):
    # Loop through list and count good ideas
    for y in x:
        good_count = 0
        if y == 'good':
            good_count += 1

    # If statements evaluate how many good ideas were counted and assign a value to good ideas based on the number.
    if good_count == 0:
        good_ideas = 'Fail'

    if good_count >= 1 and good_count <= 2:
        good_ideas = 'Publish'

    if good_count > 2:
        good_ideas = 'I smell a series'

    # Returns the value of good ideas
    return good_ideas 
