from django import forms
from .models import Enterpriseprofile

class EnterpriseprofileForm(forms.ModelForm):
	class Meta:
		model = Enterpriseprofile
		fields = ('companyName', 'descriptor', 'profileImage', 'bannerImage', 
			    'businessName', 'industry', 'legalId', 'phone', 'email',
			    'web', 'address', 'us', 'offer', 'searchKeywords',)