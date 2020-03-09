class ProxyBean():
    def __init__(self):
        self.ip = ''            # ip
        self.port = ''          # port 
        self.loaction = ''      # 位置
        self.type = ''          # 类型 

    def __init__(self, ip, port, loaction, type):
        self.ip = ip
        self.port = port
        self.loaction = loaction
        self.type = type   
    
    def to_string(self):
        # print(1)
        return '{},{},{},{}'.format(self.ip, self.port, self.loaction, self.type)


