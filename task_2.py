def bubble_sorting(catalog):
    """Sorts list in ascending order by bubble algorithm.
    :param catalog: the list for sorting"""

    # pass through the list and compare elements
    for i in range(len(catalog)):
        for j in range(len(catalog) - 1):
            # if condition is true, swap elements
            if catalog[j] > catalog[j + 1]:
                temp = catalog[j]
                catalog[j] = catalog[j + 1]
                catalog[j + 1] = temp
    return catalog


# create numerical and string variables
number = 11
string = 'This is string'

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

# sort lists in ascending order
bubble_sorting(auto_brands)
print(auto_brands)
copied_list.sort()
print(copied_list)


"""
sorted () method sorts the given sequence either in ascending order or in descending order and always return 
the a sorted list. This method does not effect the original sequence.
sort() function is very similar to sorted() but unlike sorted it returns nothing and makes changes to the original 
sequence. Moreover, sort() is a method of list class and can only be used with lists.
"""


phrase = 'This is a test string for Internship Onix for python'
# separate words from text and sort its
words = phrase.lower().split(' ')
bubble_sorting(words)
# create new text from sorted words
new_phrase = ' '.join(words)
print(new_phrase)


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
list_keys = list(months.keys())
print(list_keys)
list_values = list(months.values())
print(list_values)

# sort lists
list_keys.sort()
print(list_keys)
list_values.sort()
print(list_values)

