
def is_prime(num):
  if (num-1)%6==0 or (num+1)%6==0 or num in {2,3}:
    for i in xrange(5, int(num**0.5)+1, 2):
      if num%(i)==0: return False
    return True
  return False

def get_n_primes(n):
  primes = [2,3]
  while len(primes)<n:
    last_prime = primes[-1] + 2
    while not is_prime(last_prime):
      last_prime += 2
    primes.append(last_prime)
  return primes

def nth_prime(n):
  return get_n_primes(n)[n-1]

def test():
  from datetime import datetime
  t = datetime.now()
  print "10,0001st prime: {}".format(nth_prime(10001)), # Should be 104743
  print "-- took {} seconds".format((datetime.now()-t).total_seconds())

if __name__=="__main__":
  test()
