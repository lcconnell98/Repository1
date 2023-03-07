import sys
from PyQt5.QtWidgets import QApplication, QLabel, QInputDialog
import pandas as pd


# creates a QApplication object for password input
def email_password_app_function():
    global email_password_app
    email_password_app = QApplication(sys.argv)
    label = QLabel("Outlook Password Entry")
    label.show()
    email_password_entry, ok = QInputDialog.getText(None, "Password Input", "Enter your email password: ")
    email_password_app.quit()
    return email_password_entry if ok else None


# creates a csv for each sub with a settled transfer and places the relevant information for the report inside
def csv_status(email_password):
    print(f"email_password: {email_password}")
    # smtp_object = smtplib.SMTP('smtp-mail.outlook.com',587)
    # smtp_object.ehlo()
    # smtp_object.starttls()
    # from_email_address = 'myemail@gmail.com'
    # smtp_object.login(from_email_address,email_password)

    sub_list = set()
    # for i in transfer_references():
    #    if i[2][3:5] not in sub_list:

    # ec_dataframe = pd.DataFrame(transfer_references())
    # print("ec_dataframe")
    print("Hello")


email_password_entry = email_password_app_function()
if email_password_entry is not None:
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(email_password_app.quit)
    app.processEvents()
    csv_status(email_password_entry)
    app.exec_()