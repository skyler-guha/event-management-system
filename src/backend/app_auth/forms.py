from django import forms
from app_users.models import CustomUser
#from app_core.models import Event, Ticket, Notification

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'role']

    def save(self, commit=True) -> CustomUser:
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["username"]
        user.set_password(self.cleaned_data["password"])
        user.role = self.cleaned_data["role"]
        if commit:
            user.save()
        return user
