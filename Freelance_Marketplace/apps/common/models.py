from django.db import models


# =========================================================
# BASE MODEL
# =========================================================

class BaseModel(models.Model):
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True



# =========================================================
# COUNTRY
# =========================================================

class Country(BaseModel):
    
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"



# =========================================================
# SKILLS
# =========================================================

class SkillsCategory(BaseModel):
    
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
  
  
class Skills(BaseModel):
    
    category = models.ForeignKey(
        SkillsCategory,
        related_name="skills",
        on_delete=models.CASCADE
    )
    
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        # ordering = ["created_at"]
 