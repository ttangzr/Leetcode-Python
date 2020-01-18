'''
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

    put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
    get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
    remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.


Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 


Note:

    All keys and values will be in the range of [0, 1000000].
    The number of operations will be in the range of [1, 10000].
    Please do not use the built-in HashMap library.

'''


class MyHashMap(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap = {}
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        self.hashMap[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        if self.hashMap.get(key) is not None:
            return self.hashMap[key]
        else:
            return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        if self.hashMap.get(key) is not None:
            self.hashMap.pop(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

if __name__ == "__main__":
    hashMap = MyHashMap()
    hashMap.put(1, 1)        
    hashMap.put(2, 2)        
    print(hashMap.get(1))          # 返回 1
    print(hashMap.get(3))            # 返回 -1 (未找到)
    hashMap.put(2, 1)         # 更新已有的值
    print(hashMap.get(2))            # 返回 1 
    hashMap.remove(2)         # 删除键为2的数据
    print(hashMap.get(2))            # 返回 -1 (未找到) 
    