from django import forms

from user.models import User, Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "nick_name",
            "phone_number",
            "sex",
            "birth_year",
            "birth_month",
            "birth_day",
            "avatar",
            "location",
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "id",
            "location",
            "min_distance",
            "max_distance",
            "max_data_age",
            "min_data_age",
            "date_sex",
            "virbation",
            "friend_only",
            "auto_play",
        ]
    
    def clean_min_data_age(self):
        """自定义了clean方法"""
        cleaned_data = super().clean()
        max_data_age = cleaned_data.get("max_data_age", 0)
        min_data_age = cleaned_data.get("min_data_age", -1)
        if min_data_age > max_data_age:
            raise forms.ValidationError(' min_data_age > max_data_age')
    
    def clean_min_data_distance(self):
        cleaned_data = super().clean()
        max_distance = cleaned_data.get("max_distance", 0)
        min_distance = cleaned_data.get("min_distance", -1)
        if min_distance > max_distance :
            raise forms.ValidationError(' min_distance > max_distance ')
    
        