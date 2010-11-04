
# gordian-minifier

Automatic hardcore minification is a hard problem, especially when you want to jointly minify muiltiple types of things (e.g. a large set of JavaScript and CSS and HTML files).

gordian-minifier [slices that knot](http://duckduckgo.com/?q=Gordian+knot) by simply using a regex.

Each name that matches a regex is replaced by the shortest available alphabetic string not occuring anywhere in the code so far.

This is done in order of long-name frequency, so your most frequent long names get dibs on the shortest available strings.

## Long-name Exemptions
You can explicitly exempt some long names from being minified.

## Minifying Multiple Files
Your build script can concatenate them, use <code>findMapping</code>, and apply that mapping to each file.


## Python usage

<pre>
from gordian_minifier import minify, findMapping

# This
code = minify(code, regex=..., exemptions=[...])

# ...is equivalent to this
mapping = findMapping(code, regex=..., exemptions=[...])
for src, dest in mapping.items():
  code = code.replace(src, dest)
</pre>

## Command-line usage

<pre>... | python gordian-minifier.py | ...</pre>

<pre>... | python gordian-minifier.py
                        --regex=...
                        --exemptions=_foo,_bar,... | ...</pre>

## Default Regex

<pre>DEFAULT_REGEX = r'''(?x)
    [^a-zA-Z_](
        (?:_[a-zA-Z0-9_]+)|
        (?:[a-zA-Z_][a-zA-Z0-9_]*_CSS))'''</pre>

<pre>_example</pre>
<pre>AnotherExample_innerDiv_CSS</pre>