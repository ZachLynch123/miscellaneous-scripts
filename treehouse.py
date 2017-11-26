# ugh this is kind of boring wish I was learning something I knew 
# Woops just learned somehting new. haha Python 3 always returns floats when 
# Dividing
# String concatination

message = "{} dogs at the place"
msg1 = "%s cats at the place" % 8
message.format(8)
print(msg1)
name = 'Zach '
name += 'Lynch has '
print(name + message.format(4))
print(name + msg1)

color = ['blue', 'red', 'yellow', 'black', 'white']

states = [
    'ACTIVE',
    ['red', 'green', 'blue'],
    'CANCELLED',
    'FINISHED',
    5,
]
states.remove()
print(states)