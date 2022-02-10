# Make a function that returns a greeting statement that uses input.
# Your program should return; "Hello, <name> how are you doing today?"

name = "Jim Kapnick"

def greeting(name):
    message = "Hello, " + name + " how are you doing today?"

    return message

print(greeting(name))
