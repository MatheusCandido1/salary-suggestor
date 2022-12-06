# Python program to create
# a pdf file
from fpdf import FPDF
from fpdf.html import hex2dec
from datetime import date

sign = 'If you choose to accept this job offer, please sign the second copy of this letter and return it to me at your earliest convenience.'

acknowledgment = 'When your acknowledgment is received, we will send you employee benefit enrollment forms and an employee handbook that details our benefit plans and retirement plan. We look forward to welcoming you at our company.'

information = 'Please let me know if you have any questions or if I can provide any additional information.'

class PDF(FPDF):
    def header(self):
        #font
        self.set_font('times', 'B', 18)
        #set left margin
        self.set_left_margin(15)
        #Title
        self.cell(0,15,"JOB OFFER LETTER", border= False, ln=1, align='L')
        #line break
        self.ln(10)
        
    def body(self, name):
        #read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        #set font    
        self.set_font('times','',12)
        #insert text
        self.multi_cell(180,5,txt)
        #line break
        self.ln(6)
        
def format_currency(value):
    return f"${value:,.2f}"

def generate(company, candidate, proposal):
    pdfData = {
        "recipientName": candidate['name'],
        "jobTitle": proposal['job_title'],
        "companyName": company['name'],
        "companyAddress": company['address'],
        "city": company['city'],
        "date": proposal['proposal_date'].strftime("%B %d, %Y"),
        "salary": proposal['salary'],
        "startDate": "11/25/2022",
        "colorCode": company['color'],
        "benefits": company['benefits'],
    }
    # save FPDF() class into a
    # variable pdf
    pdf = PDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("times", size = 12)
    #set the color for the line
    pdf.set_draw_color(*hex2dec(pdfData['colorCode']))
    #set the width of the line
    pdf.set_line_width(2)
    #set the line
    pdf.line(x1 = 15, y1 = 23, x2 = 190, y2 = 23)
    #set mar gin
    pdf.set_left_margin(15)

    pdf.set_font("times", size = 12)
    # create a cell
    pdf.cell(180, 6, txt = "Date : " + str(pdfData['date']) ,ln = 1)
    # add another cell
    pdf.cell(180, 6, txt = "Recipient Name : " + pdfData['recipientName'] ,ln = 1)
    # add another cell
    pdf.cell(180, 6, txt = "Title : " + pdfData['jobTitle'] ,ln = 1)
    # add another cell
    pdf.cell(180, 6, txt = "Company Name : " + pdfData['companyName'] ,ln = 1)
    # add another cell
    pdf.cell(180, 6, txt = "Address : " + pdfData['companyAddress'] ,ln = 1)
    # add another cell
    pdf.cell(180, 6, txt = "City : " + pdfData['city'] ,ln = 1)
    # add another cell
    pdf.cell(180, 15, txt = "Dear " + pdfData['recipientName'] + "," ,ln = 1)


    pdf.multi_cell(180,5, txt= pdfData['companyName'] + "is pleased to offer you the position of " + pdfData['jobTitle'] + ". Your skills and experience will be ideal fit for our company." )
    pdf.ln(4)
    pdf.multi_cell(180,5, txt="As we discussed, your starting date will be " + pdfData['startDate'] + ". The starting salary is " +format_currency(pdfData['salary'])+" per year and is paid on a weekly basis. Direct deposit is available." )
    pdf.ln(4)
    pdf.multi_cell(180, 5, txt=pdfData['benefits'])
    pdf.ln(4)
    pdf.multi_cell(180, 5, txt=sign)
    pdf.ln(4)
    pdf.multi_cell(180, 5, txt=acknowledgment)
    pdf.ln(4)
    pdf.multi_cell(180, 5, txt=information)
    pdf.ln(6)
    pdf.cell(180, 5, txt = "Sincerely, " ,ln = 2)
    pdf.cell(180, 5, txt = pdfData['companyName'] ,ln = 2)
    pdf.cell(180, 5, txt = pdfData['companyAddress'] + ", " + pdfData['city'] ,ln = 2)
    # save the pdf with name .pdf
    filename = pdfData['recipientName'] + pdfData['jobTitle'] + "Proposal.pdf"
    filename = filename.replace(" ", "")
    print('PDF generated: ', filename)
    pdf.output(filename)