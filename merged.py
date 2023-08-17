import os
import xml.etree.ElementTree as ET

# Define inbox and outbox folders
input_folder1 = 'D:\\DP_STBLEditor\\in'
input_folder2 = 'D:\\DP_STBLEditor\\pt'
output_folder = 'D:\\DP_STBLEditor'

# Make sure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get the list of files in the first input folder
files1 = os.listdir(input_folder1)

# Browse all files in the first entry folder
for filename in files1:
    if filename.endswith('.xml'):
        # Caminho completo para os arquivos de entrada e saída
        file1 = os.path.join(input_folder1, filename)
        file2 = os.path.join(input_folder2, filename)
        output_file = os.path.join(output_folder, filename)

        # Check that the corresponding file exists in the second input folder
        if os.path.exists(file2):
            # Carregar os arquivos XML de entrada
            tree1 = ET.parse(file1)
            root1 = tree1.getroot()
            tree2 = ET.parse(file2)
            root2 = tree2.getroot()

            # Collect all InstanceIDs from the second XML file
            instance_ids_file2 = [element.attrib['InstanceID'] for element in root2.findall('.//TextStringDefinition')]

            # Create the output structure
            output_root = ET.Element('StblData')
            text_string_defs = ET.SubElement(output_root, 'TextStringDefinitions')

            # Browse all TextStringDefinition elements in the first XML file
            for element in root1.findall('.//TextStringDefinition'):
                # Se o InstanceID do elemento atual não está no segundo arquivo, adicione-o ao text_string_defs
                if element.attrib['InstanceID'] not in instance_ids_file2:
                    text_string_defs.append(element)

            # Save the new XML file
            output_tree = ET.ElementTree(output_root)
            output_tree.write(output_file, encoding='utf-8', xml_declaration=True)
