# generator.py woodr dec2013

import sys
import os

from random import randint

class generator(object):

    number_of_sets = 1000000
    out_file = None
    out_name = "cloudnine.txt"

    def __init__(self):
        pass

    def open_file(self):
        self.out_file = open(self.out_name, 'w')

    def write(self, text_out):
        self.out_file.write(text_out)
        self.out_file.write("\n")

    def close_file(self):
        self.out_file.close()

    def generate_out(self):
        # Generate sets
        for x in range(1, self.number_of_sets + 1):        
          # Get six random numbers
          next_set = []
          for y in range(6):
            n = randint(1,49)
            # Can't have the same number twice in same set
            while n in next_set:
              n = randint(1,49)
            # Add to list
            next_set.append(n)
          # Sort ascending
          next_set.sort()
          # Write the number
          self.write(str(next_set).strip('[]'))
          print("Set %d: %s" %(x, next_set))


def cli():
    print("\n* Cloud Nine *\n")
    gen = generator()
    gen.open_file()
    gen.generate_out()
    gen.close_file()
    print("\nFinished.\n")

if __name__ == '__main__':
    cli()
