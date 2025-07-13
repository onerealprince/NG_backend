from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    youtube_video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProjectCard(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='cards')
    title = models.CharField(max_length=150)
    content = models.TextField()

    def __str__(self):
        return f"Card: {self.title} ({self.project.title})"


class ProjectEvent(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=150)
    description = models.TextField()
    event_date = models.DateField()
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Event: {self.name} ({self.project.title})"
