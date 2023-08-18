
## Finalidade do Script

Este script foi criado especificamente para recuperar atualizações de texto de traduções de mods do jogo "The Sims 4". Quando um mod é atualizado, este script garante que somente as strings novas sem tradução sejam recuperadas. Isso facilita a tradução ao focar apenas nas partes novas que ainda não foram traduzidas.
## Descrição do Script
### Funções:

1. Define as pastas de entrada e saída.
2. Obtém a lista de todos os arquivos na primeira pasta de entrada.
3. Verifica, para cada arquivo na primeira pasta de entrada, se existe um arquivo correspondente na segunda pasta de entrada.
   - Se um arquivo correspondente existe:
     - Carrega ambos os arquivos.
     - Coleta todos os InstanceIDs do arquivo da segunda pasta.
4. Cria um novo elemento raiz para o arquivo de saída.
5. Identifica e processa as diferenças:
   - Para cada elemento TextStringDefinition no arquivo da primeira pasta, verifica se seu InstanceID não está no arquivo da segunda pasta.
   - Se não estiver, adiciona-o ao novo elemento raiz.
6. Ao salvar:
   - Cria um elemento raiz chamado `StblData`.
   - Adiciona um sub-elemento `TextStringDefinitions` a este elemento raiz.
   - Durante o loop que verifica as diferenças entre os arquivos, os elementos TextStringDefinition diferentes são anexados ao sub-elemento `TextStringDefinitions`.
   - Salva o novo elemento raiz como um arquivo XML na pasta de saída.
   - Especifica a codificação utf-8 e adiciona o cabeçalho XML com `xml_declaration=True`.

---
## Purpose of the Script

This script was specifically designed to retrieve text updates from translations of mods for the game "The Sims 4". When a mod is updated, this script ensures that only the new untranslated strings are retrieved. This streamlines the translation process by focusing only on the new parts that haven't been translated yet.

## Script Description (USA English)

### Functions:

1. Defines input and output folders.
2. Retrieves the list of all files in the first input folder.
3. Checks, for each file in the first input folder, if there is a corresponding file in the second input folder.
   - If a corresponding file exists:
     - Loads both files.
     - Collects all the InstanceIDs from the file of the second folder.
4. Creates a new root element for the output file.
5. Identifies and processes differences:
   - For each TextStringDefinition element in the file from the first folder, checks if its InstanceID is not in the file from the second folder.
   - If it's not, adds it to the new root element.
6. When saving:
   - Creates a root element named `StblData`.
   - Adds a sub-element `TextStringDefinitions` to this root element.
   - During the loop that checks for differences between files, different TextStringDefinition elements are appended to the `TextStringDefinitions` sub-element.
   - Saves the new root element as an XML file in the output folder.
   - Specifies utf-8 encoding and adds the XML header with `xml_declaration=True`.
