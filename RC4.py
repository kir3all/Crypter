class RC4:
    def __init__(self, key):
        self.K = [ord(c) for c in key]
        self.S = [i for i in range(256)]
        self.Q1 = 0
        self.Q2 = 0
        self.T = 0


    def keySetup(self):
        j = 0
        for i in range(256):
            j = (j + self.S[i] + self.K[i % len(self.K)]) % 256
            tmp = self.S[i]
            self.S[i] = self.S[j]
            self.S[j] = tmp
    
    
    def prng(self):
        self.Q1 = (self.Q1 + 1) % 256
        self.Q2 = (self.Q2 + self.S[self.Q1]) % 256
        self.S[self.Q1] = self.S[self.Q2] + self.S[self.Q1]
        self.S[self.Q2] = self.S[self.Q1] - self.S[self.Q2]
        self.S[self.Q1] = self.S[self.Q1] - self.S[self.Q2]
        self.T = (self.S[self.Q1] + self.S[self.Q2]) % 256
        return self.T
    

    def crypt(self, inputString):
        Y = [ord(c) for c in inputString]
        result = []
        for each in Y:
            r = self.prng()
            result.append(r ^ each)
        return ''.join([chr(c) for c in result])

    
    def reset(self):
        self.Q1 = 0
        self.Q2 = 0
        self.T = 0
        self.S = [i for i in range(256)]
        self.keySetup()



if __name__ == '__main__':
    key = str(input("enter key:"))
    crypt = RC4(key)
    crypt.keySetup()
    plained = str(input("PLease enter message : "))
    encrypted = crypt.crypt(plained)
    print(encrypted)

    crypt.reset()
    print(crypt.crypt(encrypted))