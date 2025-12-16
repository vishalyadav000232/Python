from pydantic import BaseModel, model_validator , computed_field
from datetime import datetime
from typing import Optional, Dict


# ------------------ Pydantic Model ------------------
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height : float
    dateTime: Optional[datetime] = None
    constct_details: Dict[str, str]
    # bmi : Optional[float] = None

    @model_validator(mode="after")
    def validate_emergency_contact(self):
        # Rule: If age > 30, emergency contact is required
        if self.age > 30 and "emergency" not in self.constct_details:
            raise ValueError(
                "Emergency contact is required for patients older than 30"
            )
        return self
    @computed_field
    @property
    def bmi(self)-> float:
        bmi = round((self.weight)/(self.height**2) ,2)
        return bmi


# ------------------ Functions ------------------
def insert_patient_data(user: Patient):
    print("\nInserting patient data...")
    print("Name:", user.name)
    print("Age:", user.age)
    print("Weight:", user.weight)
    print("Contact:", user.constct_details)
    print("Date:", user.dateTime)


def update_patient_data(user: Patient):
    print("\nUpdating patient data...")
    print("Name:", user.name)
    print("Age:", user.age)
    print("Weight:", user.weight)
    print("Contact:", user.constct_details)
    print("Date:", user.dateTime)
    print("Bmi:", user.bmi)


# ------------------ Input Data ------------------
person = {
    "name": "Rahul",
    "age": 31,   # Try changing this to 30 to see validation difference
    "weight": 19.0,
    "height" : 7.1 , 
    "dateTime": datetime.now(),
    "constct_details": {
        "phone": "209334",
        "emergency": "9876543210"   # Remove this to trigger validation error
    }
}

# ------------------ Create Object ------------------
user = Patient(**person)

# ------------------ Call Functions ------------------
insert_patient_data(user)
update_patient_data(user)
