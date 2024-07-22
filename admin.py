from django.contrib import admin
from .models import Banner, Category, Brand, Color, Size, Product, ProductAttribute, CartOrder, CartOrderItems, ProductReview, Wishlist, UserAddressBook

# Registering models without any custom admin classes
admin.site.register(Brand)
admin.site.register(Size)

# Custom admin class for Banner
class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_txt', 'image_tag')  
admin.site.register(Banner, BannerAdmin)

# Custom admin class for Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')  
admin.site.register(Category, CategoryAdmin)

# Custom admin class for Color
class ColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'color_bg')  
admin.site.register(Color, ColorAdmin)

# Custom admin class for Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'brand', 'status', 'is_featured')  
    list_editable = ('status', 'is_featured')  
admin.site.register(Product, ProductAdmin)

# Custom admin class for ProductAttribute
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag', 'product', 'price', 'color', 'size') 
admin.site.register(ProductAttribute, ProductAttributeAdmin)

# Custom admin class for CartOrder
class CartOrderAdmin(admin.ModelAdmin):
    list_editable = ('paid_status', 'order_status')  
    list_display = ('user', 'total_amt', 'paid_status', 'order_dt', 'order_status')  
admin.site.register(CartOrder, CartOrderAdmin)

# Custom admin class for CartOrderItems
class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ('invoice_no', 'item', 'image_tag', 'qty', 'price', 'total') 
admin.site.register(CartOrderItems, CartOrderItemsAdmin)

# Custom admin class for ProductReview
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'review_text', 'get_review_rating')  
admin.site.register(ProductReview, ProductReviewAdmin)

# Registering Wishlist without any custom admin class
admin.site.register(Wishlist)

# Custom admin class for UserAddressBook
class UserAddressBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'status')  
admin.site.register(UserAddressBook, UserAddressBookAdmin)
