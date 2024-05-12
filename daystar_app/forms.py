from django import forms

class SitterForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    location = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}), required=False)
    gender = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    next_kin = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    nin = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    recomm_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    religion = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    level_education = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    contact = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        location = cleaned_data.get('location')
        dob = cleaned_data.get('dob')
        gender = cleaned_data.get('gender')
        next_kin = cleaned_data.get('next_kin')
        nin = cleaned_data.get('nin')
        recomm_name = cleaned_data.get('recomm_name')
        religion = cleaned_data.get('religion')
        level_education = cleaned_data.get('level_education')
        contact = cleaned_data.get('contact')

        if not name or not location or not dob or not gender or not next_kin or not nin or not recomm_name or not level_education or not contact:
            self.add_error('name', 'Please add a name')
            self.add_error('location', 'Please add a location')
            self.add_error('dob', 'Please add a date of birth')
            self.add_error('gender', 'Please add a gender')
            self.add_error('next_kin', 'Please add next of kin')
            self.add_error('nin', 'Please add a national id number')
            self.add_error('recomm_name', 'Please add recommenders name')
            self.add_error('level_education', 'Please add the level of education')
            self.add_error('contact', 'Please add a contact')

        return cleaned_data    