from teachmax.aibackend.teacherGPTMaker import TeacherGPTMaker
from teachmax.aibackend.grading import Grade
import pandas

obj1 = Grade("/home/tyler/Downloads/Citizen Grad Paragraph 1.pdf").parseDict()
obj2 = Grade("/home/tyler/Downloads/Citizen Grad Paragraph 2.pdf").parseDict()
df = pandas.DataFrame([obj1,obj2])

print(df.to_excel("outputs/grades.xlsx"))