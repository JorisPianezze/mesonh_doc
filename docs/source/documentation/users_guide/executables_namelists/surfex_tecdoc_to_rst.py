import re
import os
import argparse

# Chemins d'entrée et de sortie
parser = argparse.ArgumentParser(
    description="Convert SURFEX LaTeX namelists to RST"
)

parser.add_argument(
    "input_file",
    help="Input LaTeX file (from SURFEX doc : section_XX.tex"
)

parser.add_argument(
    "-o",
    "--output-dir",
    default="rst_sections",
    help="Output directory"
)

args = parser.parse_args()

input_file = args.input_file
if not os.path.exists(input_file):
    raise FileNotFoundError(f"File not found: {input_file}")
output_dir = args.output_dir
os.makedirs(output_dir, exist_ok=True)

def clean_latex(text):
    text = text.replace(r'\_', '_')
    text = text.replace(r'\%', '%')
    text = text.replace(r'\&', '&')
    return text.strip()

def extract_itemize_blocks(text):

    lines = text.splitlines()

    blocks = []

    current = []
    level = 0

    for line in lines:

        if r'\begin{itemize}' in line or r'\begin{enumerate}' in line:

            level += 1

            # début du bloc principal
            if level == 1:
                current = []

            current.append(line)
            continue

        if level > 0:
            current.append(line)

        if r'\end{itemize}' in line or r'\end{enumerate}' in line:

            level -= 1

            # fin du bloc principal
            if level == 0:
                blocks.append("\n".join(current))

    return blocks

def convert_latex_lists_to_rst(text):

    lines = text.splitlines()

    rst = ""

    # pile des environnements
    stack = []

    for raw_line in lines:

        line = clean_latex(raw_line.strip())

        if not line:
            continue

        # Entrée itemize
        if r'\begin{itemize}' in line:
            stack.append("itemize")
            continue

        # Entrée enumerate
        if r'\begin{enumerate}' in line:
            stack.append("enumerate")
            continue

        # Sortie environnement
        if r'\end{itemize}' in line or r'\end{enumerate}' in line:
            if stack:
                stack.pop()
            continue

        # Item
        if line.startswith(r'\item'):

            content = line[len(r'\item'):].strip()

            level = len(stack)

            indent = "  " * max(level - 1, 0)

            current_env = stack[-1] if stack else "itemize"

            # Style de bullet
            bullet = "*"

            if current_env == "enumerate":
                bullet = "*"

            # Niveau principal itemize
            if level == 1 and current_env == "itemize":

                if ':' in content:

                    key, desc = content.split(':', 1)

                    rst += (
                        f"{bullet} :code:`{key.strip()}`"
                        f" : {desc.strip()}\n\n"
                    )

                else:
                    rst += f"{bullet} :code:`{content}`\n\n"

            else:
                rst += f"{indent}{bullet} {content}\n"

    return rst

# Regex pour détecter sections NAM_
section_pattern = re.compile(r'\\(section|subsection|subsubsection)\{(NAM(?:\\_[^\}\\]+)+)\}')
# Regex pour détecter tabular LaTeX
table_pattern = re.compile(r'\\begin\{tabular\}\{[^\}]*\}(.*?)\\end\{tabular\}', re.DOTALL)
# Regex pour séparer les lignes de tableau et colonnes
line_pattern = re.compile(r'^(.*)\\\\', re.MULTILINE)
col_split_pattern = re.compile(r'&')

# Lire le fichier LaTeX
with open(input_file, "r", encoding="utf-8") as f:
    latex_content = f.read()

# Trouver toutes les sections NAM_
sections = list(section_pattern.finditer(latex_content))
for i, sec in enumerate(sections):
    section_type = sec.group(1)
    section_name = clean_latex(sec.group(2).replace(r'\_', '_'))
    
    # Déterminer le contenu de la section
    start_pos = sec.end()
    end_pos = sections[i + 1].start() if i + 1 < len(sections) else len(latex_content)
    section_content = clean_latex(latex_content[start_pos:end_pos].strip())
    
    # Préparer le contenu RST
    rst_content = f".. _{section_name.lower()}:\n\n"
    rst_content += f"{section_name}\n{'-' * len(section_name)}\n\n"
    
    # Extraire les tableaux
    tables = table_pattern.findall(section_content)
    for table in tables:
        rst_content += ".. csv-table::\n   :header: \"Fortran name\", \"Fortran type\", \"Default value\"\n   :widths: 30, 30, 30\n\n"
        lines = []

        for line in line_pattern.findall(table):
            line = line.strip()
            if not line:
                continue
            if r'\hline' in line:
                continue
            lines.append(line)
        
        # Suppression de la ligne d'entête
        if lines:
            lines = lines[1:]

        for line in lines:
            cols = [c.strip() for c in col_split_pattern.split(line)]
            if len(cols) >= 4:
                # Conserver la colonne 1,2,4
                rst_content += f"   \"{cols[0]}\", \"{cols[1].upper()}\", \"{cols[3]}\"\n"
        rst_content += "\n"
    
    section_no_tables = table_pattern.sub('', section_content)
    itemize_pattern = re.compile(
        r'\\begin\{itemize\}(.*?)\\end\{itemize\}',
        re.DOTALL
    )

    item_pattern = re.compile(r'\\item\s+(.*)')

    # Extraire les descriptions de namelist
    # Suppose chaque option est sur une ligne sous forme \key{...} description
    # ou juste une ligne commençant par le nom de l'option
    itemizes = extract_itemize_blocks(section_no_tables)

    for itemize in itemizes:
        rst_content += convert_latex_lists_to_rst(itemize)
    
    # Sauvegarder le fichier RST
    rst_file = os.path.join(output_dir, f"{section_name.lower()}.rst")
    with open(rst_file, "w", encoding="utf-8") as f:
        f.write(rst_content)
    
    print(f"Section {section_name} convertie -> {rst_file}")
