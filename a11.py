Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # You will pick yourself and one other family member.
# You identify 10 favorite words (sets) for each
# You will then compute the union, intersection, difference,
# and symmetric_difference between these sets.
# You print out results.



# TODO: You need to implement these four methods

# union method
def set_union(x,y):
    return my_words.union(mom_words)
    

# intersection method
def set_intersection(x,y):
    return my_words.intersection(mom_words)

# difference method
def set_difference(x,y):
    return my_words.difference(mom_words)


# symmetric_difference method
def set_symmetric_difference(x,y):
    return my_words.symmetric_difference(mom_words)


# we will setup the test cases here
# TODO: fill in the sets with 10 words in each set
my_words = {"coffee", "dog", "car", "phone", "sleep", "food", "water", "juice", "cookie", "cake"  }
mom_words = {"house", "work", "car", "phone", "tea", "water", "home", "computer", "tv", "biscuit" }

#Now call the methods and print the results
our_union = set_union(my_words, mom_words)
our_intersection = set_intersection(my_words, mom_words)
me_mom_difference = set_difference(my_words, mom_words)
mom_me_difference = set_difference(mom_words,my_words)
our_symmetric_difference = set_symmetric_difference(my_words,mom_words)

# Now print the output/results
print("UNION: List of words that exists in my set or my mom's set")
print(*our_union)

print("INTERSECTION: List of words that exists both sets")
print(*our_intersection)

print("DIFFERENCE 1: List of words that are exclusive to me")
print(*me_mom_difference)

print("DIFFERENCE 2: List of words that are exclusive to my mom")
print(*mom_me_difference)

print("SYMMETRIC DIFFERENCE: List of words that do not have any overlap")
print(*our_symmetric_difference)