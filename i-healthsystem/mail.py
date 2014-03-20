import logging
import webapp2
import urllib
import urllib2
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.api import mail
import summarize

def call(msg,num):
    url = 'http://www.bits-isa.org/call/index.php'
    values = {'message' : msg,'to':num}

    data = urllib.urlencode(values)
    #print data
    fullurl = url + '?' + data
    #print fullurl
    response = urllib2.urlopen(fullurl)
    #print response
    page = response.read()
    #print page

class LogSenderHandler(InboundMailHandler):
    def receive(self, mail_message):
        logging.info("Received a message from: " + mail_message.sender)
        plaintext_bodies = mail_message.bodies('text/plain')
        
        reply=''
        temp=''
        
        
        for content_type,body in  plaintext_bodies:
            temp= body.decode().split()
            pos = temp.index('7568805699')
            reply =reply + ' '.join(temp[pos+1:])
            num = temp[pos-6][1:-1]
        message = mail.EmailMessage(sender="E-Health App <e-healthresponse@i-healthsystem.appspotmail.com>",subject="Reply")
        message.to = 'Application Archive <i.healthsystem@gmail.com>'
        
        logging.info("replying message with : " + reply)
        #call(reply,num)
        #print plaintext_bodies
        #logging.info("Sending message to : " +message.to)
        #logging.info("With data : " +reply)
        
        idn, sym, dis  = summarize.seq1(reply)
        if(idn==1):
                result = "Please Input Some Relevant Query"
        elif( idn==2):
                result = "Very weak symptoms. No Medicines required currently, however we suggest to consult a doctor before if symptoms aggravate"                
        elif(idn==3):
                result ="No decision could be taken for this set of symptoms. We have recorded this query and will furthur look into it.Please consult a doctor ."      
        elif(idn==4):
                result ="Your symptoms strongly match the following: "+(', '.join(dis))+"Please consult a doctor ."                
        elif(idn==5):
                result ="Your symptoms strongly match "+str(dis[0])+".We suggest based on your medical history, the medicine :"+(', '.join(dis[1]))+"."
        
        sms=""
        message.body = num + ' ' +result
        
        for x in result.split(' '):
            if( (len(sms) + len(x))>=160):
                call(sms,num)
                sms=""
            sms=sms+str(x)+" "
        
        if(len(sms)>0):
            call(sms,num)
        message.send()

        
        
        
        
app = webapp2.WSGIApplication([LogSenderHandler.mapping()], debug=True)