from time import sleep
import itertools
import string


class PasswordGenerator:
    '''Password generator \n
    |\tCreatePasswordList:
    |\t\tthis method Create a password list by generator
    |\t\ttake Min length , Max length , lowercase , uppercase and intger
    |\tCreate File :
    |\t\tthis method create a file and insert the password in the file

    '''
    def __init__(self,Min_length=4,Max_length=8,Lowercase=True,Uppercase=False,Integer=False,path='./',NameFile='passwords',WriteFile=None):
        self.Min_length = Min_length
        self.Max_length = Max_length
        self.Lowercase = Lowercase
        self.Uppercase = Uppercase
        self.Integer = Integer
        self.NameFile = NameFile
        self.WriteFile = WriteFile
        self.path = path
        self.CreateFile()
    def CreatePasswordList(self):
        if self.Min_length < self.Max_length:
            Chars = ''
            if self.Lowercase:
                Chars += string.ascii_lowercase
            if self.Uppercase:
                Chars += string.ascii_uppercase
            if self.Integer:
                Chars += string.digits

            try:
                gen = ( ''.join(j) for i in range(self.Min_length, self.Max_length + 1) for j in itertools.product(Chars, repeat=i))
                return gen
            except BaseException as error:
                print(f'{error}')
    def dely(self):
        for i in range(10):
            sleep(1)
            print('.',end='')
    def CreateFile(self):
        try:
            with open(f'{self.path}{self.NameFile}.txt','w') as file:
                for password in self.CreatePasswordList():
                    file.write(f'{password}')
        except BaseException as error:
            print(f'{error}')
        finally:
            print('Done',end='')
            self.dely()

    

if __name__ == '__main__':
    password = PasswordGenerator()



