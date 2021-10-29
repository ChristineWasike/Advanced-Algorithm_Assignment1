# generate random integer values
from numpy.random import seed
from numpy.random import randint


def sock_merchant(n, arr):
    sock_dict = {}
    pairs = 0
    for i in range(n):  # O(n)
        if arr[i] not in sock_dict:  # O(1)
            sock_dict[arr[i]] = 1
        else:
            sock_dict[arr[i]] += 1
    print(sock_dict)

    for key, value in sock_dict.items():
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
