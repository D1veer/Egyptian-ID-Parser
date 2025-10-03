from datetime import datetime

def parse_egyptian_id(card_id: str) -> dict:
    """
    Parse an Egyptian national ID and return birthdate, gender, and governorate info.
    """
    digits = list(card_id)

    # Determine century
    gen = "1900" if digits[0] == "2" else "2000"
    year = int(gen[:2] + digits[1] + digits[2])
    month = int("".join(digits[3:5]))
    day = int("".join(digits[5:7]))

    # Birthdate
    birthdate = datetime(year, month, day)

    # Gender (last digit odd = male, even = female)
    gender = "male" if int(digits[-2]) % 2 != 0 else "female"

    # Governorate table
    governorates = {
        1: "Cairo", 2: "Alexandria", 3: "Port Said", 4: "Suez",
        11: "Damietta", 12: "Dakahlia", 13: "Sharqia", 14: "Qalyubia",
        15: "Kafr El Sheikh", 16: "Gharbia", 17: "Monufia", 18: "Beheira",
        19: "Ismailia", 21: "Giza", 22: "Beni Suef", 23: "Fayoum",
        24: "Minya", 25: "Assiut", 26: "Sohag", 27: "Qena", 28: "Aswan",
        29: "Luxor", 31: "Red Sea", 32: "New Valley", 33: "Matrouh",
        34: "North Sinai", 35: "South Sinai"
    }
    gov_code = int("".join(digits[7:9]))
    governorate = governorates.get(gov_code, "Unknown")

    # Age
    today = datetime.today()
    age = today.year - birthdate.year - (
        (today.month, today.day) < (birthdate.month, birthdate.day)
    )

    return {
        "birthdate": birthdate.strftime("%Y-%m-%d"),
        "age": age,
        "gender": gender,
        "governorate": governorate
    }

if __name__ == "__main__":
    card_id = input("Please enter the ID number: ")
    info = parse_egyptian_id(card_id)
    print(info)
