from django.forms import ModelForm

from SignUp.models import SignUp


class SignUpForm(ModelForm):
    class Meta:
        models = SignUp
        fields = "__all__"

class CourierServiceForm(ModelForm):
    class Meta:
        models = SignUp
        fields = "__all__"
