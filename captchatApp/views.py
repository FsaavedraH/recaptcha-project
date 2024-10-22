from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.

class Captchat(View):
    def get(self,request):
        img1 = {'name_image':'recaptcha1.png', 'is_img':True}
        img2 = {'name_image':'recaptcha2.png', 'is_img':True}
        img3 = {'name_image':'recaptcha3.png', 'is_img':True}
        img4 = {'name_image':'recaptcha4.png', 'is_img':True}
        img5 = {'name_image':'recaptcha5.png', 'is_img':True}
        img6 = {'name_image':'recaptcha6.png', 'is_img':True}
        img7 = {'name_image':'recaptcha7.png', 'is_img':True}
        img8 = {'name_image':'recaptcha8.png', 'is_img':True}
        img9 = {'name_image':'recaptcha9.png', 'is_img':True}
        img10 = {'name_image':'recaptcha10.png', 'is_img':True}
        img11 = {'name_image':'recaptcha11.png', 'is_img':True}
        img12 = {'name_image':'recaptcha12.png', 'is_img':True}
        
        
        array_img = [img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12]
        data = {
            'titulo': 'Selecciona las imagenes similares',
            'imagenes': array_img
        }
        return render(request,'captchat.html', context=data)
        
        

        
