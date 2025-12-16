from pydantic import BaseModel, EmailStr , Field
from datetime import datetime
from typing import Optional , Annotated

class Patient(BaseModel):
    name: Annotated[str , Field(max_length=13 , title =" name of the patent ")]
    email:Annotated[EmailStr , Field(default= "abc@gmail.com")]
    age: int
    weight: Optional[float] = None
    dateTime: Optional[datetime] = None

def insert_patient_data(user: Patient):
    print("Inserting patient data...")
    print("Name:", user.name)
    print("Age:", user.age)
    print("Date:", user.dateTime)
    print("Email:", user.email)

def update_patient_data(user: Patient):
    print("Updating patient data...")
    print("Name:", user.name)
    print("Email:", user.email)
    print("Age:", user.age)
    print("Weight:", user.weight)
    print("Date:", user.dateTime)

person = {
    "name": "Rahul",
    "age": 30,
    "weight": 19.0,
    "dateTime": datetime.now(),
    "email": "ghochu@gmail.com"
}

user = Patient(**person)

insert_patient_data(user)
update_patient_data(user)
