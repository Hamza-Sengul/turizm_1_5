# core/urls.py

from django.urls import path
from .views import HomeView, HouseDetailView, AboutView, PrivacySecurityView, TermsView, CancellationRefundView, ContactView, RefundRequestView, FAQView
from .views import (
    AdminDashboardView, 
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    HouseListView, HouseCreateView, HouseUpdateView, HouseDeleteView,
    HomeView, HouseDetailView, AboutView, PrivacySecurityView, TermsView, CancellationRefundView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('house/<int:pk>/', HouseDetailView.as_view(), name='house_detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('gizlilik-guvenlik/', PrivacySecurityView.as_view(), name='privacy_security'),
    path('kullanim-kosullari/', TermsView.as_view(), name='terms'),
    path('iptal-iade/', CancellationRefundView.as_view(), name='cancellation_refund'),
    path('iletisim/', ContactView.as_view(), name='contact'),
    path('iade-talebi/', RefundRequestView.as_view(), name='refund_request'),
    path('sss/', FAQView.as_view(), name='faq'),
    path('admin-panel/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin-panel/categories/', CategoryListView.as_view(), name='admin_category_list'),
    path('admin-panel/categories/create/', CategoryCreateView.as_view(), name='admin_category_create'),
    path('admin-panel/categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='admin_category_update'),
    path('admin-panel/categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='admin_category_delete'),

    path('admin-panel/houses/', HouseListView.as_view(), name='admin_house_list'),
    path('admin-panel/houses/create/', HouseCreateView.as_view(), name='admin_house_create'),
    path('admin-panel/houses/<int:pk>/update/', HouseUpdateView.as_view(), name='admin_house_update'),
    path('admin-panel/houses/<int:pk>/delete/', HouseDeleteView.as_view(), name='admin_house_delete'),
]
