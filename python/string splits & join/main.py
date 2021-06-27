
def split_and_join(line):
    # write your code here
    line = line.split(" ")

    lines ="-".join(line)
    return lines


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print (result)