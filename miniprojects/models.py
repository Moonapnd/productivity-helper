from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
   

class Miniproject(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    github_url = models.URLField(blank=True)
    tags = TaggableManager(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    tools_used = models.TextField(blank=True)
    docs_used = models.TextField(blank=True)
    pdf_docs = models.FileField(upload_to='pdf docs', blank=True, null=True) # PDF Book uploaded (optional)
    finished = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('miniprojects:miniproject-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ('-updated_date', )

    def __str__(self):
        return self.title


