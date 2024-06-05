
from flask import Flask, render_template, request ,redirect,jsonify, send_file, url_for
from flaskext.mysql import MySQL
import csv
import os



app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''  # Replace with your MySQL password
app.config['MYSQL_DATABASE_DB'] = 'providentfundsandfurnishings'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

con = mysql.connect()
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS providentfund (id INT AUTO_INCREMENT PRIMARY KEY, mr_ms_mrs text, name text, dateofbirth date, fatherandhusband text, relationinrespect text, gender text, mobilenumber integer, email text, emppovidentfunds text, emppensionscheme text, uaborprevious text, account text, dateofexit date, certificateissued text, pensionpayment text, internationworker text, india text, otherthanindia text, passport text,  passportfrom date , passportto date, educationalqualification text, maritalstatus varchar(225), specially varchar(225), category varchar(225), bankkycnumber text, banknumber text, bankremark text, nprkycnumber text, nprnumber text, nprremark text, permanentkycnumber text, permanentnumber text,  permanentremark text, passportkycnumber text, passportnumber text, passportremark text, drivinglicencekycnumber text, drivinglicencenumber text , drivinglicenceremark text, electioncardkycnumber text, electioncardnumber text, electioncardremark text,  rationcardkycnumber text, rationcardnumber text, rationcardremark text, esiccardkycnumber text, esiccardnumber text, esiccardremark text, today_date date, your_place text, your_name text, join_date date, UAN_ALLOTED text, today_dates date)")
cur.execute("CREATE TABLE IF NOT EXISTS newjoiningforminsurance (id INT AUTO_INCREMENT PRIMARY KEY, Name text, Designation text, PresentAddress text, PermanentAddress text, Namefather text, NameMother text, PAN text, DateJoining date, DateBirth date, personalmobile text, personalemail text, Department text, Location text, MaritalStatus text, EPFNOwithPreviousEmployer text, nameofSpouseandChildren text, Relationship text, DateofBirth date, nameofSpouseandChildren1 text, Relationship1 text, DateofBirth1 date, nameofSpouseandChildren2 text, Relationship2 text, DateofBirth2 text, nameofSpouseandChildren3 text, Relationship3 text, DateofBirth3 date)")
cur.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY , username text , password text)")
cur.execute("CREATE TABLE IF NOT EXISTS admin (id INT AUTO_INCREMENT PRIMARY KEY , HRADMIN text , passwords text)")
cur.execute("CREATE TABLE IF NOT EXISTS informationform (id INT AUTO_INCREMENT PRIMARY KEY , photoimage LONGBLOB, first_name text, middle_name text, surname text, employee_code text, reporting_manager text, department text, permanent_address text, PostalCodeorPinCode text, Present_Address text, dateofbirth date, sex text, birthplace date, bloodgroup text, nationality text, religion text,  pan text, language varchar(225), maritalstatus varchar(225), marriage_date date, spouse_name text, spouse_dob date, children_count integer, first_child_name text, first_child_dob date,  second_child_name text, second_child_dob date, third_child_name text,  third_child_dob date, contact_number text,  mobile_number text, emergency_contact text, email_id text, SSCName text, SSCSpecialization text, SSCSPassingYearMonth text, SSCPercentage text, SSCGrade text, HSCName text, HSCSpecialization text,    HSCPassingYearMonth text, HSCPercentage text , HSCGrade text, GraduationName text, GraduationSpecialization text,   GraduationPassingYearMonth text, GraduationPercentage text, GraduationGrade text, DiplomaName text, DiplomaSpecialization text, DiplomaPassingYearMonth text, DiplomaPercentage text, DiplomaGrade text, DegreeName text, DegreeSpecialization text,  DegreePassingYearMonth text, DegreePercentage text, DegreeGrade text, MastersorPostGraduationName text , MastersorPostGraduationSpecialization text,  MastersorPostGraduationPassingYearMonth text, MastersorPercentage text, MastersorGrade text, DoctorateName text, DoctorateSpecialization text,  DoctoratePassingYearMonth text, DoctoratePercentage text, DoctorateGrade text, OthersName text, OthersSpecialization text,   OthersPassingYearMonth text,  OthersPercentage text, OthersGrade text, aOrganization text, aDesignation text, aLocation text, aDurationfrom date, aDurationto date, bOrganization text, bDesignation text, bLocation text, bDurationfrom date, bDurationto date, cOrganization text, cDesignation text, cLocation text, cDurationfrom date, cDurationto date, dOrganization text, dDesignation text, dLocation text, dDurationfrom date, dDurationto date, eOrganization text, eDesignation text, eLocation text, eDurationfrom date, eDurationto date, todaydate date)")
cur.execute("CREATE TABLE IF NOT EXISTS inductionforminsurance (id INT AUTO_INCREMENT PRIMARY KEY ,Employee_name text, Employee_ID text, Department text, Joining_Date date, Designation text, HRorAdminDayandTime date, HRorAdminEmployeeSign varchar(225), HRorAdminProcessOwnerSign varchar(225), Quality_EngineeringDayandTime1 date, Quality_EngineeringEmployeeSign1 varchar(225), Quality_EngineeringProcessOwnerSign1 varchar(225),  Finance_ControlDayandTime2 date, Finance_ControlEmployeeSign2 varchar(225), Finance_ControlProcessOwnerSign2 varchar(225), Project_ManagementDayandTime3 date, Project_ManagementEmployeeSign3 varchar(225), Project_ManagementProcessOwnerSign3 varchar(225), Engineering_DayandTime4 date, Engineering_EmployeeSign4 varchar(225), Engineering_ProcessOwnerSign4 varchar(225), SIBM_DayandTime5 date, SIBM_EmployeeSign5 varchar(225), SIBM_ProcessOwnerSign5 varchar(225), Procurement_DayandTime6 date, Procurement_EmployeeSign6 varchar(225), Procurement_ProcessOwnerSign6 varchar(225), Proposal_ServiceDayandTime7 date, Proposal_ServiceEmployeeSign7 varchar(225), Proposal_ServiceProcessOwnerSign7 varchar(225), Refractory_DayandTime8 date, Refractory_EmployeeSign8 varchar(225), Refractory_ProcessOwnerSign8 varchar(225), PMO_DayandTime9 date,PMO_EmployeeSign9 varchar(225), PMO_ProcessOwnerSign9 varchar(225), IT_DayandTime10 date, IT_EmployeeSign10 varchar(225), IT_ProcessOwnerSign10 varchar(225), Employee_FeedbacK text , Employee_Signature text, Date1 date, Date2 date)")
cur.execute("CREATE TABLE IF NOT EXISTS employeeoboarding (id INT AUTO_INCREMENT PRIMARY KEY, Form_No text, Date_of_Issue date, Revision text, Approved_by text, Resume BOOLEAN, Employee_Information_Form  BOOLEAN, Educational_Certificate BOOLEAN,  Relieving_Certificates_of_last_2_organizations BOOLEAN, Salary_Slips_of_last_3_months  BOOLEAN, Form_16_If_applicable BOOLEAN, Pan_Card_Mandatory BOOLEAN, Photo_ID_Proof_Voter_Aadhar_Card_Passport_etc BOOLEAN, Passport_size_Photo BOOLEAN, Permanent_Mandatory BOOLEAN, Bank_Aorc_Opening_Form_and_Formalities BOOLEAN, Current_Address_Proof  BOOLEAN, NDAorService_Agreement  BOOLEAN,  Entry_in_Keka BOOLEAN,  Appointment_Letter  BOOLEAN, Entry_in_Dax360  BOOLEAN, Entry_in_Meytou BOOLEAN, Indirect_ariff BOOLEAN, Stationary_Notepad_and_Pen BOOLEAN,  Employee_ID_Card  BOOLEAN, Extension_list  BOOLEAN,   Visiting_Cards_if_pplicable  BOOLEAN,  Adhaar_Card_Copy BOOLEAN, Appointment_Letter_Copy BOOLEAN, Nomination_Letter  BOOLEAN, Universal_Account_Number_UAN  BOOLEAN, Provident_Fund_Account_Number_PF  BOOLEAN, Bank_Account_No_and_Name  BOOLEAN, PAN_Card_Copy BOOLEAN, Seating_Arrangement  BOOLEAN, Laptopa_and_Desktop_and_Accessories  BOOLEAN, Phone_Extension  BOOLEAN, Official_Email_ID_Creation BOOLEAN, Group_and_Location_Email_Alias BOOLEAN, Sim_Card  BOOLEAN,  Head_Phone BOOLEAN, Screen BOOLEAN,  Employee_Access_Card_and_Biometrix_Access BOOLEAN,  Insurance_Form BOOLEAN, Insurance_Form1 BOOLEAN)")
cur.execute("CREATE TABLE IF NOT EXISTS taxdeduction  (id INT AUTO_INCREMENT PRIMARY KEY ,  end_year date, name_and_address text, permanent_accountno text, residential_status text, name_and_address_employer text, tan_of_employer_ito  text, permanent_account_number text, period_of_employment date, total_amount_of_salary text, total_amount_house_allowance text, value_of_perquistes_and_amount text, total_of_colume text, amount_deducted_in_respesct text, total_of_tax_deducteddu_in_the_year  text, remark text, your_name text, verified_today date, day_of_year date, name_emp_address text, permanent_account text, year_endingfrom date,  year_endingto date,  name_of_emp text, tan_of_employer text, acommodation_is_unfurnished  text, value_of_acommodation  text,  cost_of_furniture  text, perquisite_value_of_furniture  text, total_of_column1 text, rent  text, value_of_perquisite text, name_of_employee text, whether_any_conveyance text, remuneration12 text, value13 text, estimated_value14 text, employer_contribution15 text, interest16 text, total_of_columns17 text, policy text, Date5 date, gross_amount text, qualifying_amount text)")
con.commit()
cur.close()
con.close()

@app.route('/')
def index():
    return render_template("userandadmin.html")

@app.route('/logins')
def logins():
    return render_template("loginpage.html")

# @app.route('/signups')
# def signups():
#     return render_template("signup.html")


@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            con = mysql.connect()
            cur = con.cursor()
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            con.commit()
        except Exception as e:
            return f"{e}" 
        return render_template("managemployee.html")




@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        uname = request.form['uname']
        psw = request.form['psw']
        try:
            con = mysql.connect()
            cur = con.cursor()
            # print(f"Attempting to log in with username: {uname}, password: {psw}")
            cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (uname, psw))
            data = cur.fetchone()
            cur.close()
            con.close()
            # print(f"Query result: {data}")
            if data:
                return render_template("homepage.html")
            else:
                return "Login failed. Please check your username and password."
        except mysql.connector.Error as err:
            return f"MySQL Error: {err}"
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return render_template("loginpage.html")






@app.route('/admin')
def admin():
    return render_template("loginadmin.html")

@app.route('/adminadd' , methods=['POST'])
def adminadd():
    if request.method=='POST':
        admin = request.form['admin']
        adminpsw = request.form['adminpsw']
        try:
            con = mysql.connect()
            cur = con.cursor()
            # print(f"Attempting to log in with username: {uname}, password: {psw}")
            cur.execute("SELECT * FROM admin WHERE HRADMIN = %s AND passwords = %s", (admin, adminpsw))
            data = cur.fetchone()
            cur.close()
            con.close()
            # print(f"Query result: {data}")
            if data:
                return render_template("HRadmin.html")
            else:
                return "Login failed. Please check your HRAdmin and password."
        except mysql.connector.Error as err:
            return f"MySQL Error: {err}"
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return render_template("loginadmin.html")


# @app.route('/homepages')
# def homepages():
#     return render_template("HRadmin.html")
    

@app.route('/showusers' ,methods=['GET' , 'POST'])
def showusers():
        data = None
        try:
            con = mysql.connect()
            cur = con.cursor()
            if request.method == 'POST':
                username = request.form.get("username")
                cur.execute("SELECT username, password FROM users WHERE username LIKE %s", ("%" + username + "%",))
            else:
                cur.execute("SELECT * FROM users")
            
            data = cur.fetchall()
            cur.close()
            con.close()
        except Exception as e:
            return str(e)

        return render_template("managemployee.html", data=data)


@app.route('/showuser')
def showuser():
     con = mysql.connect()
     cur=con.cursor()
     cur.execute("SELECT * from users")
     data = cur.fetchall()
     return render_template("managemployees.html", data=data)
 
# @app.route('/search',methods=['GET' , 'POST']) 
# def search():
#     data = None
#     if request.method == 'POST':
#         username = request.form.get("username")
#         try:
#             con = mysql.connect()
#             cur = con.cursor()
#             cur.execute("SELECT username, password FROM users WHERE username LIKE %s", ("%" + username + "%",))
#             data = cur.fetchall()
#             cur.close()
#             con.close()
#         except Exception as e:
#             return str(e)
#     return render_template('managemployee.html', data=data)
 

@app.route('/employee_submitted')
def employee_submitted():
            con = mysql.connect()
            cur=con.cursor()
            cur.execute("SELECT id, username FROM users")
        
            datas = cur.fetchall()
            con.close()
            return render_template("Employee_submission.html" , datas=datas)
   
   
    
    
    



    

@app.route('/signup')
def signup():
    return render_template("signup.html")


    


        





@app.route('/homepage')
def homepage():
    return render_template("homepage.html")  

@app.route('/form')
def form():
    return render_template("PFform.html")



@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
            choice1 = request.form['choice1']
            name1 = request.form['name1']
            dob = request.form['dob']
            fatherandhusband = request.form['fatherandhusband']
            choice3 = request.form['choice3']
            choice4 = request.form['choice4']
            mobile = request.form['mobile']
            email = request.form['email']
            choice5 = request.form['choice5']
            choice6 = request.form['choice6']
            choice7 = request.form['choice7']
            previousemployment = request.form['previousemployment']
            dateprevious = request.form['dateprevious']
            certificateforpreviousemployment = request.form['certificateforpreviousemployment']
            persionpayment = request.form['persionpayment']
            internationalworker = request.form['internationalworker']
            india = request.form['india']
            otherindia = request.form['otherindia']
            passportnumber = request.form['passportnumber']
            passportvalid = request.form['passportvalid']
            passportvalid1 = request.form['passportvalid1']
            educationalqualification = ', '.join(request.form.getlist('educationalqualification'))
            maritalstatus = request.form.get('maritalstatus')
            specially = request.form.get('specially')
            abled = ', '.join(request.form.getlist('abled')) # Convert list to string
            bankkycnumber = request.form['bankkycnumber']
            banknumber = request.form['banknumber']
            bankremark = request.form['bankremark']
            nprkycnumber = request.form['nprkycnumber']
            nprnumber = request.form['nprnumber']
            nprremark = request.form['nprremark']
            permanentkycnumber = request.form['permanentkycnumber']
            permanentnumber = request.form['permanentnumber']
            permanentremark = request.form['permanentremark']
            passportkycnumber = request.form['passportkycnumber']
            passportnumber = request.form['passportnumber']
            passportremark = request.form['passportremark']
            drivinglicencekycnumber = request.form['drivinglicencekycnumber']
            drivinglicencenumber = request.form['drivinglicencenumber']
            drivinglicenceremark = request.form['drivinglicenceremark']
            electioncardkycnumber = request.form['electioncardkycnumber']
            electioncardnumber = request.form['electioncardnumber']
            electioncardremark = request.form['electioncardremark']
            rationcardkycnumber = request.form['rationcardkycnumber']
            rationcardnumber = request.form['rationcardnumber']
            rationcardremark = request.form['rationcardremark']
            esiccardkycnumber = request.form['esiccardkycnumber']
            esiccardnumber = request.form['esiccardnumber']
            esiccardremark = request.form['esiccardremark']
            today_date = request.form['today_date']
            your_place = request.form['your_place']
            your_name = request.form['your_name'] 
            join_date = request.form['join_date']
            UAN_ALLOTED = request.form['UAN_ALLOTED']
            today_dates = request.form['today_dates']
            try:
            # Insert data into the table
                    con = mysql.connect()
                    cur = con.cursor()
                    cur.execute("""
            INSERT INTO providentfund (
                mr_ms_mrs, name, dateofbirth, fatherandhusband, relationinrespect, gender, 
                mobilenumber, email, emppovidentfunds, emppensionscheme, uaborprevious, account, 
                dateofexit, certificateissued, pensionpayment, internationworker, india, otherthanindia, 
                passport, passportfrom, passportto, educationalqualification, maritalstatus, specially, 
                category, bankkycnumber, banknumber, bankremark, nprkycnumber, nprnumber, nprremark, 
                permanentkycnumber, permanentnumber, permanentremark, passportkycnumber, passportnumber, 
                passportremark, drivinglicencekycnumber, drivinglicencenumber, drivinglicenceremark, 
                electioncardkycnumber, electioncardnumber, electioncardremark, rationcardkycnumber, 
                rationcardnumber, rationcardremark, esiccardkycnumber, esiccardnumber, esiccardremark, today_date, 
                your_place, your_name, join_date, UAN_ALLOTED, today_dates
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """, (
            choice1, name1, dob,fatherandhusband, choice3, choice4, mobile, email, choice5, choice6, choice7, 
            previousemployment,dateprevious, certificateforpreviousemployment, persionpayment, internationalworker, 
            india, otherindia, passportnumber, passportvalid, passportvalid1, educationalqualification, 
            maritalstatus, specially, abled, bankkycnumber, banknumber, bankremark, nprkycnumber, 
            nprnumber, nprremark, permanentkycnumber, permanentnumber, permanentremark, passportkycnumber, 
            passportnumber, passportremark, drivinglicencekycnumber, drivinglicencenumber, 
            drivinglicenceremark, electioncardkycnumber, electioncardnumber, electioncardremark, 
            rationcardkycnumber, rationcardnumber, rationcardremark, esiccardkycnumber, esiccardnumber, 
            esiccardremark ,today_date, your_place, your_name, join_date, UAN_ALLOTED, today_dates
        ))

                    con.commit()
                    # emp_id = cur.lastrowid
                    # cur.close()
                    # con.close()

                    # Generate a unique filename for the form (timestamp + emp_id)
                    # timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                    # unique_filename = f"{timestamp}_emp_{emp_id}.pdf"

                    # Save the form data to a file
                    # save_form_data_to_file(request.form, unique_filename)
                    return jsonify(success=True, message="Data inserted successfully", download_url=url_for('download_data'))
                    # return jsonify(success=True, message="Data inserted successfully", download_url=url_for('download_data', filename=unique_filename))
            except Exception as e:
                    return jsonify(success=False, message=str(e))

@app.route('/download_data')
def download_data():
    try:
        con = mysql.connect()
        cursor = con.cursor()

        cursor.execute("SELECT * FROM providentfund")

        rows = cursor.fetchall()
        headers = [i[0] for i in cursor.description]

        cursor.close()
        con.close()

        csv_file_path = r'F:\html folder\dciform2\data.csv'
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(headers)
            writer.writerows(rows)

        return send_file(csv_file_path, as_attachment=True)
    except Exception as e:
            return str(e)
        
        
# def save_form_data_to_file(form_data, filename):
#     # Define the directory where forms will be saved
#     forms_directory = "forms"

#     # Create the directory if it doesn't exist
#     if not os.path.exists(forms_directory):
#         os.makedirs(forms_directory)

#     # Write the form data to a file
#     form_file_path = os.path.join(forms_directory, filename)
#     with open(form_file_path, 'w') as file:
#         for key, value in form_data.items():
#             file.write(f"{key}: {value}\n")

#     # Optionally, you can return the file path if needed
#     return form_file_path
    
    
    
    
@app.route('/forms')
def forms():
    return render_template("form12.html")

@app.route('/forminserts', methods=['POST'])
def forminserts():
    if request.method=='POST':
        end_year = request.form["end_year"]
        name_and_address = request.form["name_and_address"]
        permanent_accountno = request.form["permanent_accountno"]
        residential_status = request.form["residential_status"]
        name_and_address_employer = request.form["name_and_address_employer"]
        tan_of_employer_ito = request.form["tan_of_employer_ito"]
        permanent_account_number = request.form["permanent_account_number"]
        period_of_employment = request.form["period_of_employment"]
        total_amount_of_salary = request.form["total_amount_of_salary"]
        total_amount_house_allowance = request.form["total_amount_house_allowance"]
        value_of_perquistes_and_amount = request.form["value_of_perquistes_and_amount"]
        total_of_colume = request.form["total_of_colume"]
        amount_deducted_in_respesct = request.form["amount_deducted_in_respesct"]
        total_of_tax_deducteddu_in_the_year = request.form["total_of_tax_deducteddu_in_the_year"]
        remark = request.form["remark"]
        your_name = request.form["your_name"]
        verified_today = request.form["verified_today"]
        day_of_year = request.form["day_of_year"]
        name_emp_address = request.form["name_emp_address"]
        permanent_account = request.form["permanent_account"]
        year_endingfrom = request.form["year_endingfrom"]
        year_endingto = request.form["year_endingto"]
        name_of_emp = request.form["name_of_emp"]
        tan_of_employer = request.form["tan_of_employer"]
        acommodation_is_unfurnished = request.form["acommodation_is_unfurnished"]
        value_of_acommodation = request.form["value_of_acommodation"]
        cost_of_furniture = request.form["cost_of_furniture"]
        perquisite_value_of_furniture = request.form["perquisite_value_of_furniture"]
        total_of_column1 = request.form["total_of_column1"]
        rent = request.form["rent"]
        value_of_perquisite = request.form["value_of_perquisite"]
        name_of_employee = request.form["name_of_employee"]
        whether_any_conveyance = request.form["whether_any_conveyance"]
        remuneration12 = request.form["remuneration12"]
        value13 = request.form["value13"]
        estimated_value14 = request.form["estimated_value14"]
        employer_contribution15 = request.form["employer_contribution15"]
        interest16 = request.form["interest16"]
        total_of_columns17 = request.form["total_of_columns17"]
        policy = request.form["policy"]
        Date5 = request.form.get("Date5")
        gross_amount = request.form["gross_amount"]
        qualifying_amount = request.form["qualifying_amount"]

        try:
             
            con = mysql.connect()
            cur = con.cursor()
            cur.execute("""
                INSERT INTO taxdeduction (
                    end_year,name_and_address, permanent_accountno, residential_status, 
                    name_and_address_employer, tan_of_employer_ito, permanent_account_number, 
                    period_of_employment, total_amount_of_salary, total_amount_house_allowance, 
                    value_of_perquistes_and_amount, total_of_colume, amount_deducted_in_respesct, 
                    total_of_tax_deducteddu_in_the_year, remark, your_name, verified_today, 
                    day_of_year, name_emp_address, permanent_account, year_endingfrom, year_endingto,  name_of_emp, 
                    tan_of_employer, acommodation_is_unfurnished, value_of_acommodation, 
                    cost_of_furniture, perquisite_value_of_furniture, total_of_column1, rent, 
                    value_of_perquisite, name_of_employee, whether_any_conveyance, remuneration12, 
                    value13, estimated_value14, employer_contribution15, interest16, 
                    total_of_columns17, policy, Date5, gross_amount, qualifying_amount
                ) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
            """, (
                end_year, name_and_address, permanent_accountno, residential_status, 
                name_and_address_employer, tan_of_employer_ito, permanent_account_number, 
                period_of_employment, total_amount_of_salary, total_amount_house_allowance, 
                value_of_perquistes_and_amount, total_of_colume, amount_deducted_in_respesct, 
                total_of_tax_deducteddu_in_the_year, remark, your_name, verified_today, 
                day_of_year, name_emp_address, permanent_account, year_endingfrom, year_endingto, name_of_emp, 
                tan_of_employer, acommodation_is_unfurnished, value_of_acommodation, 
                cost_of_furniture, perquisite_value_of_furniture, total_of_column1, rent, 
                value_of_perquisite, name_of_employee, whether_any_conveyance, remuneration12, 
                value13, estimated_value14, employer_contribution15, interest16, 
                total_of_columns17, policy, Date5, gross_amount, qualifying_amount
            ))
            con.commit()
            return "Data inserted successfully"
        except Exception as e:
            return str(e)


        
    



@app.route('/informationform')
def informationform():
    return render_template("informationform.html")


@app.route('/informationforminserts', methods=['POST' , 'GET'])
def informationforminserts():
    if request.method == 'POST':
        if 'photoimage' not in request.files:
            return "No file part in the request", 400  
        photoimage = request.files['photoimage']
        if photoimage.filename == '':
            return "No selected file", 400
        photoimage_data = photoimage.read()

        first_name = request.form.get("first_name")
        middle_name = request.form.get("middle_name")
        surname = request.form.get("surname")
        employee_code = request.form.get("employee_code")
        reporting_manager = request.form.get("reporting_manager")
        department = request.form.get("department")
        permanent_address = request.form.get("permanent_address")
        PostalCodeorPinCode = request.form.get("PostalCodeorPinCode")
        Present_Address = request.form.get("Present_Address")
        dateofbirth = request.form.get("dateofbirth")
        sex = request.form.get("sex")
        birthplace = request.form.get("birthplace")
        bloodgroup = request.form.get("bloodgroup")
        nationality = request.form.get("nationality")
        religion = request.form.get("religion")
        pan = request.form.get("pan")
        language =  ', '.join(request.form.getlist("language")) 
        maritalstatus = request.form.get("maritalstatus")
        marriage_date = request.form.get("marriage_date")
        spouse_name = request.form.get("spouse_name")
        spouse_dob = request.form.get("spouse_dob")
        children_count = request.form.get("children_count")
        first_child_name = request.form.get("first_child_name")
        first_child_dob = request.form.get("first_child_dob")
        second_child_name = request.form.get("second_child_name")
        second_child_dob = request.form.get("second_child_dob")
        third_child_name = request.form.get("third_child_name")
        third_child_dob = request.form.get("third_child_dob")
        contact_number = request.form.get("contact_number")
        mobile_number = request.form.get("mobile_number")
        emergency_contact = request.form.get("emergency_contact")
        email_id = request.form.get("email_id")
        SSCName = request.form.get("SSCName")
        SSCSpecialization = request.form.get("SSCSpecialization")
        SSCSPassingYearMonth = request.form.get("SSCSPassingYearMonth")
        SSCPercentage = request.form.get("SSCPercentage")
        SSCGrade = request.form.get("SSCGrade")
        HSCName = request.form.get("HSCName")
        HSCSpecialization = request.form.get("HSCSpecialization")
        HSCPassingYearMonth = request.form.get("HSCPassingYearMonth")
        HSCPercentage = request.form.get("HSCPercentage")
        HSCGrade = request.form.get("HSCGrade")
        GraduationName = request.form.get("GraduationName")
        GraduationSpecialization = request.form.get("GraduationSpecialization")
        GraduationPassingYearMonth = request.form.get("GraduationPassingYearMonth")
        GraduationPercentage = request.form.get("GraduationPercentage")
        GraduationGrade = request.form.get("GraduationGrade")
        DiplomaName = request.form.get("DiplomaName")
        DiplomaSpecialization = request.form.get("DiplomaSpecialization")
        DiplomaPassingYearMonth = request.form.get("DiplomaPassingYearMonth")
        DiplomaPercentage = request.form.get("DiplomaPercentage")
        DiplomaGrade = request.form.get("DiplomaGrade")
        DegreeName = request.form.get("DegreeName")
        DegreeSpecialization = request.form.get("DegreeSpecialization")
        DegreePassingYearMonth = request.form.get("DegreePassingYearMonth")
        DegreePercentage = request.form.get("DegreePercentage")
        DegreeGrade = request.form.get("DegreeGrade")
        MastersorPostGraduationName = request.form.get("MastersorPostGraduationName")
        MastersorPostGraduationSpecialization = request.form.get("MastersorPostGraduationSpecialization")
        MastersorPostGraduationPassingYearMonth = request.form.get("MastersorPostGraduationPassingYearMonth")
        MastersorPercentage = request.form.get("MastersorPercentage")
        MastersorGrade = request.form.get("MastersorGrade")
        DoctorateName = request.form.get("DoctorateName")
        DoctorateSpecialization = request.form.get("DoctorateSpecialization")
        DoctoratePassingYearMonth = request.form.get("DoctoratePassingYearMonth")
        DoctoratePercentage = request.form.get("DoctoratePercentage")
        DoctorateGrade = request.form.get("DoctorateGrade")
        OthersName = request.form.get("OthersName")
        OthersSpecialization = request.form.get("OthersSpecialization")
        OthersPassingYearMonth = request.form.get("OthersPassingYearMonth")
        OthersPercentage = request.form.get("OthersPercentage")
        OthersGrade = request.form.get("OthersGrade")
        aOrganization = request.form.get("aOrganization")
        aDesignation = request.form.get("aDesignation")
        aLocation = request.form.get("aLocation")
        aDurationfrom = request.form.get("aDurationfrom")
        aDurationto = request.form.get("aDurationto")
        bOrganization = request.form.get("bOrganization")
        bDesignation = request.form.get("bDesignation")
        bLocation = request.form.get("bLocation")
        bDurationfrom = request.form.get("bDurationfrom")
        bDurationto = request.form.get("bDurationto")
        cOrganization = request.form.get("cOrganization")
        cDesignation = request.form.get("cDesignation")
        cLocation = request.form.get("cLocation")
        cDurationfrom = request.form.get("cDurationfrom")
        cDurationto = request.form.get("cDurationto")
        dOrganization = request.form.get("dOrganization")
        dDesignation = request.form.get("dDesignation")
        dLocation = request.form.get("dLocation")
        dDurationfrom = request.form.get("dDurationfrom")
        dDurationto = request.form.get("dDurationto")
        eOrganization = request.form.get("eOrganization")
        eDesignation = request.form.get("eDesignation")
        eLocation = request.form.get("eLocation")
        eDurationfrom = request.form.get("eDurationfrom")
        eDurationto = request.form.get("eDurationto")
        todaydate = request.form.get("todaydate")

        try:
            con = mysql.connect()
            cur = con.cursor()
            cur.execute(
                """INSERT INTO informationform (
                    photoimage, first_name, middle_name, surname, employee_code, reporting_manager, department, 
                    permanent_address, PostalCodeorPinCode, Present_Address, dateofbirth, sex, birthplace, 
                    bloodgroup, nationality, religion, pan, language, maritalstatus, marriage_date, 
                    spouse_name, spouse_dob, children_count, first_child_name, first_child_dob, 
                    second_child_name, second_child_dob, third_child_name, third_child_dob, contact_number, 
                    mobile_number, emergency_contact, email_id, SSCName, SSCSpecialization, 
                    SSCSPassingYearMonth, SSCPercentage, SSCGrade, HSCName, HSCSpecialization, 
                    HSCPassingYearMonth, HSCPercentage, HSCGrade, GraduationName, GraduationSpecialization, 
                    GraduationPassingYearMonth, GraduationPercentage, GraduationGrade, DiplomaName, 
                    DiplomaSpecialization, DiplomaPassingYearMonth, DiplomaPercentage, DiplomaGrade, 
                    DegreeName, DegreeSpecialization, DegreePassingYearMonth, DegreePercentage, DegreeGrade, 
                    MastersorPostGraduationName, MastersorPostGraduationSpecialization, 
                    MastersorPostGraduationPassingYearMonth, MastersorPercentage, MastersorGrade, DoctorateName, 
                    DoctorateSpecialization, DoctoratePassingYearMonth, DoctoratePercentage, DoctorateGrade, 
                    OthersName, OthersSpecialization, OthersPassingYearMonth, OthersPercentage, OthersGrade, 
                    aOrganization, aDesignation, aLocation, aDurationfrom, aDurationto, bOrganization, 
                    bDesignation, bLocation, bDurationfrom, bDurationto, cOrganization, cDesignation, 
                    cLocation, cDurationfrom, cDurationto, dOrganization, dDesignation, dLocation, 
                    dDurationfrom, dDurationto, eOrganization, eDesignation, eLocation, eDurationfrom, 
                    eDurationto, todaydate
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s,%s
                )""",
                (
                    photoimage_data, first_name, middle_name, surname, employee_code, reporting_manager, department,
                    permanent_address, PostalCodeorPinCode, Present_Address, dateofbirth, sex, birthplace,
                    bloodgroup, nationality, religion, pan, language, maritalstatus, marriage_date,
                    spouse_name, spouse_dob, children_count, first_child_name, first_child_dob,
                    second_child_name, second_child_dob, third_child_name, third_child_dob, contact_number,
                    mobile_number, emergency_contact, email_id, SSCName, SSCSpecialization,
                    SSCSPassingYearMonth, SSCPercentage, SSCGrade, HSCName, HSCSpecialization,
                    HSCPassingYearMonth, HSCPercentage, HSCGrade, GraduationName, GraduationSpecialization,
                    GraduationPassingYearMonth, GraduationPercentage, GraduationGrade, DiplomaName,
                    DiplomaSpecialization, DiplomaPassingYearMonth, DiplomaPercentage, DiplomaGrade,
                    DegreeName, DegreeSpecialization, DegreePassingYearMonth, DegreePercentage, DegreeGrade,
                    MastersorPostGraduationName, MastersorPostGraduationSpecialization,
                    MastersorPostGraduationPassingYearMonth, MastersorPercentage, MastersorGrade, DoctorateName,
                    DoctorateSpecialization, DoctoratePassingYearMonth, DoctoratePercentage, DoctorateGrade,
                    OthersName, OthersSpecialization, OthersPassingYearMonth, OthersPercentage, OthersGrade,
                    aOrganization, aDesignation, aLocation, aDurationfrom, aDurationto, bOrganization,
                    bDesignation, bLocation, bDurationfrom, bDurationto, cOrganization, cDesignation,
                    cLocation, cDurationfrom, cDurationto, dOrganization, dDesignation, dLocation,
                    dDurationfrom, dDurationto, eOrganization, eDesignation, eLocation, eDurationfrom,
                    eDurationto, todaydate
                )
            )
            con.commit()
            cur.close()
            con.close()
            return "Data inserted successfully"
        except Exception as e:
            return str(e)

           
        
            



@app.route('/newjoining')
def newjoining():
    return render_template("newjoining.html")

@app.route('/newjoininginserts' , methods=['POST' , 'GET'])
def newjoininginserts():
    if request.method=='POST':
        Name=request.form["Name"]
        Designation=request.form["Designation"]
        PresentAddress=request.form["PresentAddress"]
        PermanentAddress=request.form["PermanentAddress"]
        Namefather=request.form["Namefather"]
        NameMother=request.form["NameMother"]
        PAN=request.form["PAN"]
        DateJoining=request.form["DateJoining"]
        DateBirth=request.form["DateBirth"]
        personalmobile=request.form["personalmobile"]
        personalemail=request.form["personalemail"]
        Department=request.form["Department"]
        Location=request.form["Location"]
        MaritalStatus=request.form["MaritalStatus"]
        EPFNOwithPreviousEmployer=request.form["EPFNOwithPreviousEmployer"]
        nameofSpouseandChildren=request.form["nameofSpouseandChildren"]
        Relationship=request.form["Relationship"]
        DateofBirth=request.form["DateofBirth"]
        nameofSpouseandChildren1=request.form["nameofSpouseandChildren1"]
        Relationship1=request.form["Relationship1"]
        DateofBirth1=request.form["DateofBirth1"]
        nameofSpouseandChildren2=request.form["nameofSpouseandChildren2"]
        Relationship2=request.form["Relationship2"]
        DateofBirth2=request.form["DateofBirth2"]
        nameofSpouseandChildren3=request.form["nameofSpouseandChildren3"]
        Relationship3=request.form["Relationship3"]
        DateofBirth3=request.form["DateofBirth3"]
        try:
            con = mysql.connect()
            cur = con.cursor()
            cur.execute(
                """INSERT INTO newjoiningforminsurance (
                    Name, Designation, PresentAddress, PermanentAddress, Namefather, NameMother, PAN, 
                    DateJoining, DateBirth, personalmobile, personalemail, Department, Location, 
                    MaritalStatus, EPFNOwithPreviousEmployer, nameofSpouseandChildren, Relationship, 
                    DateofBirth, nameofSpouseandChildren1, Relationship1, DateofBirth1, 
                    nameofSpouseandChildren2, Relationship2, DateofBirth2, nameofSpouseandChildren3, 
                    Relationship3, DateofBirth3
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s)""",
                (
                    Name, Designation, PresentAddress, PermanentAddress, Namefather, NameMother, PAN, 
                    DateJoining, DateBirth, personalmobile, personalemail, Department, Location, 
                    MaritalStatus, EPFNOwithPreviousEmployer, nameofSpouseandChildren, Relationship, 
                    DateofBirth, nameofSpouseandChildren1, Relationship1, DateofBirth1, 
                    nameofSpouseandChildren2, Relationship2, DateofBirth2, nameofSpouseandChildren3, 
                    Relationship3, DateofBirth3
                )
            )
            con.commit()
            cur.close()
            con.close()
            return "Data inserted successfully"
        except Exception as e:
            return str(e)
        
        
@app.route('/newempinductionform')
def newempinductionform():
    return render_template("induction.html")


@app.route('/inductioninserts', methods=['POST'])
def inductioninserts():
    if request.method=='POST':
        Employee_name = request.form.get("Employee_name")
        Employee_ID = request.form.get("Employee_ID")
        Department = request.form.get("Department")
        Joining_Date = request.form.get("Joining_Date")
        Designation = request.form.get("Designation")
        HRorAdminDayandTime = request.form.get("HRorAdminDayandTime")
        HRorAdminEmployeeSign = request.form.get("HRorAdminEmployeeSign")
        HRorAdminProcessOwnerSign = request.form.get("HRorAdminProcessOwnerSign")
        Quality_EngineeringDayandTime1 = request.form.get("Quality_EngineeringDayandTime1")
        Quality_EngineeringEmployeeSign1 = request.form.get("Quality_EngineeringEmployeeSign1")
        Quality_EngineeringProcessOwnerSign1 = request.form.get("Quality_EngineeringProcessOwnerSign1")
        Finance_ControlDayandTime2 = request.form.get("Finance_ControlDayandTime2")
        Finance_ControlEmployeeSign2 = request.form.get("Finance_ControlEmployeeSign2")
        Finance_ControlProcessOwnerSign2 = request.form.get("Finance_ControlProcessOwnerSign2")
        Project_ManagementDayandTime3 = request.form.get("Project_ManagementDayandTime3")
        Project_ManagementEmployeeSign3 = request.form.get("Project_ManagementEmployeeSign3")
        Project_ManagementProcessOwnerSign3 = request.form.get("Project_ManagementProcessOwnerSign3")
        Engineering_DayandTime4 = request.form.get("Engineering_DayandTime4")
        Engineering_EmployeeSign4 = request.form.get("Engineering_EmployeeSign4")
        Engineering_ProcessOwnerSign4 = request.form.get("Engineering_ProcessOwnerSign4")
        SIBM_DayandTime5 = request.form.get("SIBM_DayandTime5")
        SIBM_EmployeeSign5 = request.form.get("SIBM_EmployeeSign5")
        SIBM_ProcessOwnerSign5 = request.form.get("SIBM_ProcessOwnerSign5")
        Procurement_DayandTime6 = request.form.get("Procurement_DayandTime6")
        Procurement_EmployeeSign6 = request.form.get("Procurement_EmployeeSign6")
        Procurement_ProcessOwnerSign6 = request.form.get("Procurement_ProcessOwnerSign6")
        Proposal_ServiceDayandTime7 = request.form.get("Proposal_ServiceDayandTime7")
        Proposal_ServiceEmployeeSign7 = request.form.get("Proposal_ServiceEmployeeSign7")
        Proposal_ServiceProcessOwnerSign7 = request.form.get("Proposal_ServiceProcessOwnerSign7")
        Refractory_DayandTime8 = request.form.get("Refractory_DayandTime8")
        Refractory_EmployeeSign8 = request.form.get("Refractory_EmployeeSign8")
        Refractory_ProcessOwnerSign8 = request.form.get("Refractory_ProcessOwnerSign8")
        PMO_DayandTime9 = request.form.get("PMO_DayandTime9")
        PMO_EmployeeSign9 = request.form.get("PMO_EmployeeSign9")
        PMO_ProcessOwnerSign9 = request.form.get("PMO_ProcessOwnerSign9")
        IT_DayandTime10 = request.form.get("IT_DayandTime10")
        IT_EmployeeSign10 = request.form.get("IT_EmployeeSign10")
        IT_ProcessOwnerSign10 = request.form.get("IT_ProcessOwnerSign10")
        Employee_FeedbacK = request.form.get("Employee_FeedbacK")
        Employee_Signature = request.form.get("Employee_Signature")
        Date1 = request.form.get("Date1")
        Date2 = request.form.get("Date2")
        try:
            con = mysql.connect()
            cur = con.cursor()
            cur.execute(
                """INSERT INTO inductionforminsurance (
                    Employee_name, Employee_ID, Department, Joining_Date, Designation, HRorAdminDayandTime, 
                    HRorAdminEmployeeSign, HRorAdminProcessOwnerSign, Quality_EngineeringDayandTime1, 
                    Quality_EngineeringEmployeeSign1, Quality_EngineeringProcessOwnerSign1, Finance_ControlDayandTime2, 
                    Finance_ControlEmployeeSign2, Finance_ControlProcessOwnerSign2, Project_ManagementDayandTime3, 
                    Project_ManagementEmployeeSign3, Project_ManagementProcessOwnerSign3, Engineering_DayandTime4, 
                    Engineering_EmployeeSign4, Engineering_ProcessOwnerSign4, SIBM_DayandTime5, SIBM_EmployeeSign5, 
                    SIBM_ProcessOwnerSign5, Procurement_DayandTime6, Procurement_EmployeeSign6, Procurement_ProcessOwnerSign6, 
                    Proposal_ServiceDayandTime7, Proposal_ServiceEmployeeSign7, Proposal_ServiceProcessOwnerSign7, 
                    Refractory_DayandTime8, Refractory_EmployeeSign8, Refractory_ProcessOwnerSign8, PMO_DayandTime9, 
                    PMO_EmployeeSign9, PMO_ProcessOwnerSign9, IT_DayandTime10, IT_EmployeeSign10, IT_ProcessOwnerSign10, 
                    Employee_FeedbacK, Employee_Signature, Date1, Date2
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (
                    Employee_name, Employee_ID, Department, Joining_Date, Designation, HRorAdminDayandTime, 
                    HRorAdminEmployeeSign, HRorAdminProcessOwnerSign, Quality_EngineeringDayandTime1, 
                    Quality_EngineeringEmployeeSign1, Quality_EngineeringProcessOwnerSign1, Finance_ControlDayandTime2, 
                    Finance_ControlEmployeeSign2, Finance_ControlProcessOwnerSign2, Project_ManagementDayandTime3, 
                    Project_ManagementEmployeeSign3, Project_ManagementProcessOwnerSign3, Engineering_DayandTime4, 
                    Engineering_EmployeeSign4, Engineering_ProcessOwnerSign4, SIBM_DayandTime5, SIBM_EmployeeSign5, 
                    SIBM_ProcessOwnerSign5, Procurement_DayandTime6, Procurement_EmployeeSign6, Procurement_ProcessOwnerSign6, 
                    Proposal_ServiceDayandTime7, Proposal_ServiceEmployeeSign7, Proposal_ServiceProcessOwnerSign7, 
                    Refractory_DayandTime8, Refractory_EmployeeSign8, Refractory_ProcessOwnerSign8, PMO_DayandTime9, 
                    PMO_EmployeeSign9, PMO_ProcessOwnerSign9, IT_DayandTime10, IT_EmployeeSign10, IT_ProcessOwnerSign10, 
                    Employee_FeedbacK, Employee_Signature, Date1, Date2
                )
            )
            con.commit()
            cur.close()
            con.close()
            return "Data inserted successfully"
        except Exception as e:
            return str(e)
        



@app.route('/EmployeeOboarding')
def EmployeeOboarding():
    return render_template("Employee Onboarding Checklist Form.html")


@app.route("/EmployeeOboardinginsert", methods=['POST', 'GET'])
def EmployeeOboardinginsert():
    if request.method == 'POST':
        Form_No = request.form["Form_No"]
        Date_of_Issue = request.form["Date_of_Issue"]
        Revision = request.form["Revision"]
        Approved_by = request.form["Approved_by"] 
        
        Resume = request.form.get('Resume', False)=='on'
        if Resume:
            Resume_Field = 1
        else:
            Resume_Field = 0
            
        Employee_Information_Form = request.form.get('Employee_Information_Form', False)=='on'
        if Employee_Information_Form:
            
            Employee_Information_Form_Field = 1 
        else:
            Employee_Information_Form_Field = 0
    
        
        Educational_Certificate = request.form.get('Educational_Certificate', False)=='on'
        if Educational_Certificate:
             Educational_Certificate_Field = 1  # yes
        else:
            Educational_Certificate_Field = 0   # No
        
        Relieving_Certificates_of_last_2_organizations = request.form.get('Relieving_Certificates_of_last_2_organizations', False)=='on'
        if Relieving_Certificates_of_last_2_organizations:
              Relieving_Certificates_of_last_2_organizations_Field = 1  # yes
        else:
             Relieving_Certificates_of_last_2_organizations_Field = 0   # No
        
        Salary_Slips_of_last_3_months = request.form.get('Salary_Slips_of_last_3_months', False)=='on'
        if Salary_Slips_of_last_3_months:
              Salary_Slips_of_last_3_months_Field = 1  # yes
        else:
             Salary_Slips_of_last_3_months_Field = 0   # No
             
        Form_16_If_applicable = request.form.get('Form_16_If_applicable', False)=='on'
        if Form_16_If_applicable:
              Form_16_If_applicable_Field = 1  # yes
        else:
             Form_16_If_applicable_Field = 0   # No
             
        Pan_Card_Mandatory = request.form.get('Pan_Card_Mandatory', False)=='on'
        if Pan_Card_Mandatory:
              Pan_Card_Mandatory_Field = 1  # yes
        else:
             Pan_Card_Mandatory_Field = 0   # No
             
             
             
        Photo_ID_Proof_Voter_Aadhar_Card_Passport_etc = request.form.get('Photo_ID_Proof_Voter_Aadhar_Card_Passport_etc', False)=='on'
        if Photo_ID_Proof_Voter_Aadhar_Card_Passport_etc:
             Photo_ID_Proof_Voter_Aadhar_Card_Passport_etc_Field = 1  # yes
        else:
             Photo_ID_Proof_Voter_Aadhar_Card_Passport_etc_Field = 0   # No
             
        
        Passport_size_Photo = request.form.get('Passport_size_Photo', False)=='on'
        if Passport_size_Photo:
             Passport_size_Photo_Field = 1  # yes
        else:
             Passport_size_Photo_Field = 0   # No
             
        Permanent_Mandatory = request.form.get('Permanent_Mandatory', False)=='on'
        if Permanent_Mandatory:
             Permanent_Mandatory_Field = 1  # yes
        else:
             Permanent_Mandatory_Field = 0   # No
        
        Bank_Aorc_Opening_Form_and_Formalities = request.form.get('Bank_Aorc_Opening_Form_and_Formalities', False)=='on'
        if Bank_Aorc_Opening_Form_and_Formalities:
             Bank_Aorc_Opening_Form_and_Formalitiesy_Field = 1  # yes
        else:
             Bank_Aorc_Opening_Form_and_Formalities_Field = 0   # No
        
        Current_Address_Proof = request.form.get('Current_Address_Proof', False)=='on'
        if Current_Address_Proof:
             Current_Address_Proof_Field = 1  # yes
        else:
             Current_Address_Proof_Field = 0   # No
             
        NDAorService_Agreement = request.form.get('NDAorService_Agreement', False)=='on'
        if NDAorService_Agreement:
             NDAorService_Agreement_Field = 1  # yes
        else:
             NDAorService_Agreement_Field = 0   # No
        
        Entry_in_Keka = request.form.get('Entry_in_Keka', False)=='on'
        if Entry_in_Keka:
             Entry_in_Keka_Field = 1  # yes
        else:
             Entry_in_Keka_Field = 0   # No
        
        Appointment_Letter = request.form.get('Appointment_Letter', False)=='on'
        if Appointment_Letter:
             Appointment_Letter_Field = 1  # yes
        else:
             Appointment_Letter_Field = 0   # No
        
        Entry_in_Dax360 = request.form.get('Entry_in_Dax360', False)=='on'
        if Entry_in_Dax360:
             Entry_in_Dax360_Field = 1  # yes
        else:
             Entry_in_Dax360_Field = 0   # No
        
        Entry_in_Meytou = request.form.get('Entry_in_Meytou', False)=='on'
        if Entry_in_Meytou:
             Entry_in_Meytou_Field = 1  # yes
        else:
             Entry_in_Meytou_Field = 0   # No
        
        Indirect_ariff = request.form.get('Indirect_ariff', False)=='on'
        if Indirect_ariff:
             Indirect_ariff_Field = 1  # yes
        else:
             Indirect_ariff_Field = 0   # No
        
        Stationary_Notepad_and_Pen = request.form.get('Stationary_Notepad_and_Pen', False)=='on'
        if Stationary_Notepad_and_Pen:
             Stationary_Notepad_and_Pen_Field = 1  # yes
        else:
             Stationary_Notepad_and_Pen_Field = 0   # No
        
        Employee_ID_Card = request.form.get('Employee_ID_Card', False)=='on'
        if Employee_ID_Card:
             Employee_ID_Card_Field = 1  # yes
        else:
             Employee_ID_Card_Field = 0   # No
        
        Extension_list = request.form.get('Extension_list', False)=='on'
        if Extension_list:
             Extension_list_Field = 1  # yes
        else:
             Extension_list_Field = 0   # No
        
        Visiting_Cards_if_pplicable = request.form.get('Visiting_Cards_if_pplicable', False)=='on'
        if Visiting_Cards_if_pplicable:
             Visiting_Cards_if_pplicable_Field = 1  # yes
        else:
             Visiting_Cards_if_pplicable_Field = 0   # No
        
        
        Adhaar_Card_Copy = request.form.get('Adhaar_Card_Copy', False)=='on'
        if Adhaar_Card_Copy:
             Adhaar_Card_Copy_Field = 1  # yes
        else:
             Adhaar_Card_Copy_Field = 0   # No
        
        Appointment_Letter_Copy = request.form.get('Appointment_Letter_Copy', False)=='on'
        if Appointment_Letter_Copy:
             Appointment_Letter_Copy_Field = 1  # yes
        else:
             Appointment_Letter_Copy_Field = 0   # No
        
        Nomination_Letter = request.form.get('Nomination_Letter', False)=='on'
        if Nomination_Letter:
             Nomination_Letter_Field = 1  # yes
        else:
             Nomination_Letter_Field = 0   # No
        
        
        Universal_Account_Number_UAN = request.form.get('Universal_Account_Number_UAN', False)=='on'
        if Universal_Account_Number_UAN:
            Universal_Account_Number_UAN_Field = 1  # yes
        else:
             Universal_Account_Number_UAN_Field = 0   # No
        
        
        Provident_Fund_Account_Number_PF = request.form.get('Provident_Fund_Account_Number_PF', False)=='on'
        if Provident_Fund_Account_Number_PF:
            Provident_Fund_Account_Number_PF_Field = 1  # yes
        else:
             Provident_Fund_Account_Number_PF_Field = 0   # No
        
        
        
        Bank_Account_No_and_Name = request.form.get('Bank_Account_No_and_Name', False)=='on'
        if Bank_Account_No_and_Name:
             Bank_Account_No_and_Name_Field = 1  # yes
        else:
             Bank_Account_No_and_Name_Field = 0   # No
        
        
        
        PAN_Card_Copy = request.form.get('PAN_Card_Copy', False)=='on'
        if PAN_Card_Copy:
             PAN_Card_Copy_Field = 1  # yes
        else:
             PAN_Card_Copy_Field = 0   # No
        
        Seating_Arrangement = request.form.get('Seating_Arrangement', False)=='on'
        if Seating_Arrangement:
             Seating_Arrangement_Field = 1  # yes
        else:
             Seating_Arrangement_Field = 0   # No
        
        
        
        Laptopa_and_Desktop_and_Accessories = request.form.get('Laptopa_and_Desktop_and_Accessories', False)=='on'
        if Laptopa_and_Desktop_and_Accessories:
             Laptopa_and_Desktop_and_Accessories_Field = 1  # yes
        else:
             Laptopa_and_Desktop_and_Accessories_Field = 0   # No
        
        
        Phone_Extension = request.form.get('Phone_Extension', False)=='on'
        if Phone_Extension:
           Phone_Extension_Field = 1
        else:
            Phone_Extension_Field = 0
        
        Official_Email_ID_Creation = request.form.get('Official_Email_ID_Creation', False)=='on'
        if Official_Email_ID_Creation:
           Official_Email_ID_Creation_Field = 1
        else:
            Official_Email_ID_Creation_Field = 0
            
            
            
        Group_and_Location_Email_Alias = request.form.get('Group_and_Location_Email_Alias', False)=='on'
        if Group_and_Location_Email_Alias:
            Group_and_Location_Email_Alias_Field = 1
        else:
            Group_and_Location_Email_Alias_Field = 0
            
        Sim_Card = request.form.get('Sim_Card', False)=='on'
        if Sim_Card:
            Sim_Card_Field = 1
        else:
            Sim_Card_Field = 0
        
        Head_Phone = request.form.get('Head_Phone', False)=='on'
        if Head_Phone:
            Head_Phone_Field = 1
        else:
            Head_Phone_Field = 0
        Screen = request.form.get('Screen' , False)=='on'
        if Screen:
            Screen_Field = 1
        else:
            Screen_Field = 0
        
        
        Employee_Access_Card_and_Biometrix_Access = request.form.get('Employee_Access_Card_and_Biometrix_Access', False)=='on'
        if Employee_Access_Card_and_Biometrix_Access:
            Employee_Access_Card_and_Biometrix_Access_Field = 1
        else:
            Employee_Access_Card_and_Biometrix_Access_Field = 0
        
        
        Insurance_Form = request.form.get('Insurance_Form', False)=='on'
        if Insurance_Form:
            Insurance_Form_Field = 1
        else:
            Insurance_Form_Field = 0
        
        Insurance_Form1 = request.form.get('Insurance_Form1', False)=='on' 
        if Insurance_Form1:
            Insurance_Form1_Field = 1
        else:
            Insurance_Form1_Field = 0
        try:
            # mysql = MySQL(app)
            con = mysql.connect()
            # con = mysql.connector.connect(host="localhost", user="root", password="", database="providentfundsandfurnishing")
            cur = con.cursor()
            cur.execute("""
                INSERT INTO employeeoboarding (
                    Form_No, Date_of_Issue, Revision, Approved_by, Resume,
                    Employee_Information_Form, Educational_Certificate,
                    Relieving_Certificates_of_last_2_organizations, Salary_Slips_of_last_3_months,
                    Form_16_If_applicable, Pan_Card_Mandatory, Photo_ID_Proof_Voter_Aadhar_Card_Passport_etc, 
                    Passport_size_Photo, Permanent_Mandatory, Bank_Aorc_Opening_Form_and_Formalities,
                    Current_Address_Proof, NDAorService_Agreement, Entry_in_Keka,
                    Appointment_Letter, Entry_in_Dax360, Entry_in_Meytou,
                    Indirect_ariff, Stationary_Notepad_and_Pen, Employee_ID_Card,
                    Extension_list, Visiting_Cards_if_pplicable, Adhaar_Card_Copy,
                    Appointment_Letter_Copy, Nomination_Letter, Universal_Account_Number_UAN,
                    Provident_Fund_Account_Number_PF, Bank_Account_No_and_Name, PAN_Card_Copy,
                    Seating_Arrangement, Laptopa_and_Desktop_and_Accessories, Phone_Extension,
                    Official_Email_ID_Creation, Group_and_Location_Email_Alias, Sim_Card,
                    Head_Phone, Screen, Employee_Access_Card_and_Biometrix_Access,
                    Insurance_Form, Insurance_Form1
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s
                
                )
            """, (
                Form_No, Date_of_Issue, Revision, Approved_by,Resume_Field,
                Employee_Information_Form_Field, Educational_Certificate_Field,
                Relieving_Certificates_of_last_2_organizations_Field,
                Salary_Slips_of_last_3_months_Field,Form_16_If_applicable_Field, Pan_Card_Mandatory_Field,
                Photo_ID_Proof_Voter_Aadhar_Card_Passport_etc_Field, Passport_size_Photo_Field,
                Permanent_Mandatory_Field, Bank_Aorc_Opening_Form_and_Formalities_Field,
                Current_Address_Proof_Field, NDAorService_Agreement_Field, Entry_in_Keka_Field,
                Appointment_Letter_Field, Entry_in_Dax360_Field, Entry_in_Meytou_Field,
                Indirect_ariff_Field, Stationary_Notepad_and_Pen_Field, Employee_ID_Card_Field,
                Extension_list_Field, Visiting_Cards_if_pplicable_Field, Adhaar_Card_Copy_Field,
                Appointment_Letter_Copy_Field, Nomination_Letter_Field, Universal_Account_Number_UAN_Field,
                Provident_Fund_Account_Number_PF_Field, Bank_Account_No_and_Name_Field, PAN_Card_Copy_Field,
                Seating_Arrangement_Field, Laptopa_and_Desktop_and_Accessories_Field, Phone_Extension_Field,
                Official_Email_ID_Creation_Field, Group_and_Location_Email_Alias_Field, Sim_Card_Field,
                Head_Phone, Screen_Field, Employee_Access_Card_and_Biometrix_Access_Field,
                Insurance_Form_Field, Insurance_Form1_Field
                
                
                
                # Relieving_Certificates_of_last_2_organizations, Salary_Slips_of_last_3_months,
                # Form_16_If_applicable, Pan_Card_Mandatory,
                # Photo_ID_Proof_Voter_Aadhar_Card_Passport_etc, Passport_size_Photo,
                # Permanent_Mandatory, Bank_Aorc_Opening_Form_and_Formalities,
                # Current_Address_Proof, NDAorService_Agreement, Entry_in_Keka,
                # Appointment_Letter, Entry_in_Dax360, Entry_in_Meytou,
                # Indirect_ariff, Stationary_Notepad_and_Pen, Employee_ID_Card,
                # Extension_list, Visiting_Cards_if_pplicable, Adhaar_Card_Copy,
                # Appointment_Letter_Copy, Nomination_Letter, Universal_Account_Number_UAN,
                # Provident_Fund_Account_Number_PF, Bank_Account_No_and_Name, PAN_Card_Copy,
                # Seating_Arrangement, Laptopa_and_Desktop_and_Accessories, Phone_Extension,
                # Official_Email_ID_Creation, Group_and_Location_Email_Alias, Sim_Card,
                # Head_Phone, Screen, Employee_Access_Card_and_Biometrix_Access,
                # Insurance_Form, Insurance_Form1
            ))
          
            con.commit()
           
            cur.close()
            con.close()
            return "Data inserted successfully"
        except Exception as e:
            return str(e)


if __name__ == '__main__':
    app.run(debug=True)
