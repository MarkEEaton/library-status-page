from flask import Flask, render_template
import httpx

app = Flask(__name__)

services = [
    {
        'name': 'Kingsborough library website',
        'url': 'https://library.kbcc.cuny.edu/homepage',
        'status': None,
    },
    {
        'name': 'ILLiad',
        'url': 'https://kbcc-cuny.illiad.oclc.org/illiad/logon.html',
        'status': None,
    },
    {
        'name': 'EZproxy',
        'url': 'https://kbcc.ezproxy.cuny.edu/login',
        'status': None,
    },
    {
        'name': '17th and 18th Century Burney Collection (British Newspapers)',
        'url': 'https://link.gale.com/apps/BBCN',
        'status': None,
    },
    {
        'name': '18th Century Collections Online',
        'url': 'https://link.gale.com/apps/ECCO',
        'status': None,
    },
    {
        'name': '19th Century Collections Online (NCCO)',
        'url': 'https://link.gale.com/apps/NCCO',
        'status': None,
    },
    {
        'name': 'Academic Search Complete',
        'url': 'https://library.kbcc.cuny.edu/academic-search-complete',
        'status': None,
    },
    {
        'name': 'Academic Video Online (AVON)',
        'url': 'https://video.alexanderstreet.com/channel/academic-video-online',
        'status': None,
    },
    {
        'name': 'Air & Space/Smithsonian Magazines Archive 1986-Present',
        'url': 'https://link.gale.com/apps/SMIT',
        'status': None,
    },
    {
        'name': 'American Chemical Society',
        'url': 'http://pubs.acs.org/',
        'status': None,
    },
    {
        'name': 'American College of Sports Medicine (ACSM)',
        'url': 'http://www.acsm.org',
        'status': None,
    },
    {
        'name': 'American Council on Exercise (ACE)',
        'url': 'https://www.acefitness.org/',
        'status': None,
    },
    {
        'name': 'American History Online',
        'url': 'http://online.infobaselearning.com/Direct.aspx',
        'status': None,
    },
    {
        'name': 'American Journal of Clinical Nutrition',
        'url': 'http://ajcn.nutrition.org/',
        'status': None,
    },
    {
        'name': 'American Psychological Association (APA) E-books & Handbooks',
        'url': 'http://psycnet.apa.org/bookcollections/topic/b,h/',
        'status': None,
    },
    {
        'name': 'APA Style Guide from Purdue Online Writing Lab',
        'url': 'https://owl.english.purdue.edu/owl/section/2/10/',
        'status': None,
    },
    {
        'name': 'Biography And Genealogy Master Index',
        'url': 'https://link.gale.com/apps/BGMI',
        'status': None,
    },
    {
        'name': 'Biography In Context',
        'url': 'https://link.gale.com/apps/BIC',
        'status': None,
    },
    {
        'name': 'Black Thought and Culture',
        'url': 'http://bltc.alexanderstreet.com/',
        'status': None,
    },
    {
        'name': 'Bloomsbury Drama Online',
        'url': ' https://www.dramaonlinelibrary.com',
        'status': None,
    },
    {
        'name': 'Book Review Index Plus',
        'url': 'https://link.gale.com/apps/BRIP',
        'status': None,
    },
    {
        'name': 'Brooklyn Newsstand',
        'url': 'http://bklyn.newspapers.com/',
        'status': None,
    },
    {
        'name': 'Business Insights',
        'url': 'https://link.gale.com/apps/BIE',
        'status': None,
    },
    {
        'name': 'Business Insights: Global',
        'url': 'https://link.gale.com/apps/BIG',
        'status': None,
    },
    {
        'name': 'Business Source Complete - Enhanced',
        'url': 'http://search.epnet.com/login.aspx',
        'status': None,
    },
    {
        'name': 'Career Cruising',
        'url': 'https://www.careercruising.com/home/autologin.aspx',
        'status': None,
    },
    {
        'name': 'EBSCO (all)',
        'url': 'https://search.ebscohost.com/login.aspx',
        'status': None,
    },
]

@app.route('/')
def index():
    for service in services:
        try:
            response = httpx.get(service['url'])
            service['status'] = response.status_code
        except:
            service['status'] = 500

    print(services)
    return render_template('index.html', services=services)

if __name__ == "__main__":
    app.run(port=8000, host="127.0.0.1")
