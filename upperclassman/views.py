from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.core.mail import send_mail

def upper(request):
    """ Homepage """
    if request.method == 'POST':
        form = UpperClassmanForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            netid = (form.cleaned_data['netid']).strip()
            if Upperclassman.objects.filter(netid=netid).count() > 0:
                return HttpResponseRedirect('/error_exists/')
            year = form.cleaned_data['year']
            school = form.cleaned_data['school']
            major1 = form.cleaned_data['major1']
            major2 = form.cleaned_data['major2']
            major3 = form.cleaned_data['major3']
            survey = form.cleaned_data['survey']
            organization = form.cleaned_data['organization']
            participated = form.cleaned_data['participated']
            upperclass = Upperclassman(name=name,
                netid=netid,
                year=year,
                college=school,
                major1=major1,
                major2=major2,
                major3=major3,
                survey=survey,
                participated=participated,
                organization=organization)
            upperclass.save()
            mail_title = 'Let\'s Get Coffee: Thanks!'
            message = '''Thanks for completing the Upperclassmen survey! You may wish to familiarize yourself with the schedule here: http://www.letsgetcoffeecornell.com/timeline/.When the survey window closes on Sept. 19, you will receive an email with a link to see the survey responses of new students in your major/college. As the schedule shows, you'll have the opportunity then to handpick one new student to meet. Be on the lookout for that link!'''
            # Thanks, \n
            # The CampusConnection Steering Committee\n\n
            # Blake Barr (bab354)\n
            # Emma Jesch (eaj54)\n
            # Jimmy Chen (jsc349)\n
            # Alice Chou (aec247)\n
            # Sofia Hu (shh83)\n
            # Yixuan Zhang (yz427)'''
            email = 'Let\'s Get Coffee<letsgetcoffeecornell@gmail.com>'
            recipients = [upperclass.netid + '@cornell.edu']
            try:
                send_mail(mail_title, message, email, recipients)
            except:
                pass
            return HttpResponseRedirect('/thanks_upperclassman/')
    else:
        form = UpperClassmanForm()
    return render(request, 'upperclassman/basic.html', {
        'form' : form,
        'request' : request, })

#For closed state
def upperclassman_closed(request):
    return render(request, 'upperclassman_closed.html', {
        'request' : request, })
