from django.contrib import admin

from .models import Category, Item, Offer, ItemImage

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(ItemImage)
# admin.site.register(Offer)



def accept_offers(modeladmin, request, queryset):
    # Update selected offers to mark them as accepted
    queryset.update(is_accepted=True)

def reject_offers(modeladmin, request, queryset):
    # Update selected offers to mark them as rejected
    queryset.update(is_accepted=False)

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('item', 'offer_amount', 'is_accepted', 'submitted_by')
    list_filter = ('is_accepted',)

    actions = [accept_offers, reject_offers]

    def submitted_by(self, obj):
        return obj.created_by.username

    submitted_by.short_description = 'Submitted By'
