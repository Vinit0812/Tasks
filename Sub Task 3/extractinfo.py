import re

text = """paymentadviceto:allhourselectricalwaabn:54788190299tel:92752839email:service@allhourselectricalwa.com.aucustomertuvakhusidinvoicenumberinv-3649amountdue0.00duedate4jan2025amountenclosedentertheamountyouarepayingabovetaxinvoicetuvakhusidinvoicedate4jan2025invoicenumberinv-3649referencej2911abn54788190299allhourselectricalwaabn:54788190299tel:92752839email:service@allhourselectricalwa.com.audescriptionquantityunitpricegstamountaudinstalled1xclientsuppliedlight1.00150.0010%150.00job:j2911jobaddress:8salamanderstreet,dianellasubtotal150.00totalgst10%15.00totalaud165.00addcreditcardprocessingfee2.81lessamountpaid167.81amountdueaud0.00duedate:4jan2025pleaseusetheinvoicenumberasthepaymentreference.eftdetails:bsb066-167accno10617158paymenttermsstrictly:14daysifthereareanyqueriesaboutthisinvoice,pleasedonothesitatetocontactus.thankyouforusingus,weappreciateyourbusiness!"""

abn = re.search(r'abn[:](\d{11})', text)
print("abn",abn.group(1))

email = re.search(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]+', text)
print("email",email.group(0))

amount_due = re.search(r'amountdue[a-z]*:?(\d+\.\d)', text)
print("amountdue",amount_due.group(1))

amount_paid = re.search(r'amountpaid[a-z]*:?(\d+\.\d)', text)
print("amountdue",amount_paid.group(1))

invoice_date = re.search(r'invoicedate[:]?(a-zA-Z0-9)', text)
print("invoice_date",invoice_date.group(1))

