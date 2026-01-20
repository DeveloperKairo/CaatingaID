import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path

class BotanicoAI:
    def __init__(self):
        caminho_atual = Path(__file__).resolve()
        
        pasta_raiz = caminho_atual.parents[3]
    
        caminho_env = pasta_raiz / '.env'
        
        print(f"\n🔍 DEBUG: Procurando arquivo .env em: {caminho_env}")
        
        if not caminho_env.exists():
            print(f"❌ ERRO: O Python diz que o arquivo NÃO existe nesse local.")
            print("DICA: Verifique se o arquivo não se chama '.env.txt' (Windows esconde extensões).")
        else:
            print(f"✅ Arquivo .env encontrado!")

        load_dotenv(dotenv_path=caminho_env)
        
        api_key = os.getenv("GOOGLE_API_KEY")
        
        if not api_key:
            try:
                conteudo = caminho_env.read_text()
                print(f"⚠️ O arquivo existe, mas o load_dotenv falhou. Conteúdo bruto: {conteudo[:15]}...")
            except:
                pass
            raise ValueError("Chave API não carregada. Verifique o arquivo .env")
            
        print(f"🔐 Chave carregada com sucesso: {api_key[:5]}*******")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def iniciar_identificacao(self, lista_plantas_dict):
        if not lista_plantas_dict:
            return False, "O banco de dados está vazio."

        inventario = json.dumps(lista_plantas_dict, ensure_ascii=False, indent=2)

        prompt_sistema = f"""
        Você é um botânico especialista em plantas da Caatinga.
        Seu objetivo é identificar qual planta o usuário está vendo e, após confirmar, dar dicas de cultivo.

        INVENTÁRIO DISPONÍVEL:
        {inventario}

        --- FASES DA CONVERSA ---

        1️⃣ FASE DE INVESTIGAÇÃO (Foco no Inventário)
        - Se a descrição for vaga, faça perguntas simples sobre características visuais (flores, espinhos, formato da copa).
        - Tente cruzar as informações do usuário com o INVENTÁRIO acima.

        2️⃣ FASE DE CONFIRMAÇÃO
        - Quando você tiver um palpite forte, NÃO afirme secamente.
        - Diga: "Tenho um palpite de que seja a **[Nome Popular]**. Para ter certeza, verifique se ela tem [Citar 1 ou 2 características visuais simples e marcantes dessa planta]?"
        - Espere o usuário confirmar.

        3️⃣ FASE DE PÓS-IDENTIFICAÇÃO (Liberada)
        - ASSIM QUE O USUÁRIO CONFIRMAR ("Sim", "É essa mesma"):
          a) Dê dicas de cultivo: Como regar (frequência), sol ideal e poda.
          b) A partir de agora, você está LIBERADO para usar todo seu conhecimento de botânica (além do JSON) para responder qualquer curiosidade ou dúvida do usuário sobre essa espécie.

        DICAS DE TOM:
        - Use emojis (🌵, ☀️, 💧).
        - Fale de forma simples, evitando "botaniquês" complexo sem explicação.
        """

        try:
            self.chat = self.model.start_chat(history=[
                {"role": "user", "parts": prompt_sistema},
                {"role": "model", "parts": "Entendido. Estou pronto para ajudar a identificar as plantas do inventário. Por favor, descreva o que você está vendo."}
            ])
            return True, "Contexto definido."
        except Exception as e:
            return False, f"Erro ao iniciar chat: {e}"

    def enviar_mensagem(self, texto_usuario):
        try:
            if not hasattr(self, 'chat'):
                return "Erro: Sessão não iniciada."
            
            response = self.chat.send_message(texto_usuario)
            return response.text
        except Exception as e:
            return f"Erro na comunicação: {e}"