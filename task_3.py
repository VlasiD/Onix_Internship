def task_2():
    """Print the result of work of task_2"""

    # create numerical and string variables
    number = 11
    string = 'This is a string'

    # compare types of variables
    print(type(number) == type(string))

    # convert number to string and compare types of variables
    number = str(number)
    print(type(number) == type(string))

    # create list
    auto_brands = ['BMW', 'Opel', 'Subaru', 'Audi', 'Kia']
    print(auto_brands)

    # add element to the end of the list
    auto_brands.append('Renault')
    print(auto_brands)

    # add element to the 2-nd position of the list
    auto_brands.insert(2, 'Volkswagen')
    print(auto_brands)

    # remove first element of the list
    auto_brands.pop(0)
    print(auto_brands)

    # remove 3-rd element of the list
    auto_brands.pop(2)
    print(auto_brands)

    # reverse list
    auto_brands.reverse()
    print(auto_brands)

    # calculate the number of elements
    print('The number of elements: ', len(auto_brands))

    # get a copy of the list
    copied_list = auto_brands.copy()

    # create dictionary
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May'}
    print(months)

    # add pair to the dict
    months[6] = 'June'
    print(months)

    # get value by key
    print(months[4])

    # remove element with key 2
    months.pop(2)
    print(months)

    # get all keys and all values
    print(months.keys())
    print(months.values())

    # sort dict by keys
    sorted_months_by_key = dict(sorted(months.items(), key=lambda entry: entry[0]))
    print(sorted_months_by_key)

    # sort dict by values
    sorted_months_by_value = dict(sorted(months.items(), key=lambda entry: entry[1]))
    print(sorted_months_by_value)


# the global variable
coefficient = 5


def multiply(number, result):
    """
    Multiplies the given number and the specified coefficient
    :param result: the list for recording multiplication results
    :param number: the number to multiply by coefficient
    :return the result of multiplication, written to the list and the number of elements in the list
    """
    result.append(number * coefficient)
    return result, len(result)


def show_arguments(*args, **kwargs):
    """Prints the given arguments of function"""
    print(args, kwargs)


def is_divisible_by(num, divisor):
    """
    Checks if the given number is divisible by the given divisor
    :param num: the number to check for division without remainder
    :param divisor: the number divided by the first number
    :return: True if the given number is divisible without remainder by given divisor or False if is not
    """
    return num % divisor == 0


def fibonacci(number):
    """
    Calculates the given number of Fibonacci sequence element
    :param number: the number of Fibonacci sequence element
    :return: the given number of Fibonacci sequence element
    """
    if number == 0:
        return 0
    elif number == 1:
        return 1
    elif number < 0:
        return 'The negative number of sequence does not exist'
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


if __name__ == '__main__':
    # list for recording multiplication results
    multiplication_result = []
    print(multiply(7, multiplication_result))
    print(multiply(10, multiplication_result))
    show_arguments('hello', 'world', name="Jack", age=25)
    print(is_divisible_by(40, 5))
    print(fibonacci(10))
