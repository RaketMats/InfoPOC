#!python2
import sys
import io

script, filename = sys.argv

print "We're going to erase %s." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ").decode(sys.stdin.encoding)
line2 = raw_input("line 2: ").decode(sys.stdin.encoding)
line3 = raw_input("line 3: ").decode(sys.stdin.encoding)

print "I'm going to write these to the file."

with io.open(filename, 'wt', encoding='utf8') as target:
    target.write(u"%s\n%s\n%s\n" % (line1, line2, line3))
