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

# print formated float number
# print("%.2f" % float(sum(student_marks[query_name])/len(student_marks[query_name])))

# wrap text
import textwrap
def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))

def designer_door_mat():
    # print a pattern
    h,w = map(int,input().split(' '))
    mid = h//2
    pattern = '.|.'
    for l in range(h):
        # if it's the middle row
        if l == mid:
            print('WELCOME'.center(w, '-'))
        elif l < mid:
            print((pattern*(l*2+1)).center(w,'-'))
        else:
            print((pattern*((h-l)*2-1)).center(w,'-'))

    pattern = [('.|.'*(2*i + 1)).center(w, '-') for i in range(n//2)]
    print('\n'.join(pattern + ['WELCOME'.center(w, '-')] + pattern[::-1]))

    for i in range(1,h,2): 
        print((i * ".|.").center(w, "-"))
    print("WELCOME".center(w,"-"))
    for i in range(h-2,-1,-2): 
        print((i * ".|.").center(w, "-"))

# format integers in different base
def print_formatted(number):
    w=len(bin(number)[2:])
    for i in range(1,number+1):
        print (str(i).rjust(w,' '),str(oct(i)[2:]).rjust(w,' '),str(hex(i)[2:].upper()).rjust(w,' '),str(bin(i)[2:]).rjust(w,' '),sep=' ')

        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w))