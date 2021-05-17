from django.db import models

#db 모델작성

class contacts_model(models.Model): 
   
    class Meta: 
        managed = False 
        app_label = "contacts" 
        db_table = 'search_index'

    id = models.AutoField(db_column='contact_id',primary_key=True)
    name = models.TextField(db_column='sec_name',blank=True,null=True)
    number = models.TextField(db_column='tokens',blank=True,null=True)
    
    
class message1_model(models.Model): 
   
    class Meta: 
        managed = False 
        app_label = "message" 
        db_table = 'parts'

    id = models.AutoField(db_column='_id',primary_key=True)
    text = models.TextField(blank=True,null=True)

class message2_model(models.Model): 
   
    class Meta: 
        managed = False 
        app_label = "message" 
        db_table = 'messages'

    id = models.AutoField(db_column='_id',primary_key=True)
    created_timestamp = models.TextField(blank=True,null=True)
    recipients = models.TextField(blank=True,null=True)

class map_model(models.Model): 

    class Meta: 
        managed = False 
        app_label = "map" 
        db_table = 'location'
    
    id= models.AutoField(db_column='loc_p_id',primary_key=True)
    lat=models.FloatField(db_column='latitude')
    longt=models.FloatField(db_column='longitude')

