# Creating server object and pinging
class Server(object):
    def __init__(self, ip, hostname):
        self.ip = ip
        self.hostname = hostname
    def set_ip(self, ip):
        self.ip = ip
    def set_hostname(self, hostname):
        self.hostname = hostname
    def ping(self, ip_addr):
        print ("Pinging %s from %s (%s)" % (ip_addr, self.ip, self.hostname))
if __name__ == '__main__':
    server = Server('49.207.55.213', 'myhomeip')
    server.ping('98.124.199.30')
