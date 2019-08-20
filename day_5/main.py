

def load_chain(input_file):
    with open(input_file, 'r') as open_file:
        return open_file.readline()


def evaluate_reaction(polymer_chain):
    resulting_chain = ''
    SKIP_ITERATION = False
    NEW_REACTION = False
    for letter, next_letter in zip(polymer_chain[:-1],polymer_chain[1:]):
        if SKIP_ITERATION:
            SKIP_ITERATION = False
            continue
        if not(valid_reaction(letter, next_letter)):
            resulting_chain += letter
            continue
        else:
            NEW_REACTION = True
            SKIP_ITERATION = True
            continue

    # Check last element
    if not(valid_reaction(polymer_chain[-2],polymer_chain[-1])):
        resulting_chain += polymer_chain[-1]
    else:
        NEW_REACTION = True

    return(NEW_REACTION, resulting_chain)


def valid_reaction(letter, next_letter):
    is_same_letter = letter.lower() == next_letter.lower()
    is_same_caption = next_letter.isupper() == letter.isupper() or next_letter.islower() == letter.islower()
    return is_same_letter and not(is_same_caption)


def remove_char_from_chain(polymer_chain, char):
    polymer_chain = polymer_chain.replace(char.upper(),'')
    polymer_chain = polymer_chain.replace(char.lower(),'')
    return polymer_chain



if __name__ == '__main__':

    #polymer_chain = load_chain('input')
    #reaction = True
    #while reaction:
    #    reaction, polymer_chain = evaluate_reaction(polymer_chain)
    #print(len(polymer_chain))

    # Part 2
    polymer_chain = load_chain('input')
    all_characters = 'qwertyuiopasdfghjklzxcvbnm'
    shortest_chain = 9999999
    for char in all_characters:
        reaction = True
        modified_chain = remove_char_from_chain(polymer_chain, char)
        while reaction:
            reaction, modified_chain = evaluate_reaction(modified_chain)
        if len(modified_chain) < shortest_chain:
            shortest_chain = len(modified_chain)
    print(shortest_chain)


