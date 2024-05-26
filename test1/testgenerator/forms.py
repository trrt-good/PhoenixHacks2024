from django import forms

class UploadForms(forms.Form):
    file1 = forms.FileField(label='SampleTest')