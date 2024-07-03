#creating the dictionary 
dictionary_1={
    'key1':'value1',
    'key2':'value2'
}

dictionary_2=dict(
    key1='value3',
    key2='value4'
)

#accessing values
print(dictionary_1.get('key1','default'))
print(dictionary_2['key1'])

#modifying values
dictionary_2['key1']='newvalue1'

#deleting values
del dictionary_2['key1']

#dictionary methods 
dictionary_2.keys()
dictionary_2.values()
dictionary_2.items()

#iterating over dictionary 
my_dict = {"key1": "value1", "key2": "value2"}

## Iterate over keys
for key in my_dict:
    print(key)

## Iterate over values
for value in my_dict.values():
    print(value)

## Iterate over key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")

#dictionary comprehension
squares = {x: x * x for x in range(6)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
