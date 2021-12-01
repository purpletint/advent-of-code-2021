def read_file(file_name):
    with open(file_name, "r") as f:
        content = f.readlines()
    return content

def count_increases(file_name):
    lines = read_file(file_name)
    counter = 0
    prev_line = None
    for line in lines:
        line = int(line.strip())
        print(line)
        print("prev:"+str(prev_line)+","+"curr:"+str(line))
        if prev_line == None:
            prev_line = line
            continue
        if prev_line < line:
            print("yes")
            counter += 1
            print("count:"+str(counter))
        prev_line = line
    return counter


#print(count_increases("input.txt"))


def count_increases_three(file_name):
    lines = read_file(file_name)
    counter = 0
    prev_sum = None
    # for line in lines:
    #     line = int(line.strip())
    #     print(line)
    #     print("prev:" + str(prev_line) + "," + "curr:" + str(line))
    #     if prev_line == None:
    #         prev_line = line
    #         continue
    #     if prev_line < line:
    #         print("yes")
    #         counter += 1
    #         print("count:" + str(counter))
    #     prev_line = line
    for i in range(len(lines)-2):
        cur_sum = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
        if prev_sum == None:
            prev_sum = cur_sum
            continue
        if cur_sum > prev_sum:
            counter += 1

        prev_sum = cur_sum


    return counter

print(count_increases_three("input.txt"))