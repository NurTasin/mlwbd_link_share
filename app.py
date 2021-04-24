#you cant share mlwbd links using messanger or other major social platforms
#but you can share links with mlwbd_link_share web app
from flask import Flask, request, redirect

main_uri="https://mlwbd.mobi/"
app=Flask(__name__)
@app.route("/")
def home():
    if "s" in list(request.args.keys()):
        return redirect(main_uri+"?s="+str(request.args["s"].replace(" ","+")))
    else:
        return "Service Undefined.. :'( <br>BTW. If you want to support developer then meet him @ <a href=\"https://www.github.com/NurTasin/\">GitHub</a>"


@app.route("/movie/<movie_name>/")
def get_movie(movie_name):
    return redirect(main_uri+"movie/"+movie_name+"/")

@app.route("/genre/<gname>/")
def getGenre(gname):
    return redirect(main_uri+"genre/"+gname+"/")

if __name__=="__main__":
    app.run(debug=True)
