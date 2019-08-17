def operator1_image_uploader(instance, filename):
    """Operator 1 ga tegishli qismining passport
     nusxasini yuklash uchun `handler`"""
    return f"{instance.passport_serial.replace(' ', '')}/operator1/{filename}"


def operator2_image_uploader(instance, filename):
    """Operator 2 ga tegishli qismining 4 rekursdan tushurilgan
     odam yuzinini yuklash uchun `handler`"""
    return f"{instance.passport_serial.replace(' ', '')}/operator1/{filename}"
