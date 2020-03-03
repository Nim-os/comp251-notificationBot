from last import lastMsg

stop = "<font class=\"bold\"><BR>"
nxt = False
msg = ""

raw = open("trim.txt", "r")

# Checks for the breaking point within the html
for line in raw:
    if stop in line:
        nxt = True
    if nxt
        msg = line
        break

# Removes initial 3 characters (<P>)
msg = msg[3:]

if (msg == lastMsg):
    print "No new messages"
else:
    print "New message from luc.devroye.org/251.html: " + msg
    last = open("last.py","r+")
    last.seek(0)
    last.write("lastMsg = " + msg)