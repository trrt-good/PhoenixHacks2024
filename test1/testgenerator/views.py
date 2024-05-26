from django.shortcuts import render
from .forms import UploadForms
from testvariations import TestVariations
# Create your views here.

def handle_uploaded_file(f, letter):
    with open('uploaded_files/' + letter + '.pdf', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def files(request):
    text = 'This is where the test will be generated'
    if request.method == 'POST':
        form = UploadForms(request.POST, request.FILES)
        #form1 = UploadFileForm(request.POST)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file1'], 'testSample')

        tests = TestVariations('uploaded_files/testSample.pdf',1)
        text = tests.generateTest()
        print(text)

        
    else:
        form = UploadForms()
        
    return render(request, 'testvariations.html', {'form': form, 'text':text})
