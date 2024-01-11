from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('guid', models.CharField(max_length=36)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('email_original_timestamp', models.DateTimeField(blank=True, null=True)),
                ('sender_id', models.IntegerField(blank=True, null=True)),
                ('publisher_id', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, db_collation='Greek_CI_AS', max_length=450, null=True)),
                ('summary', models.CharField(blank=True, db_collation='Greek_CI_AS', max_length=300, null=True)),
                ('body', models.TextField(blank=True, db_collation='Greek_CI_AS', null=True)),
                ('inbox_message_id', models.IntegerField(blank=True, null=True)),
                ('mail_body', models.TextField(blank=True, db_collation='Greek_CI_AS', null=True)),
                ('plain_text', models.TextField(blank=True, db_collation='Greek_CI_AS', null=True)),
                ('extracted_text_html', models.TextField(blank=True, db_collation='Greek_CI_AS', null=True)),
                ('publication_datetime', models.DateTimeField(blank=True, null=True)),
                ('isdeleted', models.BooleanField(blank=True, db_column='isDeleted', null=True)),
                ('isactive', models.BooleanField(blank=True, db_column='isActive', null=True)),
                ('attachments', models.IntegerField(blank=True, null=True)),
                ('debug_info', models.TextField(blank=True, db_collation='Greek_CI_AS', null=True)),
            ],
            options={
                'db_table': 'articles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticlesAttachments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('article_id', models.IntegerField(blank=True, null=True)),
                ('attachment_id', models.IntegerField(blank=True, null=True)),
                ('original_filename', models.CharField(blank=True, db_collation='Greek_CI_AS', max_length=250, null=True)),
                ('isattachment', models.BooleanField(blank=True, db_column='isAttachment', null=True)),
            ],
            options={
                'db_table': 'articles_attachments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content_type', models.CharField(blank=True, db_collation='Greek_CI_AS', max_length=100, null=True)),
                ('extension', models.CharField(blank=True, db_collation='Greek_CI_AS', max_length=5, null=True)),
                ('cdn_filename', models.CharField(blank=True, db_collation='Greek_CI_AS', max_length=80, null=True)),
                ('checksum', models.CharField(blank=True, db_collation='Greek_CI_AS', max_length=40, null=True, unique=True)),
                ('width', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('filesize', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'attachments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, db_collation='Greek_CI_AS', max_length=150, null=True)),
            ],
            options={
                'db_table': 'groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, db_collation='Greek_CI_AS', max_length=150, null=True)),
                ('groupid', models.IntegerField(blank=True, db_column='groupId', null=True)),
                ('imapserver', models.CharField(blank=True, db_collation='Greek_CI_AS', db_column='imapServer', max_length=80, null=True)),
                ('imapport', models.IntegerField(blank=True, db_column='imapPort', null=True)),
                ('mailboxname', models.CharField(blank=True, db_collation='Greek_CI_AS', db_column='mailboxName', max_length=50, null=True)),
                ('inboxusername', models.CharField(blank=True, db_collation='Greek_CI_AS', db_column='inboxUsername', max_length=60, null=True)),
                ('inboxpassword', models.CharField(blank=True, db_collation='Greek_CI_AS', db_column='inboxPassword', max_length=50, null=True)),
                ('app_password', models.CharField(blank=True, db_collation='Greek_CI_AS', max_length=50, null=True)),
                ('cmstype', models.CharField(blank=True, db_collation='Greek_CI_AS', db_column='cmsType', max_length=50, null=True)),
                ('isactive', models.BooleanField(blank=True, db_column='isActive', null=True)),
                ('lastupdate', models.DateTimeField(blank=True, db_column='lastUpdate', null=True)),
                ('imagemaxwidth', models.IntegerField(blank=True, db_column='imageMaxWidth', null=True)),
                ('imageminwidth', models.IntegerField(blank=True, db_column='imageMinWidth', null=True)),
                ('imagemaxheight', models.IntegerField(blank=True, db_column='imageMaxHeight', null=True)),
                ('imageminheight', models.IntegerField(blank=True, db_column='imageMinHeight', null=True)),
                ('html_preview_width', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'publishers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SenderPriorities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sender_id', models.IntegerField(blank=True, null=True)),
                ('publisher_id', models.IntegerField(blank=True, null=True)),
                ('priority', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sender_priorities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Senders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, db_collation='Greek_CI_AS', max_length=150, null=True)),
                ('emailaddress', models.CharField(blank=True, db_collation='Greek_CI_AS', db_column='emailAddress', max_length=100, null=True)),
                ('category_id', models.IntegerField(blank=True, null=True)),
                ('emailnotification', models.BooleanField(blank=True, db_column='emailNotification', null=True)),
                ('registration_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'senders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubjectKeywordsToIgnore',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('keyword', models.CharField(blank=True, db_collation='Greek_CI_AS', max_length=200, null=True)),
                ('publisher_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'subject_keywords_to_ignore',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TextsToClearPerPublisher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(blank=True, db_collation='Greek_CI_AS', max_length=500, null=True)),
                ('publisher_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'texts_to_clear_per_publisher',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, db_collation='Greek_CI_AS', max_length=50, null=True)),
                ('password', models.CharField(blank=True, db_collation='Greek_CI_AS', max_length=50, null=True)),
                ('publisher_id', models.IntegerField(blank=True, null=True)),
                ('user_level', models.CharField(blank=True, db_collation='Greek_CI_AS', max_length=50, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
