from datetime import datetime
from . import router
from fastapi import status
from fastapi import Query
from helpers.program_details import find_program
from helpers.program_details import find_program_for_special_case


@router.get("/{dob}", status_code=status.HTTP_200_OK, tags=["programs"])
async def suggest_suitable_program(dob: str) -> str:
    """
    Determine the suitable Learning Age program based on the age of the child

    - Param: **dob** - The date of birth entered by the parent on the website
    - Returns: **program** - The most suitable program based on the date of birth
    """
    date_of_birth = datetime.strptime(dob, "%Y-%m-%d").date()
    current_date = datetime.now().date()

    age_in_months = (current_date.year - date_of_birth.year) * 12 + (current_date.month - date_of_birth.month)

    if age_in_months < 6:
        return "Child too young"
    
    if age_in_months > 96:
        return "Child too old"

    if age_in_months > 11 and current_date.month == 6 and current_date.day == 1:
        program = find_program_for_special_case(age_in_months)
    else:
        program = find_program(int(age_in_months))

    return program




