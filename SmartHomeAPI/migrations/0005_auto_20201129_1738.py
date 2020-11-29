# Generated by Django 3.1.2 on 2020-11-29 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartHomeAPI', '0004_auto_20201129_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accesshistory',
            old_name='DateAccessed',
            new_name='date_accessed',
        ),
        migrations.RenameField(
            model_name='accesshistory',
            old_name='RFIDUsed',
            new_name='rfid_used',
        ),
        migrations.RenameField(
            model_name='component',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='CPF',
            new_name='cpf',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='PasswordHint',
            new_name='password_hint',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Rg',
            new_name='rg',
        ),
        migrations.RemoveField(
            model_name='accesshistory',
            name='AccessId',
        ),
        migrations.RemoveField(
            model_name='component',
            name='ComponentId',
        ),
        migrations.RemoveField(
            model_name='user',
            name='UserId',
        ),
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]