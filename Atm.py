class Atm(object):
    def __init__(self, model, color, company, bank_account):
        self.model = model
        self.color = color
        self.company = company
        self.bank_account = bank_account


    def start(self):
        print("started")

    def stop(self):
        print("finished")

    def accelarate(self):
        print("accelarating")
        "accelerator functionality"

    def withdrawal(self, withdrawl):
        print("get your withdrawal")
        "withdrawal here"

onsite = Atm("pin","red","onsite","$8000.00")
print(onsite.bank_account)