# Hub de Segurança

Este é um programa feito em Python que roda direto no terminal e serve para ajudar a investigar informações de rede e segurança em um só lugar.

---

## 🛠️ O que o programa faz?

* **1️⃣ Descobrir a Localização de um IP:** Você digita um IP e o programa mostra na tela de qual país, cidade e empresa de internet aquele IP pertence.
* **2️⃣ Testador de Portas (Port Scanner):** Você digita um site ou IP, e o programa testa as principais "portas" (como as de sites ou de acesso remoto) para ver se elas estão abertas ou fechadas/protegidas.
* **Visual Bonito e Colorido:** Toda a tela do programa usa tabelas organizadas e cores para ficar fácil de ler.
* **Avisos de Erro:** Se você digitar algo errado ou a internet cair, o programa não trava; ele te avisa com uma mensagem clara.

---

## 📦 Tecnologias Usadas

* **Python** (Linguagem de programação)
* **Requests** (Para buscar os dados de localização na internet)
* **Socket** (Para testar se as portas estão abertas)
* **Rich** (Para deixar o terminal colorido e com tabelas)

---

## 🚀 Como Rodar o Projeto

1. **Baixe o projeto no seu computador.**
2. **Instale o que o programa precisa com o comando:**
   ```bash
   pip install requests rich
