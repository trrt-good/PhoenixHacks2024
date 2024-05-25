from teacherGPTMaker import TeacherGPTMaker

teacherGPT = TeacherGPTMaker(
    name = "John Conlin",
    subject= "Math",
    class_name= "Calculus BC",
    syllabus_pdf= "path/to/syllabus.pdf",
    lesson_plan_pdf= "path/to/lesson_plan.pdf",
    class_schedule_pdf= "path/to/class_schedule.pdf"
)

print(teacherGPT("what's the retake policy?"))