import disease
from disease import *

def check_neg(word):
     if (word.startswith('no') or word.startswith('not') or word.startswith('nil') or word.startswith('zero') or word.startswith('nothing') or word.startswith('loss') or word.startswith('none') or word.startswith('never')):
          return True
     else:
          return False
          
          
def check_p(word):
     #print word
     if (word.startswith('pain') or word.startswith('trouble') or word.startswith('problem') or word.startswith('ache') or word.startswith('agon') or word.startswith('bad') or word.startswith('excruciat') or word.startswith('groan') or word.startswith('hurt') or word.startswith('irrit') or word.startswith('sting') or word.startswith('stab') or word.startswith('sore') or word.startswith('suffer') or word.startswith('throb') or word.startswith('twing') or word.startswith('injur') or word.startswith('sharp')):
          return word
     else:
          return ''
          
          

def check_sym(word):
     if( word.startswith('sleep')  or word.startswith('fever')or word.startswith('constipation') or word.startswith('rash') or word.startswith('headache')  or
         word.startswith('vomit')  or  word.startswith('nause')  or  word.startswith('ill') or word.startswith('bleed') or word.startswith('yell') or
         word.startswith('soar') or word.startswith('pain') or word.startswith('cough') or word.startswith('shaking') or word.startswith('tire') or word.startswith('anxiety') or
         word.startswith('dizziness') or word.startswith('anxiety') or word.startswith('sweating') or word.startswith('anxiety') or word.startswith('extremeweak') or
         word.startswith('seizure') or word.startswith('weakness') or  word.startswith('abnormalvision') or word.startswith('eye-pain') or word.startswith('liver-pain')  
         or word.startswith('yellow') or word.startswith('itch') or word.startswith('clums') or word.startswith('diarrhea') or word.startswith('palpitation') or word.startswith('abnorminalvision')
         or word.startswith('heaviness') or word.startswith('soreface') or word.startswith('soremouth') or word.startswith('chockedthroat') or
         word.startswith('chewing-pain') or word.startswith('abnormalvision') or word.startswith('fastheartbeat') ):
          return True
     else:
          return False
          

def check_body(word):
     if( word.startswith('arm') or word.startswith('eye') or word.startswith('eyebrow') or word.startswith('belly') or word.startswith('leg') or
         word.startswith('breast') or word.startswith('thumb') or word.startswith('elbow') or word.startswith('fist') or word.startswith('finger') or word.startswith('foot')
         or word.startswith('ankle') or word.startswith('muscle') or word.startswith('buttocks') or
         word.startswith('skin') or word.startswith('hair') or word.startswith('neck') or word.startswith('hand') or word.startswith('arm') or word.startswith('wrist') or word.startswith('hip') or word.startswith('chin')
         or word.startswith('knee') or word.startswith('head') or word.startswith('lip') or word.startswith('mouth') or word.startswith('nose') or word.startswith('nostril') or word.startswith('upper arm') or word.startswith('thigh')
         or word.startswith('ear') or word.startswith('bottom') or word.startswith(' bum') or word.startswith('back') or word.startswith('underarm') or word.startswith(' forearm')
         or word.startswith('lower leg') or word.startswith('shoulder') or word.startswith('forehead') or word.startswith('waist') or word.startswith('calf ') or
         word.startswith('cheek') or word.startswith('eyelash') or word.startswith('chest') or word.startswith('tooth') or word.startswith('teeth') or word.startswith('chew') or
         word.startswith('toe') or word.startswith('tongue')or word.startswith('abdominal') ):
          return word
     else:
          return ''



#####################################################################################################################################################		
def dis_check_1(a = []):
	count=0
	j=0
	value=0
	for i in a:
		
		if('SYM' in  dengue[a[j]]):
			value=value+ dengue[a[j]][1]
			count = count+1
		j = j+1
	return (count,value)
	
def dis_check_2(a = []):
	count=0
	j=0
	value=0
	for i in a:
		if('SYM' in pneumonia[a[j]]):
			value=value+  pneumonia[a[j]][1]
			count = count+1
		j = j+1
	return (count,value)
	
def dis_check_3(a = []):
	count=0
	j=0
	value=0
	for i in a:
		if( 'SYM' in cold[a[j]]):
			value = value+ cold[a[j]][1]
			count = count+1
		j = j+1
	return (count,value)
	
		
def dis_check_4(a = []):
	count=0
	j=0
	value=0
	for i in a:
		if('SYM' in braincancer[a[j]]):
			value = value+  braincancer[a[j]][1]
			count = count+1
		j = j+1
	return (count,value)
	
def dis_check_5(a = []):
	count=0
	j=0
	value=0
	for i in a:
		if('SYM' in heart_disease[a[j]]):
			value = value+  heart_disease[a[j]][1]
			count = count+1
		j = j+1
	return (count,value)

def dis_check_6(a = []):
	count=0
	j=0
	value=0
	for i in a:
		if('SYM' in jaundice[a[j]]):
			value = value+  jaundice[a[j]][1]
			count = count+1
		j = j+1
	return (count,value)



def dis_check_7(a = []):
	count=0
	j=0
	value=0
	for i in a:
		if('SYM' in mumps[a[j]]):
			value = value+  mumps[a[j]][1]
			count = count+1
		j = j+1
	return (count,value)
