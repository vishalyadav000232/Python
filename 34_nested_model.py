from pydantic import BaseModel 
class Address(BaseModel):
    plot_no : int
    area : str
    city : str
    pin : int
    state : str

class Patient(BaseModel):
    name : str
    gender : str
    age : int
    address :  Address



address ={
    "plot_no" : 110,
    "area" : "kathoraon",
    "city" : "varansi",
    "pin" : 221207,
    "state" : "uttar predesh"

}

Address1 = Address(**address)


p2 = {
    "name": "vishal",
    "gender": "male",
    "age":22,
    "address":Address1

}

p1 = Patient(**p2)
print(p1)
print(p1.address.area)
print(p1.address.city)
print(p1.address.pin)
temp = p1.model_dump(include=["address"])
print(temp)

json = p1.model_dump_json( exclude=['name'])
print(json)
print(type(json))