def find_program(age_in_months: int) -> str:
    programs = {
        "Bright Beginnings": range(1,12),
        "Growing Years": range(12,24),
        "Joys of Learning": range(24,36),
        "School Readiness": range(36,48),
        "After Party": range(48,97)
    }

    for i in programs.keys():
        if age_in_months in programs[i]:
            return i
    else: 
        return "Program not found"


def find_program_for_special_case(age_in_months: int) -> str:
    special_case_programs = {
        "Joys of Learning": 22,
        "School Readiness": 34,
        "After Party": 46
    }

    for i in special_case_programs.keys():
        if age_in_months == special_case_programs[i]:
            return i
     
    return find_program(age_in_months)