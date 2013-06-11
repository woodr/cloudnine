#!/python
# woodr jun2013

from random import randint

# Open output
my_file = open('cloudnine.txt', 'w')

# Generate one million sets
for x in range(1000000):
  # Get six random numbers
  next_ticket = []

  for y in range(6):
    n = randint(1,49)
    # Can't have the same number twice in same set
    while n in next_ticket:
      n = randint(1,49)
    # Add to list
    next_ticket.append(n)

  # Sort ascending
  next_ticket.sort()
  # Write to file
  my_file.write(str(next_ticket).strip('[]'))
  my_file.write("\n")

# Close output
my_file.close()
