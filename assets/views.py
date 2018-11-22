from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import get_object_or_404
from . import models
from . import forms
def index(request):

    assets = models.Asset.objects.all()
    return render(request, 'assets/index.html', locals())


# def dashboard(request):
#     pass
#     return render(request, 'assets/dashboard.html', locals())


def detail(request, asset_id):
    """
    以显示服务器类型资产详细为例，安全设备、存储设备、网络设备等参照此例。
    :param request:
    :param asset_id:
    :return:
    """
    asset = get_object_or_404(models.Asset, id=asset_id)
    return render(request, 'assets/detail.html', locals())

def dashboard(request):
    total = models.Asset.objects.count()
    upline = models.Asset.objects.filter(status=0).count()
    offline = models.Asset.objects.filter(status=1).count()
    unknown = models.Asset.objects.filter(status=2).count()
    breakdown = models.Asset.objects.filter(status=3).count()
    backup = models.Asset.objects.filter(status=4).count()
    up_rate = round(upline/total*100)
    o_rate = round(offline/total*100)
    un_rate = round(unknown/total*100)
    bd_rate = round(breakdown/total*100)
    bu_rate = round(backup/total*100)
    server_number = models.Server.objects.count()
    networkdevice_number = models.NetworkDevice.objects.count()
    storagedevice_number = models.StorageDevice.objects.count()
    securitydevice_number = models.SecurityDevice.objects.count()
    software_number = models.Software.objects.count()

    return render(request, 'assets/dashboard.html', locals())


def login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['user_name'] = user.name
                    return redirect('/assets/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'assets/login.html', {"message": message})
    return render(request, 'assets/login.html')

def add(request):
    register_form = forms.RegisterForm(request.POST)
    if request.method == 'POST':
        # register_form = forms.RegisterForm(request.POST)
        message = '请检查填写内容'
        if register_form.is_valid():
            asset_type = register_form.cleaned_data['asset_type']
            name = register_form.cleaned_data['name']
            sn = register_form.cleaned_data['sn']
            manufacturer = register_form.cleaned_data['manufacturer']
            status = register_form.cleaned_data['status']
            idc = register_form.cleaned_data['idc']
            purchase_day = register_form.cleaned_data['purchase_day']

            same_sn = models.Asset.objects.filter(sn=sn)
            if same_sn:
                message = "该设备已存在"
                return render(request, 'assets/add.html', locals())

            new_equipment = models.Asset()
            new_equipment.asset_type = asset_type
            new_equipment.name = name
            new_equipment.sn = sn
            new_equipment.manufacturer = manufacturer
            new_equipment.status = status
            new_equipment.idc = idc
            new_equipment.purchase_day = purchase_day
            new_equipment.save()
            message = '添加成功'

            return redirect('/assets/index/')
    # register_form = forms.RegisterForm()
    return render(request,'assets/add.html',locals())

def edit(request,asset_id):
    edit_form = forms.EditForm(request.POST)
    if request.method == 'POST':
        if edit_form.is_valid():
            asset_type = edit_form.cleaned_data['asset_type']
            name = edit_form.cleaned_data['name']
            sn = edit_form.cleaned_data['sn']
            manufacturer = edit_form.cleaned_data['manufacturer']
            status = edit_form.cleaned_data['status']
            idc = edit_form.cleaned_data['idc']
            purchase_day = edit_form.cleaned_data['purchase_day']

            alt = models.Asset.objects.get(id=asset_id)
            alt.asset_type = asset_type
            alt.name = name
            alt.sn = sn
            alt.manufacturer = manufacturer
            alt.status = status
            alt.idc = idc
            alt.purchase_day = purchase_day
            alt.save()
            message = '修改成功'
            return redirect('/assets/index/')
        else:
            message = '修改失败'
            edit_form = forms.EditForm()
            print('1')
            return render(request, 'assets/edit.html',{'Edit_FormInput':edit_form})
    else:
        asset_type = models.Asset.objects.only('asset_type').get(id=asset_id).asset_type
        name = models.Asset.objects.only('name').get(id=asset_id).name
        sn = models.Asset.objects.only('sn').get(id=asset_id).sn
        manufacturer = models.Asset.objects.only('manufacturer').get(id=asset_id).manufacturer
        status = models.Asset.objects.only('status').get(id=asset_id).status
        idc = models.Asset.objects.only('idc').get(id=asset_id).idc
        purchase_day = models.Asset.objects.only('purchase_day').get(id=asset_id).purchase_day

        form = forms.EditForm(
	        initial={
		        'asset_type':asset_type,
		        'name': name,
		        'sn': sn,
		        'manufacturer': manufacturer,
		        'status': status,
		        'idc': idc,
		        'm_time': purchase_day,
	        }
        )
        return render(request, 'assets/edit.html', {'Edit_FormInput':form})


def del_equipment(request,asset_id):
    models.Asset.objects.get(id=asset_id).delete()
    return redirect('/assets/index/')