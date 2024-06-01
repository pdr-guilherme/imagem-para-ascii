# Imagem Para ASCII

Este módulo fornece ferramentas para converter imagens em representações ASCII. As funções utilizam um conjunto de caracteres pré-definidos para representar diferentes níveis de brilho na imagem, permitindo a criação de arte ASCII.

## Instalação

Esse script depende da biblioteca [Pillow](https://python-pillow.org/) para funcionar, instale-a com o pip executando o seguindo comando no console.

```bash
python3 -m pip install --upgrade Pillow
```

Após isso, clone o repositório e navegue até ele.

```bash
git clone https://github.com/pdr-guilherme/imagem-para-ascii.git
cd imagem-para-ascii
```

## Uso

Esse script pode ser usado tanto pela linha de comando ou como um módulo.

Na linha de comando:

```bash
python imagem_para_ascii.py caminho/para/imagem
```

Como módulo:

```python
import imagem_para_ascii as ipa

local_imagem = "caminho/para/imagem"
ipa.mostrar_imagem(local_imagem)
```

Para um melhor entendimento de como as funções operam, veja as docstrings dentro do arquivo ou execute:

```python
import imagem_para_ascii as ipa

help(ipa)
```
