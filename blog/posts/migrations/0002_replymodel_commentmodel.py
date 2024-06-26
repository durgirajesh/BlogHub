# Generated by Django 5.0.4 on 2024-05-20 16:42

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReplyModel',
            fields=[
                ('rid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('reply', models.TextField(max_length=15)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usermodel')),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('commentId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(max_length=20)),
                ('commenter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.usermodel')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.postmodel')),
                ('RID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.replymodel')),
            ],
        ),
    ]
