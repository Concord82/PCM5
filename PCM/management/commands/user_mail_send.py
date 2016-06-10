import datetime
from django.core.management.base import BaseCommand, CommandError
from PCM.models import State, Departament
from django_auth_ldap.backend import LDAPBackend
from django.contrib.auth import get_user_model
from django.core.mail import send_mail, EmailMessage
from django.template import Context
from django.template.loader import get_template, render_to_string

User = get_user_model()


class Command(BaseCommand):
    help = 'Send mail to User'

    def add_arguments(self, parser):
        parser.add_argument('email', nargs='+', type=str)

    def execute(self, *args, **options):
        curent_date = datetime.date.today()

        State_list = State.objects.filter(LogOff__year=curent_date.year, LogOff__month=curent_date.month, LogOff__day=curent_date.day-3)

        MyMessage = []
        Dept_Messages = []


        for Stats in State_list:

            user = LDAPBackend().populate_user(Stats.User)
            if user is None:
                MyMessage.append(Stats.User)
            else:
                userprofile = User.objects.get(login_name=Stats.User)
                Departaments = Departament.objects.values_list('name', flat=True)

                Dept_Messages.append(userprofile.departament)

                if not userprofile.departament in Departaments:
                    self.stdout.write(userprofile.departament )

                    new_departament = Departament(name=userprofile.departament)


                    new_departament.save()
        for email_addr in options['email']:
            email_to = []
            email_to.append(email_addr)

            template = get_template('mail/test.html')
            context = Context({'user': MyMessage, 'Dept': Dept_Messages})
            content = template.render (context)

            msg = EmailMessage('Test', content, "admin-cj@cons.tsk.ru", to=email_to)

            msg.content_subtype = 'html'

            msg.send()



            #send_mail('Test', content, "admin-cj@cons.tsk.ru", email_to, fail_silently=False)







