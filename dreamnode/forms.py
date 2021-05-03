from django import forms
 
class ContactFormEmail(forms.Form):
	from_email = forms.EmailField(required=True)
	subject = forms.CharField(required=True)
	message = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter message', 'rows':'8', 'cols':'40'}), required=True)
 	
 	

 	