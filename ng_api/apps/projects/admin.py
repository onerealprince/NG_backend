from django.contrib import admin
from .models import Project, ProjectCard, ProjectEvent

# Inline for project cards
class ProjectCardInline(admin.TabularInline):
    model = ProjectCard
    extra = 1

# Inline for project events
class ProjectEventInline(admin.TabularInline):
    model = ProjectEvent
    extra = 1

# Main project admin
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    inlines = [ProjectCardInline, ProjectEventInline]


@admin.register(ProjectCard)
class ProjectCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'project')
    search_fields = ('title', 'content')
    list_filter = ('project',)


@admin.register(ProjectEvent)
class ProjectEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'event_date', 'location')
    search_fields = ('name', 'description', 'location')
    list_filter = ('event_date', 'project')
