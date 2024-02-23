
import os
from django.shortcuts import render
from django.conf import settings
from .forms import UploadFileForm
from .pdf_processor import extract_text_from_file

def index(request):
    extracted_data = None
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file_path = os.path.join(settings.MEDIA_ROOT, file.name)
            with open(file_path, 'wb') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            extracted_data = extract_text_from_file(file_path)
        else:
            extracted_data = "Error: No file uploaded"
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form, 'extracted_data': extracted_data})

