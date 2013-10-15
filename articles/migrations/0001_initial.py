# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'articles_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('tagline', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('intro', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('hero', self.gf('filebrowser.fields.FileBrowseField')(max_length=200, null=True, blank=True)),
            ('screen', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 13, 0, 0))),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['articles.Author'], null=True, blank=True)),
            ('photog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['articles.Photog'], null=True, blank=True)),
            ('sponsor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['articles.Sponsor'], null=True, blank=True)),
            ('more_info', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('special_js', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('special_css', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
        ))
        db.send_create_signal(u'articles', ['Article'])

        # Adding model 'Image'
        db.create_table(u'articles_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['articles.Article'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('image', self.gf('filebrowser.fields.FileBrowseField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'articles', ['Image'])

        # Adding model 'Sponsor'
        db.create_table(u'articles_sponsor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('adimg', self.gf('filebrowser.fields.FileBrowseField')(max_length=200, null=True, blank=True)),
            ('adlink', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('endorsement', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('instances', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('paid_for', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('add_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 13, 0, 0))),
        ))
        db.send_create_signal(u'articles', ['Sponsor'])

        # Adding model 'Author'
        db.create_table(u'articles_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('colophon', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'articles', ['Author'])

        # Adding model 'Photog'
        db.create_table(u'articles_photog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('colophon', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'articles', ['Photog'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'articles_article')

        # Deleting model 'Image'
        db.delete_table(u'articles_image')

        # Deleting model 'Sponsor'
        db.delete_table(u'articles_sponsor')

        # Deleting model 'Author'
        db.delete_table(u'articles_author')

        # Deleting model 'Photog'
        db.delete_table(u'articles_photog')


    models = {
        u'articles.article': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['articles.Author']", 'null': 'True', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hero': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'more_info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'photog': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['articles.Photog']", 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 13, 0, 0)'}),
            'screen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'special_css': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'special_js': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sponsor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['articles.Sponsor']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'tagline': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'articles.author': {
            'Meta': {'ordering': "['name']", 'object_name': 'Author'},
            'colophon': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'articles.image': {
            'Meta': {'object_name': 'Image'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['articles.Article']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        },
        u'articles.photog': {
            'Meta': {'ordering': "['name']", 'object_name': 'Photog'},
            'colophon': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'articles.sponsor': {
            'Meta': {'ordering': "['-add_date']", 'object_name': 'Sponsor'},
            'add_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 13, 0, 0)'}),
            'adimg': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'adlink': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'endorsement': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instances': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'paid_for': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['articles']