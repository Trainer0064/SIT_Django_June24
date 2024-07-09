# Generated by Django 5.0.4 on 2024-07-09 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllFieldsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_field', models.CharField(max_length=10)),
                ('text_field', models.TextField()),
                ('integer_field', models.IntegerField()),
                ('decimal_field', models.DecimalField(decimal_places=2, max_digits=5)),
                ('boolean_field', models.BooleanField()),
                ('email_field', models.EmailField(max_length=254)),
                ('url_field', models.URLField()),
                ('date_field', models.DateField()),
                ('datetime_field', models.DateTimeField()),
            ],
        ),
    ]
