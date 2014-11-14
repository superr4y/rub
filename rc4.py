#!/usr/bin/env python2

class RC4:
    def __init__(self, k):
        self.k = k

        # init step
        self.s = [i for i in range(0,256)]
        j = 0
        for i in range(0,256):
            j = (j+self.s[i] + ord(self.k[i % len(self.k)])) % 256
            self.s[i], self.s[j] = self.s[j], self.s[i]

    def encrypt(self, plain):
        ret = []
        i = j = 0
        for p in plain:
            i = (i + 1) % 256
            j = (j + self.s[i]) % 256
            self.s[i], self.s[j] = self.s[j], self.s[i]
            r = self.s[(self.s[i] + self.s[j]) % 256]
            ret.append(r ^ ord(p))
        return ret
        

obj = RC4("12345")        
print map(lambda x: "%0.2x"%(x), obj.encrypt("hallo"))
