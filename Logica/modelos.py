import pickle, re , nltk, warnings
from sklearn import *
from nltk.corpus import stopwords

def procesaTextoGeneral(asunto):
    puntuación = r'[,;.:¡!¿?@#$%&[\](){}<>~=+\-*/|\\_^`"\']' 
    stop = stopwords.words('spanish')
    lista = ['?', '.', ',', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0','(', ')','-']
    for i in lista:
        stop.append(i)

    

    asun = re.sub(puntuación, '', asunto)
    asun = re.sub('á', 'a', asun)
    asun = re.sub('é', 'e', asun)
    asun = re.sub('í', 'i', asun)
    asun = re.sub('ó', 'o', asun)
    asun = re.sub('ú', 'u', asun)
    asun = re.sub('ñ', 'n', asun)
    
    salida = ''
    asun = asun.lower()
    palabras = asun.split()

    for palabra in palabras:
        if palabra not in stop:
            salida +=' '+palabra
    
    return salida

def vectorizadorEntidad(texto):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        model = pickle.load(open('Modelos/vectorized_entidad.pkl','rb'))
    
    vector = [procesaTextoGeneral(texto)]
    return model.transform(vector)

def procesoEntidad(texto):
    entrada = vectorizadorEntidad(texto).toarray()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        model = pickle.load(open('Modelos/model_entidad.pkl','rb'))
    return model.predict(entrada)[0]

def vectorizadorDerecho(texto):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        model = pickle.load(open('Modelos/vectorizer_derecho.pkl','rb'))
        
    vector = [procesaTextoGeneral(texto)]

    return model.transform(vector)

def procesoDerecho(texto):
    entrada = vectorizadorDerecho(texto)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        model = pickle.load(open('Modelos/model_derecho.pkl','rb'))
    return model.predict(entrada)[0]

def vectorizadorSoli(texto):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        model = pickle.load(open('Modelos/vector_soli.pkl','rb'))
        
    vector = [procesaTextoGeneral(texto)]

    return model.transform(vector)

def procesoSoli(texto):
    entrada = vectorizadorDerecho(texto)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        model = pickle.load(open('Modelos/model_soli.pkl','rb'))
    return model.predict(entrada)[0]
"""
def vectorizadorSoliEsp(texto):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        model = pickle.load(open('Modelos/vectorizer_soles.pkl','rb'))
        
    vector = [procesaTextoGeneral(texto)]

    return model.transform(vector)

def procesoSoliEsp(texto):
    entrada = vectorizadorDerecho(texto)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        model = pickle.load(open('Modelos/model_solici_especi.pkl','rb'))
    return model.predict(entrada)[0]

"""


"""
def modelo_entidad(asunto):
    entrada = procesaTexto(asunto)

    modelo = pickle.load(open('Modelos/model_entidad.pkl', 'rb'))

    return modelo.predict(entrada)
"""


print("derecho", procesoDerecho("REFERENCIA.  ACCION DE TUTELA RADICACION: 73001-40-09-012-2021-00222-00.  NOTIFICACION FALLO DE TUTELA ACCIONANTE: REINERIO GONZALEZ FERREIRA ACCIONADO: E.P.S-S MEDIMAS Y OTROS."))
print("entidad", procesoEntidad("REFERENCIA.  ACCION DE TUTELA RADICACION: 73001-40-09-012-2021-00222-00.  NOTIFICACION FALLO DE TUTELA ACCIONANTE: REINERIO GONZALEZ FERREIRA ACCIONADO: E.P.S-S MEDIMAS Y OTROS."))
print("soli normalita", procesoSoli("REFERENCIA.  ACCION DE TUTELA RADICACION: 73001-40-09-012-2021-00222-00.  NOTIFICACION FALLO DE TUTELA ACCIONANTE: REINERIO GONZALEZ FERREIRA ACCIONADO: E.P.S-S MEDIMAS Y OTROS."))