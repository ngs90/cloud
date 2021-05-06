from flask import Flask, render_template, request
import app_charts
import named_entity_recognition as ner
from flaskext.markdown import Markdown

#create the object of Flask
app  = Flask(__name__)
Markdown(app)

app.config['SECRET_KEY'] = 'hardsecretkeymuchfun'

@app.route('/')
def text_form():
    return render_template('form.html')
 

HTML_WRAPPER = """<div style="overflow-x: auto; border: 3px solid #e6e9ef; border-radius: 0.75rem; padding: 1rem">{}</div>"""

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text_field']
    value = request.form['value_field']
    try:
        value = int(value)
    except:
        value = 1
    processed_text = text #.upper() 

    # generate some charts
    #script, div = app_charts.chart(bars_count=value)
  
    # find some entities 
    ent_sm = ner.entities(text=text, nlp_model='en_core_web_sm')
    ent_trf = ner.entities(text=text, nlp_model='en_core_web_trf') # md

    
    ent_sm, ent_trf = ent_sm.replace("\n\n","\n"), ent_trf.replace("\n\n","\n")
    ent_sm, ent_trf = HTML_WRAPPER.format(ent_sm), HTML_WRAPPER.format(ent_trf)


 
    return render_template('chart_insert.html', 
                           bars_count=value,
                           #the_div=div, the_script=script, 
                           # text=processed_text,
                           ner_ent_sm=ent_sm, ner_ent_trf=ent_trf)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)
 