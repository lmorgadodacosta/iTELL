def stdout2html(string):
    """
    This function takes the output of stdout and formats it to be shown as basic html.
    Our main sources of stdout are the bash scripts to update grammars, which include 
    ACE output when compiling grammars. The changes included here are on a necessity basis.
    """
    r = string.replace('\n', '<br />\n')
    r = r.replace("[0;1m", '')
    r = r.replace("[0m", '')
    return r
