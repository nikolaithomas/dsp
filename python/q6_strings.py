# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

def donuts(count):
    if count < 10:
        return 'Number of donuts is: ' + str(count)
    else:
        return 'Number of donuts is: many'

print donuts(12)


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    def split(str):
        if len(str) < 3:
            return ''
        else:
            first = str[0:2]
            second = str[-2:]
            return first + second
print split('spring')



def replace(str):
    if len(str) < 1:
            return ''
    else:
        first = str[0]
        rest = str[1:]
        return first + rest.replace(first, '*')
print replace('babble')
 


  def mix_up(a, b):
    if len(a or b) < 3:
            return ''
    else:
        return b[0:2] + a[2:] + ' ' + a[0:2] + b[2:]
print mix_up('pezzy', 'firm')


def verbing(s):
    if len(s) < 3:
        return s
    if s[-3:] == 'ing':
        return s + 'ly'
    else:
        return s + 'ing'

print verbing('do')


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

 def not_bad(s):
  s_not = s.find('not')
  s_bad = s.find('bad')

  if s_bad > s_not:
    s = s.replace(s[s_not:(s_bad+3)], 'good')

  return s


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back
def front_back(a, b):
  alength = len(a)
  blength = len(b)

  if alength % 2 == 0:
    aindex = alength // 2
  else:
    aindex = (alength // 2) + 1

  if blength % 2 == 0:
    bindex = blength // 2
  else:
    bindex = (blength // 2) + 1

  afront = a[0:aindex]
  aback = a[aindex:]

  bfront = b[0:bindex]
  bback = b[bindex:]

  return afront + bfront + aback + bback
