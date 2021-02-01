List_1=[1,2,3,4]
List_2=[1,3,4]
for i in List_1:
   if i not in List_2:
       print (i)
       remove=[]
       remove.append(i)
       print(remove)


"""Space Compexity: In the script above, the function accepts a list of integers and returns a list with the corresponding connditions set.
The algorithm has to allocate memory for the same number of items as in the input list.
Therefore, the space complexity of the algorithm becomes O(n)."""

"""Time Complexity: O(n)In the script above, you can see that we have only one loop that iterates through all the items in the input list and prints out based on met conditions.
The total number of steps performed is n, where n is the number of items in the input array."""
