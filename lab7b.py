def f(L1,L2,L3):
    L1[0] = [2]




import inspect
lines = inspect.getsource(f).split("\n")
L1 = [[1],[2],[3]]
L2 = [[2],[4],[6]]
L3 = [[3],[6],[9]]
parameters = lines[0].split("(")[-1][:-2].split(",")
print(parameters)
parameters_value = []
for parameter in parameters:
    exec("L = list("+ parameter+")")
    parameters_value.append(L)
print(parameters_value)
f(L1,L2,L3)
print(L1)
for index in range(len(parameters)):
    exec("L = "+ parameters[index])
    if L != parameters_value[index]:
        print(f"L{index+1} is now changed")
        exec(parameters[index] + "= parameters_value[index]")
print(L1,L2,L3)