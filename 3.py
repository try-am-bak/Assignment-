numList = [5, 10, 33, 69, 54, 46, 77, 0]

def splitevenodd(x):
   evenlist = []
   oddlist = []
   for i in x:
      if (i % 2 == 0):
         evenlist.append(i)
      else:
         oddlist.append(i)
   print("Even lists:", evenlist)
   print("Odd lists:", oddlist)
def valcheck():

    if numList[0] == numList[len(numList)-1]:
        return True
    else:
        return False

print ("Check equivalence of values of first and last number: ", valcheck())
splitevenodd(numList)