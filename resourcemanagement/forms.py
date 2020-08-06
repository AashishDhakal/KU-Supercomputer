from django import forms
from .models import Application
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        exclude = ['is_approved', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Request for Resource'))
        self.helper.layout = Layout(
            Div(
                Div('name', css_class='col-md-6', ),
                Div('email', css_class='col-md-6', ),
                Div('institution', css_class='col-md-6', ),
                Div('employment_type', css_class='col-md-6', ),
                css_class='row',
            ),
            'application_purpose'
        )