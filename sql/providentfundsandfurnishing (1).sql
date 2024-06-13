-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 11, 2024 at 06:52 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `providentfundsandfurnishing`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `HRADMIN` text DEFAULT NULL,
  `passwords` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `HRADMIN`, `passwords`) VALUES
(1, 'HRadmin@admin.com', '12345');

-- --------------------------------------------------------

--
-- Table structure for table `employeeoboarding`
--

CREATE TABLE `employeeoboarding` (
  `id` int(11) NOT NULL,
  `Form_No` text DEFAULT NULL,
  `Date_of_Issue` date DEFAULT NULL,
  `Revision` text DEFAULT NULL,
  `Approved_by` text DEFAULT NULL,
  `Resume` tinyint(1) DEFAULT NULL,
  `Employee_Information_Form` tinyint(1) DEFAULT NULL,
  `Educational_Certificate` tinyint(1) DEFAULT NULL,
  `Relieving_Certificates_of_last_2_organizations` tinyint(1) DEFAULT NULL,
  `Salary_Slips_of_last_3_months` tinyint(1) DEFAULT NULL,
  `Form_16_If_applicable` tinyint(1) DEFAULT NULL,
  `Pan_Card_Mandatory` tinyint(1) DEFAULT NULL,
  `Photo_ID_Proof_Voter_Aadhar_Card_Passport_etc` tinyint(1) DEFAULT NULL,
  `Passport_size_Photo` tinyint(1) DEFAULT NULL,
  `Permanent_Mandatory` tinyint(1) DEFAULT NULL,
  `Bank_Aorc_Opening_Form_and_Formalities` tinyint(1) DEFAULT NULL,
  `Current_Address_Proof` tinyint(1) DEFAULT NULL,
  `NDAorService_Agreement` tinyint(1) DEFAULT NULL,
  `Entry_in_Keka` tinyint(1) DEFAULT NULL,
  `Appointment_Letter` tinyint(1) DEFAULT NULL,
  `Entry_in_Dax360` tinyint(1) DEFAULT NULL,
  `Entry_in_Meytou` tinyint(1) DEFAULT NULL,
  `Indirect_ariff` tinyint(1) DEFAULT NULL,
  `Stationary_Notepad_and_Pen` tinyint(1) DEFAULT NULL,
  `Employee_ID_Card` tinyint(1) DEFAULT NULL,
  `Extension_list` tinyint(1) DEFAULT NULL,
  `Visiting_Cards_if_pplicable` tinyint(1) DEFAULT NULL,
  `Adhaar_Card_Copy` tinyint(1) DEFAULT NULL,
  `Appointment_Letter_Copy` tinyint(1) DEFAULT NULL,
  `Nomination_Letter` tinyint(1) DEFAULT NULL,
  `Universal_Account_Number_UAN` tinyint(1) DEFAULT NULL,
  `Provident_Fund_Account_Number_PF` tinyint(1) DEFAULT NULL,
  `Bank_Account_No_and_Name` tinyint(1) DEFAULT NULL,
  `PAN_Card_Copy` tinyint(1) DEFAULT NULL,
  `Seating_Arrangement` tinyint(1) DEFAULT NULL,
  `Laptopa_and_Desktop_and_Accessories` tinyint(1) DEFAULT NULL,
  `Phone_Extension` tinyint(1) DEFAULT NULL,
  `Official_Email_ID_Creation` tinyint(1) DEFAULT NULL,
  `Group_and_Location_Email_Alias` tinyint(1) DEFAULT NULL,
  `Sim_Card` tinyint(1) DEFAULT NULL,
  `Head_Phone` tinyint(1) DEFAULT NULL,
  `Screen` tinyint(1) DEFAULT NULL,
  `Employee_Access_Card_and_Biometrix_Access` tinyint(1) DEFAULT NULL,
  `Insurance_Form` tinyint(1) DEFAULT NULL,
  `Insurance_Form1` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `inductionforminsurance`
--

CREATE TABLE `inductionforminsurance` (
  `id` int(11) NOT NULL,
  `Employee_name` text DEFAULT NULL,
  `Employee_ID` text DEFAULT NULL,
  `Department` text DEFAULT NULL,
  `Joining_Date` date DEFAULT NULL,
  `Designation` text DEFAULT NULL,
  `HRorAdminDayandTime` date DEFAULT NULL,
  `HRorAdminEmployeeSign` varchar(225) DEFAULT NULL,
  `HRorAdminProcessOwnerSign` varchar(225) DEFAULT NULL,
  `Quality_EngineeringDayandTime1` date DEFAULT NULL,
  `Quality_EngineeringEmployeeSign1` varchar(225) DEFAULT NULL,
  `Quality_EngineeringProcessOwnerSign1` varchar(225) DEFAULT NULL,
  `Finance_ControlDayandTime2` date DEFAULT NULL,
  `Finance_ControlEmployeeSign2` varchar(225) DEFAULT NULL,
  `Finance_ControlProcessOwnerSign2` varchar(225) DEFAULT NULL,
  `Project_ManagementDayandTime3` date DEFAULT NULL,
  `Project_ManagementEmployeeSign3` varchar(225) DEFAULT NULL,
  `Project_ManagementProcessOwnerSign3` varchar(225) DEFAULT NULL,
  `Engineering_DayandTime4` date DEFAULT NULL,
  `Engineering_EmployeeSign4` varchar(225) DEFAULT NULL,
  `Engineering_ProcessOwnerSign4` varchar(225) DEFAULT NULL,
  `SIBM_DayandTime5` date DEFAULT NULL,
  `SIBM_EmployeeSign5` varchar(225) DEFAULT NULL,
  `SIBM_ProcessOwnerSign5` varchar(225) DEFAULT NULL,
  `Procurement_DayandTime6` date DEFAULT NULL,
  `Procurement_EmployeeSign6` varchar(225) DEFAULT NULL,
  `Procurement_ProcessOwnerSign6` varchar(225) DEFAULT NULL,
  `Proposal_ServiceDayandTime7` date DEFAULT NULL,
  `Proposal_ServiceEmployeeSign7` varchar(225) DEFAULT NULL,
  `Proposal_ServiceProcessOwnerSign7` varchar(225) DEFAULT NULL,
  `Refractory_DayandTime8` date DEFAULT NULL,
  `Refractory_EmployeeSign8` varchar(225) DEFAULT NULL,
  `Refractory_ProcessOwnerSign8` varchar(225) DEFAULT NULL,
  `PMO_DayandTime9` date DEFAULT NULL,
  `PMO_EmployeeSign9` varchar(225) DEFAULT NULL,
  `PMO_ProcessOwnerSign9` varchar(225) DEFAULT NULL,
  `IT_DayandTime10` date DEFAULT NULL,
  `IT_EmployeeSign10` varchar(225) DEFAULT NULL,
  `IT_ProcessOwnerSign10` varchar(225) DEFAULT NULL,
  `Employee_FeedbacK` text DEFAULT NULL,
  `Employee_Signature` text DEFAULT NULL,
  `Date1` date DEFAULT NULL,
  `Date2` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `informationform`
--

CREATE TABLE `informationform` (
  `id` int(11) NOT NULL,
  `photoimage` longblob DEFAULT NULL,
  `first_name` text DEFAULT NULL,
  `middle_name` text DEFAULT NULL,
  `surname` text DEFAULT NULL,
  `employee_code` text DEFAULT NULL,
  `reporting_manager` text DEFAULT NULL,
  `department` text DEFAULT NULL,
  `permanent_address` text DEFAULT NULL,
  `PostalCodeorPinCode` text DEFAULT NULL,
  `Present_Address` text DEFAULT NULL,
  `dateofbirth` date DEFAULT NULL,
  `sex` text DEFAULT NULL,
  `birthplace` date DEFAULT NULL,
  `bloodgroup` text DEFAULT NULL,
  `nationality` text DEFAULT NULL,
  `religion` text DEFAULT NULL,
  `pan` text DEFAULT NULL,
  `language` varchar(225) DEFAULT NULL,
  `maritalstatus` varchar(225) DEFAULT NULL,
  `marriage_date` date DEFAULT NULL,
  `spouse_name` text DEFAULT NULL,
  `spouse_dob` date DEFAULT NULL,
  `children_count` int(11) DEFAULT NULL,
  `first_child_name` text DEFAULT NULL,
  `first_child_dob` date DEFAULT NULL,
  `second_child_name` text DEFAULT NULL,
  `second_child_dob` date DEFAULT NULL,
  `third_child_name` text DEFAULT NULL,
  `third_child_dob` date DEFAULT NULL,
  `contact_number` text DEFAULT NULL,
  `mobile_number` text DEFAULT NULL,
  `emergency_contact` text DEFAULT NULL,
  `email_id` text DEFAULT NULL,
  `SSCName` text DEFAULT NULL,
  `SSCSpecialization` text DEFAULT NULL,
  `SSCSPassingYearMonth` text DEFAULT NULL,
  `SSCPercentage` text DEFAULT NULL,
  `SSCGrade` text DEFAULT NULL,
  `HSCName` text DEFAULT NULL,
  `HSCSpecialization` text DEFAULT NULL,
  `HSCPassingYearMonth` text DEFAULT NULL,
  `HSCPercentage` text DEFAULT NULL,
  `HSCGrade` text DEFAULT NULL,
  `GraduationName` text DEFAULT NULL,
  `GraduationSpecialization` text DEFAULT NULL,
  `GraduationPassingYearMonth` text DEFAULT NULL,
  `GraduationPercentage` text DEFAULT NULL,
  `GraduationGrade` text DEFAULT NULL,
  `DiplomaName` text DEFAULT NULL,
  `DiplomaSpecialization` text DEFAULT NULL,
  `DiplomaPassingYearMonth` text DEFAULT NULL,
  `DiplomaPercentage` text DEFAULT NULL,
  `DiplomaGrade` text DEFAULT NULL,
  `DegreeName` text DEFAULT NULL,
  `DegreeSpecialization` text DEFAULT NULL,
  `DegreePassingYearMonth` text DEFAULT NULL,
  `DegreePercentage` text DEFAULT NULL,
  `DegreeGrade` text DEFAULT NULL,
  `MastersorPostGraduationName` text DEFAULT NULL,
  `MastersorPostGraduationSpecialization` text DEFAULT NULL,
  `MastersorPostGraduationPassingYearMonth` text DEFAULT NULL,
  `MastersorPercentage` text DEFAULT NULL,
  `MastersorGrade` text DEFAULT NULL,
  `DoctorateName` text DEFAULT NULL,
  `DoctorateSpecialization` text DEFAULT NULL,
  `DoctoratePassingYearMonth` text DEFAULT NULL,
  `DoctoratePercentage` text DEFAULT NULL,
  `DoctorateGrade` text DEFAULT NULL,
  `OthersName` text DEFAULT NULL,
  `OthersSpecialization` text DEFAULT NULL,
  `OthersPassingYearMonth` text DEFAULT NULL,
  `OthersPercentage` text DEFAULT NULL,
  `OthersGrade` text DEFAULT NULL,
  `aOrganization` text DEFAULT NULL,
  `aDesignation` text DEFAULT NULL,
  `aLocation` text DEFAULT NULL,
  `aDurationfrom` date DEFAULT NULL,
  `aDurationto` date DEFAULT NULL,
  `bOrganization` text DEFAULT NULL,
  `bDesignation` text DEFAULT NULL,
  `bLocation` text DEFAULT NULL,
  `bDurationfrom` date DEFAULT NULL,
  `bDurationto` date DEFAULT NULL,
  `cOrganization` text DEFAULT NULL,
  `cDesignation` text DEFAULT NULL,
  `cLocation` text DEFAULT NULL,
  `cDurationfrom` date DEFAULT NULL,
  `cDurationto` date DEFAULT NULL,
  `dOrganization` text DEFAULT NULL,
  `dDesignation` text DEFAULT NULL,
  `dLocation` text DEFAULT NULL,
  `dDurationfrom` date DEFAULT NULL,
  `dDurationto` date DEFAULT NULL,
  `eOrganization` text DEFAULT NULL,
  `eDesignation` text DEFAULT NULL,
  `eLocation` text DEFAULT NULL,
  `eDurationfrom` date DEFAULT NULL,
  `eDurationto` date DEFAULT NULL,
  `todaydate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `newjoiningforminsurance`
--

CREATE TABLE `newjoiningforminsurance` (
  `id` int(11) NOT NULL,
  `Name` text DEFAULT NULL,
  `Designation` text DEFAULT NULL,
  `PresentAddress` text DEFAULT NULL,
  `PermanentAddress` text DEFAULT NULL,
  `Namefather` text DEFAULT NULL,
  `NameMother` text DEFAULT NULL,
  `PAN` text DEFAULT NULL,
  `DateJoining` date DEFAULT NULL,
  `DateBirth` date DEFAULT NULL,
  `personalmobile` text DEFAULT NULL,
  `personalemail` text DEFAULT NULL,
  `Department` text DEFAULT NULL,
  `Location` text DEFAULT NULL,
  `MaritalStatus` text DEFAULT NULL,
  `EPFNOwithPreviousEmployer` text DEFAULT NULL,
  `nameofSpouseandChildren` text DEFAULT NULL,
  `Relationship` text DEFAULT NULL,
  `DateofBirth` date DEFAULT NULL,
  `nameofSpouseandChildren1` text DEFAULT NULL,
  `Relationship1` text DEFAULT NULL,
  `DateofBirth1` date DEFAULT NULL,
  `nameofSpouseandChildren2` text DEFAULT NULL,
  `Relationship2` text DEFAULT NULL,
  `DateofBirth2` text DEFAULT NULL,
  `nameofSpouseandChildren3` text DEFAULT NULL,
  `Relationship3` text DEFAULT NULL,
  `DateofBirth3` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `providentfund`
--

CREATE TABLE `providentfund` (
  `id` int(11) NOT NULL,
  `mr_ms_mrs` text DEFAULT NULL,
  `name` text DEFAULT NULL,
  `dateofbirth` date DEFAULT NULL,
  `fatherandhusband` text DEFAULT NULL,
  `relationinrespect` text DEFAULT NULL,
  `gender` text DEFAULT NULL,
  `mobilenumber` int(11) DEFAULT NULL,
  `email` text DEFAULT NULL,
  `emppovidentfunds` text DEFAULT NULL,
  `emppensionscheme` text DEFAULT NULL,
  `uaborprevious` text DEFAULT NULL,
  `account` text DEFAULT NULL,
  `dateofexit` date DEFAULT NULL,
  `certificateissued` text DEFAULT NULL,
  `pensionpayment` text DEFAULT NULL,
  `internationworker` text DEFAULT NULL,
  `india` text DEFAULT NULL,
  `otherthanindia` text DEFAULT NULL,
  `passport` text DEFAULT NULL,
  `passportfrom` date DEFAULT NULL,
  `passportto` date DEFAULT NULL,
  `educationalqualification` text DEFAULT NULL,
  `maritalstatus` varchar(225) DEFAULT NULL,
  `specially` varchar(225) DEFAULT NULL,
  `category` varchar(225) DEFAULT NULL,
  `bankkycnumber` text DEFAULT NULL,
  `banknumber` text DEFAULT NULL,
  `bankremark` text DEFAULT NULL,
  `nprkycnumber` text DEFAULT NULL,
  `nprnumber` text DEFAULT NULL,
  `nprremark` text DEFAULT NULL,
  `permanentkycnumber` text DEFAULT NULL,
  `permanentnumber` text DEFAULT NULL,
  `permanentremark` text DEFAULT NULL,
  `passportkycnumber` text DEFAULT NULL,
  `passportnumber` text DEFAULT NULL,
  `passportremark` text DEFAULT NULL,
  `drivinglicencekycnumber` text DEFAULT NULL,
  `drivinglicencenumber` text DEFAULT NULL,
  `drivinglicenceremark` text DEFAULT NULL,
  `electioncardkycnumber` text DEFAULT NULL,
  `electioncardnumber` text DEFAULT NULL,
  `electioncardremark` text DEFAULT NULL,
  `rationcardkycnumber` text DEFAULT NULL,
  `rationcardnumber` text DEFAULT NULL,
  `rationcardremark` text DEFAULT NULL,
  `esiccardkycnumber` text DEFAULT NULL,
  `esiccardnumber` text DEFAULT NULL,
  `esiccardremark` text DEFAULT NULL,
  `today_date` date DEFAULT NULL,
  `your_place` text DEFAULT NULL,
  `your_name` text DEFAULT NULL,
  `join_date` date DEFAULT NULL,
  `UAN_ALLOTED` text DEFAULT NULL,
  `today_dates` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `taxdeduction`
--

CREATE TABLE `taxdeduction` (
  `id` int(11) NOT NULL,
  `end_year` date DEFAULT NULL,
  `name_and_address` text DEFAULT NULL,
  `permanent_accountno` text DEFAULT NULL,
  `residential_status` text DEFAULT NULL,
  `name_and_address_employer` text DEFAULT NULL,
  `tan_of_employer_ito` text DEFAULT NULL,
  `permanent_account_number` text DEFAULT NULL,
  `period_of_employment` date DEFAULT NULL,
  `total_amount_of_salary` text DEFAULT NULL,
  `total_amount_house_allowance` text DEFAULT NULL,
  `value_of_perquistes_and_amount` text DEFAULT NULL,
  `total_of_colume` text DEFAULT NULL,
  `amount_deducted_in_respesct` text DEFAULT NULL,
  `total_of_tax_deducteddu_in_the_year` text DEFAULT NULL,
  `remark` text DEFAULT NULL,
  `your_name` text DEFAULT NULL,
  `verified_today` date DEFAULT NULL,
  `day_of_year` date DEFAULT NULL,
  `name_emp_address` text DEFAULT NULL,
  `permanent_account` text DEFAULT NULL,
  `year_endingfrom` date DEFAULT NULL,
  `year_endingto` date DEFAULT NULL,
  `name_of_emp` text DEFAULT NULL,
  `tan_of_employer` text DEFAULT NULL,
  `acommodation_is_unfurnished` text DEFAULT NULL,
  `value_of_acommodation` text DEFAULT NULL,
  `cost_of_furniture` text DEFAULT NULL,
  `perquisite_value_of_furniture` text DEFAULT NULL,
  `total_of_column1` text DEFAULT NULL,
  `rent` text DEFAULT NULL,
  `value_of_perquisite` text DEFAULT NULL,
  `name_of_employee` text DEFAULT NULL,
  `whether_any_conveyance` text DEFAULT NULL,
  `remuneration12` text DEFAULT NULL,
  `value13` text DEFAULT NULL,
  `estimated_value14` text DEFAULT NULL,
  `employer_contribution15` text DEFAULT NULL,
  `interest16` text DEFAULT NULL,
  `total_of_columns17` text DEFAULT NULL,
  `policy` text DEFAULT NULL,
  `Date5` date DEFAULT NULL,
  `gross_amount` text DEFAULT NULL,
  `qualifying_amount` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` text DEFAULT NULL,
  `password` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'IPU@gmail.com', '12345'),
(2, 'admin', '12345');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `employeeoboarding`
--
ALTER TABLE `employeeoboarding`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `inductionforminsurance`
--
ALTER TABLE `inductionforminsurance`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `informationform`
--
ALTER TABLE `informationform`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `newjoiningforminsurance`
--
ALTER TABLE `newjoiningforminsurance`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `providentfund`
--
ALTER TABLE `providentfund`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `taxdeduction`
--
ALTER TABLE `taxdeduction`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `employeeoboarding`
--
ALTER TABLE `employeeoboarding`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inductionforminsurance`
--
ALTER TABLE `inductionforminsurance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `informationform`
--
ALTER TABLE `informationform`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `newjoiningforminsurance`
--
ALTER TABLE `newjoiningforminsurance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `providentfund`
--
ALTER TABLE `providentfund`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `taxdeduction`
--
ALTER TABLE `taxdeduction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
