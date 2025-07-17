class Queue:
    def __init__(self):
        self.array = []

    def isEmpty(self): # mengecek antrian kosong atau tidak
        return len(self.array) == 0
    
    def long(self): # Mengihitung jumlah antrian
        return len(self.array)
    
    def queFront(self): # Mengambil antrian pertama
        if self.isEmpty():
            return None
        return self.array[0]
    
    def addQue(self,data): # Menambahkan antrian
        self.array.append(data)

    def remQue(self): # Membuang antrian pertama
        if self.isEmpty():
            print("Underflow")
            return None
        data = self.array[0]
        self.array.remove(data)
        return data
    
    def __str__(self):
        ans = "["
        for i in range(self.long()):
            if len(ans) > 1:
                ans += ", "
            ans = ans + self.array[i]
        ans += "]"
        return ans

  
antrian = Queue ()
for orang in ['DON', 'KEN', 'IVAN', 'RAJA','AMIR','ADI']:
    antrian.addQue(orang)

print('Setelah ditambahkan', antrian.long(), ' orang dalam antrian') # -> antrian.long() itu method
print('Didalamnya ada: ', antrian)