from google import genai

client = genai.Client(api_key="SUA API AQUI")


def menu():
    print("==========Bem-vindo ao menu de opções!==========")
    print("escolha uma das opções para simular uma conversa")
    print("0 - conversa livre")
    print(f"1 - conversa durante uma viagem")
    print(f"2 - conversa em um restaurante")
    print(f"3 - entrevista de emprego")
    print(f"4 - situação de compras")
    print(f"5 - conversa sobre esportes")
    print(f"6 - conversa sobre filmes e séries")
    print(f"7 - conversa sobre música e artistas")
    print(f"8 - conversa em um aeroporto")
    print(f"9 - conversa em um hotel")
    print(f"10 - conversa em uma festa")
    print(f"11 - conversa sobre clima e tempo")
    print(f"12 - conversa sobre comida e receitas")
    print(f"13 - conversa sobre tecnologia e inovação")
    print(f"14 - conversa sobre estudos e aprendizado")
    print("=================================================")
    praticas = int(input("escolha a lição que deseja: "))
    idioma = input("Escolha o idioma desejado para a conversa: ")
    idiomaDoFeedback = input("Escolha o idioma desejado para o feedback: ")
    dificuldade = input("Escolha a dificuldade desejada! (iniciante, intermediário, fluente): ")
    tamanhoEscolhido = input("Profundidade da conversa (curta, média, longo): ")
    return idioma, dificuldade, tamanhoEscolhido, idiomaDoFeedback, praticas

idioma, dificuldade, tamanhoEscolhido, idiomaDoFeedback, praticas = menu()

temas = {
    0: f"Você é um amigo fluente que está conversando livremente comigo no {idioma}, adaptando o nível de dificuldade para {dificuldade} e usando textos {tamanhoEscolhido}. Não limite o tema, apenas mantenha um diálogo natural, fazendo perguntas e respondendo como em uma conversa real.",
    1: f"Você é um amigo fluente que está me ajudando a simular uma conversa durante uma viagem no {idioma} que você é fluente, use a dificuldade {dificuldade} para se comunicar com o usuário, use textos {tamanhoEscolhido}.",
    2: f"Você é um amigo fluente que está me ajudando a simular uma conversa em um restaurante no {idioma} que você é fluente, use a dificuldade {dificuldade} para se comunicar com o usuário, use textos {tamanhoEscolhido}.",
    3: f"Você é um amigo fluente que está me ajudando a simular uma entrevista de emprego no {idioma} que você é fluente, use a dificuldade {dificuldade} para se comunicar com o usuário, use textos {tamanhoEscolhido}.",
    4: f"Você é um amigo fluente que está me ajudando a simular uma situação de compras no {idioma} que você é fluente, use a dificuldade {dificuldade} para se comunicar com o usuário, use textos {tamanhoEscolhido}.",
    5: f"Você é um amigo fluente que está me ajudando a simular uma conversa sobre esportes no {idioma} que você é fluente, usando a dificuldade {dificuldade} e textos {tamanhoEscolhido}.",
    6: f"Você é um amigo fluente que está me ajudando a simular uma conversa sobre filmes e séries no {idioma} que você é fluente, usando a dificuldade {dificuldade} e textos {tamanhoEscolhido}.",
    7: f"Você é um amigo fluente que está me ajudando a simular uma conversa sobre música e artistas no {idioma} que você é fluente, usando a dificuldade {dificuldade} e textos {tamanhoEscolhido}.",
    8: f"Você é um amigo fluente que está me ajudando a simular uma conversa em um aeroporto no {idioma} que você é fluente, usando a dificuldade {dificuldade} e textos {tamanhoEscolhido}.",
    9: f"Você é um amigo fluente que está me ajudando a simular uma conversa em um hotel no {idioma} que você é fluente, usando a dificuldade {dificuldade} e textos {tamanhoEscolhido}.",
    10: f"Você é um amigo fluente que está me ajudando a simular uma conversa em uma festa no {idioma} que você é fluente, usando a dificuldade {dificuldade} e textos {tamanhoEscolhido}.",
    11: f"Você é um amigo fluente que está me ajudando a simular uma conversa sobre clima e tempo no {idioma} que você é fluente, usando a dificuldade {dificuldade} e textos {tamanhoEscolhido}.",
    12: f"Você é um amigo fluente que está me ajudando a simular uma conversa sobre comida e receitas no {idioma} que você é fluente, usando a dificuldade {dificuldade} e textos {tamanhoEscolhido}.",
    13: f"Você é um amigo fluente que está me ajudando a simular uma conversa sobre tecnologia e inovação no {idioma} que você é fluente, usando a dificuldade {dificuldade} e textos {tamanhoEscolhido}.",
    14: f"Você é um amigo fluente que está me ajudando a simular uma conversa sobre estudos e aprendizado no {idioma} que você é fluente, usando a dificuldade {dificuldade} e textos {tamanhoEscolhido}."
}

prompt_inicial = temas[praticas]

chat = client.chats.create(
    model="gemini-1.5-flash",
    history=[
        {"role": "user", "parts": [{"text": prompt_inicial}]}
    ]
)

def feadback(pergunta, resposta_usuario):
    prompt = f"""
Você é um professor de {idioma} ajudando a desenvolver de acordo com o nível {dificuldade} de fluência.
A pergunta feita foi: "{pergunta}"
A resposta do usuário foi: "{resposta_usuario}"

Forneça apenas o seguinte, de forma curta e objetiva, em {idiomaDoFeedback}:

1️⃣ Correto ou não (considere gírias corretas, mas avise que são gírias)
2️⃣ Pontos positivos: gramática, vocabulário, clareza
3️⃣ Pontos a melhorar (essa parte precisa ser de acordo com o tamanho escolhido = {tamanhoEscolhido}), (detalhes ou especificidade não é um ponto em que você deve ser incisivo, apenas diga para detalhar mais para um melhor aprendizado e nada mais)
4️⃣ Sugestão prática de frase: dê 1 ou 2 opções curtas que poderiam melhorar a resposta
5️⃣ Incentivo: elogie e motive, indicando a porcentagem aproximada de acerto (0-100%)

Evite parágrafos longos. Use listas curtas, linguagem simples e direta. 
Não explique regras complexas, apenas mostre de forma prática como melhorar. NÃO DE O FEEDBACK NO TEXTO DA IA, APENAS DO USUÁRIO

"""
    res = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[
            {"role": "user", "parts": [{"text": prompt}]}
        ]
    )
    return res.text.strip()

perguntas_iniciais = {
    0: "Oi! Como está sendo o seu dia?",
    1: "Oi! Para onde você está viajando hoje?",
    2: "Olá! Bem-vindo ao nosso restaurante. O que você gostaria de pedir?",
    3: "Oi, obrigado por participar da entrevista. Você poderia falar um pouco sobre você?",
    4: "Olá! Você está procurando algo específico para comprar hoje?",
    5: "Ei! Você assistiu ao último jogo de esportes?",
    6: "Oi! Você assistiu a algum filme bom recentemente?",
    7: "Ei! Que tipo de música você gosta?",
    8: "Olá! Para onde você está voando hoje?",
    9: "Oi! Como foi seu check-in no hotel?",
    10: "Ei! Está gostando da festa?",
    11: "Oi! Como está o clima aí onde você está?",
    12: "Olá! Qual é o seu prato favorito para cozinhar?",
    13: "Oi! Você viu as últimas notícias de tecnologia?",
    14: "Oi! O que você tem estudado ultimamente?"
}


def treinar_idioma():
    print(f"Bem-vindo ao treino de {idioma}!")
    print(f"Responda as perguntas para aprimorar seu {idioma} e receber feedbacks. Digite 'exit' para sair.")

    res = chat.send_message(perguntas_iniciais[praticas])
    pergunta = res.text
    print(f"IA: {pergunta}")

    while True:
        resposta_usuario = input("Você: ")
        if resposta_usuario.lower() == "exit":
            print("Treino encerrado, continue praticando mais tarde!")
            break

        feedback_texto = feadback(pergunta, resposta_usuario)
        print(feedback_texto)

        res = chat.send_message(resposta_usuario)
        pergunta = res.text
        print(f"IA: {pergunta}")

treinar_idioma()

