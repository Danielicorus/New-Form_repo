from flask import Flask, render_template, request ,redirect
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''  # Replace with your MySQL password
app.config['MYSQL_DATABASE_DB'] = 'providentfundsandfurnishing'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

con = mysql.connect()
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS providentfund (id INT AUTO_INCREMENT PRIMARY KEY, mr_ms_mrs text, name text, dateofbirth date, fatherandhusband text, relationinrespect text, gender text, mobilenumber integer, email text, emppovidentfunds text, emppensionscheme text, uaborprevious text, account text, dateofexit date, certificateissued text, pensionpayment text, internationworker text, india text, otherthanindia text, passport text,  passportfrom date , passportto date, educationalqualification text, maritalstatus varchar(225), specially varchar(225), category varchar(225), bankkycnumber text, banknumber text, bankremark text, nprkycnumber text, nprnumber text, nprremark text, permanentkycnumber text, permanentnumber text,  permanentremark text, passportkycnumber text, passportnumber text, passportremark text, drivinglicencekycnumber text, drivinglicencenumber text , drivinglicenceremark text, electioncardkycnumber text, electioncardnumber text, electioncardremark text,  rationcardkycnumber text, rationcardnumber text, rationcardremark text, esiccardkycnumber text, esiccardnumber text, esiccardremark text)")
cur.execute("CREATE TABLE IF NOT EXISTS newjoiningforminsurance (id INT AUTO_INCREMENT PRIMARY KEY, Name text, Designation text, PresentAddress text, PermanentAddress text, Namefather text, NameMother text, PAN text, DateJoining date, DateBirth date, personalmobile text, personalemail text, Department text, Location text, MaritalStatus text, EPFNOwithPreviousEmployer text, nameofSpouseandChildren text, Relationship text, DateofBirth date, nameofSpouseandChildren1 text, Relationship1 text, DateofBirth1 date, nameofSpouseandChildren2 text, Relationship2 text, DateofBirth2 text, nameofSpouseandChildren3 text, Relationship3 text, DateofBirth3 date)")
cur.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY , username text , password text)")
cur.execute("CREATE TABLE IF NOT EXISTS admin (id INT AUTO_INCREMENT PRIMARY KEY , HRADMIN text , passwords text)")
cur.execute("CREATE TABLE IF NOT EXISTS informationform (id INT AUTO_INCREMENT PRIMARY KEY , first_name text, middle_name text, surname text, employee_code text, reporting_manager text, department text, permanent_address text, PostalCodeorPinCode text, Present_Address text, dateofbirth date, sex text, birthplace text, bloodgroup text, nationality text, religion text,  pan text, language varchar(225), maritalstatus varchar(225), marriage_date date, spouse_name text, spouse_dob date, children_count text, first_child_name text, first_child_dob date,  second_child_name text, second_child_dob date, third_child_name text,  third_child_dob date, contact_number text,  mobile_number text, emergency_contact text, email_id text, SSCName text, SSCSpecialization text, SSCSPassingYearMonth text, SSCPercentage text, SSCGrade text, HSCName text, HSCSpecialization text,    HSCPassingYearMonth text, HSCPercentage text , HSCGrade text, GraduationName text, GraduationSpecialization text,   GraduationPassingYearMonth text, GraduationPercentage text, GraduationGrade text, DiplomaName text, DiplomaSpecialization text, DiplomaPassingYearMonth text, DiplomaPercentage text, DiplomaGrade text, DegreeName text, DegreeSpecialization text,  DegreePassingYearMonth text, DegreePercentage text, DegreeGrade text, MastersorPostGraduationName text , MastersorPostGraduationSpecialization text,  MastersorPostGraduationPassingYearMonth text, MastersorPercentage text, MastersorGrade text, DoctorateName text, DoctorateSpecialization text,  DoctoratePassingYearMonth text, DoctoratePercentage text, DoctorateGrade text, OthersName text, OthersSpecialization text,   OthersPassingYearMonth text,  OthersPercentage text, OthersGrade text, aOrganization text, aDesignation text, aLocation text, aDurationfrom date, aDurationto date, bOrganization text, bDesignation text, bLocation text, bDurationfrom date, bDurationto date, cOrganization text, cDesignation text, cLocation text, cDurationfrom date, cDurationto date, dOrganization text, dDesignation text, dLocation text, dDurationfrom date, dDurationto date, eOrganization text, eDesignation text, eLocation text, eDurationfrom date, eDurationto date, todaydate date)")
cur.execute("CREATE TABLE IF NOT EXISTS inductionforminsurance (id INT AUTO_INCREMENT PRIMARY KEY ,Employee_name text, Employee_ID text, Department text, Joining_Date date, Designation text, HRorAdminDayandTime date, HRorAdminEmployeeSign varchar(225), HRorAdminProcessOwnerSign varchar(225), HRorAdminDayandTime1 date, HRorAdminEmployeeSign1 varchar(225), HRorAdminProcessOwnerSign1 varchar(225),  HRorAdminDayandTime2 date, HRorAdminEmployeeSign2 varchar(225), HRorAdminProcessOwnerSign2 varchar(225), HRorAdminDayandTime3 date, HRorAdminEmployeeSign3 varchar(225), HRorAdminProcessOwnerSign3 varchar(225), HRorAdminDayandTime4 date, HRorAdminEmployeeSign4 varchar(225), HRorAdminProcessOwnerSign4 varchar(225), HRorAdminDayandTime5 date, HRorAdminEmployeeSign5 varchar(225), HRorAdminProcessOwnerSign5 varchar(225), HRorAdminDayandTime6 date, HRorAdminEmployeeSign6 varchar(225), HRorAdminProcessOwnerSign6 varchar(225), HRorAdminDayandTime7 date, HRorAdminEmployeeSign7 varchar(225), HRorAdminProcessOwnerSign7 varchar(225), HRorAdminDayandTime8 date, HRorAdminEmployeeSign8 varchar(225), HRorAdminProcessOwnerSign8 varchar(225), HRorAdminDayandTime9 date, HRorAdminEmployeeSign9 varchar(225), HRorAdminProcessOwnerSign9 varchar(225), HRorAdminDayandTime10 date, HRorAdminEmployeeSign10 varchar(225), HRorAdminProcessOwnerSign10 varchar(225), Employee_FeedbacK text , Employee_Signature text, Date1 date, Date2 date)")
cur.execute("CREATE TABLE IF NOT EXISTS employeeOboarding (id INT AUTO_INCREMENT PRIMARY KEY, Form_No text, Date_of_Issue date, Revision text, Approved_by text, Resume BOOLEAN, Employee_Information_Form  BOOLEAN, Educational_Certificate BOOLEAN,  Relieving_Certificates_of_last_2_organizations BOOLEAN, Salary_Slips_of_last_3_months  BOOLEAN, Form_16_If_applicable BOOLEAN, Pan_Card_Mandatory BOOLEAN, Photo_ID_Proof_Voter_Aadhar_Card_Passport_etc BOOLEAN, Passport_size_Photo BOOLEAN, Permanent_Mandatory BOOLEAN, Bank_Aorc_Opening_Form_and_Formalities BOOLEAN, Current_Address_Proof  BOOLEAN, NDAorService_Agreement  BOOLEAN,  Entry_in_Keka BOOLEAN,  Appointment_Letter  BOOLEAN, Entry_in_Dax360  BOOLEAN, Entry_in_Meytou BOOLEAN, Indirect_ariff BOOLEAN, Stationary_Notepad_and_Pen BOOLEAN,  Employee_ID_Card  BOOLEAN, Extension_list  BOOLEAN,   Visiting_Cards_if_pplicable  BOOLEAN,  Adhaar_Card_Copy BOOLEAN, Appointment_Letter_Copy BOOLEAN, Nomination_Letter  BOOLEAN, Universal_Account_Number_UAN  BOOLEAN, Provident_Fund_Account_Number_PF  BOOLEAN, Bank_Account_No_and_Name  BOOLEAN, PAN_Card_Copy BOOLEAN, Seating_Arrangement  BOOLEAN, Laptopa_and_Desktop_and_Accessories  BOOLEAN, Phone_Extension  BOOLEAN, Official_Email_ID_Creation BOOLEAN, Group_and_Location_Email_Alias BOOLEAN, Sim_Card  BOOLEAN,  Head_Phone BOOLEAN, Screen BOOLEAN,  Employee_Access_Card_and_Biometrix_Access BOOLEAN,  Insurance_Form BOOLEAN, Insurance_Form1 BOOLEAN)")
con.commit()
cur.close()
con.close()

@app.route('/')
def index():
    return render_template("userandadmin.html")

@app.route('/logins')
def logins():
    return render_template("loginpage.html")



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
                return "Login failed. Please check your username and password."
        except mysql.connector.Error as err:
            return f"MySQL Error: {err}"
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return render_template("loginadmin.html")


@app.route('/homepages')
def homepages():
    return render_template("HRadmin.html")

@app.route('/showusers')
def showusers():
     con = mysql.connect()
     cur=con.cursor()
     cur.execute("SELECT * from users")
     data = cur.fetchall()
     return render_template("managemployee.html" , data=data)


    

@app.route('/signup')
def signup():
    return render_template("signup.html")


    


        





@app.route('/homepage')
def homepage():
    return render_template("homepage.html")  

@app.route('/form')
def form():
    return render_template("form11.html")

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
            educationalqualification = request.form.get('educationalqualification')
            maritalstatus = request.form.get('maritalstatus')
            specially = request.form.get('specially')
            abled =request.form.get('abled')  # Convert list to string
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
        rationcardnumber, rationcardremark, esiccardkycnumber, esiccardnumber, esiccardremark
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s
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
    esiccardremark
))

            con.commit()
            return 'User added successfully!'

    else: return 'fail'
    return redirect('/')

@app.route('/forms')
def forms():
    return render_template("form12.html")

@app.route('/informationform')
def informationform():
    return render_template("informationform.html")


@app.route('/informationforminsert', methods=['POST' , 'GET'])
def informationforminsert():
    if request.method == 'POST':
        # Collecting form data
        first_name = request.form["first_name"]
        middle_name = request.form["middle_name"]
        surname = request.form["surname"]
        employee_code = request.form["employee_code"]
        reporting_manager = request.form["reporting_manager"]
        department = request.form["department"]
        permanent_address = request.form["permanent_address"]
        PostalCodeorPinCode = request.form["PostalCodeorPinCode"]
        Present_Address = request.form.get("Present_Address")
        dateofbirth = request.form["dateofbirth"]
        sex = request.form["sex"]
        birthplace = request.form["birthplace"]
        bloodgroup = request.form["bloodgroup"]
        nationality = request.form["nationality"]
        religion = request.form["religion"]
        pan = request.form["pan"]
        language = request.form.get("language")
        maritalstatus = request.form.get("maritalstatus")
        marriage_date = request.form["marriage_date"]
        spouse_name = request.form["spouse_name"]
        spouse_dob = request.form["spouse_dob"]
        children_count = request.form["children_count"]
        first_child_name = request.form["first_child_name"]
        first_child_dob = request.form["first_child_dob"]
        second_child_name = request.form["second_child_name"]
        second_child_dob = request.form["second_child_dob"]
        third_child_name = request.form["third_child_name"]
        third_child_dob = request.form["third_child_dob"]
        contact_number = request.form["contact_number"]
        mobile_number = request.form["mobile_number"]
        emergency_contact = request.form["emergency_contact"]
        email_id = request.form["email_id"]
        SSCName = request.form["SSCName"]
        SSCSpecialization = request.form["SSCSpecialization"]
        SSCSPassingYearMonth = request.form["SSCSPassingYearMonth"]
        SSCPercentage = request.form["SSCPercentage"]
        SSCGrade = request.form["SSCGrade"]
        HSCName = request.form["HSCName"]
        HSCSpecialization = request.form["HSCSpecialization"]
        HSCPassingYearMonth = request.form["HSCPassingYearMonth"]
        HSCPercentage = request.form["HSCPercentage"]
        HSCGrade = request.form["HSCGrade"]
        GraduationName = request.form["GraduationName"]
        GraduationSpecialization = request.form["GraduationSpecialization"]
        GraduationPassingYearMonth = request.form["GraduationPassingYearMonth"]
        GraduationPercentage = request.form["GraduationPercentage"]
        GraduationGrade = request.form["GraduationGrade"]
        DiplomaName = request.form["DiplomaName"]
        DiplomaSpecialization = request.form["DiplomaSpecialization"]
        DiplomaPassingYearMonth = request.form["DiplomaPassingYearMonth"]
        DiplomaPercentage = request.form["DiplomaPercentage"]
        DiplomaGrade = request.form["DiplomaGrade"]
        DegreeName = request.form["DegreeName"]
        DegreeSpecialization = request.form["DegreeSpecialization"]
        DegreePassingYearMonth = request.form["DegreePassingYearMonth"]
        DegreePercentage = request.form["DegreePercentage"]
        DegreeGrade = request.form["DegreeGrade"]
        MastersorPostGraduationName = request.form["MastersorPostGraduationName"]
        MastersorPostGraduationSpecialization = request.form["MastersorPostGraduationSpecialization"]
        MastersorPostGraduationPassingYearMonth = request.form["MastersorPostGraduationPassingYearMonth"]
        MastersorPercentage = request.form["MastersorPercentage"]
        MastersorGrade = request.form["MastersorGrade"]
        DoctorateName = request.form["DoctorateName"]
        DoctorateSpecialization = request.form["DoctorateSpecialization"]
        DoctoratePassingYearMonth = request.form["DoctoratePassingYearMonth"]
        DoctoratePercentage = request.form["DoctoratePercentage"]
        DoctorateGrade = request.form["DoctorateGrade"]
        OthersName = request.form["OthersName"]
        OthersSpecialization = request.form["OthersSpecialization"]
        OthersPassingYearMonth = request.form["OthersPassingYearMonth"]
        OthersPercentage = request.form["OthersPercentage"]
        OthersGrade = request.form["OthersGrade"]
        aOrganization = request.form["aOrganization"]
        aDesignation = request.form["aDesignation"]
        aLocation = request.form["aLocation"]
        aDurationfrom = request.form["aDurationfrom"]
        aDurationto = request.form["aDurationto"]
        bOrganization = request.form.get("bOrganization")
        bDesignation = request.form["bDesignation"]
        bLocation = request.form["bLocation"]
        bDurationfrom = request.form["bDurationfrom"]
        bDurationto = request.form["bDurationto"]
        cOrganization = request.form["cOrganization"]
        cDesignation = request.form["cDesignation"]
        cLocation = request.form["cLocation"]
        cDurationfrom = request.form["cDurationfrom"]
        cDurationto = request.form["cDurationto"]
        dOrganization = request.form["dOrganization"]
        dDesignation = request.form["dDesignation"]
        dLocation = request.form["dLocation"]
        dDurationfrom = request.form["dDurationfrom"]
        dDurationto = request.form["dDurationto"]
        eOrganization = request.form["eOrganization"]
        eDesignation = request.form["eDesignation"]
        eLocation = request.form["eLocation"]
        eDurationfrom = request.form["eDurationfrom"]
        eDurationto = request.form["eDurationto"]
        todaydate = request.form["todaydate"]

        try:
            con = mysql.connect()
            cur = con.cursor()
            cur.execute(
                """INSERT INTO informationform (
                    first_name, middle_name, surname, employee_code, reporting_manager, department, 
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
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                )""",
                (
                    first_name, middle_name, surname, employee_code, reporting_manager, department,
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
        
        
@app.route('/inductionform')
def inductionform():
    return render_template("induction.html")


# @app.route('/inductioninserts', methods=['POST'])
# def inductioninserts():
#     if request.method=='POST':
#         Employee_name=request.form["Employee_name"]
#         Employee_name=request.form["Employee_name"]
#         Employee_name=request.form["Employee_name"]
#         Employee_name=request.form["Employee_name"]
#         Employee_name=request.form["Employee_name"]
#         Employee_name=request.form["Employee_name"]
#         Employee_name=request.form["Employee_name"]
#         Employee_name=request.form["Employee_name"]
#         Employee_name=request.form["Employee_name"]
#         Employee_name=request.form["Employee_name"]
#         Employee_name=request.form["Employee_name"]
#         Employee_name=request.form["Employee_name"]
#         Employee_name=request.form["Employee_name"]
#         Employee_name=request.form["Employee_name"]
#         Employee_name=request.form["Employee_name"]
#         Employee_name=request.form["Employee_name"]
#         Employee_name=request.form["Employee_name"]



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
        Resume = request.form.get("Resume", "off")=="on"
        Employee_Information_Form = request.form.get("Employee_Information_Form", "off")=="on"
        Educational_Certificate = request.form.get("Educational_Certificate", "off")=="on"
        Relieving_Certificates_of_last_2_organizations = request.form.get("Relieving_Certificates_of_last_2_organizations", "off")=="on"
        Salary_Slips_of_last_3_months = request.form.get("Salary_Slips_of_last_3_months", "off")=="on"
        Form_16_If_applicable = request.form.get("Form_16_If_applicable", "off")=="on"
        Pan_Card_Mandatory = request.form.get("Pan_Card_Mandatory", "off")=="on"
        Photo_ID_Proof_Voter_Aadhar_Card_Passport_etc = request.form.get("Photo_ID_Proof_Voter_Aadhar_Card_Passport_etc", "off")=="on"
        Passport_size_Photo = request.form.get("Passport_size_Photo", "off")=="on"
        Permanent_Mandatory = request.form.get("Permanent_Mandatory", "off")=="on"
        Bank_Aorc_Opening_Form_and_Formalities = request.form.get("Bank_Aorc_Opening_Form_and_Formalities", "off")=="on"
        Current_Address_Proof = request.form.get("Current_Address_Proof", "off")=="on"
        NDAorService_Agreement = request.form.get("NDAorService_Agreement", "off")=="on"
        Entry_in_Keka = request.form.get("Entry_in_Keka", "off")=="on"
        Appointment_Letter = request.form.get("Appointment_Letter", "off")=="on"
        Entry_in_Dax360 = request.form.get("Entry_in_Dax360", "off")=="on"
        Entry_in_Meytou = request.form.get("Entry_in_Meytou", "off")=="on"
        Indirect_ariff = request.form.get("Indirect_ariff", "off")=="on"
        Stationary_Notepad_and_Pen = request.form.get("Stationary_Notepad_and_Pen", "off")=="on"
        Employee_ID_Card = request.form.get("Employee_ID_Card", "off")=="on"
        Extension_list = request.form.get("Extension_list", "off")=="on"
        Visiting_Cards_if_pplicable = request.form.get("Visiting_Cards_if_pplicable", "off")=="on"
        Adhaar_Card_Copy = request.form.get("Adhaar_Card_Copy", "off")=="on"
        Appointment_Letter_Copy = request.form.get("Appointment_Letter_Copy", "off")=="on"
        Nomination_Letter = request.form.get("Nomination_Letter", "off")=="on"
        Universal_Account_Number_UAN = request.form.get("Universal_Account_Number_UAN", "off")=="on"
        Provident_Fund_Account_Number_PF = request.form.get("Provident_Fund_Account_Number_PF", "off")=="on"
        Bank_Account_No_and_Name = request.form.get("Bank_Account_No_and_Name", "off")=="on"
        PAN_Card_Copy = request.form.get("PAN_Card_Copy", "off")=="on"
        Seating_Arrangement = request.form.get("Seating_Arrangement", "off")=="on"
        Laptopa_and_Desktop_and_Accessories = request.form.get("Laptopa_and_Desktop_and_Accessories", "off")=="on"
        Phone_Extension = request.form.get("Phone_Extension", "off")=="on"
        Official_Email_ID_Creation = request.form.get("Official_Email_ID_Creation", "off")=="on"
        Group_and_Location_Email_Alias = request.form.get("Group_and_Location_Email_Alias", "off")=="on"
        Sim_Card = request.form.get("Sim_Card", "off")=="on"
        Head_Phone = request.form.get("Head_Phone", "off")=="on"
        Screen = request.form.get("Screen" , "off")=="on"
        Employee_Access_Card_and_Biometrix_Access = request.form.get("Employee_Access_Card_and_Biometrix_Access", "off")=="on"
        Insurance_Form = request.form.get("Insurance_Form", "off")=="on"
        Insurance_Form1 = request.form.get("Insurance_Form1", "off")=="on"

        try:
            con = mysql.connect()
            cur = con.cursor()
            cur.execute("""
                INSERT INTO employeeOnboarding (
                    Form_No, Date_of_Issue, Revision, Approved_by, Resume,
                    Employee_Information_Form, Educational_Certificate,
                    Relieving_Certificates_of_last_2_organizations, Salary_Slips_of_last_3_months,
                    Form_16_If_applicable, Pan_Card_Mandatory,
                    Photo_ID_Proof_Voter_Aadhar_Card_Passport_etc, Passport_size_Photo,
                    Permanent_Mandatory, Bank_Aorc_Opening_Form_and_Formalities,
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
                    %s, %s, %s, %s, %s,%s
                )
            """, (
                Form_No, Date_of_Issue, Revision, Approved_by, Resume,
                Employee_Information_Form, Educational_Certificate,
                Relieving_Certificates_of_last_2_organizations, Salary_Slips_of_last_3_months,
                Form_16_If_applicable, Pan_Card_Mandatory,
                Photo_ID_Proof_Voter_Aadhar_Card_Passport_etc, Passport_size_Photo,
                Permanent_Mandatory, Bank_Aorc_Opening_Form_and_Formalities,
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
            ))
            con.commit()
            cur.close()
            con.close()
            return "Data inserted successfully"
        except Exception as e:
            return str(e)




    


        
        

        
        
        
    

            

if __name__ == '__main__':
    app.run(debug=True)
