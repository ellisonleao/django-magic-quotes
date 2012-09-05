# -*- encoding: utf-8 -*-                                                       
                                                                                
from django.db import models                                                    
                                                                                
class PublishedManager(models.Manager):                                         
    def get_query_set(self):                                                    
        "Publicos por padrao"                                                   
        return super(PublishedManager, self).get_query_set().filter(published=True)
                                                                                
                                                                                
class NonPublishedManager(models.Manager):                                      
    def get_query_set(self):                                                    
        "Mostra os nao publicados"                                              
        return super(NonPublishedManager, self).get_query_set().filter(published=False)
