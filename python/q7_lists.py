# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    
def match_ends(list):
    count = 0
    for word in list:
        if len(word) > 1 and word[0] == word[-1]:
            count += 1
    return count
match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])


    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
         
def front_x(list):
    xlist = []
    otherlist = []
    for word in list:
        if word[0] == 'x':
            xlist.append(word)
        else:
            otherlist.append(word)
    return sorted(xlist) + sorted(otherlist)
front_x(['aba', 'xyz', 'aa', 'x', 'bbb'])


def sort_last(tuples):
  
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

def order_tuple(list):
    def getKey(item):
        return item[1]
    newlist = sorted(list, key=getKey)
    return newlist
order_tuple([(1, 3), (3, 2), (2, 1)])


def remove_adjacent(nums):
'''
def remove_adjacent(numbers):
  result = []
  for number in numbers:
    if len(result) == 0 or number != result[-1]:
      result.append(number)
  return result



def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.
def linear_merge(list1, list2):
 combined  = []
  while len(list1) and len(list2):
    if list1[0] < list2[0]:
      combined.append(list1.pop(0))
    else:
      combined.append(list2.pop(0))

  combined.extend(list1)
 combined.extend(list2)
  return combined
