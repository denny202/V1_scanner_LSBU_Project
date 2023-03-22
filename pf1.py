import PyPDF2
import subprocess

pdf_file_name = "paf.pdf"
outcome = 1
vuln='SQL_injection'

#create pdf reader
pdf_reader = PyPDF2.PdfReader(open(pdf_file_name, "rb"))

#pages lenght
num_pages = len(pdf_reader.pages)

# Create a pdf object 
pdf_writer = PyPDF2.PdfWriter()

# Add the desired page to writer 
if outcome == 1:
    pdf_writer.add_page(pdf_reader.pages[0])
elif outcome == 2:
    pdf_writer.add_page(pdf_reader.pages[1])
# elif outcome == 3:
#     pdf_writer.add_page(pdf_reader.pages[2])

# Specify the output name
output_file_name = f"outcome_{vuln}.pdf"

#retunrn
with open(output_file_name, "wb") as output_file:
    pdf_writer.write(output_file)


paths=f'/path/path{output_file_name}'
subprocess.run(['open', paths], check=True)