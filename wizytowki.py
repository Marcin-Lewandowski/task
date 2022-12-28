from faker import Faker

class BaseContact():

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self) -> str:
        return f'{self.name} {self.phone} {self.email}'

    def __repr__(self):
        return f"BaseContact(name={self.name} phone={self.phone}, email={self.email})"

    def contact(self):
        print("Wybieram numer %s i dzwonię do %s" % (self.phone, self.name))


    @property
    def label_length(self):
        return len(self.name)



class BusinessContact(BaseContact):
    def __init__(self, job, company_name, work_phone, *args, **kwargs):
       super().__init__(*args, **kwargs)

       self.job = job
       self.company_name = company_name
       self.work_phone = work_phone

    def __str__(self) -> str:
        return f'{self.name} {self.job} {self.company_name} {self.work_phone} {self.email}'

    def __repr__(self):
        return f"BusinessContact(name = {self.name} job = {self.job} company = {self.company_name}  phone={self.work_phone} email={self.email})"


    def contact(self):
        print("Wybieram numer %s i dzwonię do %s" % (self.work_phone, self.name))

    

def create_contacts(type, quantity):

    bc = []

    if type == 1:
        for _ in range (1, quantity):
            bc.append(BaseContact(name = fake.name(), phone = fake.phone_number(), email = fake.email()))

    elif type == 2:
        for _ in range (1, quantity):
            bc.append(BusinessContact(name = fake.name(), job = fake.job(), company_name = fake.company(), phone = fake.phone_number(), work_phone = fake.phone_number(), email = fake.email()))

    return bc

    
    
fake = Faker(['pl_PL'])

w1 = BaseContact(name = fake.name(), phone = fake.phone_number(), email = fake.email())
w2 = BusinessContact(name = fake.name(), job = fake.job(), company_name = fake.company(), phone = fake.phone_number(), work_phone = fake.phone_number(), email = fake.email())

print(w1)
print(w2)
print()
w1.contact()
w2.contact()
print()
print(w1.label_length)
print(w2.label_length)
print()
print()
print("------------------")
print()
print(create_contacts(1, 4))
print()
print(create_contacts(2, 4))
'''
Używając dziedziczenia, rozdziel podstawową klasę wizytówki na dwie osobne: pierwsza (BaseContact) 
powinna przechowywać podstawowe dane kontaktowe takie jak imię, nazwisko, telefon, adres e-mail. 
Za pomocą kolejnej klasy (BusinessContact) rozszerz klasę bazową o przechowywanie informacji związanych z pracą danej osoby – stanowisko, nazwa firmy, telefon służbowy.
Oba typy wizytówek, powinny oferować metodę contact(), która wyświetli na konsoli komunikat w postaci 
“Wybieram numer +48 123456789 i dzwonię do Jan Kowalski”. Wizytówka firmowa powinna wybierać służbowy numer telefonu, a wizytówka bazowa prywatny.
Oba typy wizytówek powinny mieć dynamiczny atrybut label_length, który zwraca długość imienia i nazwiska danej osoby.

Stwórz funkcję create_contacts, która będzie potrafiła komponować losowe wizytówki. 
Niech ta funkcja przyjmuje dwa parametry: rodzaj wizytówki oraz ilość. Wykorzystaj bibliotekę faker do generowania danych.


'''
