'''
Useful module for debugging code

When you run it, you will see:
(Pdb)

Type for example x and return to query the variables

Once finished type q
'''

import pdb

x = 3
y = 5

pdb.set_trace()

z = x+y
print(z)
