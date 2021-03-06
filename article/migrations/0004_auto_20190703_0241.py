# Generated by Django 2.2.1 on 2019-07-02 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20190703_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='article.ArticleType', verbose_name='文章类型'),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
    ]
