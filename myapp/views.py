from django.http import HttpResponse
from django.shortcuts import render
from multiprocessing import Process
from django.http import HttpResponse
#import os
import matplotlib.pyplot as plot
import numpy as np
import pandas as pd
from pylab import figure, axes, pie, title, hist
from matplotlib.backends.backend_agg import FigureCanvasAgg

#def inter(request):
    #return HttpResponse("Hello,welcome to prakash world.")

def index(request):
	dat = pd.read_csv('/home/luceifer/Desktop/st.csv')
	print(dat.describe())

def login(request):
   if request.method == 'POST':
      print ('Welcome')
      username = request.POST.get('name','')
      print ('hello '+username)
      text = "Hello ",username
      return HttpResponse(text)
   else:
      return HttpResponse('Error')

# Create your views here.
"""def dashpage(request):
	"os.system('python3 app.py')
	"return render(request, 'index.html')"""


def test_matplotlib(request):
    f = figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    fracs = [15,30,45, 10]
    explode=(0, 0.05, 0, 0)
    pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
    title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})

    canvas = FigureCanvasAgg(f)    
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
 
 
#def materplot(request):
#	dat = pd.read_csv('/home/luceifer/Desktop/st.csv')
#	print(dat.describe())
#	return HttpResponse('Error')
    
# def matplot(request):
	# dat = pd.read_csv('/home/luceifer/Desktop/st.csv')
	# print(dat.describe())
	#     return HttpResponse('Error')
    #         f = figure()
   	#     x = np.random.normal(size = 1000)
    # 	plot.hist(x, normed=True, bins=50)
    # 	plot.xlabel('Weight');
    # 	plot.ylabel('Probability');
    
    # 	canvas = FigureCanvasAgg(f)    
    # 	response = HttpResponse(content_type='image/png')
    # 	canvas.print_png(response)
    # 	return response
    
def preview(request):
   return render(request, 'preview.html')
   
def hgram(request):
   if request.method == 'POST':
      print ('hello')
      array = [1,3,4,4,8,9,10,12]
      range = int((max(array)) - min(array))+1
      bins = request.POST.get("bins")
      f = figure(1, figsize=(6,6))
      x = np.random.normal(size = 1000)
      plot.hist(x, normed=True,bins = range)
      plot.xlabel('Weight')
      plot.ylabel('Probability')
      plot.title('Histogram for weightlist')
      plot.show()
      canvas = FigureCanvasAgg(f)    
      response = HttpResponse(content_type='image/png')
      canvas.print_png(response)
      return response
   else:
      return render(request, 'preview.html')
     
