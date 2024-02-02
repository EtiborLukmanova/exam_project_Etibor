from django.urls import path
from .views import SweetListView, SweetDetailView, UpdateSweetView, DeleteSweetView,AddSweetView, AddCommentView, DeleteCommentView, UpdateCommentView

urlpatterns = [
    path('sweets/', SweetListView.as_view(), name='sweet_list'),
    path('sweets/<int:pk>/', SweetDetailView.as_view(), name='sweet_detail'),
    path('update/<int:pk>/', UpdateSweetView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteSweetView.as_view(), name='delete'),
    path('sweet/add/sweet/', AddSweetView.as_view(), name='add_sweet'),
    path('sweets/add_comment/<int:pk>/', AddCommentView.as_view(), name='add_comment'),
    path("sweets/delete/comment/<int:pk>/", DeleteCommentView.as_view(), name="delete_comment"),
    path("sweets/update/comment/<int:pk>/", UpdateCommentView.as_view(), name="update_comment"),
]
