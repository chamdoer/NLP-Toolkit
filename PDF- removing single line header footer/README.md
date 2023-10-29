
This Python code is designed to remove *Single Line* headers/footers from PDF documents, making it an excellent tool for pre-processing PDFs used in natural language processing.

NOTE: This versatile code caters to general requirements, but it can be manipulated for specific needs. It's built with scalability in mind to handle PDFs with varying formats that demand different sets of processing rules. Modifications that enhance its efficiency are welcome!

Features:

1. Utilizes the Tika library for text extraction from PDFs.
2. Incorporates the Fuzzywuzzy library (GNU General Public License v2 (GPLv2)) for calculating string similarity. This is handy as text extraction can occasionally yield ambiguous results or unintended concatenation.
3. Employs the BeautifulSoup library to extract text from Tika's XML content.
4. Outputs the text of the PDF, minus *single line* headers and footers.
5. Leverages the concept of hashing to accelerate processing and optimize memory usage – especially useful when searching for headers and footers in the extracted text.

Dependencies:

1. bs4 library (MIT license)
2. fuzzywuzzy library (GNU General Public License v2 (GPLv2))
3. tika (Apache Software License)
4. Python 3.6.9

Licensed under GNU GENERAL PUBLIC LICENSE. This repo is maintained by chamdoer.