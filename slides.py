import random

from browser import document, timer, html

SLIDETEXTS = [

"""\
Brython
Uma apresentação por JS

jsobueno@gmail.com
""",
"""\
javascript

Todos os navegadores WEB rodam javascript - bem otimizado. 
Eu poderia falar muito sobre problemas do javascript - 
mas, vamos ter em mente só que 
"JavaScript (...) was created in 10 days in May 1995 by Brendan Eich, " (w3c.org)
""",
"""\
Python

Foi criado ao longo de meses por Guido van Rossum,
com o intuito de ser uma linguagem de programação didática.
Evoluiu e evolui  em _comunidade_, em discussões
abertas a qualquer participante
""",
"""\
Javascript evolui com padrões oficiais da W3C 

as discussões acontecem em comitês de difícil participação,
e envolvem política em vários níveis.
""",
"""\
Críticas

Sempre que levanto a bola de se usar compilação de Python
para javascript, chovem críticas.
A mais imediata é que "não dá para depurar" - 
dá!  Poderia rebater as críticas uma a uma,
mas o fato é que qualquer argumento contra algo como 
compilar Python para javascript  pode ser aplicado
para o Coffescript, que apesar de tudo, é
bastante popular

""",
"""\
Por que não CoffeScript?

"Having had to reverse-engineer a fairly complex piece of Coffeescript
recently, I definitely thing they went too far. It seems there 
is no formal grammar for Coffeescript, just a translator, and even
if there were a formal grammar, it would have many
odd corners and sharp edges." (G. Van Rossum, 20/01/2015)
""",
"""\
Suporte nativo a Python no Browser

Not happening.
Sem mais.

""",
"""\
Parênteses:

No Windows desde o windows 98, é possivel
usar PythonScript com o "Windows Script Host",
para scripts dentro do Internet Explorer.
Nunca vi ninguém usar isso.
""",
"""\
História

Python applets?
Não. Houve um browser escrito em Python, chamado Grail que tinha isso.
Ahá - você pode criar applets Python, com focos em jogos3D usando 
o plug-in da Blender Game Engine:  se chama "Burster" e está ativo em 
http://geta3d.com/  (surpresa ao preparar os slides)

""",
"""\
Mais applets?

Parece que Jython funciona bem, se você tem applets
java configurados.

E IronPython se você gosta de Silverlight

""",
"""\
CPython dentro do Browser?

Há o Emscriptem - compila o CPython, como ele é, e roda no browser
Só não é possível interagir com nenhum elemento da página
ou criar gráficos.

""", 
"""\
Traduzir Python offline?

Possível - o projeto Pyjamas tem essa abordagem - 
hoje ele continua sendo atualizado como "pyjs" -
mas o foco hoje parece ser aplicações para desktop,
usando um conjunto bastante acoplado de widgets.
""",
"""\
Skulpt

Python com tradução no Browser para javascript
desenvolvimento ativo
Exemplos parecem complicados
Não sei o estado do projeto
""",
"""\
Brython 

Tradução online,
instalação e uso simples
desenvolvimento "as you go", 
com um conjunto surpreendente de Python3
e (um pouco menor) da biblioteca padrão

""", 
"""\
E o que maria leva?
""",
"""\
O quê?

namespaces
import
no braces


""",
"""\
E quê mais?

classes: OOP como Deus quis!
Sobrecarga de operadores com métodos "__magic__"
Properties!

""",
"""\
Mas não desligue ainda

Formatação de strings
list comprehensions (e parentes)
""",
"""\
e mais...

Uma biblioteca padrão! 
Com funcionalidades que em Javascript você teria que 
importar de diversos projetos de software separados
""",

"""\
Mão na massa
"""

]

def rand_color(min_=0, max_=16):
    return "#%02x%02x%02x" % tuple(random.randrange(min_, max_) for _ in range(3))

class SlideShow:
    def __init__(self):
        self.slide_number = 0
        document.body.onclick = self.next
        self.show_slide()

    def show_slide(self):
        lines = SLIDETEXTS[self.slide_number].split("\n")
        document.body.html = "<h1>{}</h1>".format(lines[0])
        for line in lines[1:]:
            color = rand_color(3, 13)
            para = html.P(line, style={"color": color  })
            document.body.append(para)
        self.squares()
    
    def squares(self):
        rect = document.body.getBoundingClientRect()
        randrange = random.randrange
        for i in range(randrange(5, 15)):
            side = randrange(50, 251, 50)
            canvas = html.CANVAS(width=side, height=side, style={
                "opacity":random.normalvariate(0.15, 0.1),
                "position": "absolute",
                "top": random.randrange(rect.height - side),
                "left": random.randrange(rect.width - side),
                "background": rand_color(10, 16),
                "z-index": 0
             })
            document.body.append(canvas)

    def next(self, event):
        if event.which == 1:
            self.slide_number += 1
        elif event.which == 2:
            self.slide_number -= 1
        if self.slide_number >= len(SLIDETEXTS):
            self.slide_number = 0
        elif self.slide_number < 0:
            self.slide_number = len(SLIDETEXTS) - 1
        self.show_slide()

