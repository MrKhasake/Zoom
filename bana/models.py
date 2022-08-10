from django.db import models

# Create your models here.
class Entrepreneurship(models.Model):
    content = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='pics')
    heading1 = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    body1 = models.TextField(null=True, blank=True)
    list1 = models.CharField(max_length=1000, null=True, blank=True)
    body_list1 = models.TextField(null=True, blank=True)
    list2 = models.CharField(max_length=1000, null=True, blank=True)
    body_list2 = models.TextField(null=True, blank=True)
    list3 = models.CharField(max_length=1000, null=True, blank=True)
    body_list3 = models.TextField(null=True, blank=True)

    image2 = models.ImageField(upload_to='pics', null=True, blank=True)
    heading2 = models.CharField(max_length=1000, null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    list4 = models.CharField(max_length=1000, null=True, blank=True)
    body_list4 = models.TextField(null=True, blank=True)
    list5 = models.CharField(max_length=1000, null=True, blank=True)
    body_list5 = models.TextField(null=True, blank=True)
    list6 = models.CharField(max_length=1000, null=True, blank=True)
    body_list6 = models.TextField(null=True, blank=True)
    list7 = models.CharField(max_length=1000, null=True, blank=True)
    body_list7 = models.TextField(null=True, blank=True)
    list8 = models.CharField(max_length=1000, null=True, blank=True)
    body_list8 = models.TextField(null=True, blank=True)
    list9 = models.CharField(max_length=1000, null=True, blank=True)
    body_list9 = models.TextField(null=True, blank=True)

    image3 = models.ImageField(upload_to='pics', null=True, blank=True)
    heading3 = models.CharField(max_length=1000, null=True, blank=True)
    body3 = models.TextField(null=True, blank=True)
    list10 = models.CharField(max_length=1000, null=True, blank=True)
    body_list10 = models.TextField(null=True, blank=True)
    list11 = models.CharField(max_length=1000, null=True, blank=True)
    body_list11 = models.TextField(null=True, blank=True)
    list12 = models.CharField(max_length=1000, null=True, blank=True)
    body_list12 = models.TextField(null=True, blank=True)
    list13 = models.CharField(max_length=1000, null=True, blank=True)
    body_list13 = models.TextField(null=True, blank=True)
    list14 = models.CharField(max_length=1000, null=True, blank=True)
    body_list14 = models.TextField(null=True, blank=True)
    list15 = models.CharField(max_length=1000, null=True, blank=True)
    body_list15 = models.TextField(null=True, blank=True)

    image4 = models.ImageField(upload_to='pics', null=True, blank=True)
    heading4 = models.CharField(max_length=1000, null=True, blank=True)
    body4 = models.TextField(null=True, blank=True)
    list16 = models.CharField(max_length=1000, null=True, blank=True)
    body_list16 = models.TextField(null=True, blank=True)
    list17 = models.CharField(max_length=1000, null=True, blank=True)
    body_list17 = models.TextField(null=True, blank=True)
    list18 = models.CharField(max_length=1000, null=True, blank=True)
    body_list18 = models.TextField(null=True, blank=True)
    list19 = models.CharField(max_length=1000, null=True, blank=True)
    body_list19 = models.TextField(null=True, blank=True)
    list20 = models.CharField(max_length=1000, null=True, blank=True)
    body_list20 = models.TextField(null=True, blank=True)
    list21 = models.CharField(max_length=1000, null=True, blank=True)
    body_list21 = models.TextField(null=True, blank=True)

    class Meta:
      verbose_name_plural = 'Entrepreneurship'

class Sales(models.Model):
    content = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='pics')
    heading1 = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    body1 = models.TextField(null=True, blank=True)
    list1 = models.CharField(max_length=1000, null=True, blank=True)
    body_list1 = models.TextField(null=True, blank=True)
    list2 = models.CharField(max_length=1000, null=True, blank=True)
    body_list2 = models.TextField(null=True, blank=True)
    list3 = models.CharField(max_length=1000, null=True, blank=True)
    body_list3 = models.TextField(null=True, blank=True)

    image2 = models.ImageField(upload_to='pics', null=True, blank=True)
    heading2 = models.CharField(max_length=1000, null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    list4 = models.CharField(max_length=1000, null=True, blank=True)
    body_list4 = models.TextField(null=True, blank=True)
    list5 = models.CharField(max_length=1000, null=True, blank=True)
    body_list5 = models.TextField(null=True, blank=True)
    list6 = models.CharField(max_length=1000, null=True, blank=True)
    body_list6 = models.TextField(null=True, blank=True)
    list7 = models.CharField(max_length=1000, null=True, blank=True)
    body_list7 = models.TextField(null=True, blank=True)
    list8 = models.CharField(max_length=1000, null=True, blank=True)
    body_list8 = models.TextField(null=True, blank=True)
    list9 = models.CharField(max_length=1000, null=True, blank=True)
    body_list9 = models.TextField(null=True, blank=True)

    image3 = models.ImageField(upload_to='pics', null=True, blank=True)
    heading3 = models.CharField(max_length=1000, null=True, blank=True)
    body3 = models.TextField(null=True, blank=True)
    list10 = models.CharField(max_length=1000, null=True, blank=True)
    body_list10 = models.TextField(null=True, blank=True)
    list11 = models.CharField(max_length=1000, null=True, blank=True)
    body_list11 = models.TextField(null=True, blank=True)
    list12 = models.CharField(max_length=1000, null=True, blank=True)
    body_list12 = models.TextField(null=True, blank=True)
    list13 = models.CharField(max_length=1000, null=True, blank=True)
    body_list13 = models.TextField(null=True, blank=True)
    list14 = models.CharField(max_length=1000, null=True, blank=True)
    body_list14 = models.TextField(null=True, blank=True)
    list15 = models.CharField(max_length=1000, null=True, blank=True)
    body_list15 = models.TextField(null=True, blank=True)

    image4 = models.ImageField(upload_to='pics', null=True, blank=True)
    heading4 = models.CharField(max_length=1000, null=True, blank=True)
    body4 = models.TextField(null=True, blank=True)
    list16 = models.CharField(max_length=1000, null=True, blank=True)
    body_list16 = models.TextField(null=True, blank=True)
    list17 = models.CharField(max_length=1000, null=True, blank=True)
    body_list17 = models.TextField(null=True, blank=True)
    list18 = models.CharField(max_length=1000, null=True, blank=True)
    body_list18 = models.TextField(null=True, blank=True)
    list19 = models.CharField(max_length=1000, null=True, blank=True)
    body_list19 = models.TextField(null=True, blank=True)
    list20 = models.CharField(max_length=1000, null=True, blank=True)
    body_list20 = models.TextField(null=True, blank=True)
    list21 = models.CharField(max_length=1000, null=True, blank=True)
    body_list21 = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Sales'

    


class Finance(models.Model):
    content = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='pics')
    heading1 = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    body1 = models.TextField(null=True, blank=True)
    list1 = models.CharField(max_length=1000, null=True, blank=True)
    body_list1 = models.TextField(null=True, blank=True)
    list2 = models.CharField(max_length=1000, null=True, blank=True)
    body_list2 = models.TextField(null=True, blank=True)
    list3 = models.CharField(max_length=1000, null=True, blank=True)
    body_list3 = models.TextField(null=True, blank=True)

    image2 = models.ImageField(upload_to='pics', null=True, blank=True)
    heading2 = models.CharField(max_length=1000, null=True, blank=True)
    body2 = models.TextField(null=True, blank=True)
    list4 = models.CharField(max_length=1000, null=True, blank=True)
    body_list4 = models.TextField(null=True, blank=True)
    list5 = models.CharField(max_length=1000, null=True, blank=True)
    body_list5 = models.TextField(null=True, blank=True)
    list6 = models.CharField(max_length=1000, null=True, blank=True)
    body_list6 = models.TextField(null=True, blank=True)
    list7 = models.CharField(max_length=1000, null=True, blank=True)
    body_list7 = models.TextField(null=True, blank=True)
    list8 = models.CharField(max_length=1000, null=True, blank=True)
    body_list8 = models.TextField(null=True, blank=True)
    list9 = models.CharField(max_length=1000, null=True, blank=True)
    body_list9 = models.TextField(null=True, blank=True)

    image3 = models.ImageField(upload_to='pics', null=True, blank=True)
    heading3 = models.CharField(max_length=1000, null=True, blank=True)
    body3 = models.TextField(null=True, blank=True)
    list10 = models.CharField(max_length=1000, null=True, blank=True)
    body_list10 = models.TextField(null=True, blank=True)
    list11 = models.CharField(max_length=1000, null=True, blank=True)
    body_list11 = models.TextField(null=True, blank=True)
    list12 = models.CharField(max_length=1000, null=True, blank=True)
    body_list12 = models.TextField(null=True, blank=True)
    list13 = models.CharField(max_length=1000, null=True, blank=True)
    body_list13 = models.TextField(null=True, blank=True)
    list14 = models.CharField(max_length=1000, null=True, blank=True)
    body_list14 = models.TextField(null=True, blank=True)
    list15 = models.CharField(max_length=1000, null=True, blank=True)
    body_list15 = models.TextField(null=True, blank=True)

    image4 = models.ImageField(upload_to='pics', null=True, blank=True)
    heading4 = models.CharField(max_length=1000, null=True, blank=True)
    body4 = models.TextField(null=True, blank=True)
    list16 = models.CharField(max_length=1000, null=True, blank=True)
    body_list16 = models.TextField(null=True, blank=True)
    list17 = models.CharField(max_length=1000, null=True, blank=True)
    body_list17 = models.TextField(null=True, blank=True)
    list18 = models.CharField(max_length=1000, null=True, blank=True)
    body_list18 = models.TextField(null=True, blank=True)
    list19 = models.CharField(max_length=1000, null=True, blank=True)
    body_list19 = models.TextField(null=True, blank=True)
    list20 = models.CharField(max_length=1000, null=True, blank=True)
    body_list20 = models.TextField(null=True, blank=True)
    list21 = models.CharField(max_length=1000, null=True, blank=True)
    body_list21 = models.TextField(null=True, blank=True) 
    
    class Meta:
        verbose_name_plural = 'Finance'


class Slide(models.Model):
    img1 = models.ImageField(upload_to='pics')
    text1 = models.CharField(max_length=1000)
    summary1 = models.CharField(max_length=1000)

    img2 = models.ImageField(upload_to='pics')
    text2 = models.CharField(max_length=1000)
    summary2 = models.CharField(max_length=1000)

    img3 = models.ImageField(upload_to='pics')
    text3 = models.CharField(max_length=1000)
    summary3 = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = 'Slide'

class News(models.Model):
    pic1 = models.ImageField(upload_to='pics')
    entrepreneurship = models.CharField(max_length=1000)
    heading1 = models.CharField(max_length=1000)
    body1 = models.TextField()

    pic2 = models.ImageField(upload_to='pics')
    sales = models.CharField(max_length=1000)
    heading2 = models.CharField(max_length=1000)
    body2 = models.TextField()

    pic3 = models.ImageField(upload_to='pics')
    finance = models.CharField(max_length=1000)
    heading3 = models.CharField(max_length=1000)
    body3 = models.TextField()

    class Meta:
        verbose_name_plural = 'News'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'Contact'
