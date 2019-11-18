#rebinding a variable
some_variable = 1
print(some_variable)

#output: 1

some_variable = "printing a variable"
print(some_variable)

#output: printing a variable

#mutating a value
x = ['hi']
print(x)

#output: ['hi']

y = x
y += ['there']

print(x)
#output:['hi','there']
#expected output: ['hi']

print(y)
#output: ['hi','there']

'''
Rebinding a variable means simply the old value assigned gets updated
by the new value that has been assigned.

Mutatable means able to be changed and immutable means constant
Here we tried mutating a value, the new value simply gets added to the old
value assigned and doesn't lose its old assigned value.
'''