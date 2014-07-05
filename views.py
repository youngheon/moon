#coding:utf-8
import requests, json, xmlrpclib, re
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

#rpc 불필요한 변수 제거
def _para(request):
    list = ["skin", "v", "token", "xid", "flag"]
    data = {}
    for k in request.REQUEST.keys():
        data[k] = request.REQUEST.get(k)
    skin = data.get("skin", "")
    for k in list:
        if k in data:
            data.pop(k)
    url = request.META["PATH_INFO"]
    url = re.sub("^/rpc/", "", url)
    return url, data, skin

#순위가 필요한 리스트에서 rank 추가
def _add_rank(data, result):
    page = int(data.get("page", 1))
    num = int(data.get("num", 1))
    for idx, re in enumerate(result):
        re['rank'] = (page - 1) * num + idx + 1
    return result

#rpc skin 호출
@csrf_exempt
def rpc(request):
    user_token = request.session.get("user", {}).get("token", "")
    url, data, skin = _para(request)
    result = _load_rest(url, data, user_token)
    result['flag'] = request.GET.get("flag", "")
    if result:
        _add_rank(data, result["result"]["data"])
    if skin:
        return render(request, skin+".html", result)
    else:
        return HttpResponse(json.dumps(result), mimetype="application/json")

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
    return company(request)

#회사상세정보
def company_info(request):
    re = {}
    company_id = request.GET.get("company_id", "")
    if company_id > 0:
        re = _load_rest("company/getInfo", {"company_id":str(company_id)})
    return render(request, "company/company_info.html", {"re":re})

#회사상세정보
def company_profile(request):
    return render(request, "company/profile.html", {"re":re})

#연봉
def company_salary(request):
    return render(request, "company/salary.html", {"re":re})

#회사
def company(request):
    return render(request, "company/main.html", {})
