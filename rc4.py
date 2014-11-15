#!/usr/bin/env python2

class RC4:
    def __init__(self, k, n):
        self.k = k
        self.n = n

        # init step
        self.s = [i for i in range(0,2**self.n)]
        j = 0
        for i in range(0,2**self.n):
            j = (j+self.s[i] + self.k[i % len(self.k)]) % 2**self.n
            self.s[i], self.s[j] = self.s[j], self.s[i]
        print self

    def encrypt(self, plain):
        ret = []
        i = j = 0
        count = 1
        for p in plain:
            i = (i + 1) % 2**self.n
            j = (j + self.s[i]) % 2**self.n
            self.s[i], self.s[j] = self.s[j], self.s[i]
            r = self.s[(self.s[i] + self.s[j]) % 2**self.n]
            print "%d => %d"%(count, r)
            count += 1
            ret.append(r ^ ord(p))
        return ret

    def __str__(self):
        return "s: " + ", ".join(map(lambda e: str(e), self.s))
        

obj = RC4([4, 7, 2, 3, 1], 3)        
print map(lambda x: "%d"%(x), obj.encrypt("hallo"))

obj = RC4([521, 13, 17, 988, 101, 300, 725, 976, 464, 859, 711, 223, 392], 10)
print obj.encrypt("a"*30)
