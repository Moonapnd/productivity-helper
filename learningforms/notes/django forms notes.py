
>>> from django import forms
>>> class ContactForm(forms.Form):
...     subject = forms.CharField(max_length=200)
...     message = forms.CharField(max_length=200)
...     sender = forms.CharField(max_length=200)
...     cc_myself = forms.BooleanField(required=False)
...

>>> # create an unbound Form instance
>>> f = ContactForm()

>>> # bind data to a Form instance
>>> data = {'subject' 's' 'message' 'm' 'sender' 's' 'cc_myself' True}
>>> f = ContactForm(data)
>>> f.is_bound
True
>>> f.is_valid()
True

>>> # validate bound form
>>> data = {'subject' '' 'message' 'm' 'sender' 's' 'cc_myself' True}
>>> f = ContactForm(data)
>>> f.is_valid()
False
>>> f.errors
{'subject' ['This field is required.']}
>>> f.errors.as_data()
{'subject' [ValidationError(['This field is required.'])]}
>>> f.errors.as_json()
'{"subject" [{"message" "This field is required." "code" "required"}]}'

>>> # validate unbound form
>>> f = ContactForm()
>>> f.is_valid()
False
>>> f.errors
{}

>>> # dynamic initial values

>>> f = ContactForm(initial=data)
>>> print(f)
<tr>
    <th><label for="id_subject">Subject:</label></th>
    <td><input type="text" name="subject" maxlength="200" required id="id_subject"></td>
</tr>
<tr>
    <th><label for="id_message">Message:</label></th>
    <td><input type="text" name="message" value="m" maxlength="200" required id="id_message"></td>
</tr>
<tr>
    <th><label for="id_sender">Sender:</label></th>
    <td><input type="text" name="sender" value="s" maxlength="200" required id="id_sender"></td>
</tr>
<tr>
    <th><label for="id_cc_myself">Cc myself:</label></th>
    <td><input type="checkbox" name="cc_myself" id="id_cc_myself" checked></td>
</tr>


>>> f = ContactForm(data)
>>> print(f) # this will render the also an error message because 'subject' is empty
<tr>
    <th><label for="id_subject">Subject:</label></th>
    <td>
        <ul class="errorlist">
            <li>This field is required.</li>
        </ul>
        <input type="text" name="subject" maxlength="200" required id="id_subject">
    </td>
</tr>
<tr>
    <th><label for="id_message">Message:</label></th>
    <td><input type="text" name="message" value="m" maxlength="200" required id="id_message"></td>
</tr>
<tr>
    <th><label for="id_sender">Sender:</label></th>
    <td><input type="text" name="sender" value="s" maxlength="200" required id="id_sender"></td>
</tr>
<tr>
    <th><label for="id_cc_myself">Cc myself:</label></th>
    <td><input type="checkbox" name="cc_myself" id="id_cc_myself" checked></td>
</tr>

# ommit html id attribute on form elements
>>> f = ContactForm(initial=data, auto_id=False)
>>> print(f)
<tr><th>Subject:</th><td><input type="text" name="subject" value="s" maxlength="200" required></td></tr>
<tr><th>Message:</th><td><input type="text" name="message" value="m" maxlength="200" required></td></tr>
<tr><th>Sender:</th><td><input type="text" name="sender" value="s" maxlength="200" required></td></tr>
<tr><th>Cc myself:</th><td><input type="checkbox" name="cc_myself" checked></td></tr>

>>> # checking wich form data has changed
>>> # this is helpfull whene we recieve request.POST --- f = ContactForm(request.POST, initial=old_data) ---
>>> data = {'subject' 'new subject' 'message' 'm' 'sender' 's' 'cc_myself' True}
>>> old_data = {'subject' 's' 'message' 'm' 'sender' 's' 'cc_myself' True}
>>> f = ContactForm(old_data, initial=old_data)
>>> f.has_changed()
False
>>> f = ContactForm(data, initial=old_data)
>>> f.has_changed()
True
>>> f.changed_data
['subject']

>>> # accessing 'clean' data
>>> f = ContactForm(data)
>>> f.is_valid()
True
>>> f.cleaned_data
{'subject' 'new subject' 'message' 'm' 'sender' 's' 'cc_myself' True}

>>> data = {'subject' '' 'message' 'm' 'sender' 's' 'cc_myself' True}
>>> f = ContactForm(data)
>>> f.is_valid()
False
>>> f.cleaned_data
{'message' 'm' 'sender' 's' 'cc_myself' True}

>>> # optional field are included in cleaned_data even if data did not include a value
>>> data = {'subject' '' 'message' 'm' 'sender' 's'}
>>> f = ContactForm(data)
>>> data = {'subject' 's' 'message' 'm' 'sender' 's'}
>>> f = ContactForm(data)
>>> f.is_valid()
True
>>> f.cleaned_data
{'subject' 's' 'message' 'm' 'sender' 's' 'cc_myself' False}

>>> f = ContactForm(data, auto_id=False)
>>> print(f)
<tr><th>Subject:</th><td><input type="text" name="subject" value="s" maxlength="200" required></td></tr>
<tr><th>Message:</th><td><input type="text" name="message" value="m" maxlength="200" required></td></tr>
<tr><th>Sender:</th><td><input type="text" name="sender" value="s" maxlength="200" required></td></tr>
<tr><th>Cc myself:</th><td><input type="checkbox" name="cc_myself"></td></tr>

>>> print(f.as_p())
<p>Subject: <input type="text" name="subject" value="s" maxlength="200" required></p>
<p>Message: <input type="text" name="message" value="m" maxlength="200" required></p>
<p>Sender: <input type="text" name="sender" value="s" maxlength="200" required></p>
<p>Cc myself: <input type="checkbox" name="cc_myself"></p>

>>> print(f.as_ul())
<li>Subject: <input type="text" name="subject" value="s" maxlength="200" required></li>
<li>Message: <input type="text" name="message" value="m" maxlength="200" required></li>
<li>Sender: <input type="text" name="sender" value="s" maxlength="200" required></li>
<li>Cc myself: <input type="checkbox" name="cc_myself"></li>

>>> # you could style your errors using class='errorlist'
>>> data = {'subject' '' 'message' 'm' 'sender' 's'}
>>> f = ContactForm(data, auto_id=False)
>>> f.is_valid()
False
>>> print(f.as_p())
<ul class="errorlist"><li>This field is required.</li></ul>
<p>Subject: <input type="text" name="subject" maxlength="200" required></p>
<p>Message: <input type="text" name="message" value="m" maxlength="200" required></p>
<p>Sender: <input type="text" name="sender" value="s" maxlength="200" required></p>
<p>Cc myself: <input type="checkbox" name="cc_myself"></p>

>>> print(f.as_ul())
<li><ul class="errorlist"><li>This field is required.</li></ul>Subject: <input type="text" name="subject" maxlength="200" required></li>
<li>Message: <input type="text" name="message" value="m" maxlength="200" required></li>
<li>Sender: <input type="text" name="sender" value="s" maxlength="200" required></li>
<li>Cc myself: <input type="checkbox" name="cc_myself"></li>

>>> # also It’s pretty common to style form rows and fields that are required or have errors. For example, you might want to present required form rows in bold and highlight errors in red.
>>> class ContactForm(forms.Form):
  ...     error_css_class = 'error'
  ...     required_css_class = 'required'
  ...     ... 
  ...


