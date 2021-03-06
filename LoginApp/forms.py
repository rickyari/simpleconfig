from django import forms

class LoginForm(forms.Form):

	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'field'}), max_length=50)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'field'}))


	def clean_username(self):

		username = self.cleaned_data['username']
		return username

	def clean_password(self):

		password = self.cleaned_data['password']
		return password



	