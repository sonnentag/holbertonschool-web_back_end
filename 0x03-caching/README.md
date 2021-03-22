## 0x03-caching
Objective: to implement a basic caching system in Python, demonstrating several common cache replacement policies.
### base_caching.py
Provided class to be inherited in each assigned task below.
### 0-basic_cache.py
Basic get/put. No replacement/expiration or MAXSIZE/MAX_ITEMS.
### 1-fifo_cache.py
A simple 'first in, first out' caching method.
### 2-lifo_cache.py
A simple 'last in, first out' caching method, the opposite of task 1..
### 3-lru_cache.py
'Least recently used' method, adding just a little more complexity than tasks 1 & 2. 
### 4-mru_cache.py
'Most recently used' method, the opposite of task 3. 
### 100-lfu_cache.py
'Least frequently used' method, requiring the addition of a hit count for the replacement threshold.
