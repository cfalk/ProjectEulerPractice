"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
def wordify(n):
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
  "4":"fourty",
  "5":"fifty",
  "6":"sixty",
  "7":"seven",
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
  while parts:
    digits = parts[0]
    place = order[len(parts)]

    if len(digits)==3:
      third = ones[digits[0]]
      digits = digits[1:]
    else:
      third = ""

    if third: third += " hundred"

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

    if (third or second) and first: #TODO: Check British usage: "and" for all 100s?
      word.extend([third, "and", second, first, place])
    elif third or second or first:
      word.extend([third, second, first, place])

    parts = parts[1:]

  wordified_number = " ".join([part for part in word if part])
  return wordified_number



def test():
  words = "".join([wordify(i) for i in xrange(1,1001)])
  condensed_words = words.replace(" ","").replace("-","")
  print len(condensed_words)


if __name__=="__main__":
  test()

