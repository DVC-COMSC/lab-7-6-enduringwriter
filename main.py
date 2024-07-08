def getInput():
    """
    Get integers from user in a single line.
    Split the values and conver them into a list of integers, and return it.
    """
    return list(map(int, input("Enter a list of numbers. Press 'enter' when done.").split()))


def makeReverse(numbers):
    """
    Create a new list of numbers in rev order without using rev function.
    """
    new_numbers = []
    
    # using .insert() method
    # for n in numbers:
    #     new_numbers.insert(0, n)
    # return new_numbers
    
    # using .pop() method, is more efficient than .insert().
    # pop() removes the last element of the list.
    temp_numbers = numbers[:]
    while temp_numbers:
        x = temp_numbers.pop()
        new_numbers.append(x)
    return new_numbers

def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
