from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    return render(request, "projects/index.html")


def kinks(request: HttpRequest):
    return render(request, "projects/kinks.html")


def terminology(request: HttpRequest):
    return render(request, "projects/terms.html", context={"terms": [
        ('Abort, Terminate', 'Cancel, Stop, End, Finalise', ''),
        ('Normal', '', ''),
        ('Blacklist', 'Denylist, Blocklist', ''),
        ('Whitelist', 'Allowlist, Approvedlist', ''),
        ('Blackhat', 'Hostile actor, Hostile force', ''),
        ('Whitehat', 'Friendly actor, Security tester, ethical hacker', ''),
        ('Greyhat', '', ''),
        ('Black box', 'Opaque box, Zero-knowledge', ''),
        ('White box', 'Clear box, Open box', ''),
        ('Blind', 'Anonymous, Zero-knowledge', ''),
        ('Double blind', 'Double anonymous', ''),
        ('Dark', 'Deceptive, Manipulative', ''),
        ('Motherboard', 'Primary board, Main board', ''),
        ('Daughter board', 'Secondary board, Auxiliary board', ''),
        ('Female connector', 'Socket, Concave connector', ''),
        ('Male connector', 'Plug, Convex connector', ''),
        ('Master', 'Main, Primary, Leader, Host', ''),
        ('Slave', 'Replica, Secondary, Follower, Client', ''),
        ('Orphan', 'Unreferenced, Unlinked, De-referenced', ''),
        ('Sanity check', 'Confidence check, Unit test, Quick check', ''),
        ('Back door', '', ''),
        ('Red team', 'Outside testers, Attacking team, Attack simulators', ''),
        ('Blue team', 'Defensive team', ''),
        ('Purple team', '', ''),
        ('Demilitarised Zone', 'Public service network, Insecure segment', ''),
        ('Hacker (negative)', 'Threat actor, Attacker', ''),
        ('Man-in-the-middle', 'Interception, Interceptor, Person-in-the-middle', ''),
        ('Salt', '', ''),
        ('Trojan horse', '', ''),
        ('Zero day', '', ''),
    ]})

