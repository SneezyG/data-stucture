from timeit import time
class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        data = self.arr[h]
        if data != None and data[0] == key:
          return data[1]
        else:
          begin_itr = h
          while True:
            h += 1
            if begin_itr == h:
              print("item cannot be found")
              break
            if h == self.MAX:
              h = 0
            data = self.arr[h]
            if data != None and data[0] == key:
              return data[1]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        data = self.arr[h]
        if data == None:
          self.arr[h] = (key, val)
        else:
          if data[0] == key:
            self.arr[h] = (key, val)
          else:
            begin_itr = h
            while True:
              h += 1
              if begin_itr == h:
                print("no more space")
                break
              if h == self.MAX:
                h = 0
              data = self.arr[h]
              if data == None or data[0] == key:
                self.arr[h] = (key, val)
                break

    def __delitem__(self, key):
        h = self.get_hash(key)
        data = self.arr[h]
        if data != None and data[0] == key:
          self.arr[h] = None
        else:
          begin_itr = h
          while True:
            h += 1
            if begin_itr == h:
              print("item cannot be found")
              break
            if h == self.MAX:
              h = 0
            data = self.arr[h]
            if data != None and data[0] == key:
              self.arr[h] = None
              break
      
            
if __name__ == '__main__':
    start = time.time()
    
    t = HashTable()
    t["march 6"] = 20
    t["march 17"] =  88
    print(t.arr)
    t["march 17"] = 29
    print(t.arr)
    t["nov 1"] = 1
    print(t.arr)
    t["march 33"] = 234
    print(t.arr)
    print(t["dec 1"])
    print(t["march 33"]) 
    t["march 33"] = 999
    print(t.arr)
    print(t["march 33"])
    t["april 1"] = 87
    print(t.arr)
    t["april 2"]=123
    print(t.arr)
    t["april 3"]=234234
    print(t.arr)
    t["april 4"]=91
    print(t.arr)
    t["May 22"]=4
    print(t.arr)
    t["May 7"]=47
    print(t.arr)
    t["Jan 1"]=20
    print(t.arr)
    del t["april 2"]
    print(t.arr)
    t["Jan 1"]=0
    print(t.arr)
    
    end = time.time()
    print(f"Runtime of the program is {end - start}")
          