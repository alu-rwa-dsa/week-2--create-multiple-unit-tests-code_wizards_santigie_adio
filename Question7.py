def char_frequency(str1):
    dict={}
    for n in str1:
        Keys=dict.keys()
        if n in Keys:
            dict[n]+=1
        else:
            dict[n]=1
    return dict

print(char_frequency("google.com"))



"""Space Compexity: In the script above, the algorithm has to allocate memory for the same number of items as in the input list.
Therefore, the space complexity of the algorithm becomes O(n)."""

"""Time complexity of the above is O(n) because we have a for loop that increment based str1."""
