class SecureFile:
    def __init__(self, content, password):
        self.__content = content
        self.__password = password
        self.__log = []

    def read(self, password):
        if password == self.__password:
            return self.__content
        else:
            self.__log.append("Unauthorized attempt")
            return "Access Denied"

f = SecureFile("This is secret data", "1234")

print(f.read("1234"))
print(f.read("1111"))

