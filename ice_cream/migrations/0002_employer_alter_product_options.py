# Generated by Django 4.0.5 on 2022-06-07 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='image/employers/')),
                ('name', models.CharField(max_length=222)),
                ('position', models.CharField(max_length=222)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id']},
        ),
    ]
