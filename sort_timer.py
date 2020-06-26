#Sawyer Paeth
#5/19/2020
#Decorator function that times how many seconds it takes for bubble sort and insertion sort functions to sort a list.
#Compare_sorts takes the times from bubble sort and insertion sort for 10 different lists and graphs the resulting times.


#Import time and random modules.  Import pyplot from matplotlib
import time
import random
from matplotlib import pyplot



def sort_timer(func):
    """Decorator, times how long it takes a function to run."""

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        total = end_time - start_time
        return total

    return wrapper

@sort_timer
def bubble_sort(a_list):
  """
  Sorts a_list in ascending order
  """
  for pass_num in range(len(a_list) - 1):
    for index in range(len(a_list) - 1 - pass_num):
      if a_list[index] > a_list[index + 1]:
        temp = a_list[index]
        a_list[index] = a_list[index + 1]
        a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
  """
  Sorts a_list in ascending order
  """
  for index in range(1, len(a_list)):
    value = a_list[index]
    pos = index - 1
    while pos >= 0 and a_list[pos] > value:
      a_list[pos + 1] = a_list[pos]
      pos -= 1
    a_list[pos + 1] = value


def compare_sorts(func_one, func_two):
    '''Takes two functions as parameters. Adds times it takes function to sort list to a list and creates a graph
    of the values.'''

    #Two empty lists to add times to
    bubble_list=[]
    insertion_list= []

    #For loop the creates 10  random lists from 1000 to 10000 numbers long
    for x in range(1,11):
        rlist=[]
        for y in range(x * 1000):
            rlist.append(random.randint(1,10000))
        #Creates copy of each list in current iteration
        rlist2= list(rlist)

        #Runs each function on newly created list and keeps track of times
        bubble_list.append(func_one(rlist))
        insertion_list.append(func_two(rlist2))

    #Uses pyplot to create a graph using function times of bubble sort and insertion sort
    pyplot.plot([1, 2, 3, 4, 5, 6, 7, 8 ,9 ,10], bubble_list, 'ro--', linewidth=2, label="bubble sort")
    pyplot.plot([1, 2, 3, 4, 5, 6, 7, 8 ,9 ,10], insertion_list, 'go--', linewidth=2, label="insertion sort")
    #Adds legend, labels and titles to graph
    pyplot.legend(loc="upper left")
    pyplot.xlabel("Length of list (number)")
    pyplot.ylabel("Time taken (seconds)")
    pyplot.title('Function Sort Time')
    pyplot.show()

#Calls compare_sorts
compare_sorts(bubble_sort,insertion_sort)

