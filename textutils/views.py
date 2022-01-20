
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index.html')

def getstatus(request):
    gstninput=request.GET.get('text','default')

    charlist = [char for char in gstninput.upper()]

    a = 1
    cumhash = []

    if not type(gstninput) is str:
        raise TypeError("Only strings are allowed")

    try:
        if len(gstninput) < 15:
            raise Exception("Please ensure that the input is 15 digit long")
    except:
        pass

    for i in charlist[0:14:1]:

        if a % 2 == 0:
            multiplier = 2
        else:
            multiplier = 1

        if i.isdigit():
            intvalue = int(i)
            prod = intvalue * multiplier
            quotient = prod // 36
            remain = prod % 36
            hash = quotient + remain

        else:
            intvalue = ord(i) - 55
            prod = intvalue * multiplier
            quotient = prod // 36
            remain = prod % 36
            hash = quotient + remain

        a = a + 1

        cumhash.append(hash)

    hashsum = (sum(cumhash))

    remain = hashsum % 36

    checksum = 36 - remain

    if checksum < 10:
        finalchk = int(checksum)
    else:
        finalchk = chr(checksum + 55)

    lastchr = (gstninput[len(gstninput) - 1])

    if lastchr.isdigit():
        lastchr = int(lastchr)
    else:
        lastchr = str(lastchr)

    if finalchk == lastchr:
        result = "Check Sum MATCH"
    else:
        result = "Check Sum MISMATCH"


    owndic = {'gst': gstninput, 'final_status': result}
    return render(request,'getstatus.html',owndic)


