import PyPDF2
from PyPDF2 import pdf
from gtts import gTTS 

pdfReader=PyPDF2.PdfFileReader(open('Diary of a Wimpy Kid, Book 1 - Kinney, Jeff.pdf','rb'))
for page_num in range(16,18):
    mytext=pdfReader.getPage(page_num)
    # mytext=mytext.extract
    print(mytext.exextractText())

pdfReader.close()
# myobj = gTTS(text=mytext, lang='en', slow=False, tld='co.in')
  

# myobj.save("wimpy.wav")
