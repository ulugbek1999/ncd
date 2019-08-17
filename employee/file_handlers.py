def fingerprint(instance, filename):
    return f'{instance.passport_serial}/fingerprint/{filename}'


def passport_copy(instance, filename):
    return f'{instance.passport_serial.replace(" ", "")}/passport_copy/{filename}'


def photos(instance, filename):
    return f'{instance.passport_serial.replace(" ", "")}/photos/{filename}'


# army
def army_file_uploader(instance, filename):
    if hasattr(instance.army, 'parent'):
        return f'{instance.army.parent.employee.passport_serial.replace(" ", "")}/army/{filename}'
    return f'{instance.army.employee.passport_serial.replace(" ", "")}/army/{filename}'


# education
def education_file_uploader(instance, filename):
    if hasattr(instance.education, 'parent'):
        return f'{instance.education.parent.employee.passport_serial.replace(" ", "")}/education/{filename}'
    return f'{instance.education.employee.passport_serial.replace(" ", "")}/education/{filename}'


# language
def language_file_uploader(instance, filename):
    if hasattr(instance.language, 'parent'):
        return f'{instance.language.parent.employee.passport_serial.replace(" ", "")}/language/{filename}'
    return f'{instance.language.employee.passport_serial.replace(" ", "")}/language/{filename}'


# relative
def relative_file_uploader(instance, filename):
    if hasattr(instance.relative, 'parent'):
        return f'{instance.relative.parent.employee.passport_serial.replace(" ", "")}/relative/{filename}'
    return f'{instance.relative.employee.passport_serial.replace(" ", "")}/relative/{filename}'


# reward
def reward_file_uploader(instance, filename):
    if hasattr(instance.reward, 'parent'):
        return f'{instance.reward.parent.employee.passport_serial.replace(" ", "")}/reward/{filename}'
    return f'{instance.reward.employee.passport_serial.replace(" ", "")}/reward/{filename}'


# experience
def experience_file_uploader(instance, filename):
    if hasattr(instance.experience, 'parent'):
        return f'{instance.experience.parent.employee.passport_serial.replace(" ", "")}/experience/{filename}'
    return f'{instance.experience.employee.passport_serial.replace(" ", "")}/experience/{filename}'


# family
def family_file_uploader(instance, filename):
    if hasattr(instance.family, 'parent'):
        return f'{instance.family.parent.employee.passport_serial.replace(" ", "")}/family/{filename}'
    return f'{instance.family.employee.passport_serial.replace(" ", "")}/family/{filename}'
