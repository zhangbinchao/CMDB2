from django import forms
from . import models

class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['name', 'password']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, *kwargs)
        self.fields['name'].label = '用户名'
        self.fields['password'].label = '密码'


class RegisterForm(forms.Form):
    asset_type_choice = (
		('server', '服务器'),
		('networkdevice', '网络设备'),
		('storagedevice', '存储设备'),
		('securitydevice', '安全设备'),
		('software', '软件资产'),
	)

    asset_status = (
		(0, '在线'),
		(1, '下线'),
		(2, '未知'),
		(3, '故障'),
		(4, '备用'),
	)
    asset_type = forms.ChoiceField(label='设备类型',choices=asset_type_choice)
    name = forms.CharField(label='设备名称',max_length=128,widget=forms.TextInput(attrs={'class':'form-control'}))
    sn = forms.FloatField(label='序列号',  widget=forms.TextInput(attrs={'class': 'form-control'}))
    manufacturer = forms.CharField(label='生产厂家', max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(label='设备状态',choices=asset_status)
    idc = forms.CharField(label='机房', max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    purchase_day = forms.DateField(label='购买时间',  widget=forms.TextInput(attrs={'class': 'form-control'}))

class EditForm(forms.Form):
    asset_type_choice = (
		('server', '服务器'),
		('networkdevice', '网络设备'),
		('storagedevice', '存储设备'),
		('securitydevice', '安全设备'),

	)

    asset_status = (
		(0, '在线'),
		(1, '下线'),
		(2, '未知'),
		(3, '故障'),
		(4, '备用'),
	)
    asset_type = forms.ChoiceField(label='设备类型',choices=asset_type_choice)
    name = forms.CharField(label='设备名称',max_length=128,widget=forms.TextInput(attrs={'class':'form-control'}))
    sn = forms.FloatField(label='序列号',  widget=forms.TextInput(attrs={'class': 'form-control'}))
    manufacturer = forms.CharField(label='生产厂家', max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(label='设备状态', choices=asset_status)
    idc = forms.CharField(label='机房', max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    purchase_day = forms.DateField(label='购买时间', widget=forms.TextInput(attrs={'class': 'form-control'}))
