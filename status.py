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
        'url': 'https://psycnet-apa-org.kbcc.ezproxy.cuny.edu/search',
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
        'name': 'Career Cruising',
        'url': 'https://www.careercruising.com/home/autologin.aspx',
        'status': None,
    },
    {
        'name': 'Centers for Disease Control and Prevention (CDC)',
        'url': 'http://www.cdc.gov/',
        'status': None,
    },
    {
        'name': 'Chicago Manual of Style at Purdue Online Writing Lab',
        'url': 'https://owl.english.purdue.edu/owl/resource/717/01/',
        'status': None,
    },
    {
        'name': 'Chronicle of Higher Education',
        'url': 'http://chronicle.com/',
        'status': None,
    },
    {
        'name': 'Chronicle of Philanthropy',
        'url': 'http://philanthropy.com/',
        'status': None,
    },
    {
        'name': 'CIAO (Columbia International Affairs Online)',
        'url': 'http://www.ciaonet.org/',
        'status': None,
    },
    {
        'name': 'CollegeBoard.com',
        'url': 'https://bigfuture.collegeboard.org/college-search',
        'status': None,
    },
    {
        'name': 'Congress and the Nation',
        'url': 'http://knowledge.sagepub.com/searchresults',
        'status': None,
    },
    {
        'name': 'Contemporary Women\'s Issues',
        'url': 'https://link.gale.com/apps/CWI',
        'status': None,
    },
    {
        'name': 'CQ Researcher',
        'url': 'https://library.cqpress.com/cqresearcher/',
        'status': None,
    },
    {
        'name': 'Criminal Justice Database',
        'url': 'https://search.proquest.com/criminaljusticeperiodicals',
        'status': None,
    },
    {
        'name': 'CUNY Academic Works',
        'url': 'https://academicworks.cuny.edu/',
        'status': None,
    },
    {
        'name': 'CUNY Digital History Archive (CDHA)',
        'url': 'http://cdha.cuny.edu/',
        'status': None,
    },
    {
        'name': 'Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition',
        'url': 'http://dsm.psychiatryonline.org/doi/book/10.1176/appi.books.9780890425596',
        'status': None,
    },
    {
        'name': 'Dictionary of Literary Biography Complete Online',
        'url': 'https://link.gale.com/apps/DLBC',
        'status': None,
    },
    {
        'name': 'Digital Public Library of America',
        'url': 'https://dp.la/',
        'status': None,
    },
    {
        'name': 'Digital Theatre Plus',
        'url': 'https://edu.digitaltheatreplus.com/',
        'status': None,
    },
    {
        'name': 'Dissertations: CUNY Graduate Center Legacy (Retrospective) Dissertations, 1965-2014',
        'url': 'http://library.gc.cuny.edu/legacy/collections/browse',
        'status': None,
    },
    {
        'name': 'DOAJ: Directory of Open Access Journals',
        'url': 'https://doaj.org/',
        'status': None,
    },
    {
        'name': 'Drama Online - National Theatre Collections 1 & 2',
        'url': 'https://www.dramaonlinelibrary.com/national-theatre-collection',
        'status': None,
    },
    {
        'name': 'EasyBib',
        'url': 'http://www.easybib.com/',
        'status': None,
    },
    {
        'name': 'Ebook Central',
        'url': 'https://ebookcentral.proquest.com/lib/kbcc-ebooks/search.action',
        'status': None,
    },
    {
        'name': 'EBSCO (all)',
        'url': 'https://search.ebscohost.com/login.aspx',
        'status': None,
    },
    {
        'name': 'Economist',
        'url': 'https://link.gale.com/apps/ECON',
        'status': None,
    },
    {
        'name': 'Encyclopedia Britannica Online',
        'url': 'https://academic.eb.com/levels/collegiate',
        'status': None,
    },
    {
        'name': 'Ethinc Newswatch',
        'url': 'https://search.proquest.com/ethnicnewswatch',
        'status': None,
    },
    {
        'name': 'Exercise and Sports Sciences Reviews',
        'url': 'http://journals.lww.com/acsm-essr/pages/issuelist.aspx',
        'status': None,
    },
    {
        'name': 'Financial Times Historical Archive, 1888-2010',
        'url': 'https://link.gale.com/apps/FTHA',
        'status': None,
    },
    {
        'name': 'Foreign Policy',
        'url': 'http://foreignpolicy.com',
        'status': None,
    },
    {
        'name': 'Gale Academic OneFile',
        'url': 'https://link.gale.com/apps/AONE',
        'status': None,
    },
    {
        'name': 'Gale eBooks',
        'url': 'https://link.gale.com/apps/GVRL',
        'status': None,
    },
    {
        'name': 'Gale General OneFile',
        'url': 'https://link.gale.com/apps/ITOF',
        'status': None,
    },
    {
        'name': 'Gale Interactive: Chemistry',
        'url': 'https://link.gale.com/apps/ICHEM',
        'status': None,
    },
    {
        'name': 'Gale Interactive: Human Anatomy',
        'url': 'http://cyber.galegroup.com/cyber/IANAT',
        'status': None,
    },
    {
        'name': 'Gale Literature',
        'url': 'https://link.gale.com/apps/GLS',
        'status': None,
    },
    {
        'name': 'Gale OneFile Diversity Studies',
        'url': 'https://link.gale.com/apps/PPDS',
        'status': None,
    },
    {
        'name': 'Gale OneFile: Science',
        'url': 'https://link.gale.com/apps/PPGS',
        'status': None,
    },
    {
        'name': 'Gale Primary Sources',
        'url': 'https://link.gale.com/apps/GDCS',
        'status': None,
    },
    {
        'name': 'Gale Small Business Builder',
        'url': 'https://app.dezinersoftware.com/library',
        'status': None,
    },
    {
        'name': 'Gartner IT Research',
        'url': 'https://ssofed.gartner.com/sp/startSSO.ping',
        'status': None,
    },
    {
        'name': 'Geoportal',
        'url': 'http://www.baruch.cuny.edu/geoportal/',
        'status': None,
    },
    {
        'name': 'Gerontologist',
        'url': 'https://academic.oup.com/gerontologist',
        'status': None,
    },
    {
        'name': 'Gerontology, The Journals of, Series A',
        'url': 'https://academic.oup.com/biomedgerontology',
        'status': None,
    },
    {
        'name': 'Global Issues in Context',
        'url': 'https://link.gale.com/apps/GIC',
        'status': None,
    },
    {
        'name': 'GrantForward Database',
        'url': 'https://www.grantforward.com/index',
        'status': None,
    },
    {
        'name': 'GREENR (Global Reference On The Environment/Energy/And Natural Resources)',
        'url': 'https://link.gale.com/apps/GRNR',
        'status': None,
    },
    {
        'name': 'Health & Wellness Resource Center',
        'url': 'https://link.gale.com/apps/HWRC',
        'status': None,
    },
    {
        'name': 'Health and Environmental Studies: Archives Unbound',
        'url': 'https://link.gale.com/apps/GDSC',
        'status': None,
    },
    {
        'name': 'Health Reference Center Academic',
        'url': 'https://link.gale.com/apps/HRCA',
        'status': None,
    },
    {
        'name': 'Highwire Press',
        'url': 'http://highwire.stanford.edu/',
        'status': None,
    },
    {
        'name': 'Historic American Newspapers',
        'url': 'http://chroniclingamerica.loc.gov/',
        'status': None,
    },
    {
        'name': 'Historical New York Times - 1851 to 2016',
        'url': 'https://search.proquest.com/hnpnewyorktimes',
        'status': None,
    },
    {
        'name': 'Holocaust Archives: Archives Unbound',
        'url': 'https://link.gale.com/apps/GDSC',
        'status': None,
    },
    {
        'name': 'ICPSR ( Inter-university Consortium for Political and Social Research)',
        'url': 'http://www.icpsr.umich.edu/icpsrweb/ICPSR/',
        'status': None,
    },
    {
        'name': 'IEEE Xplore Digital Library',
        'url': 'http://www.ieee.org/ieeexplore',
        'status': None,
    },
    {
        'name': 'Infoshare',
        'url': 'http://www.infoshare.org/',
        'status': None,
    },
    {
        'name': 'InfoTrac Newsstand',
        'url': 'https://link.gale.com/apps/STND',
        'status': None,
    },
    {
        'name': 'JAMA',
        'url': 'https://jamanetwork.com/journals/jama',
        'status': None,
    },
    {
        'name': 'JSTOR',
        'url': 'http://www.jstor.org/',
        'status': None,
    },
    {
        'name': 'Kanopy',
        'url': 'https://kbcccuny.kanopy.com/',
        'status': None,
    },
    {
        'name': 'KnightCite',
        'url': 'https://www.calvin.edu/library/knightcite/',
        'status': None,
    },
    {
        'name': 'LegalTrac',
        'url': 'https://link.gale.com/apps/LT',
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
