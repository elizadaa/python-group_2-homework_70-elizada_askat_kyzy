# Generated by Django 2.1.7 on 2019-03-02 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField(verbose_name='Ряд')),
                ('place', models.IntegerField(verbose_name='Место')),
                ('hall', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='seats_in_hall', to='webapp.Hall', verbose_name='Кинозал')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name='Время начала')),
                ('end', models.DateTimeField(verbose_name='Время окончания')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена за билет')),
                ('hall', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='shows_in_hall', to='webapp.Hall', verbose_name='Зал')),
            ],
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='finish_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания проката'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='posters', verbose_name='Постер'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(verbose_name='Дата выхода в прокат'),
        ),
        migrations.AddField(
            model_name='show',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='shows_of_movie', to='webapp.Movie', verbose_name='Фильм'),
        ),
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='movies_by_category', to='webapp.Category', verbose_name='Категория фильма'),
        ),
    ]