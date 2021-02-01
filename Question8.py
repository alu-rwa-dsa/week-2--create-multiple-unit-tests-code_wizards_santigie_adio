List=[[1],[2],[3],[4],[5]]
for i in List:
    X=List.pop(0)
    for i in X:
        X=X.pop(0)
    print(X)
    List.append(X)
    print(List)



"""Space Compexity: In the script above, the function accepts a list of integers and returns a list with the corresponding squares of integers.
The algorithm has to allocate memory for the same number of items as in the input list.
Therefore, the space complexity of the algorithm becomes O(n)."""

"""Time Complexity: O(n'2)In the script above, you can see that we have an outer loop that iterates through all the items in the input list and then a nested inner loop,
which again iterates through all the items in the input list.
The total number of steps performed is n * n, where n is the number of items in the input array."""
