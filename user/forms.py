from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label= "Kullanıcı Adı")
    password = forms.CharField(label= "Parola", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı Adı")
    password = forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput) 
    confirmpassword = forms.CharField(max_length=20, label="Parolayı Doğrula", widget=forms.PasswordInput)
    
    def clean(self):
        data = self.cleaned_data
        username = data.get("username")
        password = data.get("password")
        confirm = data.get("confirmpassword")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolar Eşleşmiyor!")
        values = {
            "username": username,
            "password": password
        }
        return values