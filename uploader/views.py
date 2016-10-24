from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .functions import handle_uploaded_file


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/upload')
    else:
        form = UploadFileForm()
    return render(request, 'upload/upload.html', {'form': form})