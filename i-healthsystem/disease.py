# -*- coding: cp1252 -*-
import nltk
diag=dict()
medicine=dict()

dengue = nltk.defaultdict(str)
dengue['headache'] = ['SYM', 100]
dengue['eye-pain'] = ['SYM',50]
dengue['muscle-pain'] = ['SYM',10]
dengue['rash'] = ['SYM',150]
dengue['vomit'] = ['SYM',10]
dengue['nausea'] = ['SYM',5]
dengue['bleed'] = ['SYM', 15]
dengue['fever'] = ['SYM',25]
dengue['pain']=['SYM',10]
diag['dengue']=['blood test']
medicine['dengue']=['Use Acetaminophen',' Avoid medicines with aspirin','Check your doctor regularly']

pneumonia =nltk.defaultdict(str)
pneumonia['cough'] = ['SYM', 50]
pneumonia['shaking'] = ['SYM', 70]
pneumonia['vomit'] = ['SYM',10]
pneumonia['fever']= ['SYM',100]
pneumonia['diarrhea'] = ['SYM',20]
pneumonia['tire'] = ['SYM',10]
diag['pneumonia']=['Physical Exam : During the exam, your doctor listens to your lungs with a stethoscope to check for abnormal bubbling or crackling sounds (rales) and for rumblings (rhonchi) that signal the presence of thick liquid',
                   'Chest X-rays : X-rays can confirm the presence of pneumonia and determine the extent and location of the infection.',
                   'Blood and mucus tests: You may have a blood test to measure your white cell count and look for the presence of viruses, bacteria or other organisms. Your doctor also may examine a sample of your mucus or your blood to help identify the particular microorganism that\'s causing your illness'
                   ]
# these are the medicies which we can give to pneumonia patients
medicine['pneumonia']=['Biaxin','Vibramycin','Levaquin','piperacillin'
                       ]


jaundice=nltk.defaultdict(str)
jaundice['extremeweakness']=['SYM',50]
jaundice['headache']=['SYM',10]
jaundice['fever']=['SYM',100]
jaundice['loss-of-appetite']=['SYM',50]
jaundice['tiredness']=['SYM',20]
jaundice['yellow']=['SYM',100]
jaundice['nausea']=['SYM',30]
jaundice['constipation']=['SYM',10]
jaundice['itching']=['SYM',20]
jaundice['liver-pain']=['SYM',30]
diag['jaundice']=['A physical exam', 'A laboratory test of a sample of your baby\'s blood','A skin test with a device called a transcutaneous bilirubinometer, which measures the reflection of a special light shone through the skin']
medicine['jaundice']=['Livode Syrup','Ayuliv Capsule','Livex Tablets' ]


mumps=nltk.defaultdict(str)
mumps['headache']=['SYM',15]
mumps['loss of appetite']=['SYM',12]
mumps['weak']=['SYM',15]
mumps['drymouth']=['SYM',17]
mumps['soreface']=['SYM',100]
mumps['soremouth']=['SYM',50]
mumps['pain']=['SYM',15]
mumps['swelling']=['SYM',50]
mumps['fever']=['SYM',5]
diag['mumps']=['Blood, urine or cerebrospinal fluid (CSF) tests may be taken to confirm the diagnosis.'
                ]
medicine['mumps']=[' paracetamol'  'ibuprofen' 'LIVOAID'
                   ]
                
cold =nltk.defaultdict(str)
cold['aches'] = ['SYM',15]
cold['vomit'] = ['SYM',50]
cold['cough'] = ['SYM',150]
cold['diarrhea']= ['SYM',20]
cold['chokedthroat']=['SYM',40]
diag['cold']=['Take home remedies','Consult the doctor earliest']                
medicine['cold']=['Echinacea','Chicken soup']

                
braincancer=nltk.defaultdict(str)
braincancer['headache']=['SYM',150]
braincancer['weakness']=['SYM',10]
braincancer['clumsiness']=['SYM',70]
braincancer['diffultywalking']=['SYM',11]
braincancer['seizures']=['SYM',20]
braincancer['abnormalvision']=['SYM',50]
braincancer['nausea']=['SYM',30]
braincancer['vomit']=['SYM',10]
diag['braincancer']=['A neurological exam : A neurological exam may include, among other things, checking your vision, hearing, balance, coordination and reflexes. Difficulty in one or more areas may provide clues about the part of your brain that could be affected by a brain tumor.',
                     'Imaging Tests : Magnetic resonance imaging (MRI) is commonly used to help diagnose brain tumors. In some cases a dye may be injected through a vein in your arm before your MRI. A number of specialized MRI scans — including functional MRI, perfusion MRI and magnetic resonance spectroscopy — may help your doctor evaluate the tumor and plan treatment. Other imaging tests may include computerized tomography (CT) and positron emission tomography (PET).',
                     'Tests to find cancer in other parts of your body. If it\'s suspected that your brain tumor may be a result of cancer that has spread from another area of your body, your doctor may recommend tests and procedures to determine where the cancer originated. One example might be a CT scan of the chest to look for signs of lung cancer.',
                     'Collecting and testing a sample of abnormal tissue (biopsy) : A biopsy can be performed as part of an operation to remove the brain tumor, or a biopsy can be performed using a needle. A stereotactic needle biopsy may be done for brain tumors in hard to reach areas or very sensitive areas within your brain that might be damaged by a more extensive operation. Your neurosurgeon drills a small hole, called a burr hole, into your skull. A thin needle is then inserted through the hole. Tissue is removed using the needle, which is frequently guided by CT or MRI scanning. The biopsy sample is then viewed under a microscope to determine if it is cancerous or benign. This information is helpful in guiding treatment']

medicine['braincancer']=['high']



heart_disease=nltk.defaultdict(str)
heart_disease['shortbreath']=['SYM',25]
heart_disease['nausea']=['SYM',2]
heart_disease['fastheartbeat']=['SYM',100]
heart_disease['sweating']=['SYM',75]
heart_disease['palpitation']=['SYM',100]
heart_disease['pain in chest']=['SYM',120]
heart_disease['anxiety']=['SYM',50]
heart_disease['vomiting']=['SYM',5]
heart_disease['dizziness']=['SYM',15]
heart_disease['heaviness']=['SYM',10]
diag['heart_disease']=['Stress Test : Does your heart respond well to exertion? That\'s what a stress test looks for. Here\'s a straightforward description, including how to prepare for a stress test.']
medicine['heart_disease']=['high']
