# Generated by Django 3.0.6 on 2020-05-07 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='책의 장르를 입력하세요(ex:소설)', max_length=200)),
            ],
        ),
    ]