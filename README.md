## 🌙 Luna IA Termux — Inteligência Artificial no Terminal do Android

**Luna IA Termux** é uma assistente inteligente em **modo texto (TXT)** desenvolvida para rodar **diretamente no celular Android**, usando o **Termux**.
Ela combina **bash + Python + AIML** para criar uma IA leve, funcional e totalmente **offline**, capaz de responder perguntas, executar comandos e interagir com scripts do sistema.

---

### 📂 Estrutura do Projeto

| Arquivo / Script          | Função                                                    |
| ------------------------- | --------------------------------------------------------- |
| **ia.sh**                 | Inicia a Luna IA no modo texto.                           |
| **ia.py**                 | Núcleo em Python que processa o diálogo com base em AIML. |
| **basic.aiml**            | Banco de respostas padrão e regras de aprendizado.        |
| **clima.sh / clima.json** | Mostra a previsão do tempo atual.                         |
| **dolar.sh**              | Exibe a cotação atual do dólar.                           |
| **gasolina.sh**           | Mostra o preço médio atual da gasolina.                   |
| **hora.sh / time.sh**     | Fala ou mostra a hora atual no formato 12h/24h.           |
| **myip.sh**               | Exibe IP público e local.                                 |
| **scanrede.sh**           | Faz varredura de rede local e mostra dispositivos ativos. |
| **biohack.sh**            | Executa ajustes rápidos no Termux e otimizações.          |
| **limpa.sh**              | Limpa cache, lixo e libera espaço.                        |
| **linux.sh**              | Verifica e instala dependências Linux no ambiente Termux. |
| **openssh.sh**            | Configura acesso remoto via SSH no Termux.                |
| **source.list**           | Lista de repositórios APT otimizados para Termux.         |
| **std-startup.xml**       | Arquivo de inicialização AIML.                            |
| **.termux/tasker/**       | Integração com o Tasker (fala de hora, automações etc.).  |

---

### ⚙️ Instalação no Termux

```bash
pkg update && pkg upgrade -y
pkg install python git curl jq espeak termux-api -y
```

Clone o repositório e instale:

```bash
git clone https://github.com/seuusuario/LunaIA-Termux.git
cd LunaIA-Termux/Android
chmod +x *.sh
./linux.sh
```

Instale as bibliotecas Python necessárias:

```bash
pip install aiml requests gtts
```

---

### 💬 Uso

Para iniciar a IA:

```bash
./ia.sh
```

Exemplo de conversa:

```
> Olá Luna
Luna: Olá! Pronta para conversar 🌙
```

---

### 🧠 Recursos

* 💬 **Interface 100% em texto** — sem necessidade de GUI
* 📱 **Compatível com Termux** — roda direto no Android
* ⚙️ **Totalmente offline** após instalação
* 🔉 **Suporte a voz** via `espeak` ou `gtts`
* 🌐 Scripts integrados para clima, rede, sistema e utilidades
* 🧩 Expansível com novos módulos em bash ou Python

---

### 🧰 Dependências Principais

* **Termux**
* `bash`, `python3`, `curl`, `jq`, `git`
* `espeak` *(para voz, opcional)*
* `termux-api` *(para integração com Android)*

---

### 🚀 Exemplo de Comandos Úteis

```bash
./clima.sh São_Paulo
./dolar.sh
./gasolina.sh
./hora.sh
./scanrede.sh
```

---

### 📜 Licença

Distribuído sob a **MIT License** — livre para usar, estudar e modificar.
💡 *Feita para aprender, explorar e conversar com seu sistema.*

---

Quer que eu gere esse texto pronto como **README.md** (com emojis, seções, comandos destacados e formatação GitHub)?
Posso gerar o arquivo direto para você subir ao repositório.
