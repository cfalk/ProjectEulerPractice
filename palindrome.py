def is_palindrome_OBS(num):
  """
  Returns True if `num` is a palidrome (eg: 12321 or "catac") else False.
  """
  if type(num)!=type("string"):
    num=str(num)

  if len(num):
    return num[0]==num[-1] and is_palindrome(num[1:-1])
  else:
    return True

def is_palindrome(num):
  if type(num)!=type("string"): num = str(num)
  return num==num[::-1]


def largest_pal(n):
  """
  Computes the largest palindrome that is the product of two n-digit numbers.
  """

  # Create the search-space of numbers (eg: 100-999).
  max_bound = 10**(n)
  min_bound = 10**(n-1)
  bounds = xrange(min_bound, max_bound)

  pals = [i*j for i in bounds for j in bounds if is_palindrome(i*j)]

  return max(pals)


def testsuite():
  print "Testing Palindrome"
  tests = ["121", "1221", 1221, 123, "123"]
  for test in tests:
    print "{} ({}) --> {}".format(test, type(test), is_palindrome(test))

  print "Largest palindrome made from product of two 3-digit numbers: ",
  print largest_pal(3) #Should be 906609



if __name__=="__main__":
  testsuite()
