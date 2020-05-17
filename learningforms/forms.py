from django import forms

CHOICES = [('1', 'First'), ('2', 'Second'), ('4', 'forth'), ('5', 'fifth')]
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']

class ContactForm(forms.Form):
    char_field = forms.CharField(max_length=200)
    textarea_field = forms.CharField(widget=forms.Textarea, max_length=200)
    ###### define some widget attributes (method 1) ######
    # textarea_field2 = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), max_length=200)
    email_field = forms.EmailField(required=False)
    choice_field = forms.ChoiceField(choices=CHOICES)
    multiple_choice_field = forms.MultipleChoiceField(choices=CHOICES)
    checkbox_field = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=CHOICES)
    radio_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    date_field = forms.DateField(widget=forms.SelectDateWidget())
    boolean_field = forms.BooleanField(required=False)
    url_field = forms.URLField()

    ####### define some widget attributes (method 2) #####
    char_field.widget.attrs.update({'class': 'form-control', 'required': False})


    ####### define some widget attributes (method 3) useful when working with forms.ModelForm #####
    """
    class CommentForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['email_field'].widget.attrs.update({'class' 'form-control'})
            self.fields['url_field'].widget.attrs.update({'class' 'form-control'})
    """

    ####### display the form in template #####
    """
       {# {{ form.as_p }} #}
       {% for field in form %}
           <div class="fieldWrapper">
               {{ field.errors }}
               {{ field.label_tag }} {{ field }}
           </div>
       {% endfor %}
    """

    ####### the previous code will result this html form #####
    """
    <div class="fieldWrapper">
        <label for="id_char_field">Char field:</label>
        <input type="text" name="char_field" maxlength="200" class="form-control" required="" id="id_char_field">
    </div>

    <div class="fieldWrapper">
        <label for="id_textarea_field">Textarea field:</label>
        <textarea name="textarea_field" cols="40" rows="10" maxlength="200" required="" id="id_textarea_field"></textarea>
    </div>
    ...

    """
