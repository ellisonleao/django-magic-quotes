# -*- encoding: utf-8 -*-
from managers import PublishedManager,NonPublishedManager

class Publishable(models.Model):                                                
    """                                                                         
    Campos padroes                                                              
    """                                                                         
    created_at = models.DateTimeField(auto_now_add=True)                        
    updated_at = models.DateTimeField(auto_now=True)                            
    published = models.BooleanField(verbose_name=u"Publicado",\
        default=True, db_index=True)
                                                                                
    objects = PublishedManager()                                               
    hidden = NonPublishedManager()                                      
                                                                                
    class Meta:                                                                 
        abstract = True 
