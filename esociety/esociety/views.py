from django.http import HttpResponse
from django.shortcuts import render 
from django.conf.urls.static import static

def save_login(request):
     """ connect_mysql = esociety.connect('****', '***', '***', 'Esociety')
     cursorMYSQL = connect_mysql.cursor(esociety.cursors.DictCursor)
    query = "select id,ip,polling_time,communitydata,snmp_oid,lastcheck from snmptt_listpolls order by ip desc limit 100"
    cursorMYSQL.execute(query)
    b = cursorMYSQL.fetchall()
    connect_mysql.close() """

    # if request.POST:  
        # name=LoginForm(name.POST)

    # return render(request,"login.html")


def signup(request):
    return render(request,"signup.html")