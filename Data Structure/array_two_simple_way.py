from array import * #pilihan

arr_one = [11,12,5,2] #array dimensi satu
for x in arr_one:
    print(x)

arr_two = [[11,12,5,2], 
           [15,6,10,5], #array dimensi dua
           [10,7,12,9]] 
for x in arr_two:
    for y in x:
        print(y)

arr_two.insert(2,[8,6,10,3]) #insert data ke - 2
arr_two[0][3] = 8 #update data baris ke - 1, kolom ke - 4
del arr_two[2] #hapus data ke - 2
