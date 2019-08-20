# Import libraries.
from PIL import Image 
import pytesseract 
import sys 
import os 

#Variable to get count of total number of pages 
filelimit = 1

# Creating a text file to write the output 
outfile = "images/out_text.txt"

# Open the file in append mode so that all contents of all images are added to the same file 
f = open(outfile, "a") 

# Iterate from 1 to total number of images
for i in range(1, filelimit + 1): 
	ith = f"{i:04d}"
	# Set filename to recognize text from 
	filename = "images/"+str(ith)+".jpg"
		
	# Recognize the text as string in image using pytesserct 
	text = str(((pytesseract.image_to_string(Image.open(filename))))) 
	text = text.replace('-\n', '')	 

	# Finally, write the processed text to the file. 
	f.write(text) 

<<<<<<< HEAD
# Close the file after writing all the text. 
f.close() 
=======
# Close the file after writing all the text
f.close() 
>>>>>>> f750e8affca6fc4396584e2e4e804e6c5ad9801d
