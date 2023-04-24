if __name__ == '__main__':
    a = input('Primeira palavra que define o animal: ').strip().lower()
    b = input('Segunda palavra que define o animal: ').strip().lower()
    c = input('Terceira palavra que define o animal: ').strip().lower()

    if a == "vertebrado" and b == "ave" and c == "carnivoro":
        print("Aguia")
    elif a == "vertebrado" and b == "ave" and c == "onivoro":
        print("Pomba")
    elif a == "vertebrado" and b == "mamifero" and c == "onivoro":
        print("Homem")
    elif a == "vertebrado" and b == "mamifero" and c == "herbivoro":
        print("Vaca")
    elif a == "invertebrado" and b == "inseto" and c == "hematofago":
        print("Pulga")
    elif a == "invertebrado" and b == "inseto" and c == "herbivoro":
        print("Lagarta")
    elif a == "invertebrado" and b == "anelideo" and c == "hematofago":
        print("Sanguessuga")
    elif a == "invertebrado" and b == "anelideo" and c == "onivoro":
        print("Minhoca")