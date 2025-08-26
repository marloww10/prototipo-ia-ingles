from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


prompt_inicial = "Você é um amigo fluente em inglês ajudando um iniciante (nível A1/A2), comece perguntando 'how was your day?'."

chat = client.chats.create(
    model="gemini-1.5-flash",
    history=[
        {"role": "user", "parts": [{"text": prompt_inicial}]}
    ]
)

def feadback(pergunta,resposta_usuario):
    prompt = f"""
Você é um amigo fluente em inglês ajudando um iniciante (nível A1/A2).
A pergunta feita foi: "{pergunta}"
A resposta do usuário foi: "{resposta_usuario}"

Forneça apenas o seguinte:

1. Feedback em português, claro e direto, dividido em:
   - Correto ou não
   - Comentários sobre gramática, vocabulário e clareza
   - Sugestão de como melhorar a resposta
   - Explicação simples do erro, se houver

2. Uma nova pergunta curta em inglês (nível A1/A2) para continuar a conversa, separada do feedback. 
   - Não explique a pergunta, apenas forneça a frase.
   - Certifique-se de que seja adequada para iniciantes.

Formato de saída sugerido:

FEEDBACK:

NOVA PERGUNTA:
"""
    res = client.models.generate_content(
        model = "gemini-1.5-flash",
        contents =[
            {"role": "user", "parts": [{"text": prompt}]}]
    )
    return res.text.strip()


def treinar_ingles():
    print("Bem vindo ao treino de inglês!")
    print("Responda as perguntas para aprimorar seu inglês e receber feedbacks. Digite 'exit' para sair.")

    res = chat.send_message("Hi, how was your day?")
    pergunta = res.text
    print(f"IA: {pergunta}")

    while True:
        resposta_usuario = input ("Você: ")
        feedback = feadback(pergunta, resposta_usuario)
        print("Feedback: ", feedback)
        if resposta_usuario == "exit":
            print("treino encerrado, continue praticando mais tarde!")
            break

        res = chat.send_message(resposta_usuario)
        print(f"IA: {res.text}")


if __name__ == "__main__":
    treinar_ingles()
