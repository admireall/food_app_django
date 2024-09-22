from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import item
from .forms import itemfor
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
#def index(request):
 #   item_list=item.objects.all()
    #template=loader.get_template('food/index.html') 
  #  context={
   #     'item_list':item_list,
    #}
    #return HttpResponse(template.render(context,request))
    #return render(request,'food/index.html',context)


#This is class based view:
class IndexClassView(ListView):
    model=item
    template_name='food/index.html'
    context_object_name='item_list'

#def detail(request,item_id):
 #   it=item.objects.get(pk=item_id)
  #  context={
   #     'it':it,
    #}
    #return render(request,'food/details.html',context)
    #return HttpResponse("This is id: %s" %item_id )


class Detail_class(DetailView):
    model=item
    template_name='food/details.html'

#def create_item(request):
 #   form=itemfor(request.POST or None)
#
 #   if form.is_valid():
  #      form.save()
   #     return redirect('food:index')
    #return render(request,'food/form.html',{'form':form})

class create_class(CreateView):
    model=item
    fields=['item_name','item_desc','item_price','item_image']
    template_name='food/form.html'
    def vaild_form(self,form):
        form.instance.user_name=self.request.user
        return super().vaild_form(form)

    



def update_item(request,id):
    item1=item.objects.get(id=id)
    form=itemfor(request.POST or None, instance=item1)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/form.html',{'form':form,'item1':item1})
def delete_item(request,id):
    item1=item.objects.get(id=id)

    if request.method=='POST':
        item1.delete()
        return redirect('food:index')
    return render(request,'food/delete.html',{'item1':item1})
    