import easyocr
import os

def text_recognition(file_path,text_file_name = 'result.txt'):

      reader = easyocr.Reader(['ru','en'])
      result = reader.readtext(file_path,detail=0,paragraph=True)

      return result


