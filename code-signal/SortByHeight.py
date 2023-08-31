# Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

# Example:
# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

def solution(a):
    heights = []
    indexes = []
    for i, height in enumerate(a):
        if height != -1:
            indexes.append(i)
            heights.append(height)
    
    sorted_heights = sorted(heights) 
    
    for j, h in enumerate(sorted_heights):
        index = indexes[j]
        a[index] = h
    
    return 
