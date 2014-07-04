#coding:utf-8#coding:utf-8
import requests, json, xmlrpclib
from django.shortcuts import HttpResponse, render, HttpResponseRedirect
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

# '_' -> 내부설정함수

def _check_agent(request):
    agent = request.META.get('HTTP_USER_AGENT', '').lower()
    if "iphone" in agent:
        agent = "iphone"
    elif "ipad" in agent:
        agent = "ipad"
    elif "android" in agent:
        agent = "android"
    else:
        agent = "web"
    return agent

def _check_domain(request):
    domain = request.get_host()
    return domain

def _load_rest(url, data, token=""):
    re = {}
    result = requests.post("http://rpc.brandmoa.net/"+url, data=data, headers={"X-Auth-Token": token}, timeout=10)
    if result:
        re = json.loads(result.text)
    return re

def robots(request):
    return HttpResponse("User-agent: *\nAllow: /", mimetype="text/plain")

def session(request):
    fld = request.GET.get("fld", "")
    val = request.GET.get("val", "")
    if fld != 'user' or fld != 'device':
        request.session[fld] = val
        return HttpResponse("1")
    else:
        return HttpResponse("0")

def stat(request, action=""):
    return HttpResponse("1")

def error(request, action=""):
    return HttpResponse("1")

@csrf_exempt
def first(request):
    info = request.get_host()
    return main(request, info)

#메인
def main(request, info=''):
    token = request.session.get("user", {}).get("token", "")
    info = request.session.get("user", {})
    info.update({"status":"true","id":"La78ARnaRc","token":"dc7a6edc-f221-11e3-a335-00259094921c"})
    request.session["user"] = info
    return render(request, "main.html", {})

#회사상세정보
def company_info(request):
    re = {}
    company_id = request.GET.get("company_id", "")
    if company_id > 0:
        re = _load_rest("company/getInfo", {"company_id":str(company_id)})
    return render(request, "company_info.html", {"re":re})
