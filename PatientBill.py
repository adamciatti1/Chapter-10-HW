import PatientClass as cc
import ProcedureClass as bb 

VETERAN_RATE = 0.4

patient1 = cc.Patient(1,'Matt Jones','123 Main St, Waco Tx 76706','254-555-7415', True)

procedure1 = bb.Procedure('Physical Exam', '2/15/2022', 'Dr. Irvine', 250, 1)
procedure2 = bb.Procedure('MRI', '2/15/2022', 'Dr. Hamilton', 1500, 1)
procedure3 = bb.Procedure('CT Scan', '2/17/2022', 'Dr. Drey', 1200, 2)
procedure_list = [procedure1, procedure2, procedure3]

total_charges = procedure1.get_charges() + procedure2.get_charges()

#Final Output
print('*** Patient Bill ***')
print('Name:', patient1.get_PatientName())
print('Address:', patient1.get_PatientAddress())
print('Phone:', patient1.get_PatientPhone())

row = 0
total = 0.0
for rows in procedure_list:
    if procedure_list[row].get_PatientID() == patient1.get_PatientID():
        print('')
        print('Procedure:', procedure_list[row].get_procedure())
        print('Date:', procedure_list[row].get_date())
        print('Practitioner:', procedure_list[row].get_practitioner())
        print('Charge: ' + '$' + format(float(procedure_list[row].get_charges()), ',.2f'))
        total += procedure_list[row].get_charges()
        row += 1

if patient1.get_Veteran() == True:
    total *= (1- VETERAN_RATE)

print('\nTotal Charges: ' + '$' + format(total, ',.2f'))

