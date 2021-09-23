"""Problem Description:
input
    arr1:
        [9, 20, 28, 18, 11]
    arr2:
        [30, 1, 21, 17, 28]

output
    ["#####","# # #", "### #", "# ##", "#####"]

"""

# One Loop Version
print("One Loop Version :")

input_list1 = [9, 20, 28, 18, 11]
input_list2 = [30, 1, 21, 17, 28]

graph_output_one_loop = [format((int(input_list1[i]) | int(input_list2[i])),'05b').replace('1','#').replace('0',' ') for i in range(5)]

print(graph_output_one_loop)


# Double For Loop Version
print("Double Loop Version :")

bit_list1 = [format(i, '05b') for i in input_list1]
bit_list2 = [format(i, '05b') for i in input_list2]
graph_out_double_loop = []
for i in range(5):
    num1 = bit_list1[i]
    num2 = bit_list2[i]
    c = [int(num1[j])|int(num2[j])for j in range(5)]  

    res_str = ''
    for k in range(5):
        if c[k] == 1:
            res_str += '#'
        elif c[k] == 0:
            res_str += ' '
    graph_out_double_loop.append(res_str)

print(graph_out_double_loop)