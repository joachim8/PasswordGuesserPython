from CheckDate import OptionDate
from CheckWord import OptionWord
from Commonchar import CommonSpecialCharacters
from PasswordGuesserPython import PasswordGenerator
from Info import InfoPersonnel
from CheckMot import Checker
import datetime



# Defining main function
def main():
   print("Bienvenue dans le password guesser.")
   optionWord = OptionWord(True,True,True,True,True,True,True)
   optionDate = OptionDate(True,True,True,True,True)
   personalInfo = InfoPersonnel(["Toto","Tata"],[datetime.date.today()])
   optionCommonChar = CommonSpecialCharacters();

   # ,datetime.date(1998, 11, 8)
   checker = Checker( personalInfo, optionWord, optionDate, optionCommonChar)
   passwordGenerator = PasswordGenerator(checker)
   #print(passwordGenerator.all_combinations)
   print(str(len(passwordGenerator.all_combinations)))
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()

