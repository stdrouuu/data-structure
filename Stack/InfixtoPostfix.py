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
    
# infix: (A+B) + (C-D)
# prefix: -
# postfix: AB+CD-+

# () : di posisi 17
# * / % : di posisi 13
# +- : di posisi 12

# dimasukkan ke stack untuk mengubah infix menjadi postfix
# infix: 2 + 3 * 4
# postfix: 2 3 4 * +

# 2 -----------
# postFixLst = [2]
# opStack
# [  ]

# + ------------- (langsung ke # cek kesini (di bawah))-------------------------------------------
# postFixLst = [2]
# opStack
# [ + ]

# 3 -------------
# postFixLst = [2,3]
# opStack
# [ + ]

# * -------------
# postFixLst = [2,3]
# opStack
# [ + ]
# (prec[+] >= prec[*])
# [ * ]
# [ + ]

# 4 -------------
# postFixLst = [2,3,4]
# opStack
# [ * ]
# [ + ]

# postFixLst = [2,3,4,*]
# opStack
# [ + ]

# postFixLst = [2,3,4,*,+]
# opStack
# [  ] -> kosong karena di-pop

# setelah itu baru masuk ke #while(not opStack.isEmpty()):
        


# A * B - (C + D) + E
#      stack
# A -> -
# * -> Push *
# B -> -
# - -> 

def infixToPostfix(infixExpr):
    prec = {}
    prec ["*"] = 3
    prec ["/"] = 3
    prec ["+"] = 2
    prec ["-"] = 2
    prec ["("] = 1

    opStack = stack()
    postfixLst = []
    tokenList = infixExpr.split()

    for token in tokenList: # cek kesini------------------------------------------------------
        if token in "ABCDEFGHIJKLMNOPQRSTUVYXYZ" or token in "0123456789":
            postfixLst.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(": 
                postfixLst.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixLst.append(opStack.pop())
            opStack.push(token)

    while (not opStack.isEmpty()):
        postfixLst.append(opStack.pop())
    return " ".join(postfixLst)

print(infixToPostfix("2 + 3 * 4"))
print(infixToPostfix("( A + B ) + ( C - D )"))