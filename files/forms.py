# -*- coding: utf-8 -*-
from django import forms

class FileForm(forms.Form):
	file = forms.FileField(
	    label='Select a file',
	    help_text='max. 40 GB'
	)