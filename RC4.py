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
        # 给定S盒初始值
        self.S = [s for s in range(256)]
        # print(self.S)
        # 初始化K盒
        for i in range(256):
            self.K.append(self.key[i % len(self.key)])
        j = 0
        for i in range(256):
            j = (j + self.S[i] + self.K[i]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]


    # 生成密钥流并对数据进行加密/解密
    def encrypt(self, data):
        i, j = 0, 0
        keystream = []
        out = []
        dataLength = len(data)
        for k in range(dataLength):
            i = (i + 1) % 256
            j = (j + self.S[i]) % 256
            tmp = (self.S[i] + self.S[j] % 256) % 256
            keystream.append(self.S[tmp])
            out.append(data[k] ^ keystream[k])
        return out


# 测试部分
if __name__ == '__main__':
    # 给定初始化的十六进制密钥
    a = RC4([0x13,0x57,0x9b,0xdf,0x02,0x46,0x8A,0xCE,\
    		0x12,0x34,0x56,0x78,0x90,0xAB,0xCD,0xEF])
    # 给定十六进制的明文
    encryptData = a.encrypt([0x11,0x22,0x33,0x44,0x55,0x66,0x77,0x88,\
    		0x99,0x00,0xAA,0xBB,0xCC,0xDD,0xEE,0xFF])
    # 打印加密后的data
    showList = []
    for i in encryptData:
        showList.append(hex(i))
    print(showList)
    decryptData = a.encrypt(encryptData)
    # 打印解密后的data
    showList2 = []
    for i in decryptData:
        showList2.append(hex(i))
    print(showList2)
