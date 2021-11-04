# generate random integer values
from numpy.random import seed
from numpy.random import randint


def sock_merchant(n, arr):
    # Initialize a hashtable to store the different colors and
    # how often they occur from the pile
    sock_dict = {}

    # Initialize a variable to keep track of the number of matched pairs
    pairs = 0

    # no_of_socks -> size of the array of coloured socks
    for i in range(n):  # O(n)
        # Check if element is in dictionary
        if arr[i] not in sock_dict:  # O(1)
            sock_dict[arr[i]] = 1
        else:
            sock_dict[arr[i]] += 1
    print(sock_dict)

    for key, value in sock_dict.items():
        # using the floor division to return a whole number
        pairs += (value // 2)

    return pairs


if __name__ == '__main__':
    nums = 10
    sock_arr = [1, 2, 1, 3, 4, 2, 5, 4, 1, 3]
    print(sock_merchant(nums, sock_arr))

    # seed random number generator
    # seed(1)
    # generate some integers
    # values = randint(0, 20, 80)
    # print(values)
