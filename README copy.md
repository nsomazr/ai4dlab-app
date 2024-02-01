# ai4dlab-app
Deployable AI4D Lab Website


TABLE dportal_patientdata 
INTO OUTFILE '/var/lib/mysql-files/patient_data_collected.csv'
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY ''
LINES TERMINATED BY 'n';