def to_camel_case(text):
    text_lst = list(text)
    while "-" in text_lst or "_" in text_lst:
        for hyphen in ("-", "_"):
            if hyphen in text_lst:
                pos = text_lst.index(hyphen)
                text_lst.pop(pos)
                text_lst[pos] = text_lst[pos].upper()
    return "".join(text_lst)