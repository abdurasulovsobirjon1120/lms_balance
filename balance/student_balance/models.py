from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    start_date = models.DateField()
    balance = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=[('to\'langan', 'To\'langan'), ('qarzdor', 'Qarzdor')],
        default='to\'langan'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Balance: {self.balance} - Status: {self.status}"
