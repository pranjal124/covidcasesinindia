from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    result=requests.get('https://api.covid19india.org/data.json')
    data=result.json()['statewise']
    for i in data:
        if i['state'] == 'Total':
            conf=i['confirmed']
            reco=i['recovered']
            death=i['deaths']
            acti=i['active']
    if request.method=='POST':
        print('hlo')
        state=request.POST.get('state')
        for j in data:
            if j['state']==state:
                print(j['state'])
                cont={'data':data,'conf':conf,'reco':reco,'death':death,'acti':acti,'data1':j}
                return render(request,'covid/home.html',cont)
    cont={'data':data,'conf':conf,'reco':reco,'death':death,'acti':acti}
    return render(request,'covid/home.html',cont)
