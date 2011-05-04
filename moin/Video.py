html_open = """
<p align=center>
    <video controls="controls" src="%s" ></video><br/>
    <a href="%s">Descargar Video</a></p>
    """
def is_valid(cadena):
    valid_input = 'abcdefghijqlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ:/-_.1234567890'
    for a in cadena:
        if a in valid_input:
            continue
        else:
            return False
    return True

def macro_Video(macro, url):
    if is_valid(url):
        html = html_open % (url, url)
    else:
        html = '<pre> Url invalida para el macro Video </pre>'
    return macro.formatter.rawHTML(html)
