lb_cardname=Element("lb_cardname")
lb_hello=Element("lb_hello")

def loadAll(*args):
    f=open("db.txt",'r')

    name=f.readline()
    
    f.close()

    lb_hello.element.innerText= name+'님 안녕하세요'
    lb_cardname.element.innerText= name
    

# .txt 들어가기 쉬움
# .ini(initialize:초기화하다) txt와 동일 (windows) 설정 초기화 
# .bin(binary:2진수) 잘안열림
