# Extract-text-from-image
Extraction of text from Image using OCR

Humans can understand the contents of an image simply by looking. We perceive the text on the image as text and can read it.

Computers don't work the same way. They need something more concrete, organized in a way they can understand.

This is where Optical Character Recognition (OCR) kicks in. Whether it's recognition of car plates from a camera, or hand-written documents that should be converted into a digital copy, this technique is very useful. While it's not always perfect, it's very convenient and makes it a lot easier and faster for some people to do their jobs.

#Installation Needed:

$pip install pytesseract

This will read the text from Images. 


If any Error Occurs Like this : "TesseractNotFoundError: tesseract is not installed or it's not in your path" 

you need to install the tesseract.exe. 

and need add to your path in the Code

Format: pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
