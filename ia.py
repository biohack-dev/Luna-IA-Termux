import requests
import json
import os
import subprocess
import urllib.parse
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request
import aiml
import warnings
import time

# Suprimir warnings de depreciação
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Configurações
API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "mistralai/mistral-7b-instruct"
WORLD_NEWS_URL = "https://news.google.com/rss/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JYQjBMVUpTR2dKQ1VpZ0FQAQ?hl=pt-BR&gl=BR&ceid=BR%3Apt-419"

# Inicialização do kernel AIML
kernel = aiml.Kernel()
kernel.verbose(False)

# Patch para resolver problema do time.clock no AIML (Python 3.8+)
if not hasattr(time, 'clock'):
    time.clock = time.time

kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")

def speak(text):
    """Usa o TTS do Termux para falar o texto"""
    try:
        clean_text = text.replace('"', '\\"').replace("'", "\\'")
        subprocess.run(['termux-tts-speak', clean_text], check=True)
    except Exception as e:
        print(f">> [ERRO TTS] {str(e)}")

def get_ai_response(prompt):
    """Obtém resposta da API do OpenRouter"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "https://github.com/seu-usuario/seu-projeto",
        "X-Title": "Chatbot OpenRouter",
        "Content-Type": "application/json",
    }

    prompt_ptbr = f"Responda em português brasileiro de forma clara e concisa: {prompt}"

    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt_ptbr}],
        "temperature": 0.7,
        "max_tokens": 500,
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as err:
        return f"Erro: {err.response.status_code} - {err.response.text}"
    except Exception as e:
        return f"Erro desconhecido: {str(e)}"

def get_news(query):
    """Busca notícias no Google News"""
    string_formatada = urllib.parse.quote(query, encoding='utf-8')
    news_url = "https://news.google.com/rss/search?q=" + \
        string_formatada + "&hl=pt-BR&gl=BR&ceid=BR:pt-419"

    try:
        req = Request(news_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req) as Client:
            xml_page = Client.read()

        soup_page = soup(xml_page, "lxml-xml")
        news_list = soup_page.findAll("item")
        
        results = []
        for news in news_list[:3]:  # Limita a 3 notícias
            title = news.title.text.split(' - ')[0]
            results.append(title)
        
        return results if results else ["Nenhuma notícia encontrada sobre este assunto."]
    except Exception as e:
        print(f">> [ERRO NEWS] {str(e)}")
        return [f"Erro ao buscar notícias: {str(e)}"]

def get_world_news():
    """Busca as principais notícias mundiais"""
    try:
        req = Request(WORLD_NEWS_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req) as Client:
            xml_page = Client.read()

        soup_page = soup(xml_page, "lxml-xml")
        news_list = soup_page.findAll("item")
        
        results = []
        for news in news_list[:5]:  # Limita a 10 notícias
            title = news.title.text.split(' - ')[0]
            results.append(title)
        
        return results if results else ["Nenhuma notícia mundial encontrada."]
    except Exception as e:
        print(f">> [ERRO NOTÍCIAS MUNDIAIS] {str(e)}")
        return [f"Erro ao buscar notícias mundiais: {str(e)}"]

def main():
    os.system("clear")
    os.system("./biohack.sh")
    print("=== Luna I.A Chatbot Unificado ===")
    print("Sistemas disponíveis:")
    print("1. AIML - respostas pré-programadas")
    print("2. Mistral-7B - IA generativa")
    print("3. Notícias (digite '/news' antes da pesquisa)")
    print("4. Mundo (digite '/mundo') - Principais notícias mundiais")
    print('Digite "sair" para encerrar.')
    print('Digite "clear/cls" para limpar a tela.\n')

    while True:
        user_input = input("> ").strip()
        
        if user_input.lower() in ["sair", "exit"]:
            speak("Até logo!")
            print(">> Até logo!")
            break
            
        if not user_input:
            print(">> Por favor, digite algo.")
            continue
            
        if user_input.startswith("/ai "):
            prompt = user_input[4:]
            response = get_ai_response(prompt)
            print(f"[AI] {response}")
            speak(response)
        elif user_input.startswith("/news "):
            query = user_input[6:]
            print(f"[Buscando notícias sobre '{query}']")
            
            news_results = get_news(query)
            for i, news in enumerate(news_results, 1):
                print(f"{i}. {news}")
                speak(news)
                time.sleep(1)
        elif user_input == "/mundo":
            print("[Principais notícias mundiais]")
            world_news = get_world_news()
            for i, news in enumerate(world_news, 1):
                print(f"{i}. {news}")
                speak(news)
                time.sleep(1)
        elif user_input in ["clear", "cls"]:
            os.system("clear")
            os.system("./biohack.sh")
            print("=== Luna I.A Chatbot Unificado ===")
            print("Sistemas disponíveis:")
            print("1. AIML - respostas pré-programadas")
            print("2. Mistral-7B - IA generativa")
            print("3. Notícias (digite '/news' antes da pesquisa)")
            print("4. Mundo (digite '/mundo') - Principais notícias mundiais")
            print('Digite "sair" para encerrar.')
            print('Digite "clear/cls" para limpar a tela.\n')
        else:
            bot_response = kernel.respond(user_input)
            
            if not bot_response or bot_response.lower().startswith("warning:"):
                response = get_ai_response(user_input)
                print(f"[AI] {response}")
                speak(response)
            else:
                print(f"[AIML] {bot_response}")
                speak(bot_response)

if __name__ == "__main__":
    main()
