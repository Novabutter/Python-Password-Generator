# Version Python 3
# Maintainer: Novabutter
# Version 1.0
###### DEV NOTES #########
#
# 1) Consider adding animation as password is generated (optional)
# 2) Add save feature for parameters
# 3) Auto-copy to clipboard feature (enable/disable ability)
# 4) Implement fail-safe errors (try, except)
# 5) Option to store passwords via encryption
# 6) Menu
# 7) *Insecure method lookups (Mandatory)
# 8) *Find initial seed value (Mandatory)
#
###########################
import sys
import random
# https://pythonspot.com/objects-and-classes/
def main():
    # Changed parameter to (2) and (5) for testing purposes
    paramMin = 16
    paramMax = 32
    length = randomNumberGenerator(paramMin, paramMax)
    password = ""
    # print("DEBUG: Length is", length)
    for i in range(length):
      #method = parameterValidator(generate())
      method = generate()

      randomValue = randomNumberGenerator(method().getObjectMin(), method().getObjectMax())
      # print("DEBUG: Method is", str(method))
      if (str(method) == "<class '__main__.Special'>"):
        password += ASCIILookup(method().libraryLookup(randomValue))
      else:
        password += ASCIILookup(randomValue)
      method.incObjectNum(method) ### Kind of pointless. Keep if going to secure soon by using protected objects. Otherwise use method.num += 1
      #method.num += 1
      # print("DEBUG: method value is now", method.getObjectNum(method))
    
    
    print("Password:", password)


def randomNumberGenerator(paramMin, paramMax):
  return random.randint(paramMin, paramMax)

def ASCIILookup(num):
  # print ("DEBUG:", num, " --> '", chr(num), "'")
  return chr(num)

#def limitCheck()
def generate():
  selectionArray = ["Uppercase", "Lowercase", "Number", "Special"]
  method = selectionArray[randomNumberGenerator(0,3)]
  # print("DEBUG: Selected method is", method)
  # Method 
  return getattr(sys.modules[__name__], method)

#def parameterValidator(methodName):
  

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
      # print("DEBUG: Object incremented! value is now", method.num)
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
    # print("DEBUG: Object incremented! value is now", method.num)
  def getObjectMin(self):
    return self.objectMin
  def getObjectMax(self):
    return self.objectMax

class Number():
  # Class designed for generating ASCII character numbers between 0-9.
  # WARNING: This limits total keyspace. Numbers should be infinite for best security.
  #  However, this will also violate the total characters allowed per password param.
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
    # print("DEBUG: Object incremented! value is now", method.num)
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
    # print("DEBUG: Object incremented! value is now", method.num)
  def getObjectMin(self):
    return self.objectMin
  def getObjectMax(self):
    return self.objectMax
  def libraryLookup(self, libraryNumber):
    number = self.library[libraryNumber]
    # print("DEBUG: LibraryLookup is", number)
    return number

main()
