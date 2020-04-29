def two_sum(input_list, target):
    d = {}
    output_list = []
    for num in range(len(input_list)):
        if target - input_list[num] in d:
            output_list.append((d[target - input_list[num]], num))
        else:
            d[input_list[num]] = num
    return output_list