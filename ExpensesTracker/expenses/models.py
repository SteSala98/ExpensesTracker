from django.db import models


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Housing', 'Housing'),
        ('Groceries', 'Groceries'),
        ('Transport', 'Transport'),
        ('Restaurant', 'Restaurant'),
        ('Bar', 'Bar'),
        ('Health', 'Health'),  # Fixed the typo here
        ('Travel', 'Travel'),
        ('Beauty', 'Beauty'),
        ('Clothing', 'Clothing'),
        ('Leisure', 'Leisure'),
        ('Gifts', 'Gifts'),
        ('Subscriptions', 'Subscriptions'),
        ('Other', 'Other'),
    ]

    date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')

    def __str__(self):
        return f"{self.date} - {self.description} - {self.amount}€"
