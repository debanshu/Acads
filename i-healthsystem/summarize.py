import nltk, re, check, disease
from disease import *
from check import *




def sentenizer(str): #getting sentences
    sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    sents = sent_tokenizer.tokenize(str)
    return sents




def stem(word):
     regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment|ous)?$'
     stem, suffix = re.findall(regexp, word)[0]
     return stem

def stem2(word):
     regexp = r'^(.*?)(s|ous)?$'
     stem, suffix = re.findall(regexp, word)[0]
     return stem



def seq1(finale):
    identifier=1
    weight=dict()
    count = 0 
    prob = []
    symc = []
    cp=0
    cond = finale     #input 
    ind_sen = sentenizer(cond)
    for num in ind_sen:
        cp = cp+1
        sym = ''
        pain = ''
        b_part = ''
        neg = ''
        count=0
        ind_wod = nltk.word_tokenize(num)
        for t in ind_wod:
            t = t.lower()
            if(check_neg(t)== True):
                neg = 'no'
            t1 = stem(t)
            t2 = stem2(t)
            if(check_sym(t1)== True):
                if(sym is not ''):
                    sym = sym + ' and ' + t
                    symc.append(t1)
                else:
                    sym = t
                    symc.append(t1)
            elif(check_p(t1) is not ''):
                    pain = t
            elif(check_body(t2) is not ''):
                    b_part = t

        
        if(sym is not ''):
            if(pain is not ''):
                prob.append(neg + ' ' + pain + ' in ' + sym)
            elif(b_part is not ''):
                prob.append(neg + ' ' + sym + ' in ' + b_part)
            else:
                prob.append(neg + ' ' + sym)
        elif(b_part is not ''):
            if(pain is not ''):
                prob.append(neg + ' ' + pain + ' in ' + b_part)
            else:
                prob.append(neg + ' ' + b_part)
        elif(pain is not ''):
            prob.append(neg + ' ' + pain)
    
    data = dict()
    #This dictionary will count the symptoms of each disease

    #print 'Symptoms Matching to that of Dengue\n'
    d1=dis_check_1(symc)
    data['dengue']=d1[0]
    weight['dengue']=d1[1]
    #print dis_check_1(symc)

    #print 'Symptoms Matching to that of Pnenomenia\n'
    d1=dis_check_2(symc)
    data['pneumonia']=d1[0]
    weight['pneumonia']=d1[1]
    #print dis_check_2(symc)

    #print 'Symptoms Matching to that of common cold are\n'
    d1=dis_check_3(symc)
    data['cold']=d1[0]
    weight['cold']=d1[1]
    #print dis_check_3(symc)

    #print 'Symptoms Matching to that of heart disease are\n'
    d1=dis_check_4(symc)
    data['braincancer']=d1[0]
    weight['braincancer']=d1[1]
    #print dis_check_4(symc)

    #print 'Symptoms Matching to that of Brain Cancer are\n'
    d1=dis_check_5(symc)
    data['heart_disease']=d1[0]
    weight['heart_disease']=d1[1]
    #print dis_check_5(symc)

    #print 'Symptoms Matching to that of Jaundice are\n'
    d1=dis_check_6(symc)
    data['jaundice']=d1[0]
    weight['jaundice']=d1[1]
    #print dis_check_6(symc)

    #print 'Symptoms Matching to that of Mumps are\n'
    d1=dis_check_7(symc)
    data['mumps']=d1[0]
    weight['mumps']=d1[1]
    #print dis_check_7(symc)

    ##############################################################################

    #printing the values, in case debugging is require

    for key, value in data.items():
        print '%s %s'%(key, value)
    #############################

    for key, value in weight.items():
        print '%s %s'%(key, value)  

    ############################################################
    #calculation of approximate disease

    no_disease=0
    for key, value in data.items():
        #global no_disease
        if(value>0):
             no_disease=1
             break      
                
    if(no_disease==0):
        identifier=1
        #In case of no disease, print the appropriate output
        no_sym='Please input some symptoms'
        no_med='N/A'
        return (identifier,no_sym,no_med)
            #os._exit(1)
    #######################################################################

     #If all the symptoms are of very mild value, then no particular treatment require
    no_treatment=0
    for key, value in weight.items():
        #global no_treatment
        if(value>20):
            no_treatment=1
            break

    if(no_treatment==0):
        identifier =2
        no_medi='no medicines required'
        return (identifier,prob,no_medi)
        #os.exit(1)
       
    ########################################################################################    

    not_identified=0
    for key, value in weight.items():
        #global not_identified
        if(not(value>20 and value<=50)):
            not_identified=1
            break

    if(not_identified==0):
        identifier =3
        return (identifier,symc,'No decision could be taken for this set of symptoms')


    disease_name=''     #This variable will contains the disease name, which we can find with maximum probability
    disease_list=[]      #In case we can't determine the disease, we have to predict the list of possible disease..
    for key, value in weight.items():
        
        disease_name
        if(value>=200):
            disease_name=key
            break

    #In case disease_name is null

    if(disease_name==''):
        for key, value in weight.items():
            if(value>50):
                disease_list.append(key)


    if(disease_name):
        identifier=5
       
        return (identifier,symc, [disease_name,medicine[disease_name]])
    else:
        identifier=4
        return (identifier,symc,disease_list)
       # print 'You are require to take take the following diagnosis'
        '''for i in disease_list:
            final_diag[i]=diag[i]
        #print final_diag '''
        ''' ans=''
        i=1
        for key,value in final_diag.items():
            ans=ans+ str(i)
            ans=ans+' Disease: '
            ans=ans+str(key)
            ans=ans+' <br> Diagnosis, are as follows: <br> '
            #ans+='::'
            ans=ans+str(value)
            ans+='<br>'
            i=i+1
        return ans '''

##################################################################
def doctor_symptoms(inp):
    symc = []
    cp=0
    prob=[]
    count=0
    symptom = inp     #input 
    ind_sen = sentenizer(symptom)
    for num in ind_sen:
        cp = cp+1
        sym = ''
        pain = ''
        b_part = ''
        neg = ''
        count=0
        ind_wod = nltk.word_tokenize(num)
        for t in ind_wod:
            t = t.lower()
            if(check_neg(t)== True):
                neg = 'no'
            t1 = stem(t)
            t2 = stem2(t)
            if(check_sym(t1)== True):
                if(sym is not ''):
                    sym = sym + ' and ' + t
                    symc.append(t1)
                else:
                    sym = t
                    symc.append(t1)
            elif(check_p(t1) is not ''):
                    pain = t
            elif(check_body(t2) is not ''):
                    b_part = t

        
        if(sym is not ''):
            if(pain is not ''):
                prob.append(neg + ' ' + pain + ' in ' + sym)
            elif(b_part is not ''):
                prob.append(neg + ' ' + sym + ' in ' + b_part)
            else:
                prob.append(neg + ' ' + sym)
        elif(b_part is not ''):
            if(pain is not ''):
                prob.append(neg + ' ' + pain + ' in ' + b_part)
            else:
                prob.append(neg + ' ' + b_part)
        elif(pain is not ''):
            prob.append(neg + ' ' + pain)

    return symc
