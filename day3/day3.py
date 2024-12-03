print('Welcome to AoC 2024 - Day 3')
# find a pattern

import re

f = open("day3/day3_data.txt", "r")
to_uncorrupt = f.read()

uncorrupt = re.findall("mul\(\d+\,\d+\)", to_uncorrupt)
# print(uncorrupt)

def str_to_multiply(string_input):
    string_list = string_input.split(",")

    return (int(string_list[0][4:])*int(string_list[1][:-1]))

to_multiply = [str_to_multiply(i) for i in uncorrupt]
print(sum(to_multiply))

# enabled multiplication with do() and don't()

# error - this code split correctly but sums up the don't() also
# split_to_uncorrupt = re.split("do\(\)|don't\(\)",to_uncorrupt)
# enabled_uncorrupt = [re.findall("mul\(\d+\,\d+\)", i) for i in split_to_uncorrupt]
# enabled_to_multiply = [[str_to_multiply(j) for j in i] for i in enabled_uncorrupt]
# enabled_sum = sum([sum(i) for i in enabled_to_multiply])
# print(enabled_sum)

split_to_uncorrupt = to_uncorrupt.split("do()")
split_to_uncorrupt = [i.split("don't()")[0] for i in split_to_uncorrupt]
enabled_uncorrupt = [re.findall("mul\(\d+\,\d+\)", i) for i in split_to_uncorrupt]
enabled_uncorrupt = sum([sum([str_to_multiply(j) for j in i]) for i in enabled_uncorrupt])
print(enabled_uncorrupt)