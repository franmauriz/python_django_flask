class Usuario:
     
    def __init__(self,id_user=None,username=None,password=None):
        self.__id_user = id_user
        self.__username = username
        self.__password = password
        
    def __str__(self):
        return(
            f'ID: {self.__id_user} ,'
            f'USERNAME: {self.__username} ,'
            f'PASSWORD: {self.__password}'
        )
        
    def get_username(self):
        return self.__username
    def set_username(self,username):
        self.__username = username
    
    def get_password(self):
        return self.__password
    def set_password(self,password):
        self.password = password
        
    def get_id_user(self):
        return self.__id_user
    def set_id_user(self,id_user):
        self.__id_user = id_user