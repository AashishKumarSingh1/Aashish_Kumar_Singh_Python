no_of_row=int(input("Enter how many number of row : "))
triangle =[]

for i in range(0, no_of_row):
    col = [None for iterate in range(i+1)]
    col[0], col[-1] = 1, 1

    for j in range(1, i):
        col[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    
    triangle.append(col)
# print(len(triangle[1])) => prints the number of len at a particular row like in this case 1
string_map=0
for row in triangle:
    string_row = ' '.join(map(str, row))
    print(string_row)

print(triangle)

# def print_pascals_triangle(triangle):
#     max_width = len(' '.join(map(str, triangle[-1])))  # Calculate maximum width for formatting
#     for row in triangle:
#         print(' '.join(map(str, row)).center(max_width))

# for i in range(1,num_of_row+1):

#     for j in range(1,i+1):
#         if(j==1 or j==i):
#             print('1')
#         else:
