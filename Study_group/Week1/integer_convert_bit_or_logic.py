input_list1 = [8, 13, 2, 19, 27]
input_list2 = [23, 7, 14, 26, 2]

print(input_list1)

graph_output = [format((int(input_list1[i]) | int(input_list2[i])),'05b').replace('1','#').replace('0',' ') for i in range(5)]

print(graph_output)


# bit_list1 = [format(i, '05b') for i in input_list1]
# bit_list2 = [format(i, '05b') for i in input_list2]
# print (bit_list1)
# print (bit_list2)
# output_list = []
# for i in range(5):
#     num1 = bit_list1[i]
#     num2 = bit_list2[i]
#     c = [int(num1[j])|int(num2[j])for j in range(5)]
#     res = 0
#     for j in range(5):
#         if c[j] == 1:
#             res += 1 <<(4-j)
#     output_list.append(res)

# print(output_list)