#!/usr/bin/env python
# coding: utf-8

# In[36]:


from __future__ import annotations #для возможности предварительного объявления
from typing import Any, Optional

#Общий интерфейс для обработчиков
#Метод построения цепочки + метод для выполнения запроса
class Handler:
    def setNext(self, handler: Handler) -> Handler:
        pass
    
    def handle(self, request) -> Optional[str]:
        pass
    
#Базовый обработчик
class BaseHandler:
    
    nextHandler: Handler = None
        
    #Метод позволяет связать обработчки в одну цепь
    def setNext(self, handler:Handler) -> Handler:
        self.nextHandler = handler
        return handler
    
    def handle(self, request: Any) -> str:
        if self.nextHandler:
            return self.nextHandler.handle(request)
        return None
    
#Конкретные обработчкики
#Либо обработка запроса, либо передача следующему
class Reynolds(BaseHandler):
    
    #Код обработки запроса. Может обработать или нет.
    #Если да-говорит об этом, нет 0 передает следующему объекту
    def handle(self, request: Any) -> str:
        if request == "Deadpool" or request == "Pickachu":
            return f"\"I'll play it: {request}\" - Reynolds\n"
        else:
            return super().handle(request)
        
class Holland(BaseHandler):
    
    def handle(self, request: Any) -> str:
        if request == "Spyderman":
            return f"\"I'll play it: {request}\" - Holland\n"
        else:
            return super().handle(request)
        
class Hamsford(BaseHandler):
    
    def handle(self, request: Any) -> str:
        if request == "Thor":
            return f"\"I'll play it: {request}\" - Hamsford\n"
        else:
            return super().handle(request)
        
        

def client(handler: Handler) -> None:
    for films in ["Deadpool", "Spyderman" , "Thor", "Pickachu"]:
        print(f"Let's play in {films}:")
        actor = handler.handle(films)
        if actor:
            print(f" {actor}")
        else:
            print(f" Noone'd like to play it\n")
                
    
if __name__ == '__main__':
    rayan = Reynolds()
    tom = Holland()
    kris = Hamsford()
    
    rayan.setNext(tom).setNext(kris)
    client(rayan)
    
    print("Rayan goes away. So...\n")
    client(tom)
    


# In[ ]:




