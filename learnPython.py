def list_comprehension(x,y,z,n):
    # print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])
    all =[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    print([c for c in all if sum(c) != n])

def nested_lists(students):
    students.sort(key=lambda x: x[1])
    # lowest_score = students[0][1]
    # print(students, lowest_score)
    # while students[0][1] == lowest_score:
    #     students.pop(0)
    # print(students)
    # names = []
    # sl = students[0][1]
    # while len(students) and students[0][1] == sl:
    #     names.append(students[0][0])
    #     students.pop(0)
    # names.sort()
    # print(*names)

    second_highest = sorted(list(set([mark for name, mark in students])))[1]
    # print('\n'.join([a for a,b in sorted(students) if b == second_highest]))
    print('\n'.join([a for a,b in sorted(filter(lambda x: x[1] == second_highest ,students))]))

nested_lists([['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]])
nested_lists([['test1', 52], ['test2', 53], ['test3', 53], ['test4', 53]])