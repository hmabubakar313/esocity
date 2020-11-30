from django import forms

class  LoginForm(forms.Form):
        first_name = forms.CharField(max_length=100)
        email = forms.CharField(max_length=100)
        password = forms.IntegerField(max_value=20)
        reg_no= forms.IntegerField(max_value=20)
        f = LoginForm( )
        print(f.as_p())
