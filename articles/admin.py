from django.contrib import admin
from django import forms
from articles.models import Article, Author, Sponsor, Photog, Image, Illus, Issue


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1


class ArticleAdminForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title',
                  'tagline',
                  'show_tagline',
                  'intro',
                  'standfirst',
                  'body',
                  'slug',
                  'hero',
                  'hero_alt',
                  'hero_credit',
                  'screen',
                  'pub_date',
                  'author',
                  'photog',
                  'illus',
                  'sponsor',
                  'more_info',
                  'featured',
                  'issue',
                  'special_js',
                  'special_css',
                  'logo_fill',
                  'logo_outline',
                  'nav_color',
                  'nav_hover',
                  'template_name',
                  'mapcode',
                  'status',
                  'popular',
                  ]


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ('title', 'pub_date', 'status', 'featured', 'popular')
    list_editable = ('status', 'featured', 'popular')

    inlines = [ImageInline, ]
    form = ArticleAdminForm

admin.site.register(Article, ArticleAdmin)


class AuthorAdminForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['name',
                  'link',
                  'colophon',
                  ]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    form = AuthorAdminForm

admin.site.register(Author, AuthorAdmin)


class PhotogAdminForm(forms.ModelForm):

    class Meta:
        model = Photog
        fields = ['name',
                  'link',
                  'colophon',
                  ]


class PhotogAdmin(admin.ModelAdmin):
    list_display = ('name',)
    form = PhotogAdminForm

admin.site.register(Photog, PhotogAdmin)


class IllusAdminForm(forms.ModelForm):

    class Meta:
        model = Illus
        fields = ['name',
                  'link',
                  'colophon',
                  ]


class IllusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    form = IllusAdminForm

admin.site.register(Illus, IllusAdmin)


class SponsorAdminForm(forms.ModelForm):

    class Meta:
        model = Sponsor
        fields = ['name',
                  'adimg',
                  'adlink',
                  'endorsement',
                  'add_date',
                  ]


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    form = SponsorAdminForm

admin.site.register(Sponsor, SponsorAdmin)


class IssueAdminForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = [  'volume',
                    'month',
                    'slug',
                    'title',
                    'tagline',
                    'inside',
                    'hero',
                    'hero_alt',
                    'pub_date',
                    'cover_img',
                    'special_js',
                    'special_css',
                    'logo_fill',
                    'logo_outline',
                    'nav_color',
                    'nav_hover',
                    'template_name',
                    'screen',
                    'price',
                    'shipping',
                    'he_link',
                    'in_stores',
                    'sku',
                    'for_sale',
                    'status',
                ]


class IssueAdmin(admin.ModelAdmin):
    list_display = ('volume', 'month', 'image_thumbnail', 'status', 'for_sale', 'in_stores', 'price', 'shipping')
    list_editable = ('status', 'for_sale', 'in_stores')
    form = IssueAdminForm

admin.site.register(Issue, IssueAdmin)
