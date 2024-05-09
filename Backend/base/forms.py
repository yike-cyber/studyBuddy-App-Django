from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model=Room
        fields = '__all__'  # or can filter the field as list
        exclude = ['host','participants']