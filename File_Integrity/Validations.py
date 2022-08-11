import os
import hashlib


class HashGenerator(object):
    def __init__(self, file):
        self.file = file.replace('"', "")
        self.BUF_SIZE = 65536
        self.file_name = str(file.split("/")[-1])
        try:
            drive = str(file.split("/")[0])
            file_path = os.path.join(file.strip(self.file_name))
            if str(file_path.split("/")[0]) != drive:
                file_path = str(drive.strip(":") + file_path)
            os.chdir(file_path)
        except Exception as E:
            print(E)


class MD5(HashGenerator):
    def __init__(self, *args, **kwargs):
        super(MD5, self).__init__(*args, **kwargs)
        self.md5_sum = hashlib.md5()
        self.generate()

    def generate(self):
        with open(self.file_name, "rb") as file:
            while True:
                data = file.read(self.BUF_SIZE)
                if not data:
                    break
                self.md5_sum.update(data)

    def __str__(self):
        return str(self.md5_sum.hexdigest())


class SHA1(HashGenerator):
    def __init__(self, *args, **kwargs):
        super(SHA1, self).__init__(*args, **kwargs)
        self.sha1_sum = hashlib.sha1()
        self.generate()

    def generate(self):
        with open(self.file_name, "rb") as file:
            while True:
                data = file.read(self.BUF_SIZE)
                if not data:
                    break
                self.sha1_sum.update(data)

    def __str__(self):
        return str(self.sha1_sum.hexdigest())


class SHA256(HashGenerator):
    def __init__(self, *args, **kwargs):
        super(SHA256, self).__init__(*args, **kwargs)
        self.sha256_sum = hashlib.sha256()
        self.generate()

    def generate(self):
        with open(self.file_name, "rb") as file:
            while True:
                data = file.read(self.BUF_SIZE)
                if not data:
                    break
                self.sha256_sum.update(data)

    def __str__(self):
        return str(self.sha256_sum.hexdigest())
