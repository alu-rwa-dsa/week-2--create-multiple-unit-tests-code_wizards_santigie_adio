

n = int(input("enter a number: "))
for i in range(1, n+1):
    for j in range(1,i+1):
        print(i, end="")
    print()
    


"""Space Compexity: In the script above, the function accepts a number and returns a range of number in a row based on the first for loop,
and another inner for loop. The algorithm has to allocate memory for the same number of items as in the input list.
Therefore, the space complexity of the algorithm becomes O(n)."""

"""Time Complexity: O(log(n)In the script above, you can see that the running time grows in proportion to the logarithm of the input size."""

