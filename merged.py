import os
import xml.etree.ElementTree as ET

# Definir as pastas de entrada e saída
input_folder1 = 'D:\\DP_STBLEditor\\in'
input_folder2 = 'D:\\DP_STBLEditor\\pt'
output_folder = 'D:\\DP_STBLEditor'

# Certifique-se de que a pasta de saída existe
os.makedirs(output_folder, exist_ok=True)

# Obter a lista de arquivos na primeira pasta de entrada
files1 = os.listdir(input_folder1)

# Percorrer todos os arquivos na primeira pasta de entrada
for filename in files1:
    if filename.endswith('.xml'):
        # Caminho completo para os arquivos de entrada e saída
        file1 = os.path.join(input_folder1, filename)
        file2 = os.path.join(input_folder2, filename)
        output_file = os.path.join(output_folder, filename)

        # Verificar se o arquivo correspondente existe na segunda pasta de entrada
        if os.path.exists(file2):
            # Carregar os arquivos XML de entrada
            tree1 = ET.parse(file1)
            root1 = tree1.getroot()
            tree2 = ET.parse(file2)
            root2 = tree2.getroot()

            # Coletar todos os InstanceIDs do segundo arquivo XML
            instance_ids_file2 = [element.attrib['InstanceID'] for element in root2.findall('.//TextStringDefinition')]

            # Criar a estrutura de saída
            output_root = ET.Element('StblData')
            text_string_defs = ET.SubElement(output_root, 'TextStringDefinitions')

            # Percorrer todos os elementos TextStringDefinition do primeiro arquivo XML
            for element in root1.findall('.//TextStringDefinition'):
                # Se o InstanceID do elemento atual não está no segundo arquivo, adicione-o ao text_string_defs
                if element.attrib['InstanceID'] not in instance_ids_file2:
                    text_string_defs.append(element)

            # Salvar o novo arquivo XML
            output_tree = ET.ElementTree(output_root)
            output_tree.write(output_file, encoding='utf-8', xml_declaration=True)
