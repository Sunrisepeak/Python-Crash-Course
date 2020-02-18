lt = [1, 1.1, 'str', ['list']] # contain type : [int, float, string, list]

print(lt[0]) #output: 1

# Tiny skill: output last element of list by -1(index), rather than 3(lenght - 1)
print(lt[-1]) # output: ['list']

lt.append('Adding')
print(lt) # output: [1, 1.1, 'str', ['list'], 'Adding']

lt.insert(0, 'insert_0')
lt.insert(-1, 'insert_end(-1)')
print(lt) # output:['insert_0', 1, 1.1, 'str', ['list'], 'insert_end(-1)', 'Adding']

del lt[-1]
print(lt) # output: ['insert_0', 1, 1.1, 'str', ['list'], 'insert_end(-1)']

# like stack -- DS
re_value = lt.pop()
print(re_value)
print(lt)

lt.remove(1)
print(lt)

lt[-2] = 'string' # change 'str' to 'string'
print(lt)
