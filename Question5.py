from abc import ABC, abstractmethod


# Abstract Base Class
class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


# Concrete TextFileHandler class
class TextFileHandler(FileHandler):
    def read(self):
        return "Reading text file..."

    def write(self, data):
        return f"Writing '{data}' to text file..."


# Concrete BinaryFileHandler class
class BinaryFileHandler(FileHandler):
    def read(self):
        return "Reading binary file..."

    def write(self, data):
        return f"Writing binary data: {data}"


# Testing the classes
text_handler = TextFileHandler()
binary_handler = BinaryFileHandler()

print(text_handler.read())  # Output: Reading text file...
print(text_handler.write("Hello"))  # Output: Writing 'Hello' to text file...
print(binary_handler.read())  # Output: Reading binary file...
print(binary_handler.write(b'101010'))  # Output: Writing binary data: b'101010'