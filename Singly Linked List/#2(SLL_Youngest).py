class Student:
    def __init__(self, fname = "", lname = "", yob = 0, mob = 0, dob = 0, sex ="", next=None):
        self.fname = fname
        self.lname = lname
        self.yob = yob
        self.mob = mob
        self.dob = dob
        self.sex = sex
        self.next = next

start = Student()
last = None
New = None

def insert(node):
    global last
    node = start.next
    last = start
    while node:
        node = node.next
        last = last.next

    if node is None:
        global New
        New = Student()
        New.next = node
        last.next = New
        name = input("\nEnter the first name: ")
        New.fname = name
        name = input("\nEnter the last name: ")
        New.lname = name
        n = int(input("\nEnter the year of birth: "))
        New.yob = n
        n = int(input("\nEnter the month of birth: "))
        New.mob = n
        n = int(input("\nEnter the day of birth: "))
        New.dob = n
        ch = input("\nEnter the sex [m/f]: ")
        New.sex = ch

def create(node):
    global start
    n = 0
    ch = ""
    start.next = None
    node = start
    while True:
        node.next = Student()
        node = node.next
        name = input("\nEnter the first name: ")
        node.fname = name
        name = input("\nEnter the last name: ")
        node.lname = name
        n = int(input("\nEnter the year of birth: "))
        node.yob = n
        n = int(input("\nEnter the month of birth: "))
        node.mob = n
        n = int(input("\nEnter the day of birth: "))
        node.dob = n
        ch = input("\nEnter the sex [m/f]: ")
        node.sex = ch
        node.next = None
        ch = input("\nDo you want to create more nodes [y/n]: ")
        if ch.lower() == "n":
            break

def display(node):
    node = start.next
    print("\nData Siswa:")
    while node:
        print(f"{node.fname}\t{node.lname}\t{node.yob}\t{node.mob}\t{node.dob}\t{node.sex}")
        node = node.next

def delete(node):
    name = input("\nEnter the first name that will be deleted: ")
    node = start.next
    preNode = start
    while node is not None:
        if node.fname == name:
            preNode.next = node.next
            print(f"\nData '{name}' berhasil dihapus.")
            return
        else:
            preNode = node
            node = node.next
    print("Data not found.")


#Fungsi termuda----------------------------------------------------------------------------------------------------
def youngest_student(node):
    node = start.next
    if node is None:
        print("\nNo students available.")
        return

    youngest = node  
    while node:
        if node.yob > youngest.yob:
            youngest = node  
        elif node.yob == youngest.yob:
            if node.mob > youngest.mob:
                youngest = node
            elif node.mob == youngest.mob:
                if node.dob > youngest.dob:
                    youngest = node
        node = node.next  
    print("\nYoungest Student: " + youngest.fname + " " + youngest.lname +
          "\n Year of Birth: " + str(youngest.yob) +
          "\n Month of Birth: " + str(youngest.mob) +
          "\n Day of Birth: " + str(youngest.dob) +
          "\n Sex: " + youngest.sex)


#---------------------------------------------------------------------------------------------------------------------

def main():
    node = None
    create(node)
    while True:
        print("\nMenu:")
        print("1. Tambah Data Siswa")
        print("2. Data Siswa")
        print("3. Hapus Data Siswa")
        print("4. Siswa Termuda")
        print("0. Exit")
        opt = int(input("\nEnter your choice: "))
        if opt == 1:
            insert(node)
        elif opt == 2:
            display(node)
        elif opt == 3:
            delete(node)
        elif opt == 4:
            youngest_student(node)
        elif opt == 0:
            print("\nProgram selesai.")
            break
        else:
            print("\nInvalid choice.")

if __name__ == "__main__":
    main()