from enum import Enum
from typing import Optional
from dataclasses import dataclass
#ENUM ( hằng số )
class ReporterRole(str , Enum):
    VICTIM = "victim"
    WITNESS= "witness"
    ANONYMOUS ="anonymous"
    
    
class ReporterInfo:
    role : ReporterRole # public
    phone_number: Optional[str] = None # private
    name : str|None # public
    allow_call_back : bool = False # public
    
    
    """ Nếu người báo là ẩn danh:
    
    - Không được có tên
    - Không được có số điện thoại
    - Không được cho phép gọi lại
    
        Ngược lại (không ẩn danh):
    - Nếu cho phép gọi lại thì bắt buộc phải có số điện thoại"""
    
    
    "set attribute ko cho sua du lieu sau khi khai bao"
    def __init__(self,role,name,phone_number,allow_call_back):
        object.__setattr__(self, "role", role)
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "phone_number", phone_number)
        object.__setattr__(self, "allow_call_back", allow_call_back)
        
        if(self.role == ReporterRole.ANONYMOUS):
            if(self.name is not None or self.phone_number is not None):
                raise ValueError("NO PHONENUMBER AND NAME FOR ANONYMOUS")
            if(self.allow_call_back == True):
                raise ValueError(" no call back for ANONYMOUS ")
        else:
            if(self.allow_call_back == True and self.phone_number is None):
                raise ValueError("require phone number to callback")
                
    def __setattr__(self, name, value):
        raise ValueError("Value is immutable")     
        
    def getReporterInfo(self):
        return {
            "role": self.role,
            "name": self.name,
            "phone_number": self.phone_number,
            "allow_call_back": self.allow_call_back,
        }
    
person = ReporterInfo(
    role = ReporterRole.VICTIM,
    name = "Do Minh Triet",
    phone_number = "0388550712",
    allow_call_back = True
)

   
mang = person.getReporterInfo()
for name in mang.values():
    print(name,"\n")


        
        
    
    