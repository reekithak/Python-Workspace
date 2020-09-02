import re
def clean_text(
string:str ,
punctuations=r'''!()-[]{};:'"\,<>./?@#$%^&*_~''',
stop_words = ['the','a','and','be','is','be','will']) -> str:
    #URLS
    string = re.sub(r'https?://\S+|www\.\S+', '', string)
    
    #HTML
    string = re.sub(r'<.*?>', '', string)
    
    #Punctuations
    for x in string.lower():
        if x in punctuations:
            string = string.replace(x,"")
    
    #TO lower convertion
    string = string.lower()
    
    #Removing stop words
    string = ' '.join([word for word in string.split() if word not in stop_words])
    
    #whitespaces
    string = re.sub(r'\s+', ' ', string).strip()
    
    return string