from pathlib import Path

folder_path = Path(__file__).parent

big_data_set = folder_path / "big_data.txt"
small_data_set = folder_path / "small_data.txt"

def get_and_parse_data(data_path):
    with open(data_path, "r") as f:
        banks = f.read()

    return banks.strip().split("\n")


#------------Part One------------#

def get_joltage_1():
    banks = get_and_parse_data(big_data_set)
    total = 0

    for bank in banks:
        best_joltage = -1
        max_seen = -1
        for batteriy in bank:
            charge = int(batteriy)
            if max_seen != -1:
                candidate = max_seen * 10 + charge
                if candidate > best_joltage:
                    best_joltage = candidate
            if charge > max_seen:
                max_seen = charge
        total += best_joltage
    return total


#------------Part Two------------#

def get_joltage_2():
    banks = get_and_parse_data(big_data_set)
    total = 0
    
    for bank in banks:
        amount_batteries = len(bank)
        max_batteries = 12
        
        charges = []
        
        for battery, battery_charge in enumerate(bank):

            while charges and battery_charge > charges[-1] and len(charges) + (amount_batteries - battery) > max_batteries:
                charges.pop()

            if len(charges) < max_batteries:
                charges.append(battery_charge)
        
        result = int(''.join(charges))
        total += result
    
    return total


# function that works for n batterries:

def get_joltage(banks, max_batteries = 12):
    banks = banks.strip().split("\n")
    total = 0
    
    for bank in banks:
        amount_batteries = len(bank)
        
        charges = []
        
        for battery, battery_charge in enumerate(bank):

            while charges and battery_charge > charges[-1] and len(charges) + (amount_batteries - battery) > max_batteries:
                charges.pop()

            if len(charges) < max_batteries:
                charges.append(battery_charge)
        
        result = int(''.join(charges))
        total += result
    
    return total

print(f"Solution 1: {get_joltage_1()}")
print(f"Solution 2: {get_joltage_2()}")