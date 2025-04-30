from personagem import Personagem

# Criando personagens
guerreiro = Personagem("Aragorn", "Guerreiro")
mago = Personagem("Gandalf", "Mago")

# Exibindo status inicial
print("Status inicial do guerreiro:")
print(guerreiro.status())

# Simulando uma batalha
print("\nBatalha começando...")
dano_guerreiro = guerreiro.atacar() 
print(f"{guerreiro.nome} ataca causando {dano_guerreiro} de dano!")
vida_mago = mago.receber_dano(dano_guerreiro)
print(f"{mago.nome} agora tem {vida_mago} de vida.")
# Continua...

# Continuação
dano_mago = mago.atacar()
print(f"{mago.nome} contra-ataca causando {dano_mago} de dano!")
vida_guerreiro = guerreiro.receber_dano(dano_mago)
print(f"{guerreiro.nome} agora tem {vida_guerreiro} de vida.")

# Ganhando experiência e itens
print("\nApós a batalha...")
guerreiro.ganhar_experiencia(150)
guerreiro.adicionar_item("Espada Longa")
guerreiro.adicionar_item("Poção de Cura")

# Exibindo status atualizado
print("\nStatus atualizado do guerreiro:")
print(guerreiro.status())

