import graphviz

def lolviz(table):
    """
    Given a list of lists such as:

      [ [('a','3')], [], [('b',230), ('c',21)] ]

    return the dot/graphviz to display as a two-dimensional
    structure.
    """
    s = """
    digraph G {
        nodesep=.05;
        rankdir=LR;
        node [shape=record,width=.1,height=.1];
    """
    # Make outer list as vertical
    labels = []
    for i in range(len(table)):
        bucket = table[i]
        if len(bucket)==0: labels.append(str(i))
        else: labels.append("<f%d> %d" % (i,i))

    s += '    mainlist [color="#444443", fontsize="9", fontcolor="#444443", fontname="Helvetica", style=filled, fillcolor="#D9E6F5", label = "'+'|'.join(labels)+'"];\n'

    # define inner lists
    for i in range(len(table)):
        bucket = table[i]
        if not bucket or len(bucket)==0: continue
        elements = []
        for j, el in enumerate(bucket):
            if type(el)==tuple and len(el)==2: els = "%s&rarr;%s" % el
            else: els = repr(el)
            elements.append('<table BORDER="0" CELLBORDER="1" CELLSPACING="0"><tr><td cellspacing="0" bgcolor="#FBFEB0" border="1" sides="b" valign="top"><font color="#444443" point-size="9">%d</font></td></tr><tr><td bgcolor="#FBFEB0" border="0" align="center">%s</td></tr></table>' % (j, els))
        s += 'node%d [color="#444443", fontname="Helvetica", margin="0.01", space="0.0", shape=record label=<{%s}>];\n' % (i, '|'.join(elements))

    # Do edges
    for i in range(len(table)):
        bucket = table[i]
        if not bucket or len(bucket)==0: continue
        s += 'mainlist:f%d -> node%d [arrowsize=.5]\n' % (i,i)
    s += "}\n"
    print s
    return s

x = [ [('a','3')], [], [('b',230), ('c',21)] ]
dot = lolviz(x)
g = graphviz.Source(dot)
g.render(view=True)