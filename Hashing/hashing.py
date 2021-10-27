# HASHING

class Hashing:
    def __init__(self):
        self.MAX=10
        self.arr=[[] for item in range(self.MAX)]

    def gethash(self,key):
        total=0
        for i in key:
            total+=ord(i)
        return total%self.MAX

    def __getitem__(self, key):
        hash_val=self.gethash(key)
        for item in self.arr[hash_val]:
            if item[0]==key:
                return item[1]

    def __setitem__(self, key, value):
        hash_val=self.gethash(key)
        found=False
        for idx,elem in enumerate(self.arr[hash_val]):
            if len(elem)==2 and elem[0]==key:
                self.arr[hash_val][idx]=(key,value)
                found=True
                break

        if not found:
            self.arr[hash_val].append((key,value))


hsh=Hashing()
hsh['day1']="Yoga"
hsh['day2']="GYM"
hsh['day3']="Cycling"
print(hsh['day1'])
