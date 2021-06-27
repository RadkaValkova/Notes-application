from django.urls import path

from notes.notes_app.views import edit_note, delete_note, note_details, add_note, index

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', note_details, name='note details'),

]