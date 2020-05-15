# Version Python 3
# Maintainer: Novabutter
# Version 0.9
import sys
import random
def main():
    paramMin = 16
    paramMax = 32
    length = randomNumberGenerator(paramMin, paramMax)
    password = ""
    for i in range(length):
      method = generate()

      randomValue = randomNumberGenerator(method().getObjectMin(), method().getObjectMax())
      if (str(method) == "<class '__main__.Special'>"):
        password += ASCIILookup(method().libraryLookup(randomValue))
      else:
        password += ASCIILookup(randomValue)
      method.incObjectNum(method) 
    print("Password:", password)

def randomNumberGenerator(paramMin, paramMax):
  return random.randint(paramMin, paramMax)

def ASCIILookup(num):
  return chr(num)

def generate():
  selectionArray = ["Uppercase", "Lowercase", "Number", "Special"]
  method = selectionArray[randomNumberGenerator(0,3)]
  # Method 
  return getattr(sys.modules[__name__], method)

  

class Uppercase:
    # Class designed for generating uppercase ASCII character values
    objectLimit = 12
    objectMin = 65
    objectMax = 90
    num = 0
    def getObjectLimit(self):
        return self.objectLimit
    def getObjectNum(method):
      return method.num
    def incObjectNum(method):
      method.num += 1
    def getObjectMin(self):
      return self.objectMin
    def getObjectMax(self):
      return self.objectMax

class Lowercase():
  # Class designed for generating lowercase ASCII character values
  objectLimit = 12
  objectMin = 97
  objectMax = 122
  num = 0
  def getObjectLimit(self):
    return self.objectLimit
  def getObjectNum(self):
    return self.num
  def incObjectNum(method):
    method.num += 1
  def getObjectMin(self):
    return self.objectMin
  def getObjectMax(self):
    return self.objectMax

class Number():
  # Class designed for generating ASCII character numbers between 0-9.
  objectLimit = 12
  objectMin = 48
  objectMax = 57
  num = 0
  def getObjectLimit(self):
    return self.objectLimit
  def getObjectNum(self):
    return self.num
  def incObjectNum(method):
    method.num += 1
  def getObjectMin(self):
    return self.objectMin
  def getObjectMax(self):
    return self.objectMax

class Special():
  # Class designed for generating ASCII character special characters: (!, #, $, %, &, *, -, ., ?, @, _)
  objectLimit = 6
  objectMin = 0
  objectMax = 10
  library = [33, 35, 36, 37, 38, 42, 45, 46, 63, 64, 95]
  num = 0
  def getObjectLimit(self):
    return self.objectLimit
  def getObjectNum(self):
    return self.num
  def incObjectNum(method):
    method.num += 1
  def getObjectMin(self):
    return self.objectMin
  def getObjectMax(self):
    return self.objectMax
  def libraryLookup(self, libraryNumber):
    number = self.library[libraryNumber]
    return number

main()
