from django_cron import CronJobBase, Schedule

from operators.models import RegisterNumber


class IncreaseRegisterNumber(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'

    def do(self):
        r = RegisterNumber.objects.first()
        r.number = 0
        r.save()
