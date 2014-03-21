# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Issue'
        db.create_table(u'articles_issue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('volume', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('month', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('cover_img', self.gf('filebrowser.fields.FileBrowseField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'articles', ['Issue'])

        # Adding M2M table for field issue on 'Article'
        m2m_table_name = db.shorten_name(u'articles_article_issue')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm[u'articles.article'], null=False)),
            ('issue', models.ForeignKey(orm[u'articles.issue'], null=False))
        ))
        db.create_unique(m2m_table_name, ['article_id', 'issue_id'])


    def backwards(self, orm):
        # Deleting model 'Issue'
        db.delete_table(u'articles_issue')

        # Removing M2M table for field issue on 'Article'
        db.delete_table(db.shorten_name(u'articles_article_issue'))


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
            'issue': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['articles.Issue']", 'symmetrical': 'False', 'blank': 'True'}),
            'more_info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'photog': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['articles.Photog']", 'symmetrical': 'False', 'blank': 'True'}),
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
        u'articles.image': {
            'Meta': {'object_name': 'Image'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['articles.Article']"}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        },
        u'articles.issue': {
            'Meta': {'object_name': 'Issue'},
            'cover_img': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
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
            'add_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 21, 0, 0)'}),
            'adimg': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'adlink': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'endorsement': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['articles']