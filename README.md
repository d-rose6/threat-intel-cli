# Threat Intel CLI 🚀

Uma ferramenta em linha de comando (CLI) desenvolvida em Python para investigação, inteligência de ameaças e geolocalização de endereços IP suspeitos.

O projeto consome uma API pública de geolocalização e exibe os dados estruturados de forma elegante e profissional diretamente no terminal.

---

## 🛠️ Funcionalidades

* **Consulta de IP Dinâmica:** Investiga informações de localização e provedor de qualquer IP informado.
* **Interface CLI Avançada:** Menu interativo, tabelas estilizadas e paginação fluida construída com a biblioteca `Rich`.
* **Tratamento de Erros:** Validações robustas de input (evitando consultas vazias acidentais) e tratamento de exceções de rede.
* **Modularização:** Arquitetura limpa com separação de responsabilidades (funções de API isoladas em pacotes).

---

## 📦 Tecnologias Utilizadas

* **Python 3.13+**
* **Requests:** Para consumo da API Rest (`ip-api.com`).
* **Rich:** Para estilização do terminal, tabelas e inputs interativos.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Antes de começar, você vai precisar ter o **Python** instalado na sua máquina e também tenha a biblioteca Rich instalada 
