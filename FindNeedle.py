# Can you find the needle in the haystack?
# Write a function findNeedle() that takes an array full of junk but containing one "needle"
# After your function finds the needle it should return a message (as a string) that says:
# "found the needle at position " plus the index it found the needle, so:
# should return "found the needle at position 5"

haystack = ['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']


def findneedle(haystack):
    count = 0
    for needle in haystack:
        count += 1
        if needle == 'needle':
            position = count - 1

    return "found the needle at position " + str(position)

print(findneedle(haystack))
