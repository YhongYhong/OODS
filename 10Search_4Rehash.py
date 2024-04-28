class HashTable:
    def __init__(self, capacity, collision, threshold):
        self.capacity = capacity
        self.collision = collision
        self.size = 0
        self.collision_check = 0
        self.threshold = threshold
        self.table = [None] * capacity

    def _hash(self, key):
        return key % self.capacity

    def insert(self, num, arr):
        index = self._hash(num)
        self.size += 1
        if (self.size/self.capacity)*100 >= self.threshold:
                print(f"Add : {num}")
                print("****** Data over threshold - Rehash !!! ******")
                self.find_prime()
                self.table = [None] * self.capacity
                self.hashing(arr, self.size)
                
        elif self.table[index] is None :
            print(f"Add : {num}")
            self.table[index] = num
            
        else:
            print(f"Add : {num}")
            for i in range(index, len(self.table)+1):
                if i == len(self.table)-1:
                    index = 0 
                    self.collision_check += 1
                    self.table[index] = num
                    print(f"collision number {self.collision_check} at {self.capacity - 1}") 
                    break
                else: 
                    if self.table[i] != None:
                        index = i 
                        self.collision_check += 1
                        if self.table[i] is not None:
                            print(f"collision number {self.collision_check} at {index}")
                        else:
                            break
                    elif self.table[i] == None:
                        self.table[i] = num
                        break

            if self.collision_check >= self.collision:
                self.find_prime()
                self.table = [None] * self.capacity
                print("****** Max collision - Rehash !!! ******")
                self.hashing(arr, self.size)
            self.collision_check = 0
        
            
                

    def hashing(self, arr, N):
        self.collision_check = 0
        for i in range(N):
    
            hash_value = arr[i] % self.capacity
            if(self.table[hash_value] == -1):
                self.table[hash_value] = arr[i]
            
            else:
                
                for j in range(len(self.table)):
                    
                    new_hash = (hash_value + j * j) % self.capacity
                    if (self.table[new_hash] is None):
                        self.table[new_hash] = arr[i]
                        break
                    else: 
                        self.collision_check += 1
                        print(f"collision number {self.collision_check} at {new_hash}")
                

    def find_prime(self):
        self.capacity = self.capacity * 2
        
        while self.capacity > 1:
            self.capacity += 1
            for i in range(2, int(self.capacity/2)+1):
                if (self.capacity % i == 0 or self.capacity % (i + 1) == 0):
                    break
                else:
                    return 
        
            
    def print_table(self):
        if self.size == 0:
            print("Initial Table :")
        for i in range(0, self.capacity):
            print(f"#{i + 1}	{self.table[i]}")
        print("----------------------------------------")

print(" ***** Rehashing *****")
data1, data2 = input("Enter Input : ").split("/")
data1 = data1.split(" ")
data2 = data2.split(" ")
data1 = list(map(int, data1))
data2 = list(map(int, data2))
ht = HashTable(data1[0], data1[1], data1[2])
ht.print_table()
for num in data2:
    ht.insert(num, data2)
    ht.print_table()