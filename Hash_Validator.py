import os
import sys
import hashlib
from tabulate import tabulate

class Hash_Check(object):
    def __init__(self, check_file, hash_key):
        self.check_file = check_file
        self.hash_key = hash_key
        self.script_path = os.getcwd()
        # Reads in 64kb chunks.
        self.BUF_SIZE = 65536
        self.md5 = hashlib.md5()
        self.sha1 = hashlib.sha1()
        self.sha256 = hashlib.sha256()
        self.hash_generator()

    def __str__(self):
        values = str(self.validate())
        return values

    def hash_generator(self):
        drive = str(self.check_file.split("\\")[0])
        file_name = str(self.check_file.split("\\")[-1])
        file_path = os.path.join(self.check_file.strip(file_name))
        if str(file_path.split("\\")[0]) != drive:
            file_path = str(drive.strip(":") + file_path)
        os.chdir(file_path)
        with open(file_name, 'rb') as file:
            while True:
                data = file.read(self.BUF_SIZE)
                if not data:
                    break
                self.md5.update(data)
                self.sha1.update(data)
                self.sha256.update(data)
    

    def validate(self):
        hash_sha = str(self.sha1.hexdigest())
        hash_md5 = str(self.md5.hexdigest())
        hash_sha256 = str(self.sha256.hexdigest())
        while True:
            if hash_sha == hash_key:
                table = tabulate([["Validation:", "Hashes Match!"],
                                  ["Key Given:", self.hash_key],
                                  ["sha1sum", hash_sha]],
                        headers="firstrow", tablefmt="grid")
            elif hash_md5 == hash_key:
                table = tabulate([["Validation:", "Hashes Match!"],
                                  ["Key Given:", self.hash_key],
                                  ["md5sum", hash_md5]],
                        headers="firstrow", tablefmt="grid")
            elif hash_sha256 == hash_key:
                table = tabulate([["Validation:", "Hashes Match!"],
                                  ["Key Given:", self.hash_key],
                                  ["sha256sum", hash_sha256]],
                        headers="firstrow", tablefmt="grid")
            else:
                table = tabulate([["Validation:", "Hashes Don't Match!"],
                                  ["Key Given:", self.hash_key],
                                  ["sha1sum", hash_sha],
                                  ["md5sum", hash_md5]],
                        headers="firstrow", tablefmt="grid")
            return table
        

if __name__ == "__main__":
    """ Be Aware of tailing whitespace"""
    print("Drag 'n Drop File Here:")
    check_file = str(input(r"  >> ")).replace('"', "")
    print("Enter Official hash-Key Here:")
    hash_key = str(input(r"  >> "))
    validation = Hash_Check(check_file, hash_key)
    print(validation)


