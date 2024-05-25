from groq import Groq
from PyPDF2 import PdfReader

class TeacherGPTMaker:
    def __init__(self, full_name, subject, class_name, syllabus_pdf, lesson_plan_pdf, class_schedule_pdf):
        self.full_name = full_name
        self.subject = subject
        self.class_name = class_name
        self.syllabus = self.pdf_to_text(syllabus_pdf)
        self.lesson_plan = self.pdf_to_text(lesson_plan_pdf)
        self.class_schedule = self.pdf_to_text(class_schedule_pdf)
        self.system_prompt = f"""
You are {full_name}, a {subject} teacher teaching {class_name}. You will be interacting with your students. Your syllabus, lesson plans, and class schedule is below:

Class Syllabus:
{self.syllabus}

Lesson plans:
{self.lesson_plan}

Class Schedule:
{self.class_schedule}

"""
        self.groq_client = Groq(api_key="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")

    def pdf_to_text(self, pdf_file):
        reader = PdfReader(pdf_file)
        page = reader.pages[0]
        return page.extract_text()

    def __call__(self, user_prompt):
        messages = [{"role": "system", "content": self.system_prompt}, {"role": "user", "content": user_prompt}]
        response = self.groq_client.chat.completions.create(
            model="llama3-70b-8192",
            messages=messages,
            temperature=0.0,
            max_tokens=4096
        )
        return response.choices[0].message.content.strip()