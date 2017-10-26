import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
message = 'Был яркий прохладный апрельский день, и часы пробили час пополудни.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)