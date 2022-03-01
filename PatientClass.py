class Patient:

    def __init__(self,ID,name,address,phone,veteran):
        self.__PatientID = ID 
        self.__PatientName = name
        self.__PatientAddress = address
        self.__PatientPhone = phone
        self.__Veteran = veteran

    def set_PatientID(self,ID):
        self.__PatientID = ID

    def set_PatientName(self,name):
        self.__PatientName = name
    
    def set_PatientAddress(self,address):
        self.__PatientAddress = address

    def set_PatientPhone(self,phone):
        self.__PatientPhone = phone

    def set_Veteran(self,veteran):
        self.__Veteran = veteran

    def get_PatientID(self):
        return self.__PatientID

    def get_PatientName(self):
        return self.__PatientName 
    
    def get_PatientAddress(self):
        return self.__PatientAddress
    
    def get_PatientPhone(self):
        return self.__PatientPhone

    def get_Veteran(self):
        return self.__Veteran