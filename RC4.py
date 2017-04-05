'''
author : Rouzip
date : 2017.4.3
'''

class RC4:
    def __init__(self, key):
        self.K = []
        self.S = []
        self.key = key


    # 初始化S盒
    def initKey(self):
        # 给定S盒初始值
        self.S = [s for s in range(256)]
        # print(self.S)
        # 初始化K盒
        for i in range(256):
            self.K.append(ord(self.key[i % len(self.key)]))
        j = 0
        for i in range(256):
            j = (j + self.S[i] + self.K[i]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]


    # 生成密钥流并对数据进行加密/解密
    def encrypt(self, data):
        i, j = 0, 0
        keystream = []
        out = ''
        dataLength = len(data)
        for k in range(dataLength):
            i = (i + 1) % 256
            j = (j + self.S[i]) % 256
            tmp = (self.S[i] + self.S[j]) % 256
            keystream.append(self.S[tmp])

        for k in range(dataLength):
            out += chr(ord(data[k]) ^ keystream[k])
        return out

# 测试部分
if __name__ == '__main__':
    a = RC4('aslkfjsafjskajfsglkjsafkhsakfhsafjksahk')
    a.initKey()
    encryptData = a.encrypt('asfsasafsgdshdfsgasgadfgafdgafsfsfsafsag')
    # 打印加密后的data
    print(encryptData)
    decryptData = a.encrypt(encryptData)
    # 打印解密后的data
    print(decryptData)
