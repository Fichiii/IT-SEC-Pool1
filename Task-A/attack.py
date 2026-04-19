import sys, itertools, string, hashlib

def bruteForce_attack():

    alphabet = string.ascii_uppercase

    with open(sys.argv[1], "r", encoding="utf-8") as file:
        for line in file:
            new_line = line.strip()

            name, password = new_line.split(":")

            for length in range(1,5):

                for combination in itertools.product(alphabet, repeat=length):
                    versuch = "".join(combination)

                    versuch_hash = hashlib.sha1(versuch.encode('ascii')).hexdigest()

                    if versuch_hash == password:
                        print(f"Name: {name} mit Passwort: {versuch}")
                        break 



bruteForce_attack()
