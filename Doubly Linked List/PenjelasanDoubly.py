class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def set_data(self,data):
        self.data = data
    def get_data(self):
        return self.data
    
    def set_next(self,next):
        self.next = next
    def get_next(self):
        return self.next
    def has_next(self):
        return self.next != None
    
    def set_prev(self,prev):
        self.prev = prev
    def get_prev(self):
        return self.prev
    def has_prev(self):
        return self.prev != None
    
    def __str__(self):
        return "Mode[Data-%s]" % (self.data,)
    

class DoublyLinkedList:
    def __init__(self): #definisiin/inisialisasiin 
        self.head = None #head bakal di-set ke node pertama
        self.tail = None #tail bakal di-set ke node terakhir
#Awalnya, linked list kosong, jadi keduanya None.
        
    def insert(self,data): #def untuk menambahkan node baru ke linked list
        if(self.head == None): #memeriksa apakah linked list kosong dengan cek self.head = None
            self.head = Node(data) #Jika linked list kosong, node baru dibentuk.
            self.tail = self.head # Karena ini adalah satu-satunya simpul dalam linked list.
        else: # jika linked list tidak kosong, kita masuk ke blok else
            current = self.head #buat pointer current yang menunjuk ke node pertama
            while(current.next != None): #loop while yang digunakan untuk menelusuri linked list hingga mencapai node terakhir.
                current = current.next
                #current.next digunakan untuk memeriksa apakah ada node berikutnya. 
                #Jika tidak ada (None), berarti current adalah node terakhir.
            current.next = Node(data,None,current) #Setelah mencapai node terakhir, kita membuat node baru
                                 #None berarti node baru ini tidak memiliki node berikutnya
                                 #Current adalah referensi ke node sebelumnya sebelum penambahan node baru.
            self.tail = current.next #memperbarui tail menunjuk ke node baru yang baru ditambahkan

    def delete(self,data): #def untuk menambahkan menghapus elemen dari linked list.
        current = self.head #inisialisasi variabel current yg menunjuk ke node pertama
        if current.data == data: #memeriksa apakah data dari node pertama (current.data)-
                                 #-sama dengan yg ingin dihapus (data)
            self.head = current.next #Jika data dari node pertama sama dengan data,-
                                     #-maka head akan menunjuk ke node berikutnya (current.next)
            self.head.prev = None #setelah mengubah head, kita jg harus ubah prev dari node baru menjadi None
            return True #penghapusan berhasil
        if current == None: #jika current = None, berarti linked list kosong
            return False #penghapusan gagal
        if self.tail == data: #memeriksa apakah data yg ingin dihapus sama dengan data dari node terakhir (tail)
            self.tail = self.tail.prev #Jika data dari node terakhir sama dengan data, kita mengatur tail- 
                                       #-menunjuk ke node sebelumnya (tail.prev)
            self.tail.next = None ##setelah mengubah tail, kita jg harus ubah next dari node baru menjadi None
            return True #penghapusan berhasil
        while current != None: #Jika elemen yang ingin dihapus bukan node pertama atau terakhir, masuk ke blok while 
            if current.data == data: #memeriksa apakah data dari node saat ini (current.data),-
                                     #-sama dengan yang ingin dihapus (data)
                current.prev.next = current.next #Jika data dari current.data = data
                #mengatur next dari node sebelumnya (current.prev) menunjuk node berikutnya (current.next)
                current.next.prev = current.prev #mengatur prev dari node berikutnya (current.next)-
                                                 #-untuk menunjuk ke node sebelumnya (current.prev)
                return True #penghapusan berhasil
            current = current.next ##Jika data dari current.data != data
        return False #penghapusan gagal
    
    def insertAtBegining(self,data): #menambahkan node baru dengan nilai data di awal linked list.
        newNode = Node(data, None, None) #membuat node baru, dimana parameternya next dan prev = None
        if(self.head == None): #memeriksa apakah linked list kosong, jika head = None, maka tidak ada node dlm LL
            self.head = self.tail = newNode #menetapkan Node Baru Sebagai Head dan Tail
        else: #Jika linked list tidak kosong, kita masuk ke blok else
            newNode.set_prev(None) #Mengatur Prev Node Baru
            #pointer prev dari newNode menjadi None, karena node baru ini akan menjadi node pertama
            newNode.set_next(self.head) #Mengatur Next Node Baru: 
            #pointer next dari newNode menunjuk ke node yang saat ini menjadi head (self.head)
            self.head.set_prev(newNode) 
            #Pointer prev dari node yang saat ini menjadi head (self.head) diatur untuk menunjuk ke newNode.
            #set newNode menjadi prev dari head sebelumnya
            self.head = newNode #Memperbarui Head: Terakhir, 
            #Kita memperbarui self.head untuk menunjuk ke newNode, menjadikannya sebagai node pertama dalam linked list
            #set newNode menjadi self.head (head)
    def getNode(self,index): #mengembalikan node yang berada di index tertentu.
        currentNode = self.head #Inisialisasi Node Saat Ini yaitu head
        if currentNode == None: #jika current node = None, maka LL kosong
            return None #jika LL kosong, akan None karena tidak ada node yg dpt diambil
        i = 0 #inisialisasi i=0 (indeks, untuk melacak posisi dlm LL)
        while i < index and currentNode.get_next() is not None: 
            #Loop untuk mencari node di index tertentu, dengan kondisi i < index dan current node
            currentNode = currentNode.get_next()
            #memperbarui currentNode untuk menunjuk ke node berikutnya dalam LL
            if currentNode == None: #periksa kembali current Node = None (langkah keamanan agar tdk mengakses node yg tdk ad)
                break #loop dihentikan
            i += 1 #indeks ditingkatkan +1 utk melanjutkan ke node berikutnya dalam LL
        return currentNode #mengembalikan node yang ditemukan setelah loop selesai
    
        
    def insertAtGivenPosition(self,index,data): 
        #untuk menyisipkan node baru pada posisi tertentu dalam linked list, dgn 2 parameter;
           #-> index (posisi di mana node baru akan disisipkan) 
           #-> data (nilai yang akan dimasukkan ke dalam node baru).
        newNode = Node(data) #membuat node baru
        if self.head == None or index == 0: #periksa apakah LL kosong atau indeks=0
            self.insertAtBegining(data) #jika salah satu if benar, maka sisipkan node baru di awal LL
        elif index < 0: #memeriksa apakah indeks yang diberikan kurang dari 0
            temp = self.getNode(index) #mencoba mendapatkan node(yang negatif) pada indeks yang diberikan 
            if temp == None or temp.get_next() == None: #memeriksa apakah temp = None 
                                                        #(artinya tidak ada node pada indeks negatif) 
                self.insert(data) #jika salah satu dari if di atas benar,
                                  #kita memanggil metode insert untuk menambahkan node baru di akhir LL
            else: #Jika indeks tidak negatif dan tidak 0, 
                  #kita masuk ke blok else untuk menyisipkan node baru di posisi yang valid.
                newNode.set_next(temp.get_next()) #mengatur next dari node baru, menunjuk ke node berikutnya dari temp
                                                  #mengatur pointer next dari newNode untuk menunjuk ke node berikutnya dari temp
                newNode.set_prev(temp) #mengatur prev dari node baru, menunjuk ke temp
                                       #mengatur pointer prev dari newNode untuk menunjuk ke temp
                temp.get_next().set_prev(newNode) #Memperbarui Prev Node Berikutnya
                #memperbarui pointer prev dari node berikutnya (temp.get_next()) untuk menunjuk ke newNode
                temp.set_next(newNode) #Mmperbarui Next Node Temp
                #mengatur pointer next dari temp untuk menunjuk ke newNode
                return True #penyisipan berhasil
            
            def find(self,data): #def untuk mencari, dengan parameter data 
                current = self.head #current diatur untuk menunjuk ke head dari LL,-
                                    #-yang merupakan titik awal pencarian.
                while current != None: #loop akan terus berjalan selama current tidak sama dengan None
                    if current.data == data: #memeriksa apakah nilai dari node saat ini (current.data) 
                                             #sama dengan nilai yang dicari (data)
                        return True #Jika nilai yang dicari ditemukan dalam node saat ini (current.data),-
                                    #-maka mengembalikan True
                    current = current.next #Jika nilai tidak ditemukan, 
                    #kita memperbarui current untuk menunjuk ke node berikutnya (current.next), melanjutkan pencarian.
                return False #jika loop selesai dan node tidak ditemukan, maka false
            
            def fwd_print(self):
                current = self.head #inisialisasi current menunjuk ke head (node pertama dlm LL)
                if current == None: #jika current = None, maka LL kosong
                    print("No Elements") #Cetak tidak ada element
                    return False #kembalikan False krn tdk ad yg dicetak
                while(current != None): #loop akan terus berjalan selama current tidak sama dengan None
                    print(current.data) #Di dalam loop, nilai dari node saat ini (current.data) dicetak
                    current = current.next #Jika nilai telah dicetak,-
                                           #-current diperbarui untuk menunjuk ke node berikutnya (current.next)
                return True #pencetakan berhasil
            
            def rev_print(self): 
                current = self.tail ##inisialisasi current menunjuk ke tail (node terakhir dlm LL)
                if (self.tail == None): #memeriksa apakah tail = None
                    print("No Elements") #Cetak tidak ada element
                    return False #kembalikan False krn tdk ad yg dicetak
                while (current != None): #loop akan terus berjalan selama current tidak sama dengan None
                    print(current.data) #Di dalam loop, nilai dari node saat ini (current.data) dicetak
                    current = current.prev #Jika nilai telah dicetak,-
                                           #-current diperbarui untuk menunjuk ke node sebelumnya (current.prev)
                return True #pencetakan berhasil
            
from doubly import *

dll = DoublyLinkedList()
dll.insert("alice")
print(dll.getNode(0).get_data())
# 'alice'

dll.insert("bob")
dll.insert("charlie")
print(dll.getNode(1).get_data())
# 'bob'
print(dll.getNode(2).get_data())
# 'charlie'

dll.insertAtGivenPosition(1,"donna")
print(dll.getNode(0).get_data())
# 'alice'
print(dll.getNode(1).get_data())
# 'bob'
print(dll.getNode(2).get_data())
# 'donna'
print(dll.getNode(3).get_data())
# 'charlie'
print(dll.delete("donna"))
# True


# jika, ---------------------
dll.insertAtBegining("donna")
print(dll.getNode(0).get_data())
# 'donna'
print(dll.getNode(1).get_data())
# 'bob'
print(dll.getNode(2).get_data())
# 'donna'
print(dll.getNode(3).get_data())
# 'charlie'
