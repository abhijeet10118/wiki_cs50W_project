from django.shortcuts import render
import markdown
import random as rand
from . import util

def convert_md_to_markdown(title):
    content=util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None :
        return None
    else:
        return markdowner.convert(content)

def index(request):
  
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def entry(request,title):
    html_content=convert_md_to_markdown(title)
    if html_content == None :
        return render(request,"encyclopedia/error.html",
                      {"message":"this file is not present"})
    else:
        return render(request,"encyclopedia/entry.html",
                      {"title":title,
                      "content":html_content}
                      )

def search(request):
    if request.method=="POST":
        entry_search = request.POST['q']
        html_content = convert_md_to_markdown(entry_search)
        if html_content is not None :
            return render(request,"encyclopedia/entry.html",
                      {"title":entry_search,
                      "content":html_content}
                      )
        else :
            all=util.list_entries()
            reccomondation=[]
            for data in all :
                if entry_search.lower() in data.lower() :
                    reccomondation.append(data)
            if len(reccomondation) != 0:
                return render(request,"encyclopedia/recomend.html",{
                    "reccomondation":reccomondation
                })
                    
            else :
                return render(request,"encyclopedia/empty.html")
                    
def new_page(request):
    if request.method == "GET":
        return render (request , "encyclopedia/new.html")
    else:
        new_title=request.POST['title']
        content=request.POST['content']
        all=util.list_entries()
        for data in all :
            if new_title.lower() == data.lower() :
                return render(request,"encyclopedia/error.html",{
                    "message":"there's already a file with same name"
                })
        content = f"# {new_title}\n\n{content}"
           
        util.save_entry(new_title,content)
        html_content=convert_md_to_markdown(new_title)
        return render(request,"encyclopedia/entry.html",
                      {"title":new_title,
                      "content":html_content}
                      )
        
def edit(request):
    if request.method=="POST":
        title=request.POST['entry_title']
        content=util.get_entry(title)
        return render(request,"encyclopedia/edit.html",
                      {
                          "title":title,
                          "content":content
                      })
def do_edit(request):
    if request.method=="POST" :
        title=request.POST['title']
        content=request.POST['content']
        util.save_entry(title,content)
        html_content=convert_md_to_markdown(title)
        return render(request,"encyclopedia/entry.html",
                      {"title":title,
                      "content":html_content}
                      )

def random(request):
    all=util.list_entries()
    k=rand.choice(all)
    html_content=convert_md_to_markdown(k)
    return render(request,"encyclopedia/entry.html",
                      {"title":k,
                      "content":html_content}
                      )
    
    
        
        
    
    
    
        
        
                
        
    

