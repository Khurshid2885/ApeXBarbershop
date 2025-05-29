from modeltranslation.translator import translator, TranslationOptions
from .models import Service
from .models.service import ServiceCategory


class ServiceTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Service, ServiceTranslationOptions)


class ServiceCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(ServiceCategory, ServiceCategoryTranslationOptions)
