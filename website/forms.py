from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Request, Event, UserProfile, RequestStatusChoice, RequesterStatusChoice, MaintainerStatusChoice, \
    AuditorStatusChoice, EventStatusChoice, EventDurationChoice, EventTypeChoice, HardDriveStatusChoice, \
    HardDriveClassificationChoice, HardDriveBootTestStatusChoice, HardDriveSizeChoice


# django inheritance forms
################################################################
class DateInput(forms.DateInput):
    input_type = 'date'


# authentication forms
################################################################
class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        widgets = {
            # inheriting Django's password field to remain hidden when typing
            'password': forms.PasswordInput()
        }


# creation forms
################################################################
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]
        labels = {
            'first_name': '*First Name',
            'last_name': '*Last Name',
            'username': '*Username',
            'email': '*Email',
        }


class RegisterFormAddOns(ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'direct_supervisor_email',
            'branch_chief_email',
        ]
        labels = {
            'direct_supervisor_email': '*Direct Supervisor Email',
            'branch_chief_email': '*Branch Chief Email'
        }


class CreateRequestForm(ModelForm):
    class Meta:
        model = Request
        fields = [
            'requester',
            'event',
            'pickup_date',
            'number_of_classified_hard_drives_needed',
            'number_of_unclassified_hard_drives_needed',
            'comment'
        ]
        widgets = {
            'pickup_date': DateInput()
        }
        # override label names something more user friendly
        labels = {
            'requester': '*Requester Name',
            'event': '*Event',
            'pickup_date': '*Pickup Date',
            'number_of_classified_hard_drives_needed': '*Quantity(C.H.D) requested',
            'number_of_unclassified_hard_drives_needed': '*Quantity(U.H.D) requested',
            'comment': 'Additional requests/comments',
        }


class CreateEventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'name',
            'description',
            'location',
            'lead',
            'participants',
            'type',
            'start_date',
            'end_date'
        ]
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }
        labels = {
            'name': '*Event Name',
            'description': '*Event Description',
            'location': '*Event Location',
            'lead': '*Event Lead',
            'participants': '*Event Participants',
            'type': '*Event Type',
            'start_date': '*Event Start Date',
            'end_date': '*Event End Date',
        }


# update forms
################################################################

class UpdateProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'profile_picture',
            'first_name',
            'last_name',
            'email',
            'direct_supervisor_email',
            'branch_chief_email',
        ]


class UpdateRequestForm(ModelForm):
    class Meta:
        model = Request
        fields = [
            'requester',
            'pickup_date',
            'number_of_classified_hard_drives_needed',
            'number_of_unclassified_hard_drives_needed',
            'comment'
        ]
        widgets = {
            'pickup_date': DateInput()
        }
        # override label names something more user friendly
        labels = {
            'requester': 'Requester Name',
            'pickup_date': '*Pickup Date',
            'number_of_classified_hard_drives_needed': '*Quantity(C.H.D) requested',
            'number_of_unclassified_hard_drives_needed': '*Quantity(U.H.D) requested',
            'comment': 'Additional requests/comments',
        }


class UpdateEventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'description',
            'location',
            'lead',
            'participants',
            'type',
            'start_date',
            'end_date'
        ]
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }
        labels = {
            'description': '*Event Description',
            'location': '*Event Location',
            'lead': '*Event Lead',
            'participants': '*Event Participants',
            'type': '*Event Type',
            'start_date': '*Event Start Date',
            'end_date': '*Event End Date',
        }


# configuration forms
################################################################
class CreateOrUpdateRequestStatusChoiceForm(ModelForm):
    class Meta:
        model = RequestStatusChoice
        fields = '__all__'


class CreateOrUpdateRequesterStatusChoiceForm(ModelForm):
    class Meta:
        model = RequesterStatusChoice
        fields = '__all__'


class CreateOrUpdateMaintainerStatusChoiceForm(ModelForm):
    class Meta:
        model = MaintainerStatusChoice
        fields = '__all__'


class CreateOrUpdateAuditorStatusChoiceForm(ModelForm):
    class Meta:
        model = AuditorStatusChoice
        fields = '__all__'


class CreateOrUpdateEventStatusChoiceForm(ModelForm):
    class Meta:
        model = EventStatusChoice
        fields = '__all__'


class CreateOrUpdateEventDurationChoiceForm(ModelForm):
    class Meta:
        model = EventDurationChoice
        fields = '__all__'


class CreateOrUpdateEventTypeChoiceForm(ModelForm):
    class Meta:
        model = EventTypeChoice
        fields = '__all__'


class CreateOrUpdateHardDriveStatusChoiceForm(ModelForm):
    class Meta:
        model = HardDriveStatusChoice
        fields = '__all__'


class CreateOrUpdateHardDriveClassificationChoiceForm(ModelForm):
    class Meta:
        model = HardDriveClassificationChoice
        fields = '__all__'


class CreateOrUpdateHardDriveBootTestStatusChoiceForm(ModelForm):
    class Meta:
        model = HardDriveBootTestStatusChoice
        fields = '__all__'


class CreateOrUpdateHardDriveSizeChoiceForm(ModelForm):
    class Meta:
        model = HardDriveSizeChoice
        fields = '__all__'
