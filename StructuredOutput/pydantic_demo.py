from pydantic import BaseModel, EmailStr,Field
from typing import Optional

class Student(BaseModel):

    name : str
    age : Optional[int]=None
    email : EmailStr
    cgpa : float = Field(gt = 0, lt=10,default = 2.5, description = 'A decimal number representing CGPA of the student')


one_student = {'name':'Kareem','age':32,'email':"abdulkareem.bscs4971@student.iiu.edu.pk"}

student = Student(**one_student)


print(dict(student))

# Let say in line no 10 i pass string instead of int Behind the scenes it will be implicitly converted to int 


