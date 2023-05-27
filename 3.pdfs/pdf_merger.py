# -*- coding: utf-8 -*-
# Program to merge pdf files
#pip install PyPDF2

from PyPDF2 import Pdf

# first read the pdf files
pdf_file1 = PyPDF2.PdfFileReader("html_course_chapter_0.pdf")
pdf_file2 = PyPDF2.PdfFileReader("html_course_chapter_2.pdf")
pdf_file3 = PyPDF2.PdfFileReader("html_course_chapter_3.pdf")
pdf_file4 = PyPDF2.PdfFileReader("html_course_chapter_4.pdf")
pdf_file5 = PyPDF2.PdfFileReader("html_course_chapter_5.pdf")

# create a pdf file merger object
output = PyPDF2.PdfFileMerger()

# append the pdf reader objects in to it
output.append(pdf_file1)
output.append(pdf_file2)
output.append(pdf_file3)
output.append(pdf_file4)
output.append(pdf_file5)

# save the merged pdf
output.write("merged.pdf")
