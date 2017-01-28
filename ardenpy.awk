#!/usr/bin/gawk

BEGIN {
  # Initialize program state
  context = ""
  IGNORECASE = 1
  OFS = " "
}

# Change comments into Python style
## Single-line C++ style (//)
# The following cannot catch the case where '//' occurs in a multi-line comment
#{sub("\/\/", $0)}
## Multi-line C style (/* */)

/^\s*maintenance:\s*$/ {
  context = "maintenance"
}

match($0, "^\\s*title:\\s*([^\n]*);;\\s*$", a) {
  print "title = " "\"" a[1] "\""
}

match($0, "^\\s*mlmname:\\s*([a-zA-Z]?[a-zA-Z0-9.-_]{0,79});;\\s*$", a) {
  print "mlmname = " "\"" a[1] "\""
}
match($0, "^\\s*filename:\\s*([a-zA-Z]?[a-zA-Z0-9.-_]{0,79});;\\s*$", a) {
  print "filename = " "\"" a[1] "\""
}

match($0, "^\\s*arden:\\s*version\\s*([0-9.]*);;\\s*$", a) {
  print "arden = " "\"" a[1] "\""
}

match($0, "^\\s*version:\\s*([0-9.]*);;\\s*$", a) {
  print "version = " "\"" a[1] "\""
}

match($0, "^\\s*institution:\\s*([^\n]{0,80});;\\s*$", a) {
  print "institution = " "\"" a[1] "\""
}

match($0, "^\\s*author:\\s*([^\n]*?);;\\s*$", a) {
  print "author = ["
  split(a[1], b, ";\\s*")
  l = length(b)
  for (i=1;i<=l;i++) {
    print b[i] ","
  }
  print "]"
}

match($0, "^\\s*specialist:\\s*([^\n]*?);;\\s*$", a) {
  print "specialist = ["
  split(a[1], b, ";\\s*")
  l = length(b)
  for (i=1;i<=l;i++) {
    print b[i] ","
  }
  print "]"
}