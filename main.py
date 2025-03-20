from decimal import Decimal
import re
ROMAN_NUMERALS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
galactic_units = {}

def roman_to_int(roman):
    
    total = 0
    prev_value = 0

    for char in reversed(roman):
        if char not in ROMAN_NUMERALS:
            print(f"Invalid Roman numeral: {roman} contains unknown symbol '{char}'")
            return -1 

        value = ROMAN_NUMERALS[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

def is_valid_roman(roman):


    if not all(char in ROMAN_NUMERALS for char in roman):
        return False 

    if re.search(r"(IIII|VV|XXXX|LL|CCCC|DD|MMMM)", roman):
        return False

    invalid_subtractions = ["IL", "IC", "ID", "IM",  
                            "VX", "VL", "VC", "VD", "VM",  
                            "XD", "XM",  
                            "LC", "LD", "LM",  
                            "DM",  
                            "VV", "LL", "DD"] 

    for pattern in invalid_subtractions:
        if pattern in roman:
            return False
    for i in range(len(roman) - 2):
        if ROMAN_NUMERALS[roman[i]] < ROMAN_NUMERALS[roman[i+1]] and ROMAN_NUMERALS[roman[i]] < ROMAN_NUMERALS[roman[i+2]]:
            return False  

    return True

def process_metal(line, metal):
    parts = line.split(metal)
    
    if len(parts) != 2:
        print("Invalid metal line format.")
        return

    units = parts[0].strip().split()
    credits_str = parts[1].strip().split()[-2]

    try:
        credits = int(credits_str)
    except ValueError:
        print("Invalid credit value.")
        return

    roman_value = ''.join(galactic_units.get(u, '') for u in units)

    if not roman_value or not is_valid_roman(roman_value) or roman_to_int(roman_value) == -1:
        print("I have no idea what you are talking about")
        return

    converted_int = roman_to_int(roman_value)

    if converted_int == 0:
        print("Invalid Roman numeral conversion.")
        return

    galactic_units[metal] = Decimal(credits) / Decimal(converted_int)

def translate(line, separator):
    
    parts = line.split(separator)
    
    if len(parts) != 2:
        print("Invalid translation format.")
        return

    units = parts[1].strip().split()
    
    roman_value = ""
    total = 0

    for u in units:
        if u in galactic_units:
            if u in ['Silver', 'Gold', 'Iron']:
                metal_value = Decimal(galactic_units[u])
                total = metal_value * roman_to_int(roman_value)
                print(f"{' '.join(units)} is {int(total)} Credits")
                return
            else:
                roman_value += galactic_units[u]
        else:
            print("I have no idea what you are talking about")
            return

    if roman_value:
        if is_valid_roman(roman_value) and roman_to_int(roman_value) != -1:
            total = roman_to_int(roman_value)
            print(f"{' '.join(units)} is {total}")
        else:
            print("Invalid Roman numeral format.")

def parse(line):

    line = line.strip().rstrip("?")

    if "how many Credits" in line:
        translate(line, "how many Credits is")
    
    elif "Silver" in line:
        process_metal(line, "Silver")
    
    elif "Gold" in line:
        process_metal(line, "Gold")
    
    elif "Iron" in line:
        process_metal(line, "Iron")
    
    elif "how much is" in line:
        translate(line, "how much is")
    
    elif "is" in line and not line.startswith("how"):
        parts = line.split(" is ")
        if len(parts) == 2:
            galactic_units[parts[0].strip()] = parts[1].strip()
        else:
            print("I have no idea what you are talking about")
    else:
        print("I have no idea what you are talking about")

def main():
  
    with open("input.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        parse(line)

if __name__ == "__main__":
    main()
