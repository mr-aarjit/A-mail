from .models import Mail
from .logic import Mail_geneneration
from django.shortcuts import render, redirect
from django.db import DatabaseError

# Create your views here.
def home(request):
    return render(request, 'index.html')



def prompt(request):
    return render(request, 'prompt.html')



def generated(request):
    if(request.method == "GET"):
        return redirect('home')
    else:

        user_prompt = request.POST.get("prompt")

        already_generated = None
        try:
            already_generated = Mail.objects.filter(
                prompt=user_prompt,
            ).first()
        except DatabaseError:
            already_generated = None

        if already_generated and already_generated.generated_mail:
            created_mail = already_generated.generated_mail
            print('We used existing mail')
        else:
            created_mail = Mail_geneneration(user_prompt)
            if ( created_mail != "Hello, I am Aarjit's Mail Generator. I am designed to generate mails." and created_mail != "Service temporarily unavailable due to API limits. "):
                try:
                    Mail.objects.create(
                        prompt=user_prompt,
                        generated_mail=created_mail
                    )
                except DatabaseError:
                    # Serverless deployments often use read-only/non-migrated SQLite.
                    pass
            

        return render(request, 'output.html', context={"generated_email": created_mail})
    



