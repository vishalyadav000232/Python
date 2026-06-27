

class Mobile:
    def __init__(self, name, model, passWord):
        self.name = name          # public
        self._model = model       # protected
        self.__password = passWord  # private

    # getter (read access)
    def get_password(self):
        return self.__password

    # setter (write access)
    def set_password(self, new_pass):
        self.__password = new_pass


class Brand(Mobile):
    def __init__(self, name, model, passWord, brand_name):
        super().__init__(name, model, passWord)
        self.brand_name = brand_name

    # ✅ child class accessing private via parent method
    def show_password(self):
        return self.get_password() 


b1 = Brand("Infinix", "i2", 1234, "Xor")

print(b1.show_password())     # ✅ 1234

b1.set_password(9999)         # ✅ change password safely
print(b1.show_password())     # ✅ 9999

class Test:
    def __init__(self):
        self.__private_var = "I am private"

    def get_private_var(self):
        return self.__private_var