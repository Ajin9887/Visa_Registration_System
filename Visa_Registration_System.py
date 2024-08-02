from tkinter import *
from tkcalendar import Calendar, DateEntry
import mysql.connector as mycon
import tkinter.messagebox as msg
from datetime import datetime

mydb = mycon.connect(host='localhost', port='3306', user='root', password='Ajinkc@40d', database='visa_registration')
mycursor = mydb.cursor()

class User:
    def __init__(self, root):
        self.root = root
        self.root.title("General Details")
        self.root.geometry("1000x600")
        self.root.configure(bg='white')
        
        title = Label(self.root, text="GENERAL DETAILS", font=('bold', '25'), bg="white", fg="black")
        title.pack()

        # General Details Fields
        passport_type_label = Label(self.root, text="Passport Type", font=('bold', '17'), bg="white", fg="black")
        passport_type_label.place(x=300, y=175)
        p_types = ["Ordinary Passport", "Official Passport", "Diplomatic Passport", "Service Passport", "Special Passport"]
        self.click_ptype = StringVar()
        self.click_ptype.set("Select a Passport type")
        drop_p = OptionMenu(self.root, self.click_ptype, *p_types)
        drop_p.place(x=460, y=180)
        
        nationality_label = Label(self.root, text="Nationality", font=('bold', '17'), bg="white", fg="black")
        nationality_label.place(x=340, y=225)
        n_types = ['Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans', 'Argentinean', 
                   'Armenian', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian',
                   'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bhutanese', 'Bolivian', 
                   'Bosnian', 'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese', 'Burundian', 
                   'Cambodian', 'Cameroonian', 'Canadian', 'Cape Verdean', 'Central African', 'Chadian', 'Chilean', 'Chinese', 
                   'Colombian', 'Comoran',  'Congolese', 'Costa Rican', 'Croatian', 'Cuban', 'Cypriot', 'Czech', 'Danish', 
                   'Djibouti', 'Dominican', 'Dutch', 'Dutchman', 'Dutchwoman', 'East Timorese', 'Ecuadorean', 'Egyptian', 
                   'Emirian', 'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Fijian', 'Filipino', 'Finnish', 
                   'French', 'Gabonese', 'Gambian', 'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan', 
                   'Guinea-Bissauan', 'Guinean', 'Guyanese', 'Haitian', 'Herzegovinian', 'Honduran', 'Hungarian', 'I-Kiribati', 
                   'Icelander', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivorian', 'Jamaican', 
                   'Japanese', 'Jordanian', 'Kazakhstani', 'Kenyan', 'Kittian and Nevisian', 'Kuwaiti', 'Kyrgyz', 'Laotian', 
                   'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 'Macedonian', 
                   'Malagasy', 'Malawian', 'Malaysian', 'Maldivan', 'Malian', 'Maltese', 'Marshallese', 'Mauritanian', 'Mauritian', 
                   'Mexican', 'Micronesian', 'Moldovan', 'Monacan', 'Mongolian', 'Moroccan', 'Mosotho', 'Motswana', 'Mozambican', 
                   'Namibian', 'Nauruan', 'Nepalese', 'Netherlander', 'New Zealander', 'Ni-Vanuatu', 'Nicaraguan', 'Nigerian', 
                   'Nigerien', 'North Korean', 'Northern Irish', 'Norwegian', 'Omani', 'Pakistani', 'Palauan', 'Panamanian', 
                   'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari', 'Romanian', 'Russian', 'Rwandan', 
                   'Saint Lucian', 'Salvadoran', 'Samoan', 'San Marinese', 'Sao Tomean', 'Saudi', 'Scottish', 'Senegalese', 'Serbian', 
                   'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovakian', 'Slovenian', 'Solomon Islander', 'Somali', 'South African', 
                   'South Korean', 'Spanish', 'Sri Lankan', 'Sudanese', 'Surinamer', 'Swazi', 'Swedish', 'Swiss', 'Syrian', 'Taiwanese', 
                   'Tajik', 'Tanzanian', 'Thai', 'Togolese', 'Tongan', 'Trinidadian or Tobagonian', 'Tunisian', 'Turkish', 'Tuvaluan', 
                   'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbekistani', 'Venezuelan', 'Vietnamese', 'Welsh', 'Yemenite', 'Zambian', 'Zimbabwean']
        self.click_ntype = StringVar()
        self.click_ntype.set("Select a nationality")
        drop_n = OptionMenu(self.root, self.click_ntype, *n_types)
        drop_n.place(x=460, y=230)

        dob_label = Label(self.root, text="Date of Birth", font=('bold', '17'), bg="white", fg="black")
        dob_label.place(x=320, y=278)
        self.cal_dob = DateEntry(self.root, width=16, background="magenta3", foreground="white", bd=2)
        self.cal_dob.place(x=460, y=283)
        
        email_label = Label(self.root, text="Email ID", font=('bold', '17'), bg="white", fg="black")
        email_label.place(x=360, y=340)
        self.email_entry = Entry(self.root)
        self.email_entry.place(x=460, y=347)

        conf_email_label = Label(self.root, text="Re confirm Email ID", font=('bold', '17'), bg="white", fg="black")
        conf_email_label.place(x=243, y=370)
        self.conf_email_entry = Entry(self.root)
        self.conf_email_entry.place(x=460, y=377)

        visa_service_label = Label(self.root, text="Visa Service", font=('bold', '17'), bg="white", fg="black")
        visa_service_label.place(x=315, y=405)
        v_types = ["Tourist Visa", "Medical Visa", "Business Visa", "Conference Visa"]
        self.click_vtype = StringVar()
        self.click_vtype.set("Select a visa service")
        drop_v = OptionMenu(self.root, self.click_vtype, *v_types)
        drop_v.place(x=457, y=407)

        submit_button = Button(self.root, text="Submit", command=self.first)
        submit_button.place(x=750, y=470)
        continue_button = Button(self.root, text="Continue", command=self.applicant_details_page)
        continue_button.place(x=750, y=500)

    def first(self):
        email = self.email_entry.get()
        conf_email = self.conf_email_entry.get()
        if email != conf_email:
            msg.showerror("Error", "Emails do not match!")
            return

        ptype = self.click_ptype.get()
        ntype = self.click_ntype.get()
        dob = self.cal_dob.get_date().strftime('%Y-%m-%d')
        vtype = self.click_vtype.get()

        mycursor.execute("INSERT INTO general_details VALUES (%s, %s, %s, %s, %s)", (ptype, ntype, dob, email, vtype))
        mydb.commit()

        msg.showinfo("General Details", "Entered successfully!")

    def applicant_details_page(self):
        applic_window = Toplevel(self.root)
        applic_window.title("Applicant Details")
        applic_window.geometry("1000x600")
        applic_window.configure(bg='white')
        title = Label(applic_window, text="APPLICANT DETAILS", font=('bold', '25'), bg="white", fg="black")
        title.pack()

        # Applicant Details Fields
        fname_label = Label(applic_window, text="First Name", font=('bold', '17'), bg="white", fg="black")
        fname_label.place(x=300, y=100)
        self.fname_entry = Entry(applic_window)
        self.fname_entry.place(x=500, y=105)

        lname_label = Label(applic_window, text="Last Name", font=('bold', '17'), bg="white", fg="black")
        lname_label.place(x=300, y=150)
        self.lname_entry = Entry(applic_window)
        self.lname_entry.place(x=500, y=155)

        gender_label = Label(applic_window, text="Gender", font=('bold', '17'), bg="white", fg="black")
        gender_label.place(x=370, y=200)
        g_types = ["Male", "Female", "Other"]
        self.click_gender = StringVar()
        self.click_gender.set("Select a gender")
        drop_g = OptionMenu(applic_window, self.click_gender, *g_types)
        drop_g.place(x=500, y=205)

        country_of_birth_label = Label(applic_window, text="Country of Birth", font=('bold', '17'), bg="white", fg="black")
        country_of_birth_label.place(x=280, y=250)
        self.country_of_birth_entry = Entry(applic_window)
        self.country_of_birth_entry.place(x=500, y=255)

        national_id_label = Label(applic_window, text="National ID", font=('bold', '17'), bg="white", fg="black")
        national_id_label.place(x=330, y=300)
        self.national_id_entry = Entry(applic_window)
        self.national_id_entry.place(x=500, y=305)

        religion_label = Label(applic_window, text="Religion", font=('bold', '17'), bg="white", fg="black")
        religion_label.place(x=350, y=350)
        self.religion_entry = Entry(applic_window)
        self.religion_entry.place(x=500, y=355)

        email_label = Label(applic_window, text="Email ID", font=('bold', '17'), bg="white", fg="black")
        email_label.place(x=360, y=400)
        self.applicant_email_entry = Entry(applic_window)
        self.applicant_email_entry.place(x=500, y=405)

        # Buttons
        submit_button = Button(applic_window, text="Submit", command=self.second)
        submit_button.place(x=750, y=450)
        continue_button = Button(applic_window, text="Continue", command=self.address_details_page)
        continue_button.place(x=750, y=480)

    def second(self):
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        gender = self.click_gender.get()
        country_of_birth = self.country_of_birth_entry.get()
        national_id = self.national_id_entry.get()
        religion = self.religion_entry.get()
        email = self.applicant_email_entry.get()

        mycursor.execute("INSERT INTO applicant_details VALUES (%s, %s, %s, %s, %s, %s, %s)", (fname, lname, gender, country_of_birth, national_id, religion, email))
        mydb.commit()

        msg.showinfo("Applicant Details", "Entered successfully!")

    def address_details_page(self):
        address_window = Toplevel(self.root)
        address_window.title("Address Details")
        address_window.geometry("1000x600")
        address_window.configure(bg='white')
        title = Label(address_window, text="ADDRESS DETAILS", font=('bold', '25'), bg="white", fg="black")
        title.pack()

        # Address Details Fields
        street_label = Label(address_window, text="Street", font=('bold', '17'), bg="white", fg="black")
        street_label.place(x=300, y=100)
        self.street_entry = Entry(address_window)
        self.street_entry.place(x=500, y=105)

        city_label = Label(address_window, text="City", font=('bold', '17'), bg="white", fg="black")
        city_label.place(x=300, y=150)
        self.city_entry = Entry(address_window)
        self.city_entry.place(x=500, y=155)

        state_label = Label(address_window, text="State", font=('bold', '17'), bg="white", fg="black")
        state_label.place(x=300, y=200)
        self.state_entry = Entry(address_window)
        self.state_entry.place(x=500, y=205)

        country_label = Label(address_window, text="Country", font=('bold', '17'), bg="white", fg="black")
        country_label.place(x=300, y=250)
        self.country_entry = Entry(address_window)
        self.country_entry.place(x=500, y=255)

        zip_code_label = Label(address_window, text="Zip Code", font=('bold', '17'), bg="white", fg="black")
        zip_code_label.place(x=300, y=300)
        self.zip_code_entry = Entry(address_window)
        self.zip_code_entry.place(x=500, y=305)

        phone_label = Label(address_window, text="Phone", font=('bold', '17'), bg="white", fg="black")
        phone_label.place(x=300, y=350)
        self.phone_entry = Entry(address_window)
        self.phone_entry.place(x=500, y=355)

        # Buttons
        submit_button = Button(address_window, text="Submit", command=self.third)
        submit_button.place(x=750, y=450)
        continue_button = Button(address_window, text="Continue", command=self.passport_details_page)
        continue_button.place(x=750, y=480)

    def third(self):
        street = self.street_entry.get()
        city = self.city_entry.get()
        state = self.state_entry.get()
        country = self.country_entry.get()
        zip_code = self.zip_code_entry.get()
        phone = self.phone_entry.get()

        mycursor.execute("INSERT INTO address VALUES (%s, %s, %s, %s, %s, %s)", (street, city, state, country, zip_code, phone))
        mydb.commit()

        msg.showinfo("Address Details", "Entered successfully!")

    def passport_details_page(self):
        passport_window = Toplevel(self.root)
        passport_window.title("Passport Details")
        passport_window.geometry("1000x600")
        passport_window.configure(bg='white')
        title = Label(passport_window, text="PASSPORT DETAILS", font=('bold', '25'), bg="white", fg="black")
        title.pack()

        # Passport Details Fields
        passport_no_label = Label(passport_window, text="Passport Number", font=('bold', '17'), bg="white", fg="black")
        passport_no_label.place(x=300, y=100)
        self.passport_no_entry = Entry(passport_window)
        self.passport_no_entry.place(x=500, y=105)

        issue_place_label = Label(passport_window, text="Place of Issue", font=('bold', '17'), bg="white", fg="black")
        issue_place_label.place(x=330, y=150)
        self.issue_place_entry = Entry(passport_window)
        self.issue_place_entry.place(x=500, y=155)

        issue_date_label = Label(passport_window, text="Date of Issue", font=('bold', '17'), bg="white", fg="black")
        issue_date_label.place(x=340, y=200)
        self.cal_issue_date = DateEntry(passport_window, width=16, background="magenta3", foreground="white", bd=2)
        self.cal_issue_date.place(x=500, y=205)

        expiry_date_label = Label(passport_window, text="Date of Expiry", font=('bold', '17'), bg="white", fg="black")
        expiry_date_label.place(x=340, y=250)
        self.cal_expiry_date = DateEntry(passport_window, width=16, background="magenta3", foreground="white", bd=2)
        self.cal_expiry_date.place(x=500, y=255)

        issue_authority_label = Label(passport_window, text="Issuing Authority", font=('bold', '17'), bg="white", fg="black")
        issue_authority_label.place(x=320, y=300)
        self.issue_authority_entry = Entry(passport_window)
        self.issue_authority_entry.place(x=500, y=305)

        # Buttons
        submit_button = Button(passport_window, text="Submit", command=self.fourth)
        submit_button.place(x=750, y=450)

    def fourth(self):
        passport_no = self.passport_no_entry.get()
        issue_place = self.issue_place_entry.get()
        issue_date = self.cal_issue_date.get_date().strftime('%Y-%m-%d')
        expiry_date = self.cal_expiry_date.get_date().strftime('%Y-%m-%d')
        issue_authority = self.issue_authority_entry.get()

        mycursor.execute("INSERT INTO passport_details VALUES (%s, %s, %s, %s)", (passport_no, issue_place, issue_date, expiry_date))
        mydb.commit()

        msg.showinfo("Passport Details", "Entered successfully!")

if __name__ == "__main__":
    root = Tk()
    obj = User(root)
    root.mainloop()
