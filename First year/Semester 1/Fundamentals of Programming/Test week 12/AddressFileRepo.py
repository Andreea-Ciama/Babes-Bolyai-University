from Repo import Repository
from Domain import Address


class AddressFileRepo(Repository):
    def __init__(self, fileName):
        super().__init__()
        self.__file=open(fileName, 'r')
        for line in self.__file.readlines():
            if line == '':
                break
            a = line
            a = a.strip()
            a = a.split(',')

            self.store(Address(int(a[0]), a[1], int(a[2]), int(a[3])))
        self.__file.close()
        #self._loadFile()



    def _saveFile(self):
        f = open("addresses.txt", 'w')
        for i in self._objects:
            f.write(str(i))

    def store(self, obj):
        Repository.store(self, obj)
        self._saveFile()

