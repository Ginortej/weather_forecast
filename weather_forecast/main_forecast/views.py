from django.shortcuts import render

setings = [
        {
        'days' : 7,
        'sediments': True,
        'Wind direction': True, 
        'Evaporation': True,
        'The overall level of cloud cover' : True,
        'Surface pressure': True, 
        'Sunrise': True,
        'Sunset': True,
        'daylight hours':True,}
    ]


def index(reqests):
    template = 'index.html'
    context = {'psrametres': setings}
    return render(reqests,template,context)

def setings(reqests):
    template = 'setings.html'
    return render(reqests, template,)

