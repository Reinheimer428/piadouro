from django.urls import path
from piado.views import PiadoCreate, PiadoDelete, PiadoLike, RePiado, PiadoView, PiadoComment, HashtagsList, HashtagDetail

urlpatterns = [
    path('adicionar/', PiadoCreate.as_view(), name='piado-create'),
    path('hashtags/', HashtagsList.as_view(), name='hashtags'),
    path('remover/<int:pk>/', PiadoDelete.as_view(), name='piado-delete'),
    path('curtir/<int:pk>/', PiadoLike.as_view(), name='piado-like'),
    path('repiar/<int:pk>/', RePiado.as_view(), name='repiar'),
    path('<int:pk>/', PiadoView.as_view(), name='piado-detail'),
    path('comentario/<int:hospedeiro>/', PiadoComment.as_view(), name='piado-comment'),
    path('hashtags/<slug:conteudo>', HashtagDetail.as_view(), name='hashtag-detail'),
]
