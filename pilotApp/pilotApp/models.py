# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Articles(models.Model):
    id = models.AutoField(primary_key=True)
    guid = models.CharField(max_length=36)
    timestamp = models.DateTimeField(blank=True, null=True)
    email_original_timestamp = models.DateTimeField(blank=True, null=True)
    sent_timestamp = models.DateTimeField(blank=True, null=True)
    sender_id = models.IntegerField(blank=True, null=True)
    publisher_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=450, db_collation='Greek_CI_AS', blank=True, null=True)
    summary = models.CharField(max_length=300, db_collation='Greek_CI_AS', blank=True, null=True)
    body = models.TextField(db_collation='Greek_CI_AS', blank=True, null=True)
    inbox_message_id = models.IntegerField(blank=True, null=True)
    mail_body = models.TextField(db_collation='Greek_CI_AS', blank=True, null=True)
    plain_text = models.TextField(db_collation='Greek_CI_AS', blank=True, null=True)
    extracted_text_html = models.TextField(db_collation='Greek_CI_AS', blank=True, null=True)
    publication_datetime = models.DateTimeField(blank=True, null=True)
    isdeleted = models.BooleanField(db_column='isDeleted', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.
    ispublished = models.BooleanField(db_column='isPublished', blank=True, null=True)  # Field name made lowercase.
    attachments = models.IntegerField(blank=True, null=True)
    debug_info = models.TextField(db_collation='Greek_CI_AS', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'articles'


class ArticlesAttachments(models.Model):
    id = models.AutoField(primary_key=True)
    article_id = models.IntegerField(blank=True, null=True)
    attachment_id = models.IntegerField(blank=True, null=True)
    original_filename = models.CharField(max_length=250, db_collation='Greek_CI_AS', blank=True, null=True)
    isattachment = models.BooleanField(db_column='isAttachment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'articles_attachments'
        unique_together = (('article_id', 'attachment_id'),)


class Attachments(models.Model):
    id = models.AutoField(primary_key=True)
    content_type = models.CharField(max_length=100, db_collation='Greek_CI_AS', blank=True, null=True)
    extension = models.CharField(max_length=5, db_collation='Greek_CI_AS', blank=True, null=True)
    cdn_filename = models.CharField(max_length=80, db_collation='Greek_CI_AS', blank=True, null=True)
    checksum = models.CharField(unique=True, max_length=40, db_collation='Greek_CI_AS', blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    filesize = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'attachments'


class Groups(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, db_collation='Greek_CI_AS', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'groups'


class Publishers(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, db_collation='Greek_CI_AS', blank=True, null=True)
    groupid = models.IntegerField(db_column='groupId', blank=True, null=True)  # Field name made lowercase.
    imapserver = models.CharField(db_column='imapServer', max_length=80, db_collation='Greek_CI_AS', blank=True, null=True)  # Field name made lowercase.
    imapport = models.IntegerField(db_column='imapPort', blank=True, null=True)  # Field name made lowercase.
    mailboxname = models.CharField(db_column='mailboxName', max_length=50, db_collation='Greek_CI_AS', blank=True, null=True)  # Field name made lowercase.
    inboxusername = models.CharField(db_column='inboxUsername', max_length=60, db_collation='Greek_CI_AS', blank=True, null=True)  # Field name made lowercase.
    inboxpassword = models.CharField(db_column='inboxPassword', max_length=50, db_collation='Greek_CI_AS', blank=True, null=True)  # Field name made lowercase.
    app_password = models.CharField(max_length=50, db_collation='Greek_CI_AS', blank=True, null=True)
    cmstype = models.CharField(db_column='cmsType', max_length=50, db_collation='Greek_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='lastUpdate', blank=True, null=True)  # Field name made lowercase.
    imagemaxwidth = models.IntegerField(db_column='imageMaxWidth', blank=True, null=True)  # Field name made lowercase.
    imageminwidth = models.IntegerField(db_column='imageMinWidth', blank=True, null=True)  # Field name made lowercase.
    imagemaxheight = models.IntegerField(db_column='imageMaxHeight', blank=True, null=True)  # Field name made lowercase.
    imageminheight = models.IntegerField(db_column='imageMinHeight', blank=True, null=True)  # Field name made lowercase.
    html_preview_width = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'publishers'


class SenderPriorities(models.Model):
    id = models.AutoField(primary_key=True)
    sender_id = models.IntegerField(blank=True, null=True)
    publisher_id = models.IntegerField(blank=True, null=True)
    priority = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sender_priorities'


class Senders(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, db_collation='Greek_CI_AS', blank=True, null=True)
    emailaddress = models.CharField(db_column='emailAddress', max_length=100, db_collation='Greek_CI_AS', blank=True, null=True)  # Field name made lowercase.
    category_id = models.IntegerField(blank=True, null=True)
    emailnotification = models.BooleanField(db_column='emailNotification', blank=True, null=True)  # Field name made lowercase.
    registration_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'senders'


class SubjectKeywordsToIgnore(models.Model):
    id = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=200, db_collation='Greek_CI_AS', blank=True, null=True)
    publisher_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'subject_keywords_to_ignore'
        unique_together = (('keyword', 'publisher_id'),)


class TextsToClearPerPublisher(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=500, db_collation='Greek_CI_AS', blank=True, null=True)
    publisher_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'texts_to_clear_per_publisher'


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, db_collation='Greek_CI_AS', blank=True, null=True)
    password = models.CharField(max_length=50, db_collation='Greek_CI_AS', blank=True, null=True)
    publisher_id = models.IntegerField(blank=True, null=True)
    user_level = models.CharField(max_length=50, db_collation='Greek_CI_AS', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'users'
