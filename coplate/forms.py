
from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname", "kakao_id", "address"]

    def signup(self, request, user):
      user.nickname = self.cleaned_data["nickname"]
      user.nickname = self.cleaned_data["kakao_id"]
      user.nickname = self.cleaned_data["address"]
      user.save()