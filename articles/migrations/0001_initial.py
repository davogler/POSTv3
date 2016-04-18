# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('tagline', models.TextField(blank=True)),
                ('show_tagline', models.BooleanField(default=True, help_text=b'check to show tagline on article summary page')),
                ('intro', models.TextField(help_text=b'For article list view teaser- can be identical to standfirst if desired.', blank=True)),
                ('standfirst', models.TextField(help_text=b'First paragraph in article body.', blank=True)),
                ('body', models.TextField()),
                ('slug', models.SlugField(unique_for_date=b'pub_date')),
                ('hero', filebrowser.fields.FileBrowseField(help_text=b'Choose an huge image for this article. Minimum 1280 x 900', max_length=200, null=True, verbose_name=b'Hero Image', blank=True)),
                ('hero_alt', filebrowser.fields.FileBrowseField(help_text=b'For displaying in SM metadata. (FB:1280x670) Optional.', max_length=200, null=True, verbose_name=b'Hero Alternate Image', blank=True)),
                ('hero_credit', models.CharField(max_length=250, blank=True)),
                ('screen', models.BooleanField(default=False, help_text=b'check for dark image needing light screen in header')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('more_info', models.TextField(blank=True)),
                ('featured', models.BooleanField(default=False)),
                ('special_js', models.TextField(blank=True)),
                ('special_css', models.TextField(help_text=b'Mainly h2.unique and p.tagline', null=True, blank=True)),
                ('logo_fill', models.CharField(default=b'#333333', help_text=b'Hex color for Post logo #333333', max_length=250)),
                ('logo_outline', models.CharField(default=b'#ffffff', help_text=b'Hex color for Post logo outline #ffffff', max_length=250)),
                ('nav_color', models.CharField(default=b'#0073b6', help_text=b'Hex color for Nav links #0073b6', max_length=250)),
                ('nav_hover', models.CharField(default=b'#a7a7a7', help_text=b'Hex color for Nav link hover state #a7a7a7', max_length=250)),
                ('template_name', models.CharField(help_text=b'enter optional template to override default', max_length=250, blank=True)),
                ('mapcode', models.TextField(help_text=b'Straight up JS to display map.', null=True, blank=True)),
                ('status', models.IntegerField(default=2, choices=[(1, b'Published'), (2, b'Draft')])),
                ('popular', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-pub_date'],
                'verbose_name_plural': 'Articles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('link', models.URLField(blank=True)),
                ('colophon', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Authors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Illus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('link', models.URLField(blank=True)),
                ('colophon', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Illustrators',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=35)),
                ('image', filebrowser.fields.FileBrowseField(help_text=b'Inline image, yo. 960 640 or 525', max_length=200, null=True, verbose_name=b'Inline IMage', blank=True)),
                ('caption', models.CharField(max_length=500, null=True, blank=True)),
                ('article', models.ForeignKey(to='articles.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('volume', models.CharField(help_text=b'As in Issue X', max_length=250)),
                ('month', models.CharField(help_text=b'As Month/Month 2014', max_length=250)),
                ('slug', models.SlugField(unique_for_date=b'pub_date')),
                ('title', models.CharField(default=b'A Magazine About Rochester', help_text=b'A Magazine About Rochester', max_length=250)),
                ('tagline', models.TextField(default=b'Stories From the City We Love', help_text=b'Stories From the City We Love', blank=True)),
                ('inside', models.TextField(help_text=b'Brief listing of what is inside this issue.', null=True, blank=True)),
                ('hero', filebrowser.fields.FileBrowseField(help_text=b'Choose a huge image for this article. Minimum 1280 x 900', max_length=200, null=True, verbose_name=b'Hero Image', blank=True)),
                ('hero_alt', filebrowser.fields.FileBrowseField(help_text=b'For displaying in SM metadata. (FB:1280 x 670) Optional.', max_length=200, null=True, verbose_name=b'Hero Alternate Image', blank=True)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, help_text=b'Pick first of first month, for ordering', blank=True)),
                ('cover_img', filebrowser.fields.FileBrowseField(help_text=b'Upload a cover image; pick any version', max_length=200, null=True, verbose_name=b'Cover Image', blank=True)),
                ('special_js', models.TextField(blank=True)),
                ('special_css', models.TextField(help_text=b'Mainly h2.unique and p.tagline', null=True, blank=True)),
                ('logo_fill', models.CharField(default=b'#333333', help_text=b'Hex color for Post logo #333333', max_length=250)),
                ('logo_outline', models.CharField(default=b'#ffffff', help_text=b'Hex color for Post logo outline #ffffff', max_length=250)),
                ('nav_color', models.CharField(default=b'#0073b6', help_text=b'Hex color for Nav links #0073b6', max_length=250)),
                ('nav_hover', models.CharField(default=b'#a7a7a7', help_text=b'Hex color for Nav link hover state #a7a7a7', max_length=250)),
                ('template_name', models.CharField(help_text=b'enter optional template to override default', max_length=250, blank=True)),
                ('screen', models.BooleanField(default=False, help_text=b'check for dark image needing light screen in header')),
                ('price', models.FloatField(default=6.0, null=True, blank=True)),
                ('shipping', models.FloatField(default=4.0, null=True, blank=True)),
                ('he_link', models.URLField(max_length=250, null=True, blank=True)),
                ('in_stores', models.BooleanField(default=False, help_text=b'Is this currently at newstands?')),
                ('sku', models.CharField(max_length=200, null=True, blank=True)),
                ('for_sale', models.BooleanField(default=False, help_text=b'This will make it show up on product page.')),
                ('status', models.IntegerField(default=2, choices=[(1, b'Published'), (2, b'Draft')])),
            ],
            options={
                'ordering': ['-pub_date'],
                'verbose_name_plural': 'Issues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('link', models.URLField(blank=True)),
                ('colophon', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Photographers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('adimg', filebrowser.fields.FileBrowseField(help_text=b'Upload an image to be used for advertising min width 525px', max_length=200, null=True, verbose_name=b'Ad Image', blank=True)),
                ('adlink', models.URLField()),
                ('endorsement', models.TextField(blank=True)),
                ('add_date', models.DateTimeField(default=datetime.datetime(2016, 1, 24, 23, 55, 16, 175249))),
            ],
            options={
                'ordering': ['-add_date'],
                'verbose_name_plural': 'Sponsors',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ManyToManyField(to='articles.Author', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='illus',
            field=models.ManyToManyField(to='articles.Illus', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='issue',
            field=models.ForeignKey(blank=True, to='articles.Issue', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='photog',
            field=models.ManyToManyField(to='articles.Photog', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='sponsor',
            field=models.ForeignKey(blank=True, to='articles.Sponsor', null=True),
            preserve_default=True,
        ),
    ]
