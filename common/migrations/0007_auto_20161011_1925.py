# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 19:25
from __future__ import unicode_literals

import common.blocks.columns
import common.blocks.tabs
from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0029_unicode_slugfield_dj19'),
        ('common', '0006_auto_20161010_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageAlias',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('alias_for_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aliases', to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='custompage',
            name='custom_url',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='custom_url',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='custompage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('appeal', wagtail.wagtailcore.blocks.StructBlock((('icon', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('flask', 'flask'), ('group', 'group'), ('laptop', 'laptop'), ('sitemap', 'sitemap'), ('user', 'user'), ('book', 'book'), ('download', 'download')])), ('topic', wagtail.wagtailcore.blocks.CharBlock(max_length=35, required=True)), ('content', wagtail.wagtailcore.blocks.TextBlock(max_length=255, required=True))), classname='appeal', icon='tick', template='common/blocks/appeal.html')), ('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('statement', wagtail.wagtailcore.blocks.CharBlock()), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('imagechooser', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('column', common.blocks.columns.ColumnsBlock()), ('tabbed_block', common.blocks.tabs.TabbedBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('main_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('style', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('max-width:225px;max-height:145px', 'small display'), ('max_width:250px;max-height:250px', 'middle display'), ('max_width:250px;max-height:250px;padding-top:20px', 'middle + padding display'), ('height:auto', 'auto display')], default='height:auto')), ('url', wagtail.wagtailcore.blocks.CharBlock(max_length=250, required=False))))), ('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock(help_text='With great power comes great responsibility. This HTML is unescaped. Be careful!')), ('people_block', wagtail.wagtailcore.blocks.StructBlock((('displayStyle', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('concise-team', 'concise-team'), ('concise-ambassador', 'concise-ambassador'), ('detailed', 'detailed')], default='concise')), ('tag', wagtail.wagtailcore.blocks.CharBlock(max_length=20))))), ('centered_text', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()),))), ('hero_block', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('description', wagtail.wagtailcore.blocks.RichTextBlock(required=True))))), ('spotlight_block', wagtail.wagtailcore.blocks.StructBlock((('bubbles', wagtail.wagtailcore.blocks.StreamBlock((('bubble_block', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('title', wagtail.wagtailcore.blocks.CharBlock(max_length=35, required=True)), ('description', wagtail.wagtailcore.blocks.RichTextBlock(required=True))))),))),))), ('job_whole_block', wagtail.wagtailcore.blocks.StructBlock(())), ('embed_block', wagtail.wagtailembeds.blocks.EmbedBlock()), ('clear_fixblock', wagtail.wagtailcore.blocks.StructBlock(()))), blank=True, null=True),
        ),
    ]
