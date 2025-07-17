class Student:
    def __init__(self, fname="", lname="", yob=0, mob=0,
                 dob=0, sex="", next=None):
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
        ch = input("\nEnter the sex[m/f]: ")
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
        ch = input("\nEnter the sex[m/f]: ")
        node.sex = ch
        node.next = None
        ch = input("\nDo you want to create more nodes[y/n]: ")
        if ch.lower() == "n":
            break

def display(node):
    node = start.next
    while node:
        print(f"\n{node.fname}\t{node.lname}\t{node.yob}\t{node.mob}\t{node.dob}\t{node.sex}")
        node = node.next

def delete(node):
    name = input("\nEnter the first name of the student to be deleted: ")
    node = start.next
    preNode = start
    while node is not None and (node.fname != name or node):
        if node.fname == name:
            preNode.next = node.next
            return
        else:
            preNode = node
            node = node.next
    print("Data not found")

#Fungsi tertua--------------------------------------------------------------
def oldest_student():
    node = start.next
    if node is None:
        print("No students available.")
        return

    oldest = node 
    while node: 
        if node.yob < oldest.yob:  
            oldest = node  
        elif node.yob == oldest.yob: 
            
            if node.mob < oldest.mob:  
                oldest = node  
            elif node.mob == oldest.mob:  
                
                if node.dob < oldest.dob:  
                    oldest = node  
        node = node.next  

    print("\nOldest Student: " + oldest.fname + " " + oldest.lname + 
          ", Year of Birth: " + str(oldest.yob) + 
          ", Month of Birth: " + str(oldest.mob) + 
          ", Day of Birth: " + str(oldest.dob) + 
          ", Sex: " + oldest.sex)
#--------------------------------------------------------------------------
def main():
    node = None
    create(node)
    while True:
        print("\n1.Add Student\n2.Display Students\n3.Delete Student\n4.Find Oldest Student\n0.Exit")
        opt = int(input("\nEnter the choice: "))
        if opt == 1:
            insert(node)
        elif opt == 2:
            display(node)
        elif opt == 3:
            delete(node)
        elif opt == 4:
            oldest_student()
        elif opt == 0:
            break
        else:
            print("\nInvalid Choice")

if __name__ == "__main__":
    main()