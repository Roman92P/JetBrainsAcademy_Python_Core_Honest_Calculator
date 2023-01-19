name = input()

def normalize(name):

    # put your code here
    new_name = name.replace('é', 'e').replace("ë", 'e').replace('á', 'a').replace('å', 'aa').replace('œ', 'oe').replace('æ', 'ae')

    return new_name

print(normalize(name))