from django.db import models
from pytils.translit import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class GalleryImage(models.Model):
    image = models.ImageField('Картинка', upload_to='event_img/', blank=False)
    showIndex = models.BooleanField('Показывать на главной?', default=False)

class Event(models.Model):
    name = models.CharField('Название', max_length=255, default='')
    name_slug = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='event_img/', blank=True)
    place = models.CharField('Место', max_length=255, default='')
    shortDescription = models.CharField('Короткое описание', max_length=200, default='')
    description = RichTextUploadingField('Описание', blank=True, null=True)
    is_active = models.BooleanField('Отображать на главной?', default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return 'Ивент %s ' % self.name

    class Meta:
        verbose_name = "Ивент"
        verbose_name_plural = "Ивенты"


class EventItemImage(models.Model):
        item = models.ForeignKey(Event, blank=False, null=True, on_delete=models.CASCADE, verbose_name='Кейс',
                                 related_name='eventItemImages')
        image = models.ImageField('Картинка', upload_to='portfolio_img/', blank=False)


class News(models.Model):
    name = models.CharField('Название', max_length=255, default='')
    name_slug = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='event_img/', blank=True)
    shortDescription = models.CharField('Короткое описание', max_length=200, default='')
    description = RichTextUploadingField('Описание', blank=True, null=True)
    is_active = models.BooleanField('Отображать на главной?', default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return 'Новость %s ' % self.name

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Callback(models.Model):
    name = models.CharField('Поле - Ваше имя',max_length=255, blank=False, default='Нет данных')
    company = models.CharField('Поле - Телефон', max_length=255, blank=True, default='Нет данных')
    phone = models.CharField('Поле - Телефон', max_length=255, blank=False, default='Нет данных')
    email = models.EmailField('Поле - Email', max_length=255, blank=True, default='Нет данных')
    message = models.TextField('Поле - Сообщение', max_length=255, blank=True, default='Нет данных')