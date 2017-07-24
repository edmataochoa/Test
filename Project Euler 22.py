names = open("p022_names.txt", "r").read()

def numerical_value(letter):
    return ord(letter.lower()) - 96

def sort_names(lst):
    current_name = ""
    names_list = []
    for character in lst:
        if character.isalpha():
            current_name += character
        if character == ",":
            names_list.append(current_name)
            current_name = ""
    names_list.append(current_name)
    names_list.sort()
    return names_list

def convert_to_num(lst):
    sum_name = 0
    rank = 1
    scores_sum = 0
    for name in lst:
        for character in name:
            sum_name += numerical_value(character)
        scores_sum += rank * sum_name
        if name == "COLIN":
            print("COLIN")
            print("rank = ", rank)
            print("sum_name = ", sum_name)
            print("sum = ", rank * sum_name)
        sum_name = 0
        rank += 1
    return scores_sum

def get_score(lst):
    return convert_to_num(sort_names(lst))

print(get_score(names))
