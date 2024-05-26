from django import forms


class UploadFileForm(forms.Form):
    file1 = forms.FileField(label='Syllabus')
    file2 = forms.FileField(label='Lesson Plans')
    file3 = forms.FileField(label='Class Schedule')
    file4 = forms.CharField(label='Teacher Name', max_length=100)
    file5 = forms.CharField(label='Class Name', max_length=100)
    file6 = forms.CharField(label='Subject', max_length=100)


class ChatForm(forms.Form):
    text1 = forms.CharField(label='message', max_length=500 )
    