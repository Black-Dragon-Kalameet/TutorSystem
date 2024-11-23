# Generated by Django 4.2.16 on 2024-11-02 12:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_tutor_tutorname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="username",
            field=models.CharField(max_length=180),
        ),
        migrations.CreateModel(
            name="message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.TextField()),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "attachment",
                    models.FileField(blank=True, null=True, upload_to="attachments/"),
                ),
                (
                    "receiver_student",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_messages_student",
                        to="main.student",
                    ),
                ),
                (
                    "receiver_tutor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_messages_tutor",
                        to="main.tutor",
                    ),
                ),
                (
                    "sender_student",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.student",
                    ),
                ),
                (
                    "sender_tutor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.tutor",
                    ),
                ),
            ],
        ),
    ]