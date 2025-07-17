class stack: # stack itu tumpukan
    def __init__(self):
        self.items = []

    def push(self,item): # push: menambahkan node
        self.items.append(item)

    def pop(self): # pop: menghapus, membuang, remove node(buang yang paling atas)
        return self.items.pop()
    
    def isEmpty(self): # cek kosong atau tidak
        return (self.items == [])
    
    def peek(self): # melihat item paling atas
        return self.items[-1]
    
    def __str__(self): # fungsi tambahan untuk konversi menjadi str (string)
        return str(self.items)
    
def isPalindrome(str):
    strStack = stack ()
    palindrome = False
    for char in str:
        strStack.push(char)
    for char in str:
        if(char == strStack.pop()):
            palindrome = True
        else:
            palindrome = False
    return palindrome

print(isPalindrome("ada"))
