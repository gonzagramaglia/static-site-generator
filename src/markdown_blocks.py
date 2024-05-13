import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
        heading_pattern = re.compile(r'^(#{1,6})\s(.+)$')
        code_pattern = re.compile(r'^```(.+?)^```', re.DOTALL | re.MULTILINE)
        quote_pattern = re.compile(r'^>\s*(.*)$', re.MULTILINE)
        ulist_pattern = re.compile(r'^[*-]\s(.*)$', re.MULTILINE)
        olist_pattern = re.compile(r'^(?:\d+\. )(.*)$', re.MULTILINE)

        patterns = [
                (heading_pattern, block_type_heading),
                (code_pattern, block_type_code),
                (quote_pattern, block_type_quote),
                (ulist_pattern, block_type_ulist),
                (olist_pattern, block_type_olist)
        ]

        for pattern, block_type in patterns:
                if pattern.search(block):
                        return block_type

        return block_type_paragraph