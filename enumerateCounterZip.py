# enumerateCounterZip.py
'''
Recalls of
- enumerate;
- counter;
- zip function;
'''
from collections import Counter
#
# enumerate
#
text1 = 'I like like chocolate chocolate a lot.'
print(f"\ntext1.split() = text1.split(): {text1.split()}")

# creatin list of tuples [(index, value)]
print(f"\nlist(enumerate(text1)): \n{list(enumerate(text1.split()))}\n")

# creating list of sorted tuples according to index's values
print(
    f"\nlist(enumerate(sorted(text1.split()))):\n{list(enumerate(sorted(text1.split())))}\n")

# iterate through enumerate list of tuples and unpack index and value
for indeX, valuE in list(enumerate(text1.split())):
    print(f"indeX{indeX}.: {indeX} valuE{indeX}: {valuE}")
print()

# iterate through the sorted list with the usage of enumerate() function
for indeX, valuE in list(enumerate(sorted(text1.split()))):
    print(f"index{indeX}: {indeX}-->sorted Value{indeX}:{valuE}")
print()

# Creating a primitive bar chart with the usage of enumerate function
numbers = [19, 22, 55, 43, 6, 12]

print(f"\n\n{'index':<12}{'value':<13}{'bar'}")
for indeX1, valuE1 in list(enumerate(numbers)):
    print(f"bar{indeX1+1:<9}{valuE1:<13}{valuE1*'*'}")


#
#
# Counter / tokenizing - breaking the text into single words and counting the occurrence
#
counter = Counter(text1.split())
print(f"\n\ncounter = Counter(text1): {counter}")

#   added items to create sorted dictionary as per key values, otherwise counter not counting
counter2 = sorted(Counter(text1.lower().split()).items())
print(f"\nsorted(Counter(text1.lower().split()).items()):\n{counter2}\n")

# tokenizing and counting the words without the Counter
text3 = ('this is a sample text with several words' +
         'this is more sample sample with some different words')

dicT = {}
counter = 0
for word in text3.split():

    if word in dicT.keys():
        dicT[word] += 1
    else:
        dicT[word] = 1

print(f"\nsorted(dicT.items()):\n{sorted(dicT.items())}\n")

# tokenizning and counting the text3 with Counter
print(
    f"\nsorted(Counter(text3.split()).items()):\n{sorted(Counter(text3.split()).items())}\n")  # must be .items() to count the words

#
#
# zip function
#
print(f"{'for val1, val2, val3 in zip(text1.split(), numbers, text3.split()):'}\n")
for val1, val2, val3 in zip(text1.split(), numbers, text3.split()):
    # print according to the lowest number of indexes from these 3 lists
    print(f"val1:{val1:<9} val2:{val2:<13} val3:{val3}")
print('\n\n')

# packing 2 values form list's tuples to the 2 seperate values
print('attractions_lats, attractions_lngs = zip(*[(37.769901, -122.498331),')

attractions_lats, attractions_lngs = zip(*[  # 2 seperate tuples
    (37.769901, -122.498331),
    (37.768645, -122.475328),
    (37.771478, -122.468677),
    (37.769867, -122.466102),
    (37.767187, -122.467496),
    (37.770104, -122.470436)
])
print(f"attractions_lats: {attractions_lats}")
print(f"attractions_lngs: {attractions_lngs}\n\n")

# creating zip object
golden_gate_park = zip(*[
    (37.771269, -122.511015),
    (37.773495, -122.464830),
    (37.774797, -122.454538),
    (37.771988, -122.454018),
    (37.773646, -122.440979),
    (37.772742, -122.440797),
    (37.771096, -122.453889),
    (37.768669, -122.453518),
    (37.766227, -122.460213),
    (37.764028, -122.510347)
])
# list iterate through the zip object golden_gate_park
print(f"list(golden_gate_park):\n{list(golden_gate_park)}\n") # returns 2 tuples in the list


'''
out:

text1.split() = text1.split(): ['I', 'like', 'like', 'chocolate', 'chocolate', 'a', 'lot.']

list(enumerate(text1)): 
[(0, 'I'), (1, 'like'), (2, 'like'), (3, 'chocolate'), (4, 'chocolate'), (5, 'a'), (6, 'lot.')]


list(enumerate(sorted(text1.split()))):
[(0, 'I'), (1, 'a'), (2, 'chocolate'), (3, 'chocolate'), (4, 'like'), (5, 'like'), (6, 'lot.')]

indeX0.: 0 valuE0: I
indeX1.: 1 valuE1: like
indeX2.: 2 valuE2: like
indeX3.: 3 valuE3: chocolate
indeX4.: 4 valuE4: chocolate
indeX5.: 5 valuE5: a
indeX6.: 6 valuE6: lot.

index0: 0-->sorted Value0:I
index1: 1-->sorted Value1:a
index2: 2-->sorted Value2:chocolate
index3: 3-->sorted Value3:chocolate
index4: 4-->sorted Value4:like
index5: 5-->sorted Value5:like
index6: 6-->sorted Value6:lot.



index       value        bar
bar1        19           *******************
bar2        22           **********************
bar3        55           *******************************************************
bar4        43           *******************************************
bar5        6            ******
bar6        12           ************


counter = Counter(text1): Counter({'like': 2, 'chocolate': 2, 'I': 1, 'a': 1, 'lot.': 1})

sorted(Counter(text1.lower().split()).items()):
[('a', 1), ('chocolate', 2), ('i', 1), ('like', 2), ('lot.', 1)]


sorted(dicT.items()):
[('a', 1), ('different', 1), ('is', 2), ('more', 1), ('sample', 3), ('several', 1), ('some', 1), ('text', 1), ('this', 1), ('with', 2), ('words', 1), ('wordsthis', 1)]


sorted(Counter(text3.split()).items()):
[('a', 1), ('different', 1), ('is', 2), ('more', 1), ('sample', 3), ('several', 1), ('some', 1), ('text', 1), ('this', 1), ('with', 2), ('words', 1), ('wordsthis', 1)]

for val1, val2, val3 in zip(text1.split(), numbers, text3.split()):

val1:I         val2:19            val3:this
val1:like      val2:22            val3:is
val1:like      val2:55            val3:a
val1:chocolate val2:43            val3:sample
val1:chocolate val2:6             val3:text
val1:a         val2:12            val3:with



attractions_lats, attractions_lngs = zip(*[(37.769901, -122.498331),
attractions_lats: (37.769901, 37.768645, 37.771478, 37.769867, 37.767187, 37.770104)
attractions_lngs: (-122.498331, -122.475328, -122.468677, -122.466102, -122.467496, -122.470436)


list(golden_gate_park):
[(37.771269, 37.773495, 37.774797, 37.771988, 37.773646, 37.772742, 37.771096, 37.768669, 37.766227, 37.764028), (-122.511015, -122.46483, -122.454538, -122.454018, -122.440979, -122.440797, -122.453889, -122.453518, -122.460213, -122.510347)]

'''
