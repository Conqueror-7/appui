from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.apps import apps
from django.contrib import messages
from .models import Message, Notification


@login_required
def envoyer_message(request, destinataire_id):
    user_model = apps.get_model(settings.AUTH_USER_MODEL)
    destinataire = get_object_or_404(user_model, id=destinataire_id)

    if request.method == 'POST':
        contenu = request.POST.get('contenu')
        if contenu:
            message = Message.objects.create(
                expediteur=request.user,
                destinataire=destinataire,
                contenu=contenu
            )
            Notification.objects.create(utilisateur=destinataire, message=message)
            messages.success(request, "✅ Message envoyé avec succès !")
            return redirect('conversations')
        else:
            messages.error(request, "❌ Le message ne peut pas être vide.")
            return redirect('conversations')

    return render(request, 'messagerie/envoyer.html', {'destinataire': destinataire})


@login_required
def conversations(request):
    """Boîte de réception"""
    messages_recus = Message.objects.filter(destinataire=request.user).order_by('-date_envoi')
    return render(request, 'messagerie/conversations.html', {'messages': messages_recus})


@login_required
def details_message(request, message_id):
    """Détail d'un message"""
    message = get_object_or_404(Message, id=message_id, destinataire=request.user)

    if not message.lu:
        message.lu = True
        message.save()
        Notification.objects.filter(message=message, utilisateur=request.user).update(lu=True)

    return render(request, 'messagerie/details.html', {'message': message})


# Garde les anciennes fonctions pour compatibilité (si besoin)
@login_required
def boite_reception(request):
    return conversations(request)


@login_required
def lire_message(request, message_id):
    return details_message(request, message_id)


@login_required
def notifications(request):
    user_notifications = Notification.objects.filter(utilisateur=request.user).order_by('-date_creation')
    return render(request, 'messagerie/notifications.html', {'notifications': user_notifications})


@login_required
def marquer_notification_lue(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, utilisateur=request.user)
    notification.lu = True
    notification.save()
    return redirect('details_message', message_id=notification.message.id)