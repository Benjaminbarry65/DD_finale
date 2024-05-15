from django import forms



class BabyForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    gender = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    location = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    name_dropper = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    time_arrival = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control'}), required=False)
    name_parents = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    amount_paid = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'step': 0.1}), required=False)
    period_stay = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    #baby_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        gender = cleaned_data.get('gender')
        age = cleaned_data.get('age')
        location = cleaned_data.get('location')
        name_dropper = cleaned_data.get('name_dropper')
        time_arrival = cleaned_data.get('time_arrival')
        name_parents = cleaned_data.get('name_parents')
        amount_paid = cleaned_data.get('amount_paid') 
        period_stay = cleaned_data.get('period_stay') 
        #baby_number = cleaned_data.get('baby_number')

        if not name or not gender or not age or not location or not name_dropper or not time_arrival or not name_parents or not amount_paid or not period_stay:
            self.add_error('name', 'Please add a name')
            self.add_error('gender', 'Please add a gender')
            self.add_error('age', 'Please add the age')
            self.add_error('location', 'Please add the location')
            self.add_error('name_dropper', 'Please add name of person dropping baby')
            self.add_error('time_arrival', 'Please add the arrival time')
            self.add_error('name_parents', 'Please add name of babys parent')
            self.add_error('amount_paid', 'Please add the amount paid')
            self.add_error('period_stay', 'Please add the period of stay')
            #self.add_error('baby_number', 'Please add the baby number')
        elif len(amount_paid) < 10000:
            self.add_error('amount_paid', 'Amount paid must be atleast Ugx10,000')

        return cleaned_data    



class PickupForm(forms.Form):
    #baby_name = forms.ForeignKey(BabyForm, on_delete=models.CASCADE, null=False, blank=False, default=0)
    #baby_dropper = forms.ForeignKey(BabyForm, on_delete=models.CASCADE)
    #baby_arrival = forms.ForeignKey(BabyForm, on_delete=models.CASCADE)
    baby_picked = forms.DateTimeField()  
    name_picker = forms.CharField(max_length=100)
    comment = forms.CharField(max_length=300)




class ItemForm(forms.Form):
    item_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    item_quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        item_name = cleaned_data.get('item_name')
        item_quantity = cleaned_data.get('item_quantity')

        if not item_name or not item_quantity:
            self.add_error('item_name', 'Please add an item name')
            self.add_error('item_quantity', 'Please add an item quantity')
        elif item_quantity < 1:
            self.add_error('item_quantity', 'Item quantity must be atleast 1')

        return cleaned_data    