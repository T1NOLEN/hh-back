from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200, default=None)
    description = models.TextField(max_length=200, default=None)
    city = models.CharField(max_length=200, default=None)
    address = models.TextField(max_length=200, default=None)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=200, default=None)
    description = models.TextField(max_length=200, default=None)
    salary = models.FloatField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company_id
        }
