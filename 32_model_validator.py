from pydantic import BaseModel, model_validator
from datetime import datetime
from typing import Optional, Dict


# ------------------ Pydantic Model ------------------
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    dateTime: Optional[datetime] = None
    constct_details: Dict[str, str]

    @model_validator(mode="after")
    def validate_emergency_contact(self):
        # Rule: If age > 30, emergency contact is required
        if self.age > 30 and "emergency" not in self.constct_details:
            raise ValueError(
                "Emergency contact is required for patients older than 30"
            )
        return self


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


# ------------------ Input Data ------------------
person = {
    "name": "Rahul",
    "age": 31,   # Try changing this to 30 to see validation difference
    "weight": 19.0,
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
