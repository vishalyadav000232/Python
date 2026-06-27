'''  
Pydantic model --> 


pydantic is a data validation + prasing the data using the python type hint 


'''

#  Models -> one of the primary way to definig the schemma  in pydantic via model , model are simply classess which inherit from the basemodel and definig feils with anoteda attribites 

from pydantic import BaseModel



from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = None

user = User(
    id=1,
    name="Vishal",
    email="vishal@gmail.com",
    is_active=True
)


print(user.model_dump(include={"name" , "email"}))

print(user.model_dump(exclude=["id" , "email"]))

print(user.model_dump(exclude_none=False))