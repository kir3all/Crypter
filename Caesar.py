class Caesar:
    def __init__(self, shift):
        self.shift = shift

    def crypt(self, inputString, decrypt=False):
        message = [ord(c) for c in inputString]
        result = []
        for i in range(len(message)):
            if decrypt:
                result.append((message[i] - self.shift)%1114111)
            else:
                result.append((message[i] + self.shift)%1114111)
        return ''.join([chr(c) for c in result])

    

if __name__ == '__main__':
    mg = str(input("PLease type the message : "))
    shifts = int(input("Choose number of shifts : "))
    encrypt = Caesar(shifts)
    answer = encrypt.crypt(mg)
    print(answer.encode('utf8'))
    answer2 = encrypt.crypt(answer, True)
    print(answer2.encode('utf8'))

