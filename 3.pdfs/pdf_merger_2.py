from PyPDF2 import PdfFileMerger, PdfFileReader
 
# Call the PdfFileMerger
mergedObject = PdfFileMerger()
 
# Loop through all of them and append their pages
for fileNumber in range(0,9):
    mergedObject.append(PdfFileReader(f'{fileNumber}.pdf', 'rb'))
    print(type(f'{fileNumber}.pdf'))

# Write all the files into a file which is named as shown below
mergedObject.write("HTML_complete_handwritten_notes.pdf")
