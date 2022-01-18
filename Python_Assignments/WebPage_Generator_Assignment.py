

import webbrowser
x = 'WebPage_Generator_for_Python_Assignment.html'
#creating html file
f = open(x, "w")
f.write('''<!DOCTYPE html>
<html>
    <body>
        <h1>
    Stay tuned for our amazing summer sale!
        </h1>
    </body>

</html>''')
f.close()

#opening file thru py command

webbrowser.open_new_tab(x)
