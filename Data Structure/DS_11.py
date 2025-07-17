from array import *
arrNilai = array("i", [10, 20, 30, 40, 50]) 
for  x in arrNilai:
    print(x)

#Description: 
#import array module
#declare arrNilai with integer data type
# i : integer, c : character, f : float, d : double
#print all data from arrNilai

print(arrNilai[3])

#print value of arrNilai with index-3

arrNilai.insert(2, 25) #menjadi [10, 20, -25-, 30, 40, 50]
for  x in arrNilai:
    print(x)

#insert a new value 25 at index-2

arrNilai.remove(25)
for  x in arrNilai:
    print(x)

#remove value 25 from arrNilai

print(arrNilai.index(40)) #index dari 40 yaitu 3
#print(arrNilai.index(60))

#find value 40 and 60 from arrNilai

arrNilai[arrNilai.index(40)] = 70 #update value 40 to 70 from arrNilai
for  x in arrNilai:
    print(x)

