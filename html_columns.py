#!/bin/python

# input a text file sepiarated by blank lines
# output an html file with the text divided into columns
# we want to keep tyhe oriinal file lines

def read_it(filename):
    pieces = []
    apiece = ""
    with open(filename) as f:
        lines = f.readlines()
    for aline in lines:
        if aline.rstrip() == "":
            if len(apiece):
                pieces.append(apiece)
                apiece = ""
        else:
            apiece = apiece + aline.rstrip() + "<br/>\n"
    if len(apiece):
        pieces.append(apiece)
    #print("last piece", pieces[-1]) 
    return pieces


def outname(name):
    where = name.index('.')
    return name[0:where] + ".html"


def write_it(outname, pieces, columns):
    ii = 0
    unclosed = False
    with open(outname, "w") as outfile:
        outfile.write("<html>")
        outfile.write("<table>")
        for apiece in pieces:
            if ii % columns == 0:
                outfile.write("<tr>\n")
                unclosed = True
            outfile.write("<td>")
            outfile.write(apiece)
            outfile.write("</td>\n")
            if ii % columns == columns - 1:
                outfile.write("</tr>\n")
                unclosed = False
            ii += 1
        if unclosed:
            outfile.write("</tr>\n")
        outfile.write("</table>")
        outfile.write("</html>")

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--columns', type=int, default=3)
    parser.add_argument('--input', help='name of input file')
    parser.add_argument('--output', help='name of output file', default=None)
    args = parser.parse_args()
    if args.output:
        output_name = args.output
    else:
        output_name = outname(args.input)
    pieces = read_it(args.input)
    write_it(output_name, pieces, columns=args.columns)


