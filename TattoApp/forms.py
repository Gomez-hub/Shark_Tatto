from django import forms
from .models import contacto

# class UserRegisterForm(UserCreationForm):
# 	email = forms.EmailField()
# 	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
# 	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

# 	class Meta:
# 		model = User
# 		fields = ['username', 'email', 'password1', 'password2']
# 		help_texts = {k:"" for k in fields }

# class PostForm(forms.ModelForm):
# 	content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder': '¿Qué está pasando?'}), required=True)

# 	class Meta:
# 		model = Post
# 		fields = ['content']


class ContactoForm(forms.ModelForm):
    
	class Meta:
		model = contacto
		# fields = ["name", "Email", "Message"]
		fields = "__all__"