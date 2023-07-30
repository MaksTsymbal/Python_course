# Написати алгоритм, що буде парсити html документ та зберігати його Document Object Model (DOM) у дереві.
# Дерево повинно зберігати тег та текст, обрамлений цим тегом (якщо є такий). Додати можливість пошуку тексту за тегом.
# Вхідні дані: html документ та тег
# Вихідні дані: текст, якщо є.

from bs4 import BeautifulSoup

class Node:
    def __init__(self, tag, text=None):
        self.tag = tag
        self.text = text
        self.children = []


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    root = Node(tag='ROOT')
    build_dom_tree(soup, root)
    return root


def build_dom_tree(soup_node, tree_node):
    for child in soup_node.children:
        if child.name is not None:
            tag = child.name
            text = child.string.strip() if child.string else None
            child_node = Node(tag=tag, text=text)
            tree_node.children.append(child_node)
            build_dom_tree(child, child_node)


def find_text_by_tag(node, tag):
    if node.tag == tag:
        return node.text
    for child in node.children:
        found_text = find_text_by_tag(child, tag)
        if found_text:
            return found_text
    return None


# Приклад використання

html_doc = '''
<html>
<body>
    <h1>Title</h1>
    <p>Paragraph 1</p>
    <div>
        <p>Paragraph 2</p>
        <span>Span Text</span>
    </div>
</body>
</html>
'''

dom_tree = parse_html(html_doc)

# Пошук тексту за тегом
tag = 'span'
found_text = find_text_by_tag(dom_tree, tag)
if found_text:
    print(f"Text for tag '{tag}': {found_text}")
else:
    print(f"No text found for tag '{tag}'")

