import express from "express";
import mysql from "mysql";
import dotenv from "dotenv";
import path from "path";
import { fileURLToPath } from "url";
import bodyParser from "body-parser";
import multer from "multer";
import session from "express-session";



dotenv.config({ path: './.env' });


const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const port = 3000;

// Set up MySQL connection
const db = mysql.createConnection({
    host: process.env.DATABASE_HOST,
    user: process.env.DATABASE_USER,
    password: process.env.DATABASE_PASSWORD,
    database: process.env.DATABASE
});


db.connect((error) => {
    if (error) {
        console.log('Error connecting to MySQL:', error);
    } else {
        console.log('MySQL Connected...');
    }
});

app.use(bodyParser.urlencoded({ extended: true }));


// app.use(session({
//     secret: 'your_secret_key', // Replace with a strong secret key
//     resave: false,
//     saveUninitialized: true,
//    // Set to true if using HTTPS
// }));

// const getCurrentUser = (req, res, next) => {
//     if (req.session.users) {
//         const users = req.session.users;
//         db.query('SELECT * FROM users WHERE username = ?', [users], (err, result) => {
//             if (err) throw err;
//             if (result.length > 0) {
//                 req.currentUser = result[0];
//             } else {
//                 req.currentUser = null;
//             }
//             next();
//         });
//     } else {
//         req.currentUser = null;
//         next();
//     }
// };



const publicDirectory = path.join(__dirname, './public');
app.use(express.static(publicDirectory));


app.set('view engine', 'hbs');


app.get("/", (req, res) => {
    res.render("userandadmin.hbs");
});

app.get("/login", (req, res) => {
    res.render("loginpage.hbs");
});

app.post("/login", (req, res) => {
    const { uname, psw } = req.body;
    const query = "SELECT * FROM users WHERE username = ? AND password = ?";

    db.query(query, [uname, psw], (error, results) => {
        if (error) {
            console.error("Error executing query:", error);
            res.status(500).send("Server Error");
        } else if (results.length > 0) {
            // req.session.users = result[0].uname;
            res.render("homepage.hbs");
        } else {
            res.send("Invalid username or password.");
        }
    });
});

app.get("/homepage", (req, res) => {
    res.render("homepage.hbs");
});

app.post('/logininsert', (req, res) => {
    const { username, password } = req.body;

    if (!username || !password) {
        return res.status(400).send('all file are required');
    }

    const sql = "INSERT INTO users (username , password) VALUES (?, ?)";
    db.query(sql, [username, password], (err, result) => {
        if (err) {
            return res.status(500).send('Database insert failed');
        }
        res.render("managemployee.hbs",)
    });
});



app.post("/admin", (req, res) => {
    const { admin, adminpsw } = req.body;
    const query = "SELECT * FROM admin WHERE HRADMIN = ? AND passwords = ?";

    db.query(query, [admin, adminpsw], (error, results) => {
        if (error) {
            console.error("Error executing query:", error);
            res.status(500).send("Server Error");
        } else if (results.length > 0) {
            res.render("HRadmin.hbs")
        } else {
            res.send("Invalid username or password.");
        }
    });
});


app.get("/admin", (req, res) => {
    res.render("loginadmin.hbs");
});


app.get("/PFform", (req, res) => {
    res.render("PFform.hbs");
});

app.post('/PFforminsert', (req, res) => {
    const { choice1, name1, dob, fatherandhusband, choice3, choice4, mobile, email, choice5, choice6, choice7,
        previousemployment, dateprevious, certificateforpreviousemployment, persionpayment, internationalworker,
        india, otherindia, passport, passportvalid, passportvalid1, educationalqualification,
        maritalstatus, specially, abled, bankkycnumber, banknumber, bankremark, nprkycnumber,
        nprnumber, nprremark, permanentkycnumber, permanentnumber, permanentremark, passportkycnumber,
        passportnumber, passportremark, drivinglicencekycnumber, drivinglicencenumber,
        drivinglicenceremark, electioncardkycnumber, electioncardnumber, electioncardremark,
        rationcardkycnumber, rationcardnumber, rationcardremark, esiccardkycnumber, esiccardnumber,
        esiccardremark, today_date, your_place, your_name, join_date, UAN_ALLOTED, today_dates } = req.body;

    const educationalqualifications = Array.isArray(req.body.educationalqualification) ? req.body.educationalqualification : [req.body.educationalqualification];

    const educationalqualificationstring = educationalqualifications.join(', ');

    const ableds = Array.isArray(req.body.abled) ? req.body.abled : [req.body.abled];

    const abledstring = ableds.join(', ');


    // if (!choice1 || !name1 || !dob || !fatherandhusband || !choice3 || !choice4 || !mobile || !email || !choice5 || !choice6 || !choice7 || !previousemployment,dateprevious|| !certificateforpreviousemployment || !persionpayment || !internationalworker || !india || !otherindia || !passport || !passportvalid || !passportvalid1 || !educationalqualification|| !maritalstatus || !specially || !abled || !bankkycnumber || !banknumber || !bankremark || !nprkycnumber || !nprnumber || !nprremark || !permanentkycnumber || !permanentnumber || !permanentremark || !passportkycnumber || !passportnumber || !passportremark || !drivinglicencekycnumber || !drivinglicencenumber || !drivinglicenceremark || !electioncardkycnumber || !electioncardnumber || !electioncardremark || !rationcardkycnumber || !rationcardnumber || !rationcardremark || !esiccardkycnumber || !esiccardnumber || !esiccardremark || !today_date || !your_place|| !your_name || !join_date || !UAN_ALLOTED || !today_dates) {
    //     return res.status(400).send('all file are required');
    // }


    const sql = "INSERT INTO providentfund (mr_ms_mrs, name, dateofbirth, fatherandhusband, relationinrespect, gender, mobilenumber, email, emppovidentfunds, emppensionscheme, uaborprevious, account,  dateofexit, certificateissued, pensionpayment, internationworker, india, otherthanindia, passport, passportfrom, passportto, educationalqualification, maritalstatus, specially, category, bankkycnumber, banknumber, bankremark, nprkycnumber, nprnumber, nprremark, permanentkycnumber, permanentnumber, permanentremark, passportkycnumber, passportnumber, passportremark, drivinglicencekycnumber, drivinglicencenumber, drivinglicenceremark, electioncardkycnumber, electioncardnumber, electioncardremark, rationcardkycnumber,  rationcardnumber, rationcardremark, esiccardkycnumber, esiccardnumber, esiccardremark, today_date,  your_place, your_name, join_date, UAN_ALLOTED, today_dates) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
    db.query(sql, [choice1, name1, dob, fatherandhusband, choice3, choice4, mobile, email, choice5, choice6, choice7,
        previousemployment, dateprevious, certificateforpreviousemployment, persionpayment, internationalworker,
        india, otherindia, passport, passportvalid, passportvalid1, educationalqualificationstring,
        maritalstatus, specially, abledstring, bankkycnumber, banknumber, bankremark, nprkycnumber,
        nprnumber, nprremark, permanentkycnumber, permanentnumber, permanentremark, passportkycnumber,
        passportnumber, passportremark, drivinglicencekycnumber, drivinglicencenumber,
        drivinglicenceremark, electioncardkycnumber, electioncardnumber, electioncardremark,
        rationcardkycnumber, rationcardnumber, rationcardremark, esiccardkycnumber, esiccardnumber,
        esiccardremark, today_date, your_place, your_name, join_date, UAN_ALLOTED, today_dates], (err, result) => {
            if (err) {
                return res.status(500).send('Database insert failed');
            }
            res.render("homepage.hbs");
        });
});




app.get("/form12", (req, res) => {
    res.render("form12.hbs");
});


app.post('/form12insert', (req, res) => {
    const { end_year, name_and_address, permanent_accountno, residential_status,
        name_and_address_employer, tan_of_employer_ito, permanent_account_number,
        period_of_employment, total_amount_of_salary, total_amount_house_allowance,
        value_of_perquistes_and_amount, total_of_colume, amount_deducted_in_respesct,
        total_of_tax_deducteddu_in_the_year, remark, your_name, verified_today,
        day_of_year, name_emp_address, permanent_account, year_endingfrom, year_endingto, name_of_emp,
        tan_of_employer, acommodation_is_unfurnished, value_of_acommodation,
        cost_of_furniture, perquisite_value_of_furniture, total_of_column1, rent,
        value_of_perquisite, name_of_employee, whether_any_conveyance, remuneration12,
        value13, estimated_value14, employer_contribution15, interest16,
        total_of_columns17, policy, Date5, gross_amount, qualifying_amount } = req.body;

    // if (!username || !password) {
    //     return res.status(400).send('all file are required');
    // }

    const sql = "INSERT INTO taxdeduction (end_year,name_and_address, permanent_accountno, residential_status,  name_and_address_employer, tan_of_employer_ito, permanent_account_number, period_of_employment, total_amount_of_salary, total_amount_house_allowance,  value_of_perquistes_and_amount, total_of_colume, amount_deducted_in_respesct, total_of_tax_deducteddu_in_the_year, remark, your_name, verified_today, day_of_year, name_emp_address, permanent_account, year_endingfrom, year_endingto,  name_of_emp, tan_of_employer, acommodation_is_unfurnished, value_of_acommodation, cost_of_furniture, perquisite_value_of_furniture, total_of_column1, rent, value_of_perquisite, name_of_employee, whether_any_conveyance, remuneration12, value13, estimated_value14, employer_contribution15, interest16, total_of_columns17, policy, Date5, gross_amount, qualifying_amount) VALUES (?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?)";
    db.query(sql, [end_year, name_and_address, permanent_accountno, residential_status,
        name_and_address_employer, tan_of_employer_ito, permanent_account_number,
        period_of_employment, total_amount_of_salary, total_amount_house_allowance,
        value_of_perquistes_and_amount, total_of_colume, amount_deducted_in_respesct,
        total_of_tax_deducteddu_in_the_year, remark, your_name, verified_today,
        day_of_year, name_emp_address, permanent_account, year_endingfrom, year_endingto, name_of_emp,
        tan_of_employer, acommodation_is_unfurnished, value_of_acommodation,
        cost_of_furniture, perquisite_value_of_furniture, total_of_column1, rent,
        value_of_perquisite, name_of_employee, whether_any_conveyance, remuneration12,
        value13, estimated_value14, employer_contribution15, interest16,
        total_of_columns17, policy, Date5, gross_amount, qualifying_amount], (err, result) => {
            if (err) {
                return res.status(500).send('Database insert failed');
            }
            res.render("homepage.hbs")
        });
});


app.get("/forms12", (req, res) => {
    res.render("forms12.hbs");
});

app.get("/newjoining", (req, res) => {
    res.render("newjoining.hbs");
});



app.post('/newjoininsert', (req, res) => {
    const { Name, Designation, PresentAddress, PermanentAddress, Namefather, NameMother, PAN, DateJoining, DateBirth, personalmobile, personalemail, Department, Location, MaritalStatus, EPFNOwithPreviousEmployer, nameofSpouseandChildren, Relationship, DateofBirth, nameofSpouseandChildren1, Relationship1, DateofBirth1, nameofSpouseandChildren2, Relationship2, DateofBirth2, nameofSpouseandChildren3, Relationship3, DateofBirth3 } = req.body;

    // if ( !Name || !Designation || !PresentAddress || !PermanentAddress || !Namefather || !NameMother || !PAN || !DateJoining || !DateBirth || !personalmobile || !personalemail || !Department || !Location || !MaritalStatus || !EPFNOwithPreviousEmployer || !nameofSpouseandChildren || !Relationship || !DateofBirth || ! nameofSpouseandChildren1 || !Relationship1 || !DateofBirth1 || !nameofSpouseandChildren2 || !Relationship2 || !DateofBirth2 || !nameofSpouseandChildren3 || !Relationship3 || !DateofBirth3) {
    //     return res.status(400).send('all file are required');
    // }

    const sql = "INSERT INTO newjoiningforminsurance (Name, Designation, PresentAddress, PermanentAddress, Namefather, NameMother, PAN, DateJoining, DateBirth, personalmobile, personalemail, Department, Location, MaritalStatus, EPFNOwithPreviousEmployer, nameofSpouseandChildren, Relationship, DateofBirth, nameofSpouseandChildren1, Relationship1, DateofBirth1, nameofSpouseandChildren2, Relationship2, DateofBirth2, nameofSpouseandChildren3, Relationship3, DateofBirth3) VALUES (?, ?,? , ?, ?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?)";
    db.query(sql, [Name, Designation, PresentAddress, PermanentAddress, Namefather, NameMother, PAN, DateJoining, DateBirth, personalmobile, personalemail, Department, Location, MaritalStatus, EPFNOwithPreviousEmployer, nameofSpouseandChildren, Relationship, DateofBirth, nameofSpouseandChildren1, Relationship1, DateofBirth1, nameofSpouseandChildren2, Relationship2, DateofBirth2, nameofSpouseandChildren3, Relationship3, DateofBirth3], (err, result) => {
        if (err) {
            return res.status(500).send('Database insert failed');
        }
        res.render("homepage.hbs")
    });
});

const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, '');
    },
    filename: (req, file, cb) => {
        cb(null, Date.now() + path.extname(file.originalname));
    }
});

const upload = multer({ storage: storage });


app.get("/informationform", (req, res) => {
    res.render("informationform.hbs");
});

app.post('/informationforminsert', upload.single('photoimage'), (req, res) => {
    const { first_name, middle_name, surname, employee_code, reporting_manager, department,
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
        eDurationto, todaydate } = req.body;

    // if (!username || !password) {
    //     return res.status(400).send('all file are required');
    // }
    if (!req.file) {
        return res.status(400).send('No file uploaded.');
    }
    const photoimage = req.file.filename

    const languages = Array.isArray(req.body.language) ? req.body.language : [req.body.language];


    const languageString = languages.join(', ');

    const sql = "INSERT INTO informationform ( photoimage, first_name, middle_name, surname, employee_code, reporting_manager, department, permanent_address, PostalCodeorPinCode, Present_Address, dateofbirth, sex, birthplace, bloodgroup, nationality, religion, pan, language, maritalstatus, marriage_date, spouse_name, spouse_dob, children_count, first_child_name, first_child_dob, second_child_name, second_child_dob, third_child_name, third_child_dob, contact_number, mobile_number, emergency_contact, email_id, SSCName, SSCSpecialization, SSCSPassingYearMonth, SSCPercentage, SSCGrade, HSCName, HSCSpecialization,  HSCPassingYearMonth, HSCPercentage, HSCGrade, GraduationName, GraduationSpecialization, GraduationPassingYearMonth, GraduationPercentage, GraduationGrade, DiplomaName, DiplomaSpecialization, DiplomaPassingYearMonth, DiplomaPercentage, DiplomaGrade, DegreeName, DegreeSpecialization, DegreePassingYearMonth, DegreePercentage, DegreeGrade, MastersorPostGraduationName, MastersorPostGraduationSpecialization,  MastersorPostGraduationPassingYearMonth, MastersorPercentage, MastersorGrade, DoctorateName, DoctorateSpecialization, DoctoratePassingYearMonth, DoctoratePercentage, DoctorateGrade, OthersName, OthersSpecialization, OthersPassingYearMonth, OthersPercentage, OthersGrade, aOrganization, aDesignation, aLocation, aDurationfrom, aDurationto, bOrganization, bDesignation, bLocation, bDurationfrom, bDurationto, cOrganization, cDesignation, cLocation, cDurationfrom, cDurationto, dOrganization, dDesignation, dLocation, dDurationfrom, dDurationto, eOrganization, eDesignation, eLocation, eDurationfrom, eDurationto, todaydate) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)";
    db.query(sql, [photoimage, first_name, middle_name, surname, employee_code, reporting_manager, department,
        permanent_address, PostalCodeorPinCode, Present_Address, dateofbirth, sex, birthplace,
        bloodgroup, nationality, religion, pan, languageString, maritalstatus, marriage_date,
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
        eDurationto, todaydate], (err, result) => {
            if (err) {
                return res.status(500).send('Database insert failed');
            }
            res.render("homepage.hbs");
        });
});





app.get("/induction", (req, res) => {
    res.render("induction.hbs");
});


app.post('/inductioninsert', (req, res) => {
    const { Employee_name, Employee_ID, Department, Joining_Date, Designation, HRorAdminDayandTime,
        HRorAdminEmployeeSign, HRorAdminProcessOwnerSign, Quality_EngineeringDayandTime1,
        Quality_EngineeringEmployeeSign1, Quality_EngineeringProcessOwnerSign1, Finance_ControlDayandTime2,
        Finance_ControlEmployeeSign2, Finance_ControlProcessOwnerSign2, Project_ManagementDayandTime3,
        Project_ManagementEmployeeSign3, Project_ManagementProcessOwnerSign3, Engineering_DayandTime4,
        Engineering_EmployeeSign4, Engineering_ProcessOwnerSign4, SIBM_DayandTime5, SIBM_EmployeeSign5,
        SIBM_ProcessOwnerSign5, Procurement_DayandTime6, Procurement_EmployeeSign6, Procurement_ProcessOwnerSign6,
        Proposal_ServiceDayandTime7, Proposal_ServiceEmployeeSign7, Proposal_ServiceProcessOwnerSign7,
        Refractory_DayandTime8, Refractory_EmployeeSign8, Refractory_ProcessOwnerSign8, PMO_DayandTime9,
        PMO_EmployeeSign9, PMO_ProcessOwnerSign9, IT_DayandTime10, IT_EmployeeSign10, IT_ProcessOwnerSign10,
        Employee_FeedbacK, Employee_Signature, Date1, Date2 } = req.body;

    // if (  !Employee_name || !Employee_ID || !Department || !Joining_Date || !Designation || !HRorAdminDayandTime || !HRorAdminEmployeeSign || !HRorAdminProcessOwnerSign || !Quality_EngineeringDayandTime1 || !Quality_EngineeringEmployeeSign1 || !Quality_EngineeringProcessOwnerSign1 || !Finance_ControlDayandTime2 || !Finance_ControlEmployeeSign2 || !Finance_ControlProcessOwnerSign2|| !Project_ManagementDayandTime3 || !Project_ManagementEmployeeSign3 || !Project_ManagementProcessOwnerSign3 || !Engineering_DayandTime4 || !Engineering_EmployeeSign4 || !Engineering_ProcessOwnerSign4|| !SIBM_DayandTime5 || !SIBM_EmployeeSign5 || !SIBM_ProcessOwnerSign5 || !Procurement_DayandTime6 || !Procurement_EmployeeSign6 || !Procurement_ProcessOwnerSign6 || !Proposal_ServiceDayandTime7 || !Proposal_ServiceEmployeeSign7 || !Proposal_ServiceProcessOwnerSign7 || !Refractory_DayandTime8 || !Refractory_EmployeeSign8 || !Refractory_ProcessOwnerSign8 || !PMO_DayandTime9 || !PMO_EmployeeSign9 || !PMO_ProcessOwnerSign9 || !IT_DayandTime10 || !IT_EmployeeSign10 || !IT_ProcessOwnerSign10 || !Employee_FeedbacK || !Employee_Signature || !Date1 || !Date2) {
    //     return res.status(400).send('all file are required');
    // }

    const sql = "INSERT INTO inductionforminsurance ( Employee_name, Employee_ID, Department, Joining_Date, Designation, HRorAdminDayandTime, HRorAdminEmployeeSign, HRorAdminProcessOwnerSign, Quality_EngineeringDayandTime1, Quality_EngineeringEmployeeSign1, Quality_EngineeringProcessOwnerSign1, Finance_ControlDayandTime2, Finance_ControlEmployeeSign2, Finance_ControlProcessOwnerSign2, Project_ManagementDayandTime3, Project_ManagementEmployeeSign3, Project_ManagementProcessOwnerSign3, Engineering_DayandTime4, Engineering_EmployeeSign4, Engineering_ProcessOwnerSign4, SIBM_DayandTime5, SIBM_EmployeeSign5, SIBM_ProcessOwnerSign5, Procurement_DayandTime6, Procurement_EmployeeSign6, Procurement_ProcessOwnerSign6, Proposal_ServiceDayandTime7, Proposal_ServiceEmployeeSign7, Proposal_ServiceProcessOwnerSign7, Refractory_DayandTime8, Refractory_EmployeeSign8, Refractory_ProcessOwnerSign8, PMO_DayandTime9, PMO_EmployeeSign9, PMO_ProcessOwnerSign9, IT_DayandTime10, IT_EmployeeSign10, IT_ProcessOwnerSign10, Employee_FeedbacK, Employee_Signature, Date1, Date2) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)";
    db.query(sql, [Employee_name, Employee_ID, Department, Joining_Date, Designation, HRorAdminDayandTime,
        HRorAdminEmployeeSign, HRorAdminProcessOwnerSign, Quality_EngineeringDayandTime1,
        Quality_EngineeringEmployeeSign1, Quality_EngineeringProcessOwnerSign1, Finance_ControlDayandTime2,
        Finance_ControlEmployeeSign2, Finance_ControlProcessOwnerSign2, Project_ManagementDayandTime3,
        Project_ManagementEmployeeSign3, Project_ManagementProcessOwnerSign3, Engineering_DayandTime4,
        Engineering_EmployeeSign4, Engineering_ProcessOwnerSign4, SIBM_DayandTime5, SIBM_EmployeeSign5,
        SIBM_ProcessOwnerSign5, Procurement_DayandTime6, Procurement_EmployeeSign6, Procurement_ProcessOwnerSign6,
        Proposal_ServiceDayandTime7, Proposal_ServiceEmployeeSign7, Proposal_ServiceProcessOwnerSign7,
        Refractory_DayandTime8, Refractory_EmployeeSign8, Refractory_ProcessOwnerSign8, PMO_DayandTime9,
        PMO_EmployeeSign9, PMO_ProcessOwnerSign9, IT_DayandTime10, IT_EmployeeSign10, IT_ProcessOwnerSign10,
        Employee_FeedbacK, Employee_Signature, Date1, Date2], (err, result) => {
            if (err) {
                return res.status(500).send('Database insert failed');
            }
            res.render("homepage.hbs");
        });
});



// app.get("/managemployee", (req, res) => {
//     res.render("manageemployee.hbs");
// });

app.get("/Employee_submission", (req, res) => {
    res.render("Employee_submission.hbs", { formNo });
});


app.get('/managemployee', (req, res) => {
    const sql = "SELECT * FROM users";
    db.query(sql, (err, results) => {
        if (err) {
            console.error('Database query failed:', err);
            return res.status(500).send('Database query failed');
        }
        res.render('managemployee.hbs', { users: results });
    });
});


app.post('/search', (req, res) => {
    const searchTerm = req.body.username;
    const sql = `SELECT * FROM users WHERE username LIKE ?`;
    db.query(sql, [`%${searchTerm}%`], (err, result) => {
        if (err) throw err;
        res.render("managemployee.hbs", { users: result })
    });
});


app.get('/managemployees', (req, res) => {
    const sql = "SELECT * FROM users";
    db.query(sql, (err, results) => {
        if (err) {
            console.error('Database query failed:', err);
            return res.status(500).send('Database query failed');
        }
        res.render('managemployees.hbs', { users: results });

    });
});

app.post('/searchs', (req, res) => {
    const searchTerm = req.body.username;
    const sql = `SELECT * FROM users WHERE username LIKE ?`;
    db.query(sql, [`%${searchTerm}%`], (err, result) => {
        if (err) throw err;
        res.render("managemployees.hbs", { users: result })
    });
})

app.get("/EmployeeOnboardingChecklistForm" , (req, res) => {
    res.render("Employee Onboarding Checklist Form.hbs");
});

app.post('/EmployeeOnboardingChecklistForminsert', (req, res) => {

    const { Form_No, Date_of_Issue, Revision, Approved_by } = req.body;
    const getBooleanField = (field) => req.body[field] === 'on' ? 1 : 0;

    const fields = [
        'Resume', 'Employee_Information_Form', 'Educational_Certificate',
        'Relieving_Certificates_of_last_2_organizations', 'Salary_Slips_of_last_3_months',
        'Form_16_If_applicable', 'Pan_Card_Mandatory', 'Photo_ID_Proof_Voter_Aadhar_Card_Passport_etc',
        'Passport_size_Photo', 'Permanent_Mandatory', 'Bank_Aorc_Opening_Form_and_Formalities',
        'Current_Address_Proof', 'NDAorService_Agreement', 'Entry_in_Keka',
        'Appointment_Letter', 'Entry_in_Dax360', 'Entry_in_Meytou',
        'Indirect_ariff', 'Stationary_Notepad_and_Pen', 'Employee_ID_Card',
        'Extension_list', 'Visiting_Cards_if_pplicable', 'Adhaar_Card_Copy',
        'Appointment_Letter_Copy', 'Nomination_Letter', 'Universal_Account_Number_UAN',
        'Provident_Fund_Account_Number_PF', 'Bank_Account_No_and_Name', 'PAN_Card_Copy',
        'Seating_Arrangement', 'Laptopa_and_Desktop_and_Accessories', 'Phone_Extension',
        'Official_Email_ID_Creation', 'Group_and_Location_Email_Alias', 'Sim_Card',
        'Head_Phone', 'Screen', 'Employee_Access_Card_and_Biometrix_Access',
        'Insurance_Form', 'Insurance_Form1'
    ];

    const booleanValues = fields.map(field => getBooleanField(field));
    const values = [Form_No, Date_of_Issue, Revision, Approved_by, ...booleanValues];

    const sql = "INSERT INTO employeeoboarding (Form_No, Date_of_Issue, Revision, Approved_by, Resume, Employee_Information_Form, Educational_Certificate, Relieving_Certificates_of_last_2_organizations, Salary_Slips_of_last_3_months,Form_16_If_applicable, Pan_Card_Mandatory, Photo_ID_Proof_Voter_Aadhar_Card_Passport_etc, Passport_size_Photo, Permanent_Mandatory, Bank_Aorc_Opening_Form_and_Formalities,Current_Address_Proof, NDAorService_Agreement, Entry_in_Keka, Appointment_Letter, Entry_in_Dax360, Entry_in_Meytou, Indirect_ariff, Stationary_Notepad_and_Pen, Employee_ID_Card, Extension_list, Visiting_Cards_if_pplicable, Adhaar_Card_Copy, Appointment_Letter_Copy, Nomination_Letter, Universal_Account_Number_UAN, Provident_Fund_Account_Number_PF, Bank_Account_No_and_Name, PAN_Card_Copy, Seating_Arrangement, Laptopa_and_Desktop_and_Accessories, Phone_Extension, Official_Email_ID_Creation, Group_and_Location_Email_Alias, Sim_Card, Head_Phone, Screen, Employee_Access_Card_and_Biometrix_Access, Insurance_Form, Insurance_Form1) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

    db.query(sql, values, (err, result) => {
        if (err) {
            console.error('Database insert error:', err);
            return res.status(500).send('Database insert failed: ' + err.message);
        }
        console.log('Insert successful. Rows affected:', result.affectedRows);
        res.send("done");
    });
});











app.listen(port, () => {
    console.log('Server running on port localhost. ' + port);
});

































