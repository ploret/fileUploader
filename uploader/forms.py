from django import forms

class UploadFileForm(forms.Form):
    """ Upload form """
    title = forms.CharField(max_length=50)
    file = forms.FileField()