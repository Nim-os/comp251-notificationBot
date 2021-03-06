try: # Tries to import lastMsg. If it fails, it creates last.py and fills it.
    from last import lastMsg
except ImportError:
    print("Creating last.py...\nMessage below is the most recent message")
    open("last.py","w").write("lastMsg = \"\"")
    from last import lastMsg
import time

if(time.localtime().tm_hour > 0 | time.localtime().tm_hour < 8):
    exit(0)

stop = "New / Messages&nbsp;&nbsp;</font><BR></TD>" # Old break: "<font class=\"bold\"><BR>"
nxt = 0
msg = ""

raw = open("251.html", "r")

# Checks for the breaking point within the html
for line in raw:
    if stop in line:
        nxt += 1
        continue
    if nxt != 0:
        nxt += 1
    if nxt == 4:
        msg = line
        break

# Removes <P> new line character
msg = msg[3:-1]

if (msg == lastMsg):
    print("No new messages")
else:
    print("\nNew message from luc.devroye.org/251.html\n" + msg + "\n")
    last = open("last.py","w")
    last.seek(0)
    last.write("lastMsg = \"" + msg + "\"")
