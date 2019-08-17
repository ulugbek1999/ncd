from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from employee.model.army import ArmyFile, ArmyChangesFile
from employee.model.education import EducationFile, EducationChangesFile
from employee.model.employee import Employee
from employee.model.experience import ExperienceFile, ExperienceChangesFile
from employee.model.family import FamilyChanges, FamilyFile
from employee.model.language import LanguageFile, LanguageChangesFile
from employee.model.relative import RelativeFile, RelativeChangesFile
from employee.model.reward import RewardFile, RewardChangesFile
from employee.model.score import Score
from operators.models import RegisterNumber
from utils.mail import send_email
from utils.sms import send_sms


@receiver(post_save, sender=Employee)
def create_user(instance, created, **kwargs):
    if created:
        import datetime
        user = User()
        if instance.username:
            user.username = instance.username
        else:
            user.username = instance.passport_serial.replace(' ', '')
        passwd = str(int(datetime.datetime.now().timestamp()))
        user.set_password(passwd)
        user.save()
        instance.user = user
        instance.save()
        if instance.send_sms:
            send_sms(instance.phone, f"Ваш логин на uzncd.com: {instance.user.username}\nВаш пароль: {passwd}")
        if instance.send_email and instance.email:
            print(instance.email)
            send_email(
                title='uzncd.com',
                text=f"<b>Ваш логин на uzncd.com</b>: {instance.user.username}\n<b>Ваш пароль</b>: {passwd}",
                emails=[instance.email]
            )


@receiver(post_save, sender=Employee)
def notify_operator2(instance, **kwargs):
    """2/3/4-operator uchun birinchi operator yangi
    odamni ro'yhatga kiritganligi haqida `notification` yuboradi"""
    import json
    from channels.layers import get_channel_layer
    from asgiref.sync import async_to_sync

    if instance.step_finished == 1 and not instance.op2_ws_sent:
        if not hasattr(instance, 'group'):
            return
        if not hasattr(instance.group, 'operator2'):
            return
        r = RegisterNumber.objects.first()
        r.number += 1
        r.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(instance.group.operator2.channel, {
            "type": "notify",
            "message": json.loads(json.dumps({
                "id": instance.id,
                "fullname": f"{instance.full_name_ru} / {instance.full_name_en}",
            }))
        })
        instance.op2_ws_sent = True
        instance.save()
        return
    elif instance.step_finished == 2 and not instance.op3_ws_sent:
        if not hasattr(instance, 'group'):
            return
        if not hasattr(instance.group, 'operator3'):
            return
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(instance.group.operator3.channel, {
            "type": "notify",
            "message": json.loads(json.dumps({
                "id": instance.id,
                "fullname": f"{instance.full_name_ru} / {instance.full_name_en}",
            }))
        })
        instance.op3_ws_sent = True
        instance.save()
        return
    elif instance.step_finished == 3 and not instance.op4_ws_sent:
        if not hasattr(instance, 'group'):
            return
        if not hasattr(instance.group, 'operator4'):
            return
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(instance.group.operator4.channel, {
            "type": "notify",
            "message": json.loads(json.dumps({
                "id": instance.id,
                "fullname": f"{instance.full_name_ru} / {instance.full_name_en}",
            }))
        })
        instance.op4_ws_sent = True
        instance.save()
        return
    elif instance.step_finished == 4:
        from employee.model.score import Score
        # generate scores
        score, _ = Score.objects.get_or_create(employee_id=instance.id)
        # country
        c = 0
        for i in instance.countries.all():
            if i.country.score:
                c += i.country.score
        score.country = c
        # language
        la = 0
        for i in instance.language_set.all():
            if i.level == 1:
                la += i.language.excellent
            elif i.level == 2:
                la += i.language.good
            elif i.level == 3:
                la += i.language.not_bad
        score.language = la
        # education
        e = 0
        for i in instance.education_set.all():
            if i.type.score:
                e += i.type.score
        score.education = e
        # medical
        score.medical = instance.medical_score()
        # birth date
        score.birth_year = instance.birth_date_score()
        # university
        score.education = instance.university_score()
        # wages
        score.wages = instance.wages_score()

        score.summa = c + la + e + score.medical + score.birth_year + score.education + score.wages
        score.save()


# army
@receiver(post_delete, sender=ArmyFile)
def delete_file(instance, **kwargs):
    instance.file.delete(True)


@receiver(post_delete, sender=ArmyChangesFile)
def delete_file(instance, **kwargs):
    instance.file.delete(True)


# education
@receiver(post_delete, sender=EducationFile)
def delete_file(instance, **kwargs):
    instance.file.delete(True)


@receiver(post_delete, sender=EducationChangesFile)
def delete_file(instance, **kwargs):
    instance.file.delete(True)


# experience
@receiver(post_delete, sender=ExperienceFile)
def delete_file(instance, **kwargs):
    instance.file.delete(True)


@receiver(post_delete, sender=ExperienceChangesFile)
def delete_file(instance, **kwargs):
    instance.file.delete(True)


# family
@receiver(post_delete, sender=FamilyFile)
def delete_file(instance, **kwargs):
    instance.file.delete(True)


@receiver(post_delete, sender=FamilyChanges)
def delete_file(instance, **kwargs):
    instance.file.delete(True)


# language
@receiver(post_delete, sender=LanguageFile)
def delete_file(instance, **kwargs):
    instance.file.delete(True)


@receiver(post_delete, sender=LanguageChangesFile)
def delete_file(instance, **kwargs):
    instance.file.delete(True)


# relative
@receiver(post_delete, sender=RelativeFile)
def delete_file(instance, **kwargs):
    instance.file.delete(True)


@receiver(post_delete, sender=RelativeChangesFile)
def delete_file(instance, **kwargs):
    instance.file.delete(True)


# reward
@receiver(post_delete, sender=RewardFile)
def delete_file(instance, **kwargs):
    instance.file.delete(True)


@receiver(post_delete, sender=RewardChangesFile)
def delete_file(instance, **kwargs):
    instance.file.delete(True)


@receiver(post_save, sender=Score)
def scoring(instance, **kwargs):
    if instance.category == '':
        instance.sum()
