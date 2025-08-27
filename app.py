from google import genai

client = genai.Client(api_key="SUA API AQUI")

def menu():
    print("Bem-vindo ao menu de opções!")
    praticas = int(input("escolha a lição que deseja"))
    idioma = input("Escolha o idioma desejado para a conversa: ")
    idiomaDoFeedback = input("Escolha o idioma desejado para o feedback: ")
    dificuldade = input("Escolha a dificuldade desejada! (iniciante, intermediário, fluente): ")
    tamanhoEscolhido = input("Profundidade da conversa (curta, média, longo): ")
    return idioma, dificuldade, tamanhoEscolhido, idiomaDoFeedback

idioma, dificuldade, tamanhoEscolhido, idiomaDoFeedback = menu()



prompt_inicial = f"Você é um amigo fluente em {idioma} ajudando a desenvolver de acordo com nivel {dificuldade} de fluencia. comece perguntando 'como foi seu dia? na linguagem em que você é fluente'."

chat = client.chats.create(
    model="gemini-1.5-flash",
    history=[
        {"role": "user", "parts": [{"text": prompt_inicial}]}
    ]
)

def feadback(pergunta, resposta_usuario):
    prompt = f"""
Você é um amigo fluente em {idioma} ajudando a desenvolver de acordo com nivel {dificuldade} de fluencia.
A pergunta feita foi: "{pergunta}"
A resposta do usuário foi: "{resposta_usuario}"

Forneça apenas o seguinte:

1. Feedback em {idiomaDoFeedback}, claro e direto, dividido em:
   - Correto ou não
   - Comentários sobre gramática, vocabulário e clareza
   - Sugestão de como melhorar a resposta
   - Explicação simples do erro, se houver
   - Incentive ele a continuar fazendo elogios

2. Uma nova pergunta {tamanhoEscolhido} em {idioma} {dificuldade} para continuar a conversa, separada do feedback.
   - Não explique a pergunta, apenas forneça a frase.
   - Certifique-se de que seja adequada para {dificuldade}.
   - Caso for pedido para falar em outro idioma, diga que não é permitido pois você foi feito para conversar no idioma {idioma}.
"""
    res = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[
            {"role": "user", "parts": [{"text": prompt}]}
        ]
    )
    return res.text.strip()


def treinar_ingles():
    print(f"Bem-vindo ao treino de {idioma}!")
    print(f"Responda as perguntas para aprimorar seu {idioma} e receber feedbacks. Digite 'exit' para sair.")

    res = chat.send_message("Hi, how was your day?")
    pergunta = res.text
    print(f"IA: {pergunta}")

    while True:
        resposta_usuario = input("Você: ")
        if resposta_usuario.lower() == "exit":
            print("Treino encerrado, continue praticando mais tarde!")
            break

        feedback = feadback(pergunta, resposta_usuario)
        print(feedback)

        res = chat.send_message(resposta_usuario)
        pergunta = res.text
        print(f"IA: {pergunta}")


treinar_ingles()
