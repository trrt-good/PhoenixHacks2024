from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm, ChatForm
from teacherGPTMaker import TeacherGPTMaker


# Create your views here.
#def index(request):
#    return HttpResponse("helloworld")

#def temp(name):
#    return lof"this is my name:{name}"
#def chatai(messages) :
#    return "chatresponse"
system_text = 'Ask a Question and I will answer here'
def chat(request):
    system_text = 'Ask a Question and I will answer here'
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            message = request.POST.get('text1', '')
        
        teacherGPT = sendInfo()
        system_text = teacherGPT(message) + '\n'


    else:
        form = ChatForm()

    return render(request, 'chatbot.html', {'form': form, 'system_text':system_text})


def handle_uploaded_file(f, letter):
    with open('uploaded_files/' + letter + '.pdf', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        #form1 = UploadFileForm(request.POST)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file1'], 'Syllabus')
            handle_uploaded_file(request.FILES['file2'], 'LessonPlans')
            handle_uploaded_file(request.FILES['file3'], 'ClassSchedule')

            teachName = request.POST.get('file4', '')
            className = request.POST.get('file5', '')
            subject = request.POST.get('file6', '')

            data_strings = [
            f"{teachName}\n",
            f"{className}\n",
            f"{subject}\n"
            ]

            with open ('uploaded_files/teacherinfo.txt', 'w') as file:
                file.writelines(data_strings)

            sendInfo()

            return HttpResponseRedirect('/chatbot/chat')
    else:
        form = UploadFileForm()
        
    return render(request, 'upload.html', {'form': form})

# def convert_pdf():
    
#     letters = ['S', 'L', 'C']
#     for x in letters:
#         reader = PdfReader('uploaded_files/LessonPlans/'+x+'.pdf') 
#         pages = len(reader.pages)
#         for i in range(pages)
#             with open('uploaded_files/LessonPlans/'+x '.txt', 'w') as f:

def sendInfo():
    name1 = ''
    subject1 = ''
    class_name1 = ''
    with open('uploaded_files/teacherinfo.txt', 'r') as file:
        name1 = file.readline()
        name1.strip()
        class_name1 = file.readline()
        class_name1.strip()
        subject1 = file.readline()
        subject1.strip()
        teacherGPT = TeacherGPTMaker(
            full_name = name1,
            subject= subject1,
            class_name= class_name1,
            syllabus_pdf= "uploaded_files/Syllabus.pdf",
            lesson_plan_pdf= "uploaded_files/LessonPlans.pdf",
            class_schedule_pdf= "uploaded_files/ClassSchedule.pdf"
        )

        print(teacherGPT("what's the retake policy?"))
    return teacherGPT


    

