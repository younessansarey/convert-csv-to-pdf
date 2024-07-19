import pandas as pd  
from fpdf import FPDF  

# Read the CSV file  
csv_file = 'student_results.csv'  # Change this to your CSV file  
df = pd.read_csv(csv_file)  

# Create a PDF class  
class PDF(FPDF):  
    def header(self):  
        self.set_font('Arial', 'B', 12)  
        self.cell(0, 10, 'CSV to PDF', 0, 1, 'C')  

    def footer(self):  
        self.set_y(-15)  
        self.set_font('Arial', 'I', 8)  
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')  

# Create a PDF object  
pdf = PDF()  
pdf.add_page()  

# Set font  
pdf.set_font("Arial", size=12)  

# Loop through the DataFrame and write to PDF  
for i in range(df.shape[0]):  
    row = df.iloc[i]  
    pdf.cell(0, 10, ', '.join(str(item) for item in row), 0, 1)  

# Save the PDF  
pdf_file = 'student_results.pdf'  
pdf.output(pdf_file)  

print(f"Converted '{csv_file}' to '{pdf_file}'")