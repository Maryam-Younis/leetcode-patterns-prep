# Common Python Template

# Time Complexity

**Best:**

**Average:**

**Worst:**

**Space:**

# Notes

### Some background of Arrays/Hashing

- **Dynamic Arrays**
    - Dynamic! Meaning arrays with the ability to change. For Python this is `list`.
        - **Example:**
        ```python
        items = [3, 5]
        ```
        where `len(items)` will output `2`. We can easily add items using:

        ```python
        items.append(8)
        ```

        - Accessing an element:

        ```python
        items[0]
        ```

        starts the first element at `0` and is always random access meaning that it would only need **O(1)**.

        - However, inserting or deleting items requires **O(n)** because we have to shift all the elements that are affected by the insertion or the deletion.

- **Hash Table**
    - A hash table MAPS a key and a value. In Python, this would be a `dict`.
        - **Example:**

        ```python
        num_of_CoffeeBags = {
            "Ethiopian": 2,
            "Colombian": 1,
            "Sumatra": 4,
        }
        ```

        - For value output:

        ```python
        num_of_CoffeeBags["Colombian"]
        ```

        should then output `1`.

        - We can think of a hash table like an array of "buckets" where each bucket has a key, for example `"Colombian"` and then the pair is HASHED. The hash gives the location of the bucket in the array.

        ```text
        hash("Colombian") = 47815923856832475849010262 % 5 = 1(location)
        ```

        - Because these are hashed, the average case for searching, inserting, and deleting would be **O(1)**.

        - Important to note, a key can be **ANY hashable type**, whereas a value can be almost anything.
            - A hashable type is basically anything that's not mutable. For example, a dynamic list as a key would not work because dynamic lists are mutable, just like dictionaries.

- **Prefix Sum**
    - Sometimes called the cumulative sum. It's the sequence of numbers we get after adding up the previous sequence of numbers.

    - This is usually portrayed as a function in Python.

    **Example:**

    ```python
    def runningSum(nums):

        result = [nums[0]]

        for i in range(1, len(nums)):
            result.append(result[i - 1] + nums[i])

        return result
    ```

    - We will store the result in this dynamic list with the first element of `nums`, `nums[0]`, to kick off the list.

    - We will start at `1`, so the second element, because the first element is already in `result`, `nums[0]`. Remember, in `range(x, y)` the `y` is a stopping point and does not run.

    - Add up the last element in `result` with the next element in `nums` and append that result to `result`.

- **Differences/Use Cases**
    - Hash tables are more efficient than arrays (**O(1)** vs. **O(n)** for searching), but they have no guaranteed order.

    - Arrays are best used when order needs to be kept and most operations will be indexing, meaning **O(1)**.

# List of Problems Solved

- [ ] __________