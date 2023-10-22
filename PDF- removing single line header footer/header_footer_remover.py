
"""
!pip install bs4
!pip install fuzzywuzzy
!pip install tika 
"""

#Check if two strings match 
def matcher(Str1,Str2):
  from fuzzywuzzy import fuzz  #Fuzzywuzzy is modified version of 'levenshtein distance' to check similarity of strings
  Partial_Ratio = fuzz.partial_ratio(Str1.lower(),Str2.lower())
  Token_Sort_Ratio = fuzz.token_sort_ratio(Str1,Str2)
  if (Token_Sort_Ratio>80) : 
    return 1
  else :
    if Partial_Ratio>85 :  
      return 1
    else :
      return 0

import tika
tika.initVM()
from tika import parser
parsed = parser.from_file('/content/brain.pdf', xmlContent=True)   #Input your PDF file here