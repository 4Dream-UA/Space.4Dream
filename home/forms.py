from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()

class RegisterInviteForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "email", "position")
