print('Welcome to AoC 2024')
# given two lists - left, right return the (custom) distance between the lists.

import pandas as pd

data = pd.read_csv('day1/day1_data.csv', header=None, sep='   ')

left_list = list(data[0])
right_list = list(data[1])

def calculate_distance(list1, list2):
    list1.sort()
    list2.sort()
    distance = [abs(i-j) for i,j in zip(list1, list2)]
    distance_sum = sum(distance)
    
    return distance_sum

print(calculate_distance(left_list, right_list))

# given a list and a value, calculate the frequency of the value in the list
# def freq_count(val, list):
#     list.sort()
#     i=0
#     while i<val+1:


              

def similarity_score(list1, list2):
    score = 0
    for val in list1:
        val_freq = list2.count(val)
        score += val*val_freq
    
    return score

print(similarity_score(left_list, right_list))