from flask import Flask, request, render_template
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import webbrowser
import threading

app = Flask(__name__)

codes_to_names = {
    'themes/1247874246': 'ثيم رائد',
    'themes/568597563': 'ثيم نمو',
    'themes/2038173539': 'ثيم واثق',
    'themes/404046066': 'ثيم فريد',
    'themes/392563753': 'ثيم زين',
    'themes/766360058': 'ثيم فخامة',
    'themes/1617628556': 'ثيم امتياز',
    'themes/1034648396': 'ثيم ملاك',
    'themes/1696219221': 'ثيم وسام',
    'themes/197173496': 'ثيم مختلف',
    'themes/575338046': 'ثيم زاهر',
    'themes/513499943': 'ثيم بريستيج',
    'themes/268429610': 'ثيم مختلف',
    'themes/1245464956': 'ثيم جميل',
    'themes/1049159835': 'ثيم موعد',
    'themes/600639717': 'ثيم كليك',
    'themes/466157229': 'ثيم اكاسيا',
    'themes/2048178472': 'ثيم بيوتى',
    'themes/1480248829': 'ثيم متجر',
    'themes/2101895899': 'ثيم رهيب',
    'themes/1894368909': 'ثيم اطلالة',
    'themes/1974201424': 'ثيم روية',
    'themes/1660707346': 'ثيم رقمى',
    'themes/581928698': 'ثيم سـيليا',
    'themes/1753517624': 'ثيم عالي',
    'themes/1755865368 ': 'ثيم بوتيك',
    'themes/1974201424': 'ثيم رؤية',
    'themes/466157229': 'ثيم أكاسيا',
    'themes/268429610': 'ثيم نور',
    'themes/1253916907': 'ثيم تالا',
    'themes/724522601': 'ثيم مبدع',
    'themes/2048178472': 'ثيم بيوتي',
    'themes/1048198927': 'ثيم شوبنج',
    'themes/2093313756': 'ثيم يافا',
    'themes/2142196958': 'ثيم بريق',
    'themes/1016570170': 'ثيم علا',
    'themes/2071596307': 'ثيم جلامور',
    'themes/1485429532': 'ثيم ريس',
    'themes/539684003': 'ثيم خطوه',
    'themes/1462103872': 'ثيم قصص',
    'themes/1145699248': 'ثيم كراون',
    'themes/338190499': 'ثيم كيان',
    'themes/1582624105': 'ثيم لوفيزا',
    'themes/368921700': 'ثيم نماء',
    'themes/1662840947': 'ثيم ماركت',
    'themes/245671147': 'ثيم روح',
    'themes/822457965': 'ثيم عطاء',
    'themes/1546328629': 'ثيم سمارت',
    'themes/0000000': 'ثيم 00000'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    url = request.form['url']

    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    page_source = driver.page_source
    driver.quit()

    found_names = [name for code, name in codes_to_names.items() if code in page_source]

    return render_template('index.html', result=found_names)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000')

if __name__ == '__main__':
    threading.Timer(1.25, open_browser).start()
    app.run(debug=True)
