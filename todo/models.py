from django.db import models
from django.utils.text import slugify



class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    slug =  models.SlugField(blank=True, null=True)


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        global str
        if self.slug == None:
            slug = slugify(self.title)

            has_slug = Todo.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count)
                has_slug = Todo.objects.filter(slug=slug).exists()
            self.slug = slug
        super().save(*args, **kwargs)