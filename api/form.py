from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Client


# Form for nem client
class ClientCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Client
        fields = ('avatar',  'gender', 'first_name', 'last_name', 'email')

       
class ClientChangeForm(UserChangeForm):
    class Meta:
        model = Client
        fields = ('avatar',  'gender', 'first_name', 'last_name', 'email')

        