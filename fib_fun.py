def fib(n):
  """
  Finds the nth Fib number starting at n=1.
  """
  fibs = [1,2]
  while (len(fibs)<n):
    fibs.append(fibs[-1]+fibs[-2])
  return fibs[n-1]


def fibBetween(lowerBound, upperBound):
  """
  Returns a section of the Fib sequence between a lower and upper bound.
  """
  fibs = []
  n = 1
  while True:
    newFib = fib(n)
    if not (lowerBound < newFib < upperBound):
      return fibs
    fibs.append(newFib)
    n+=1


def evens(lst):
  """
  Returns a list of the even values in an iterable.
  """
  return filter(lambda x:x%2==0, lst)



def runTests():
  tests = [
           "fib(1)", "fib(2)", "fib(3)", "fib(4)", "fib(10)",
           "fibBetween(0,10)", "fibBetween(0,4000000)",
           "evens([1,2,3,4,5,6,7,8,9,10])",
          ]
  for test in tests:
    print "{} --> {}".format(test, eval(test))

  print "Sum of evens of Fib under 4 million:",
  print sum(evens(fibBetween(0,4000000)))


if __name__=="__main__":
  runTests()
