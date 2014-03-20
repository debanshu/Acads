
import jinja2
import os
import cgi
import datetime
import urllib
import webapp2
import summarize
import time
import logging

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.api.datastore import Key

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class patient(db.Model):
    name = db.StringProperty()
    email = db.EmailProperty()
    number = db.StringProperty()
    reg_date = db.DateProperty()
	
class doctor(db.Model):
    name = db.StringProperty()
    email = db.EmailProperty()
    number = db.StringProperty()
    reg_date = db.DateProperty()
	
class record(db.Model):
    symptoms = db.StringListProperty()
    disease = db.StringListProperty()
    medicine = db.StringProperty()
    rec_date = db.DateProperty()
    doc = db.StringProperty()
    

class MainPage(webapp2.RequestHandler):
    def get(self):
        	
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render())
		
		
class Processor(webapp2.RequestHandler):
    def post(self):
        query = self.request.get('query')
        id= self.request.get('id')
        		
        idn, sym, dis  = summarize.seq1(query)
        q= patient.all(keys_only=True)
        q.filter("__key__ >=", Key.from_path('patient', id))
        res = q.get()
        #logging.info("res : " + res)
        if res:
        
            if(idn==1):
                result = "Please Input Some Relevant Query"
            elif( idn==2):
                result = "Very weak symptoms. No Medicines required currently, however we suggest to consult a doctor before if symptoms aggravate"
                rec = record(parent=res, symptoms = sym, medicine = 'not_any', doc = 'ehealth')
                rec.rec_date =datetime.datetime.now().date()
                rec.put()
            elif(idn==3):
                result ="No decision could be taken for this set of symptoms. We have recorded this query and will furthur look into it. <br> <b> Please consult a doctor . </b>"
                rec = record(parent=res, symptoms = sym, medicine = 'not_checked', doc = 'ehealth')
                rec.rec_date =datetime.datetime.now().date()
                rec.put()
            elif(idn==4):
                result ="Your symptoms strongly match the following: "+(','.join(dis))+"<br><b>Please consult a doctor .</b>"
                rec = record(parent=res, symptoms = sym, disease =dis, doc = 'ehealth')
                rec.rec_date =datetime.datetime.now().date()
                rec.put()
            elif(idn==5):
                result ="Your symptoms strongly match "+str(dis[0])+".<br> We suggest based on your medical history, the medicine :"+(','.join(dis[1]))+"."
                rec = record(parent=res, symptoms = sym, disease =[dis[0]],medicine= (','.join(dis[1])), doc = 'ehealth')
                rec.rec_date =datetime.datetime.now().date()
                rec.put()
        else:
            result = "Invalid ID"
        
        template_values = {
        'result': result,
        'name':self.request.get('name')
        }
        template = jinja_environment.get_template('process.html')
        self.response.out.write(template.render(template_values))

        
class Updator(webapp2.RequestHandler):
    def post(self):
        query = self.request.get('symptoms')
        id= self.request.get('id')
        did= self.request.get('did')
        dis = self.request.get('disease').split(' ')
        med = self.request.get('medicine')
        		
        sym  = summarize.doctor_symptoms(query)
        q= patient.all(keys_only=True)
        q.filter("__key__ >=", Key.from_path('patient', id))
        res = q.get()
        
        if res:
            d= doctor.all(keys_only=True)
            d.filter("__key__ >=", Key.from_path('doctor', did))
            resd = d.get()
            if resd:
                result ="Updated successfully"
                rec = record(parent=res, symptoms = sym, disease =dis,medicine=med, doc = did)
                rec.rec_date =datetime.datetime.now().date()
                rec.put() 
            else:
                result ="Invalid DocID"
        else:
            result ="Invalid PatientID"
        
        
        
        template_values = {
        'result': result
        
        }
        template = jinja_environment.get_template('message.html')
        self.response.out.write(template.render(template_values))
        
class Records(webapp2.RequestHandler):
    def post(self):
        
        id= self.request.get('id')
        
        q= patient.all()
        q.filter("__key__ >=", Key.from_path('patient', id))
        res = q.get()
        result=""
        
        if res:
            result = result + "Name: "+res.name+"<br> ID: "+id+"<br>"
            recs = record.all().ancestor(res).fetch(100)
            for r in recs:
                result = result + "<br><br>Date: "+str(r.rec_date)+"<br> DoctorID: "+r.doc+"<br>"
                if r.symptoms:
                    result =result + "Symptoms Recorded: "+ (','.join(r.symptoms)) + "<br>"
                if r.disease:
                    result =result + "Disease Recorded: "+ (','.join(r.disease)) + "<br>"
                if r.medicine:
                    result =result + "Medicine Recorded: "+ r.medicine +"<br>"
        else:
            result ="Invalid PatientID"
        
        
        
        template_values = {
        'result': result
        
        }
        template = jinja_environment.get_template('message.html')
        self.response.out.write(template.render(template_values))


        
class Registration(webapp2.RequestHandler):
    def post(self):
		n = self.request.get('name')
		i = self.request.get('id')
		e = self.request.get('email')
		ph = self.request.get('phone')
		t = self.request.get('type')
		if( t == '1'):
			p = patient(key_name=i, name=n, email=e, number=ph)
			p.reg_date =datetime.datetime.now().date()
			p.put()
		elif( t == '2'):
			p = doctor(key_name=i, name=n, email=e, number=ph)
			p.reg_date =datetime.datetime.now().date()
			p.put() 

                result = "Registered Successfully"      
                template_values = {
                'result': result        
                }
                template = jinja_environment.get_template('message.html')
                self.response.out.write(template.render(template_values))
        
		
		

		
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/process', Processor),
							   ('/reg', Registration),
                               ('/update', Updator),
                               ('/records', Records)],
                              debug=True)