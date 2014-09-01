"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
def wordify(n, debug=False):
  ones = {
  "0":"",
  "1":"one",
  "2":"two",
  "3":"three",
  "4":"four",
  "5":"five",
  "6":"six",
  "7":"seven",
  "8":"eight",
  "9":"nine",
  }
  tens = {
  "0":"",
  "1":{
      "0":"ten",
      "1":"eleven",
      "2":"twelve",
      "3":"thirteen",
      "4":"fourteen",
      "5":"fifteen",
      "6":"sixteen",
      "7":"seventeen",
      "8":"eighteen",
      "9":"nineteen",
      },
  "2":"twenty",
  "3":"thirty",
  "4":"forty",
  "5":"fifty",
  "6":"sixty",
  "7":"seventy",
  "8":"eighty",
  "9":"ninety",
  }
  order = ["", "", "thousand", "million", "billion"]

  # Break the number into 3-digit parts.
  n = str(n)
  num_chars = len(n)
  parts = [n[::-1][i:i+3][::-1] for i in xrange(0,num_chars,3)][::-1]

  # Determine the word for each number.
  word = []
  for digits in parts:
    place = order[len(parts)]

    if len(digits)==3:
      third = ones[digits[0]]
      if third: third += " hundred"
      digits = digits[1:]
    else:
      third = ""


    if len(digits)==2:
      second = tens[digits[0]]
      digits = digits[1:]
    else:
      second = ""

    if type(second) == dict:
      first = second[digits[0]]
      second = ""
    else:
      first = ones[digits[0]]

    if (third) and (second or first):
      word.extend([third, "and", second, first, place])
    elif third or second or first:
      word.extend([third, second, first, place])

  wordified_number = " ".join([part for part in word if part])
  if debug:
    print "{}  ==>  {} (len:{})".format(n, wordified_number, len(wordified_number))

  return wordified_number

def condense(word):
  return word.replace(" ","").replace("-","")

def test():
  print "Testing..."
  test_342 = condense(wordify(342, True))

  print "Calculating ranges:"
  # Ranges from: http://www.mathblog.dk/project-euler-17-letters-in-the-numbers-1-1000/
  ranges = [(1,9,36), (10,19,70), (20,99,748), (100,999,20259), (1,1000, 21124)]
  for (min,max,correct) in ranges:
    # Prints out individual numbers if set to True.
    debug = False

    # Count the words created by the inclusive range.
    words = "".join([wordify(i, debug) for i in xrange(min, max+1)])
    success = "SUCCESS" if correct==len(condense(words)) else "FAIL"

    # Print out the results...
    print "[{}-{}]: {} ({})".format(min,max,len(condense(words)),success)


if __name__=="__main__":
  test()

