from bankmodel import BankModel, Customer, ServiceType

class BankView(object):
    def __init__(self, model):
        self.model = model

    def run(self):
        menu = "=== Bank Queue System ===\n" + \
               "  1. Tambah pelanggan baru ke antrian\n" + \
               "  2. Layani 1 pelanggan berikutnya\n" + \
               "  3. Layani semua pelanggan\n" + \
               "  4. Keluar\n"
        while True:
            command = self.getCommand(4, menu)
            if command == 1:
                self.addQueueCustomer()
            elif command == 2:
                self.serveNext()
            elif command == 3:
                self.serveAll()
            else:
                break

    def addQueueCustomer(self): #pilih 1
        name = input("\nMasukkan nama pelanggan: ")
        service_type = self.getServiceType()
        self.model.addCustomer(Customer(name, service_type))
        print(name, "ditambahkan ke antrian Layanan", service_type, "\n")

    def serveNext(self): #pilih 2
        if self.model.isEmpty():
            print("Tidak ada pelanggan dalam antrian.")
        else:
            customer = self.model.serveNext()
            print(customer, "sedang dilayani..")

    def serveAll(self): #pilih 3
        if self.model.isEmpty():
            print("Tidak ada pelanggan dalam antrian.")
        else:
            while not self.model.isEmpty():
                self.serveNext()

    def getServiceType(self):
        menu = "\nJenis Layanan:\n" + \
               "  1. Pengaduan Kritis\n" + \
               "  2. Transaksi Besar\n" + \
               "  3. Layanan Umum\n"
        #1 = prioritas tinggi, 2 = prioritas sedang, 3 = prioritas rendah
        number = self.getCommand(3, menu)
        return ServiceType(number)

    def getCommand(self, high, menu):
        prompt = "Pilih angka (1-" + str(high) + "): "
        commandRange = list(map(str, range(1, high + 1)))
        while True:
            print(menu)
            command = input(prompt)
            if command in commandRange:
                return int(command)
            else:
                print("Input salah, coba lagi.")

def main():
    model = BankModel()
    view = BankView(model)
    view.run()

if __name__ == "__main__":
    main()
