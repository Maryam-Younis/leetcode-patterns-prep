# Common Python Template


# Time Complexity

Best:

Average:

Worst:

Space:

# Notes

### Some background of Arrays/Hashing

- ***Dynamic Arrays***
    - Dynamic! Meaning arrays with the ability to change. For Python this is "list" 
        - ***Example:*** items = [3,5], where "len(items)" will output 2. We can easily add items using items.append(8)
        - Accessing an element: "items[0]", starts the first element at 0 and is always random access meaning that it would only need O(1)
        - However, inserting or deleting items requires O(n) because we have to shift all the elements that are effected by the insertion or the deletion. 

- ***Hash Table***
    - A hash table MAPS a key and a value. In Python, this would be a dict
        -  ***Example:*** 
        num_of_CoffeeBags = {
            "Ethiopian" : 2,
            "Colombian" : 1,
            "Sumatra" : 4,
        }
        - For value output, num_of_CoffeeBags[Colombian], should then output 2
        - We can think of a hash table like a array of "buckets" where each bucket has a key, for example "Colombian" and then the pair is HASHED, the hash gives the location of the bucket in the array. 
        so hash('colombian') = 47815923856832475849010262 % 5 = 2
        - Because these are hashed, the average case for searching, inserting, and deleting would be O(1)
        - Important to note, a key can be ANY hashable type, whereas a value can be almost anothing. 
            - A hashable type is besically anything that's not mutable. For exaple, a dynamic list as a key would not work out because dynamic lists are mutable, just like dict.

- ***Prefix Sum***
    - Sometimes called the cummalitive sum. It's the sequence of numbers we get after adding up the previous sequence of numbers.
    - This is usually portrayed as a function in python. ***Example:***
    
    ***def runningSum(nums):***

        ***result = [nums[0]]***

        ***for i in range(1, len(nums)):***

            ***result.append(result[i-1] + num[i])***

        ***return result***

    - We will store the result in this  dynamic list with the first elemenet of nums, num[0], to kick off the list.
    - we will start at 1, so second element because the first element is already in result, num[0]. Remember in range(x,y) the y is a stoping point and does not run. 
    - add up the last element in result with the next element in num and append that result to element. 
    

- ***Differences/Use Cases***
    - Hash tables are more effecient then arrays O(1) < O(n) but they have no order. 
    - Arrays are best used when order needs to be kept and most opperations will be indexing, maining O(1)

        


# List of Problems solved:

- [ ] __________