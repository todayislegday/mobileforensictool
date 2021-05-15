from django.db import models

#db 모델작성

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
    
    loc_p_id = models.AutoField(primary_key=True)
    latitude=models.FloatField()
    longitude=models.FloatField()

