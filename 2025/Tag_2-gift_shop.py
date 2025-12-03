ids_all = "197-407,262128-339499,557930-573266,25-57,92856246-93001520,2-12,1919108745-1919268183,48414903-48538379,38342224-38444598,483824-534754,1056-1771,4603696-4688732,75712519-75792205,20124-44038,714164-782292,4429019-4570680,9648251-9913729,6812551522-6812585188,58-134,881574-897488,648613-673853,5261723647-5261785283,60035-128980,9944818-10047126,857821365-857927915,206885-246173,1922-9652,424942-446151,408-1000"
ids_short = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

#------------Part One------------#

def check_id_1(ids):
    ids_seperated = [pair.split("-") for pair in ids.split(",")]
    total = 0
    for start, end in ids_seperated:
        for id in range(int(start), int(end) + 1):
            id_str = str(id)
            length = len(id_str)
            if id_str[length//2:] == id_str[:length//2]:
                total += id
    return total

#------------Part Two------------#


def is_invalid_repetition(id):
    length = len(id)
    for window_size in range(1, length):
        if length % window_size == 0:                 
            repeats = length // window_size
            if repeats >= 2:           
                pattern = id[:window_size]
                if pattern * repeats == id:
                    return True
    
    return False

def check_id_2(ids):
    ids_separated = [pair.split("-") for pair in ids.split(",")]
    total = 0

    for start, end in ids_separated:
        for id in range(int(start), int(end) + 1):
            if is_invalid_repetition(str(id)):
                total += id

    return total


print(check_id_2(ids_all))