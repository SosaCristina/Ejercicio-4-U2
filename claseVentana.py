class Ventana:
    __titulo=""
    __xSupIz=0
    __ySupIz=0
    __xInfDe=0
    __yInfDe=0

    def __init__(self,titulo,xid=0,yid=0,xsi=0,ysi=0):
        self.__titulo=titulo
        self.__xSupIz=xsi
        self.__ySupIz=ysi
        self.__xInfDe=xid
        self.__yInfDe=yid

    

    def mostrar(self):
        print("Vertice superior izquierdo({},{}) vertice inferior derecho ({},{})".format(self.__xSupIz,self.__ySupIz,self.__xInfDe,self.__yInfDe))

    
    def getTitulo(self):
        return self.__titulo
    

    def ancho(self):
        if (self.__xSupIz<self.__xInfDe):
            ancho=self.__xInfDe-self.__xSupIz
            return ancho
        
        else:
            print("Error no se puede calcular")


    def alto (self):
        if (self.__yInfDe>self.__ySupIz):
            alto=self.__yInfDe-self.__ySupIz
            return alto
        else:
            print("Error no se puede calcular")

    def moverDerecha(self,num1):
        self.__xSupIz+=num1
        self.__xInfDe+=num1       

    def moverIzquierda (self,num2):
        self.__xSupIz-=num2
        self.__xInfDe-=num2

    def bajar (self, num3=1):
        self.__yInfDe-=num3
        self.__ySupIz-=num3

    def subir (self, num4=1):
        self.__yInfDe+=num4
        self.__ySupIz+=num4       





        
    



