# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BadPerson'
        db.create_table(u'insta_badperson', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'insta', ['BadPerson'])

        # Adding model 'IGTag'
        db.create_table(u'insta_igtag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('ig_id', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'insta', ['IGTag'])

        # Adding M2M table for field articles on 'IGTag'
        m2m_table_name = db.shorten_name(u'insta_igtag_articles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('igtag', models.ForeignKey(orm[u'insta.igtag'], null=False)),
            ('article', models.ForeignKey(orm[u'articles.article'], null=False))
        ))
        db.create_unique(m2m_table_name, ['igtag_id', 'article_id'])

        # Adding model 'InstaPost'
        db.create_table(u'insta_instapost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('insta_id', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=100, blank=True)),
            ('profile_picture', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['insta.IGTag'], null=True, blank=True)),
            ('standard_resolution', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('caption_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'insta', ['InstaPost'])


    def backwards(self, orm):
        # Deleting model 'BadPerson'
        db.delete_table(u'insta_badperson')

        # Deleting model 'IGTag'
        db.delete_table(u'insta_igtag')

        # Removing M2M table for field articles on 'IGTag'
        db.delete_table(db.shorten_name(u'insta_igtag_articles'))

        # Deleting model 'InstaPost'
        db.delete_table(u'insta_instapost')


    models = {
        u'articles.article': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['articles.Author']", 'symmetrical': 'False', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hero': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'hero_alt': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'hero_credit': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illus': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['articles.Illus']", 'symmetrical': 'False', 'blank': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['articles.Issue']", 'null': 'True', 'blank': 'True'}),
            'logo_fill': ('django.db.models.fields.CharField', [], {'default': "'#333333'", 'max_length': '250'}),
            'logo_outline': ('django.db.models.fields.CharField', [], {'default': "'#ffffff'", 'max_length': '250'}),
            'mapcode': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'more_info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'nav_color': ('django.db.models.fields.CharField', [], {'default': "'#0073b6'", 'max_length': '250'}),
            'nav_hover': ('django.db.models.fields.CharField', [], {'default': "'#a7a7a7'", 'max_length': '250'}),
            'photog': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['articles.Photog']", 'symmetrical': 'False', 'blank': 'True'}),
            'popular': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'screen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'special_css': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'special_js': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sponsor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['articles.Sponsor']", 'null': 'True', 'blank': 'True'}),
            'standfirst': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'tagline': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'articles.author': {
            'Meta': {'ordering': "['name']", 'object_name': 'Author'},
            'colophon': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'articles.illus': {
            'Meta': {'ordering': "['name']", 'object_name': 'Illus'},
            'colophon': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'articles.issue': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Issue'},
            'cover_img': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'for_sale': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'he_link': ('django.db.models.fields.URLField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'hero': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'hero_alt': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_stores': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'inside': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'logo_fill': ('django.db.models.fields.CharField', [], {'default': "'#333333'", 'max_length': '250'}),
            'logo_outline': ('django.db.models.fields.CharField', [], {'default': "'#ffffff'", 'max_length': '250'}),
            'month': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'nav_color': ('django.db.models.fields.CharField', [], {'default': "'#0073b6'", 'max_length': '250'}),
            'nav_hover': ('django.db.models.fields.CharField', [], {'default': "'#a7a7a7'", 'max_length': '250'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '6.0', 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'screen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shipping': ('django.db.models.fields.FloatField', [], {'default': '4.0', 'null': 'True', 'blank': 'True'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'special_css': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'special_js': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'tagline': ('django.db.models.fields.TextField', [], {'default': "'Stories From the City We Love'", 'blank': 'True'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'A Magazine About Rochester'", 'max_length': '250'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '250'})
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
            'add_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 5, 2, 0, 0)'}),
            'adimg': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'adlink': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'endorsement': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'insta.badperson': {
            'Meta': {'ordering': "['-timestamp']", 'object_name': 'BadPerson'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'insta.igtag': {
            'Meta': {'ordering': "['-timestamp']", 'object_name': 'IGTag'},
            'articles': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['articles.Article']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ig_id': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'insta.instapost': {
            'Meta': {'ordering': "['-created_time']", 'object_name': 'InstaPost'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'caption_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insta_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'profile_picture': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'standard_resolution': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['insta.IGTag']", 'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['insta']