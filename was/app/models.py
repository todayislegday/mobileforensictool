from django.db import models


#db 모델작성

class contacts_model(models.Model): #어진
   
    class Meta: 
        managed = False 
        app_label = "contacts" 
        db_table = 'search_index'

    id = models.AutoField(db_column='contact_id',primary_key=True)
    name = models.TextField(db_column='sec_name',blank=True,null=True)
    number = models.TextField(db_column='tokens',blank=True,null=True)

class calllog_model(models.Model): #용하
   
    class Meta: 
        managed = False 
        app_label = "calllog" 
        db_table = 'calls'

    id = models.AutoField(db_column='_id',primary_key=True)
    number = models.TextField(blank=True,null=True)
    date = models.TextField(blank=True,null=True)
    duration = models.TextField(blank=True,null=True)
    name=models.TextField(blank=True,null=True)
    type=models.TextField(blank=True,null=True)

class message1_model(models.Model): #어진
   
    class Meta: 
        managed = False 
        app_label = "message" 
        db_table = 'parts'

    id = models.AutoField(db_column='_id',primary_key=True)
    text = models.TextField(blank=True,null=True)

class message2_model(models.Model): #어진
   
    class Meta: 
        managed = False 
        app_label = "message" 
        db_table = 'messages'

    id = models.AutoField(db_column='_id',primary_key=True)
    created_timestamp = models.TextField(blank=True,null=True)
    recipients = models.TextField(blank=True,null=True)

class mms_model(models.Model): #용하
   
    class Meta: 
        managed = False 
        app_label = "mms" 
        db_table = 'messages'

    id = models.AutoField(db_column='_id',primary_key=True)
    address= models.TextField(blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    date = models.TextField(blank=True,null=True)
    box_type= models.TextField(blank=True,null=True)
    
class map_model(models.Model): #재식

    class Meta: 
        managed = False 
        app_label = "map" 
        db_table = 'files'
    
    id= models.AutoField(db_column='_id',primary_key=True)
    lat=models.FloatField(db_column='latitude',blank=True,null=True)
    longt=models.FloatField(db_column='longitude',blank=True,null=True)
    displayname=models.TextField(db_column='_display_name',blank=True,null=True)
    data=models.TextField(db_column='_data',blank=True,null=True)
    datetaken=models.TextField(blank=True,null=True)
    
    
class chrome2_model(models.Model): #용하

    class Meta: 
        managed = False 
        app_label = "chrome2" 
        db_table = 'keyword_search_terms'
    
    id= models.AutoField(db_column='keyword_id',primary_key=True)
    url_id=models.FloatField(blank=True,null=True)
    term=models.FloatField(blank=True,null=True)

class chrome3_model(models.Model): #용하

    class Meta: 
        managed = False 
        app_label = "chrome2" 
        db_table = 'urls'
    
    id= models.AutoField(primary_key=True)
    url=models.FloatField(blank=True,null=True)
    title=models.FloatField(blank=True,null=True)

class chrome4_model(models.Model): #용하

    class Meta: 
        managed = False 
        app_label = "chrome2" 
        db_table = 'visits'
    
    id= models.AutoField(primary_key=True)
    url=models.FloatField(blank=True,null=True)
    visit_time=models.FloatField(blank=True,null=True)

class chrome5_model(models.Model): #용하

    class Meta: 
        managed = False 
        app_label = "chrome2" 
        db_table = 'downloads'
    
    id=models.AutoField(primary_key=True)
   

class chrome6_model(models.Model): #용하

    class Meta: 
        managed = False 
        app_label = "chrome2" 
        db_table = 'downloads_url_chains'
    
    id= models.AutoField(primary_key=True)
    url=models.FloatField(blank=True,null=True)
   

class Sam1_model(models.Model): #용하

    class Meta: 
        managed = False 
        app_label = "SAMINT" 
        db_table = 'keyword_search_terms'
    
    id= models.AutoField(db_column='keyword_id',primary_key=True)
    url_id=models.FloatField(blank=True,null=True)
    term=models.FloatField(blank=True,null=True)

class Sam2_model(models.Model): #용하

    class Meta: 
        managed = False 
        app_label = "SAMINT" 
        db_table = 'urls'
    
    id= models.AutoField(primary_key=True)
    url=models.FloatField(blank=True,null=True)
    title=models.FloatField(blank=True,null=True)

class Sam3_model(models.Model): #용하

    class Meta: 
        managed = False 
        app_label = "SAMINT" 
        db_table = 'visits'
    
    id= models.AutoField(primary_key=True)
    url=models.FloatField(blank=True,null=True)
    visit_time=models.FloatField(blank=True,null=True)

class Sam4_model(models.Model): #용하

    class Meta: 
        managed = False 
        app_label = "SAMINT" 
        db_table = 'downloads'
    
    id= models.AutoField(primary_key=True)
  

class Sam5_model(models.Model): #용하

    class Meta: 
        managed = False 
        app_label = "SAMINT" 
        db_table = 'downloads_url_chains'
    
    id= models.AutoField(primary_key=True)
    url=models.FloatField(blank=True,null=True)
  

class webdowndata_model(models.Model): #용하

    class Meta: 
        managed = False 
        app_label = "WebDowndata" 
        db_table = 'downloads'
    
    id= models.AutoField(db_column='_id',primary_key=True)
    uri=models.FloatField(blank=True,null=True)
    


class webext_model(models.Model): #용하

    class Meta: 
        managed = False 
        app_label = "Webext" 
        db_table = 'downloads'
    
    id= models.AutoField(db_column='_id',primary_key=True)
    _display_name=models.FloatField(blank=True,null=True)
    date_added=models.FloatField(blank=True,null=True)
    download_uri=models.FloatField(blank=True,null=True)
    owner_package_name = models.TextField(blank=True, null=True)
    _data = models.TextField(blank=True, null=True)

class Appinslog_model(models.Model): #용하

    class Meta: 
        managed = False 
        app_label = "Appinslog" 
        db_table = 'appstate'
    
    id= models.TextField(db_column='package_name',primary_key=True)
    title=models.FloatField(blank=True,null=True)
    first_download_ms=models.FloatField(blank=True,null=True)
    delivery_data_timestamp_ms=models.FloatField(blank=True,null=True)
    last_update_timestamp_ms=models.FloatField(blank=True,null=True)
    install_request_timestamp_ms=models.FloatField(blank=True,null=True)
    package_name= models.TextField(blank=True, null=True)

class Media_model(models.Model): #용하

    class Meta: 
        managed = False 
        app_label = "Media" 
        db_table = 'files'
    
    id= models.AutoField(db_column='_id',primary_key=True)
    date_added=models.FloatField(blank=True,null=True)
    title=models.FloatField(blank=True,null=True)
    bucket_display_name = models.TextField(blank=True, null=True)
    owner_package_name = models.TextField(blank=True, null=True)
    data= models.TextField(db_column='_data',blank=True, null=True)

    
class calendar_model(models.Model): #귀수
   
    class Meta: 
        managed = False 
        app_label = "Calendar" 
        db_table = 'Events'

    id = models.AutoField(db_column='_id',primary_key=True)
    title = models.TextField(blank=True,null=True)
    dtstart = models.FloatField(blank=True,null=True)
    dtend = models.FloatField(blank=True,null=True)