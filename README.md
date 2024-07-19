# Convert .csv to .pdf

This code snippet is written in Python and demonstrates how to read a CSV file using the `pandas` library and convert its contents into a PDF file using the `FPDF` library. Here's a complete breakdown of the code and its components:

### Imports
```python
import pandas as pd  
from fpdf import FPDF  
```
1. **pandas**: This is a widely used library for data manipulation and analysis. It allows you to read and manipulate data in DataFrames.
2. **FPDF**: This is a library for generating PDF files in Python. It provides functions to create custom PDFs, manipulate texts, and manage pages.

### Reading the CSV file
```python
csv_file = 'student_results.csv'  # Change this to your CSV file  
df = pd.read_csv(csv_file)  
```
1. **`csv_file`**: This variable specifies the name of the CSV file you want to read. You should change this string to match the path of your actual CSV file.
2. **`pd.read_csv(csv_file)`**: This reads the CSV file into a pandas DataFrame (`df`). The DataFrame is a 2D labeled data structure that allows you to work with tabular data.

### Creating a PDF class
```python
class PDF(FPDF):  
    def header(self):  
        self.set_font('Arial', 'B', 12)  
        self.cell(0, 10, 'CSV to PDF', 0, 1, 'C')  

    def footer(self):  
        self.set_y(-15)  
        self.set_font('Arial', 'I', 8)  
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')  
```
1. **Defining PDF class**: A subclass of `FPDF` is created to customize the appearance of the PDF.
2. **`header` method**: This method sets the header for each page:
   - `self.set_font('Arial', 'B', 12)`: Sets the font to Arial, bold, size 12.
   - `self.cell(...)`: Adds a cell in the header with the title "CSV to PDF", centered.
3. **`footer` method**: This method sets the footer for each page:
   - `self.set_y(-15)`: Positions the cursor 15 millimeters from the bottom of the page.
   - `self.cell(...)`: Adds a cell displaying the page number at the center.

### Creating a PDF object
```python
pdf = PDF()  
pdf.add_page()  
```
1. **`pdf = PDF()`**: Creates an instance of the custom PDF class.
2. **`pdf.add_page()`**: Adds a new page to the PDF document.

### Setting the font
```python
pdf.set_font("Arial", size=12)  
```
This sets the font for the content of the PDF to Arial, size 12.

### Looping through the DataFrame and writing to PDF
```python
for i in range(df.shape[0]):  
    row = df.iloc[i]  
    pdf.cell(0, 10, ', '.join(str(item) for item in row), 0, 1)  
```
1. **`for i in range(df.shape[0])`**: Iterates over each row in the DataFrame. `df.shape[0]` returns the number of rows.
2. **`row = df.iloc[i]`**: Retrieves each row using integer-location based indexing.
3. **`pdf.cell(...)`**: Writes the contents of each row to the PDF:
   - `', '.join(str(item) for item in row)`: Joins all items in the row into a single string, separated by commas. Each item is converted to a string to ensure proper formatting.
   - `0, 10`: The first `0` means the cell width is auto, and `10` is the height of the cell.
   - `0, 1`: The first `0` indicates no border, and `1` indicates to move the cursor to the next line after writing.

### Saving the PDF
```python
pdf_file = 'student_results.pdf'  
pdf.output(pdf_file)  
```
1. **`pdf_file`**: Variable specifying the name of the output PDF file.
2. **`pdf.output(pdf_file)`**: Generates and saves the PDF document to the specified filename.

### Print Confirmation
```python
print(f"Converted '{csv_file}' to '{pdf_file}'")
```
This line prints a confirmation message in the console indicating that the conversion has been successfully completed, outputting the names of the CSV file and the generated PDF file.

### Summary
Overall, this code:
1. Reads a CSV file containing student results.
2. Creates a PDF document with a custom header and footer.
3. Iterates through each row of the DataFrame and writes the data to the PDF.
4. Saves the resulting PDF file.

You can run this script as long as you have the necessary libraries (`pandas` and `fpdf`) installed and the specified CSV file exists.




## Ongoing Improvements:
"I am currently updating this project to improve its features and content. It's a work in progress, so please check back for the completed version." 
