import constraint

print("\nQUESTION 1\n")
problem = constraint.Problem()
problem.addVariable('a', range(10))
problem.addVariable('b', range(20))


problem.addConstraint(lambda a, b: a * 2 ==b)
solutions = problem.getSolutions()

for i in solutions:
    print(i)


print("-"*50)
print("\nQUESTION 2\n")
problem = constraint.Problem()
problem.addVariable('x', [1,2,3])
problem.addVariable('y', range(10))


problem.addConstraint(lambda x,y:x + y >= 5, ['x','y'])
solutions = problem.getSolutions()
for i in solutions:
    print(i)


