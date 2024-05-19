import time, os

fanfic = {
  "1": """Era uma manhã ensolarada na Universidade de Projetos Avançados. Ed, o respeitado professor de desenvolvimento de projetos, caminhava pelos corredores com sua careca brilhando sob a luz fluorescente. Conhecido por sua competência e rigor, ninguém imaginava seu segredo: nas noites de lua cheia, Ed se transformava em um lobisomem poderoso, o macho alfa de sua alcateia.""",
  "2": """Certo dia, durante uma de suas aulas mais desafiadoras, Ed estava explicando um conceito complexo sobre gestão de projetos quando um de seus alunos, um rapaz introvertido e muito inteligente, mas um tanto desajeitado, aproximou-se para tirar uma dúvida.""",
  "3": """"Professor Ed, precisa de ajuda?" perguntou o aluno, ainda tímido.""",
  "4": """"Ah, sim, professor. Eu queria entender melhor essa parte do cronograma..." começou a falar, mas, em um movimento desastrado, sua mão bateu acidentalmente na careca de Ed, produzindo um som oco e ressoante.""",  
  "5": """A sala ficou em silêncio. Todos os alunos ficaram boquiabertos, esperando a reação de Ed. O aluno ficou vermelho como um tomate, sem saber onde enfiar a cara.""",  
  "6": """Para a surpresa de todos, Ed riu. Uma risada alta e contagiante que fez todos na sala relaxarem. "Está tudo bem. Acontece." Ele deu uma piscadela para o aluno ainda atordoado. "Mas tente ser mais cuidadoso na próxima vez, certo?""", 
  "7": """O incidente poderia ter sido esquecido, mas o aluno, mesmo sem querer, começou a sentir algo diferente. Havia algo em Ed que o intrigava, algo além de sua aparência severa e suas habilidades excepcionais como professor.""", 
  "8": """Com o passar do tempo, os dois passaram a interagir mais frequentemente. O aluno admirava a dedicação de Ed e seu conhecimento profundo, enquanto Ed notava a inteligência e a perspectiva única do aluno. Em algumas noites, Ed, em sua forma de lobisomem, observava de longe o campus, especialmente o aluno, sentindo uma ligação inexplicável.""", 
  "9": """Uma noite, sob a luz da lua cheia, o aluno estava trabalhando tarde na biblioteca. Ele sentiu um arrepio e olhou pela janela, vendo uma figura imponente entre as árvores. Era um lobisomem, mas havia algo familiar nele.""",  
  "10": """O aluno não sentiu medo, mas uma curiosidade crescente. Ele saiu da biblioteca e se aproximou cautelosamente. "Professor Ed?" ele sussurrou, incrédulo.""",  
  "11": """O lobisomem olhou para o aluno com olhos brilhantes e, para surpresa do aluno, assentiu. Lentamente, ele voltou à sua forma humana, com a luz da lua ainda iluminando seu rosto sério.""", 
  "12": """"Sim, sou eu." Ed disse, sua voz mais suave do que nunca. "Tenho um segredo que não compartilho com ninguém.""",
  "13": """O aluno sorriu, sentindo uma conexão profunda com Ed. "Eu sempre soube que havia algo especial em você, professor. E, de alguma forma, isso faz sentido.""",  
  "14": """A partir daquela noite, a relação entre Ed e o aluno se aprofundou. Eles não apenas compartilhavam segredos e conhecimento, mas também um vínculo que transcendia a compreensão comum. O aluno, com seu espírito sigma independente, e Ed, com sua natureza alfa protetora, encontraram um equilíbrio perfeito.""", 
  "15": """E assim, entre projetos complexos e noites de lua cheia, um romance inusitado e encantador floresceu, mostrando que, às vezes, o amor pode surgir das situações mais inesperadas e das conexões mais profundas.""", 
  "16": """Moral da história: Nunca subestime o poder de uma careca brilhante e de um lobisomem apaixonado. Fim."""
}

def main():
  for i in range(1, 17):
    limpar()
    animate(fanfic[str(i)], 0.01)
    input("\nPressione Enter para continuar...")


def animate(text, delay):
  for i in text:
    print(i, end="", flush=True)
    time.sleep(delay)

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
  main()

