class Procedure:
    
    def __init__(self,procedure,date,practitioner,charges,ID):
        self.__procedure = procedure
        self.__date = date
        self.__practitioner = practitioner
        self.__charges = charges
        self._PatientID = ID

    def set_procedure(self,procedure):
        self.__procedure = procedure

    def set_date(self,date):
        self.__date = date

    def set_practitioner(self, practitioner):
       self.__practitioner = practitioner 

    def set_charges(self, charges):
        self.__charges = charges

    def set_PatientID(self, ID):  
        self._PatientID = ID

    def get_procedure(self):
        return self.__procedure

    def get_date(self):
        return self.__date

    def get_practitioner(self):
       return self.__practitioner 

    def get_charges(self):
        return self.__charges

    def get_PatientID(self):  
        return self._PatientID