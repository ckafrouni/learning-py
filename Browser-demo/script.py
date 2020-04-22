from browser import document, console, alert
from browser.template import Template

#script 0
def show(e):
    console.log(e)
    alert('Hello World')
    document['hello'] <= 'Hello World'

document['alert-btn'].bind('click', show)

#script 1
def show_text(e):
    document['output'].textContent = e.target.value

document['text'].bind('input', show_text)

#script 2
Template(document['greet']).render(name="James")