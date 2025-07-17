class Queue(object):
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

class Condition(object):
    def __init__(self, rank):
        self.rank = rank

    def __ge__(self, other): # Membandingkan prioritas
        return self.rank >= other.rank

    def __str__(self):
        if self.rank == 1: return "critical"
        elif self.rank == 2: return "serious"
        else: return "fair"

