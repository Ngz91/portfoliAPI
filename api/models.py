from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField
import multiselectfield

class Project(models.Model):
    tech_choice = (
        ("Python", "Python"),
        ("Javascript", "Javascript"),
        ("Typescript", "Typescript"),
        ("Html5", "Html5"),
        ("Css3", "Css3"),
        ("React", "React"),
        ("NextJs", "NextJs"),
        ("TailwindCss", "TailwindCss"),
        ("MaterialUI", "MaterialUI"),
        ("Bootstrap", "Bootstrap"),
        ("Django/DRF", "Django/DRF"),
        ("Sqlite", "Sqlite"),
        ("Postgresql", "Postgresql"),
        ("MySql", "MySql"),
        ("Graphql", "Graphql"),
        ("Anaconda", "Anaconda"),
        ("Tensorflow", "Tensorflow"),
        ("Numpy", "Numpy"),
        ("Pandas", "Pandas"),
        ("Jupyter", "Jupyter"),
        ("Pytest", "Pytest"),
        ("Selenium", "Selenium"),
        ("Heroku", "Heroku"),
        ("Ubuntu", "Ubuntu"),
        ("Linux", "Linux"),
        ("Vim", "Vim"),
        ("Vscode", "Vscode"),
    )

    name = models.CharField(max_length=255, verbose_name="Project's name", help_text="Required", db_index=True)
    description = models.TextField(verbose_name="Project's description", help_text="Required")
    brief_description = models.CharField(max_length=400, verbose_name="Brief description", help_text="Required", null=True)
    slug = models.SlugField(max_length=255, help_text="Required", unique=True)
    image = models.ImageField(upload_to="projects/%Y/%m/%d", blank=True, verbose_name="Project's image")
    github_repo = models.URLField(blank=True)
    technologies = MultiSelectField(choices=tech_choice)
    project_date = models.DateField(verbose_name="Date when the porject was created", help_text="Required")

    class Meta:
        ordering = ("name",)
        index_together = (("id", "slug"))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("api:project-details", args=[self.id, self.slug])
