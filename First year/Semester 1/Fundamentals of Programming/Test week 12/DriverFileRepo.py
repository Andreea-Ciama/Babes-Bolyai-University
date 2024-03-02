from Repo import Repository
from Domain import Driver


class DriverFileRepo(Repository):
    def __init__(self, fileName):
        super().__init__()
        self.__file = open(fileName, 'r')
        for line in self.__file.readlines():
            if line == '':
                break
            a = line
            a = a.strip()
            a = a.split(',')

            self.store(Driver(a[0], int(a[1]), int(a[2])))
        self.__file.close()




    def _saveFile(self):
        f = open("drivers.txt", 'w')
        for i in self._objects:
            f.write(str(i))
        f.close()

    def store(self, obj):
        Repository.store(self, obj)
        self._saveFile()
