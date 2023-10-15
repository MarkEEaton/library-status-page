from flask import Flask, render_template
import httpx

app = Flask(__name__)

services = [
    {
        'name': 'Kingsborough library website',
        'url': 'https://library.kbcc.cuny.edu/homepage',
    },
    {
        'name': 'ILLiad',
        'url': 'https://kbcc-cuny.illiad.oclc.org/illiad/logon.html',
    },
    {
        'name': 'EZproxy',
        'url': 'https://kbcc.ezproxy.cuny.edu/login',
    },
    {
        'name': '17th and 18th Century Burney Collection (British Newspapers)',
        'url': 'https://link.gale.com/apps/BBCN',
    },
    {
        'name': '18th Century Collections Online',
        'url': 'https://link.gale.com/apps/ECCO',
    },
    {
        'name': '19th Century Collections Online (NCCO)',
        'url': 'https://link.gale.com/apps/NCCO',
    },
    {
        'name': 'Academic Search Complete',
        'url': 'https://library.kbcc.cuny.edu/academic-search-complete',
    },
    {
        'name': 'Academic Video Online (AVON)',
        'url': 'https://video.alexanderstreet.com/channel/academic-video-online',
    },
    {
        'name': 'Air & Space/Smithsonian Magazines Archive 1986-Present',
        'url': 'https://link.gale.com/apps/SMIT',
    },
    {
        'name': 'American Chemical Society',
        'url': 'http://pubs.acs.org/',
    },
    {
        'name': 'American College of Sports Medicine (ACSM)',
        'url': 'http://www.acsm.org',
    },
    {
        'name': 'American Council on Exercise (ACE)',
        'url': 'https://www.acefitness.org/',
    },
    {
        'name': 'American History Online',
        'url': 'http://online.infobaselearning.com/Direct.aspx',
    },
    {
        'name': 'American Journal of Clinical Nutrition',
        'url': 'http://ajcn.nutrition.org/',
    },
    {
        'name': 'American Psychological Association (APA) E-books & Handbooks',
        'url': 'https://psycnet-apa-org.kbcc.ezproxy.cuny.edu/search',
    },
    {
        'name': 'APA Style Guide from Purdue Online Writing Lab',
        'url': 'https://owl.english.purdue.edu/owl/section/2/10/',
    },
    {
        'name': 'Biography And Genealogy Master Index',
        'url': 'https://link.gale.com/apps/BGMI',
    },
    {
        'name': 'Biography In Context',
        'url': 'https://link.gale.com/apps/BIC',
    },
    {
        'name': 'Black Thought and Culture',
        'url': 'http://bltc.alexanderstreet.com/',
    },
    {
        'name': 'Book Review Index Plus',
        'url': 'https://link.gale.com/apps/BRIP',
    },
    {
        'name': 'Brooklyn Newsstand',
        'url': 'http://bklyn.newspapers.com/',
    },
    {
        'name': 'Business Insights',
        'url': 'https://link.gale.com/apps/BIE',
    },
    {
        'name': 'Business Insights: Global',
        'url': 'https://link.gale.com/apps/BIG',
    },
    {
        'name': 'Career Cruising',
        'url': 'https://www.careercruising.com/home/autologin.aspx',
    },
    {
        'name': 'Centers for Disease Control and Prevention (CDC)',
        'url': 'http://www.cdc.gov/',
    },
    {
        'name': 'Chicago Manual of Style at Purdue Online Writing Lab',
        'url': 'https://owl.english.purdue.edu/owl/resource/717/01/',
    },
    {
        'name': 'Chronicle of Higher Education',
        'url': 'http://chronicle.com/',
    },
    {
        'name': 'Chronicle of Philanthropy',
        'url': 'http://philanthropy.com/',
    },
    {
        'name': 'CIAO (Columbia International Affairs Online)',
        'url': 'http://www.ciaonet.org/',
    },
    {
        'name': 'CollegeBoard.com',
        'url': 'https://bigfuture.collegeboard.org/college-search',
    },
    {
        'name': 'Congress and the Nation',
        'url': 'http://knowledge.sagepub.com/searchresults',
    },
    {
        'name': 'Contemporary Women\'s Issues',
        'url': 'https://link.gale.com/apps/CWI',
    },
    {
        'name': 'CQ Researcher',
        'url': 'https://library.cqpress.com/cqresearcher/',
    },
    {
        'name': 'Criminal Justice Database',
        'url': 'https://search.proquest.com/criminaljusticeperiodicals',
    },
    {
        'name': 'CUNY Academic Works',
        'url': 'https://academicworks.cuny.edu/',
    },
    {
        'name': 'CUNY Digital History Archive (CDHA)',
        'url': 'http://cdha.cuny.edu/',
    },
    {
        'name': 'Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition',
        'url': 'http://dsm.psychiatryonline.org/doi/book/10.1176/appi.books.9780890425596',
    },
    {
        'name': 'Dictionary of Literary Biography Complete Online',
        'url': 'https://link.gale.com/apps/DLBC',
    },
    {
        'name': 'Digital Public Library of America',
        'url': 'https://dp.la/',
    },
    {
        'name': 'Digital Theatre Plus',
        'url': 'https://edu.digitaltheatreplus.com/',
    },
    {
        'name': 'Dissertations: CUNY Graduate Center Legacy (Retrospective) Dissertations, 1965-2014',
        'url': 'http://library.gc.cuny.edu/legacy/collections/browse',
    },
    {
        'name': 'DOAJ: Directory of Open Access Journals',
        'url': 'https://doaj.org/',
    },
    {
        'name': 'Drama Online - National Theatre Collections 1 & 2',
        'url': 'https://www.dramaonlinelibrary.com/national-theatre-collection',
    },
    {
        'name': 'EasyBib',
        'url': 'http://www.easybib.com/',
    },
    {
        'name': 'Ebook Central',
        'url': 'https://ebookcentral.proquest.com/lib/kbcc-ebooks/search.action',
    },
    {
        'name': 'EBSCO (all)',
        'url': 'https://search.ebscohost.com/login.aspx',
    },
    {
        'name': 'Economist',
        'url': 'https://link.gale.com/apps/ECON',
    },
    {
        'name': 'Encyclopedia Britannica Online',
        'url': 'https://academic.eb.com/levels/collegiate',
    },
    {
        'name': 'Ethinc Newswatch',
        'url': 'https://search.proquest.com/ethnicnewswatch',
    },
    {
        'name': 'Exercise and Sports Sciences Reviews',
        'url': 'http://journals.lww.com/acsm-essr/pages/issuelist.aspx',
    },
    {
        'name': 'Financial Times Historical Archive, 1888-2010',
        'url': 'https://link.gale.com/apps/FTHA',
    },
    {
        'name': 'Foreign Policy',
        'url': 'http://foreignpolicy.com',
    },
    {
        'name': 'Gale Academic OneFile',
        'url': 'https://link.gale.com/apps/AONE',
    },
    {
        'name': 'Gale eBooks',
        'url': 'https://link.gale.com/apps/GVRL',
    },
    {
        'name': 'Gale General OneFile',
        'url': 'https://link.gale.com/apps/ITOF',
    },
    {
        'name': 'Gale Interactive: Chemistry',
        'url': 'https://link.gale.com/apps/ICHEM',
    },
    {
        'name': 'Gale Interactive: Human Anatomy',
        'url': 'http://cyber.galegroup.com/cyber/IANAT',
    },
    {
        'name': 'Gale Literature',
        'url': 'https://link.gale.com/apps/GLS',
    },
    {
        'name': 'Gale OneFile Diversity Studies',
        'url': 'https://link.gale.com/apps/PPDS',
    },
    {
        'name': 'Gale OneFile: Science',
        'url': 'https://link.gale.com/apps/PPGS',
    },
    {
        'name': 'Gale Primary Sources',
        'url': 'https://link.gale.com/apps/GDCS',
    },
    {
        'name': 'Gale Small Business Builder',
        'url': 'https://app.dezinersoftware.com/library',
    },
    {
        'name': 'Gartner IT Research',
        'url': 'https://ssofed.gartner.com/sp/startSSO.ping',
    },
    {
        'name': 'Geoportal',
        'url': 'http://www.baruch.cuny.edu/geoportal/',
    },
    {
        'name': 'Gerontologist',
        'url': 'https://academic.oup.com/gerontologist',
    },
    {
        'name': 'Gerontology, The Journals of, Series A',
        'url': 'https://academic.oup.com/biomedgerontology',
    },
    {
        'name': 'Global Issues in Context',
        'url': 'https://link.gale.com/apps/GIC',
    },
    {
        'name': 'GrantForward Database',
        'url': 'https://www.grantforward.com/index',
    },
    {
        'name': 'GREENR (Global Reference On The Environment/Energy/And Natural Resources)',
        'url': 'https://link.gale.com/apps/GRNR',
    },
    {
        'name': 'Health & Wellness Resource Center',
        'url': 'https://link.gale.com/apps/HWRC',
    },
    {
        'name': 'Health and Environmental Studies: Archives Unbound',
        'url': 'https://link.gale.com/apps/GDSC',
    },
    {
        'name': 'Health Reference Center Academic',
        'url': 'https://link.gale.com/apps/HRCA',
    },
    {
        'name': 'Highwire Press',
        'url': 'http://highwire.stanford.edu/',
    },
    {
        'name': 'Historic American Newspapers',
        'url': 'http://chroniclingamerica.loc.gov/',
    },
    {
        'name': 'Historical New York Times - 1851 to 2016',
        'url': 'https://search.proquest.com/hnpnewyorktimes',
    },
    {
        'name': 'Holocaust Archives: Archives Unbound',
        'url': 'https://link.gale.com/apps/GDSC',
    },
    {
        'name': 'ICPSR ( Inter-university Consortium for Political and Social Research)',
        'url': 'http://www.icpsr.umich.edu/icpsrweb/ICPSR/',
    },
    {
        'name': 'IEEE Xplore Digital Library',
        'url': 'http://www.ieee.org/ieeexplore',
    },
    {
        'name': 'Infoshare',
        'url': 'http://www.infoshare.org/',
    },
    {
        'name': 'InfoTrac Newsstand',
        'url': 'https://link.gale.com/apps/STND',
    },
    {
        'name': 'JAMA',
        'url': 'https://jamanetwork.com/journals/jama',
    },
    {
        'name': 'JSTOR',
        'url': 'http://www.jstor.org/',
    },
    {
        'name': 'Kanopy',
        'url': 'https://kbcccuny.kanopy.com/',
    },
    {
        'name': 'KnightCite',
        'url': 'https://www.calvin.edu/library/knightcite/',
    },
    {
        'name': 'LegalTrac',
        'url': 'https://link.gale.com/apps/LT',
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
