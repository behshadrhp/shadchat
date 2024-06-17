from django.db import models


class GenderType(models.TextChoices):
    """
    Choice Gender on Profile Account.
    """
    
    MR = "mr", "male"
    MRS = "mrs", "female"
    OTHER = "oth", "other"
