# Generated by Django 4.2.16 on 2024-12-06 14:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0008_library"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="date_of_birth",
            field=models.DateField(default="2011-12-12"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="email",
            field=models.EmailField(default=2, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="phone_number",
            field=models.CharField(default=2, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="profile_picture",
            field=models.ImageField(blank=True, null=True, upload_to="profiles/"),
        ),
    ]
