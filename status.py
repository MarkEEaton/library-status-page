from quart import Quart, render_template
import httpx
import asyncio

app = Quart(__name__)

services = [
    {
        'name': 'Kingsborough library website',
        'url': 'https://library.kbcc.cuny.edu/homepage',
        'proxy': False,
    },
    {
        'name': 'Primo',
        'url': 'https://cuny-kb.primo.exlibrisgroup.com/discovery/search?tab=Everything&vid=01CUNY_KB:CUNY_KB&lang=en',
        'proxy': False,
    },
    {
        'name': 'ILLiad',
        'url': 'https://kbcc-cuny.illiad.oclc.org/illiad/logon.html',
        'proxy': False,
    },
    {
        'name': 'EZproxy',
        'url': 'https://kbcc.ezproxy.cuny.edu/login',
        'proxy': False,
    },
    {
        'name': '17th and 18th Century Burney Collection (British Newspapers)',
        'url': 'https://link.gale.com/apps/BBCN',
        'proxy': True,
    },
    {
        'name': '18th Century Collections Online',
        'url': 'https://link.gale.com/apps/ECCO',
        'proxy': True,
    },
    {
        'name': '19th Century Collections Online (NCCO)',
        'url': 'https://link.gale.com/apps/NCCO',
        'proxy': True,
    },
    {
        'name': 'Academic Search Complete',
        'url': 'https://library.kbcc.cuny.edu/academic-search-complete',
        'proxy': True,
    },
    {
        'name': 'Academic Video Online (AVON)',
        'url': 'https://video.alexanderstreet.com/channel/academic-video-online',
        'proxy': True,
    },
    {
        'name': 'Air & Space/Smithsonian Magazines Archive 1986-Present',
        'url': 'https://link.gale.com/apps/SMIT',
        'proxy': True,
    },
    {
        'name': 'American Chemical Society',
        'url': 'http://pubs.acs.org/',
        'proxy': True,
    },
    {
        'name': 'American College of Sports Medicine (ACSM)',
        'url': 'http://www.acsm.org',
        'proxy': False,
    },
    {
        'name': 'American Council on Exercise (ACE)',
        'url': 'https://www.acefitness.org/',
        'proxy': False,
    },
    {
        'name': 'American History Online',
        'url': 'http://online.infobaselearning.com/Direct.aspx',
        'proxy': True,
    },
    {
        'name': 'American Journal of Clinical Nutrition',
        'url': 'http://ajcn.nutrition.org/',
        'proxy': True,
    },
    {
        'name': 'American Psychological Association (APA) E-books & Handbooks',
        'url': 'https://psycnet-apa-org.kbcc.ezproxy.cuny.edu/search',
        'proxy': True,
    },
    {
        'name': 'APA Style Guide from Purdue Online Writing Lab',
        'url': 'https://owl.english.purdue.edu/owl/section/2/10/',
        'proxy': False,
    },
    {
        'name': 'Biography And Genealogy Master Index',
        'url': 'https://link.gale.com/apps/BGMI',
        'proxy': True,
    },
    {
        'name': 'Biography In Context',
        'url': 'https://link.gale.com/apps/BIC',
        'proxy': True,
    },
    {
        'name': 'Black Thought and Culture',
        'url': 'http://bltc.alexanderstreet.com/',
        'proxy': True,
    },
    {
        'name': 'Book Review Index Plus',
        'url': 'https://link.gale.com/apps/BRIP',
        'proxy': True,
    },
    {
        'name': 'Brooklyn Newsstand',
        'url': 'http://bklyn.newspapers.com/',
        'proxy': False,
    },
    {
        'name': 'Business Insights',
        'url': 'https://link.gale.com/apps/BIE',
        'proxy': True,
    },
    {
        'name': 'Business Insights: Global',
        'url': 'https://link.gale.com/apps/BIG',
        'proxy': True,
    },
    {
        'name': 'Career Cruising',
        'url': 'https://www.careercruising.com/home/autologin.aspx',
        'proxy': True,
    },
    {
        'name': 'Centers for Disease Control and Prevention (CDC)',
        'url': 'http://www.cdc.gov/',
        'proxy': False,
    },
    {
        'name': 'Chicago Manual of Style at Purdue Online Writing Lab',
        'url': 'https://owl.english.purdue.edu/owl/resource/717/01/',
        'proxy': False,
    },
    {
        'name': 'Chronicle of Higher Education',
        'url': 'http://chronicle.com/',
        'proxy': True,
    },
    {
        'name': 'Chronicle of Philanthropy',
        'url': 'http://philanthropy.com/',
        'proxy': True,
    },
    {
        'name': 'CIAO (Columbia International Affairs Online)',
        'url': 'http://www.ciaonet.org/',
        'proxy': True,
    },
    {
        'name': 'CollegeBoard.com',
        'url': 'https://bigfuture.collegeboard.org/college-search',
        'proxy': False,
    },
    {
        'name': 'Congress and the Nation',
        'url': 'http://knowledge.sagepub.com/searchresults',
        'proxy': True,
    },
    {
        'name': 'Contemporary Women\'s Issues',
        'url': 'https://link.gale.com/apps/CWI',
        'proxy': True,
    },
    {
        'name': 'CQ Researcher',
        'url': 'https://library.cqpress.com/cqresearcher/',
        'proxy': True,
    },
    {
        'name': 'Criminal Justice Database',
        'url': 'https://search.proquest.com/criminaljusticeperiodicals',
        'proxy': True,
    },
    {
        'name': 'CUNY Academic Works',
        'url': 'https://academicworks.cuny.edu/',
        'proxy': False,
    },
    {
        'name': 'CUNY Digital History Archive (CDHA)',
        'url': 'http://cdha.cuny.edu/',
        'proxy': False,
    },
    {
        'name': 'Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition',
        'url': 'http://dsm.psychiatryonline.org/doi/book/10.1176/appi.books.9780890425596',
        'proxy': True,
    },
    {
        'name': 'Dictionary of Literary Biography Complete Online',
        'url': 'https://link.gale.com/apps/DLBC',
        'proxy': True,
    },
    {
        'name': 'Digital Public Library of America',
        'url': 'https://dp.la/',
        'proxy': False,
    },
    {
        'name': 'Digital Theatre Plus',
        'url': 'https://edu.digitaltheatreplus.com/',
        'proxy': True,
    },
    {
        'name': 'Dissertations: CUNY Graduate Center Legacy (Retrospective) Dissertations, 1965-2014',
        'url': 'http://library.gc.cuny.edu/legacy/collections/browse',
        'proxy': False,
    },
    {
        'name': 'DOAJ: Directory of Open Access Journals',
        'url': 'https://doaj.org/',
        'proxy': False,
    },
    {
        'name': 'Drama Online - National Theatre Collections 1 & 2',
        'url': 'https://www.dramaonlinelibrary.com/national-theatre-collection',
        'proxy': True,
    },
    {
        'name': 'EasyBib',
        'url': 'http://www.easybib.com/',
        'proxy': False,
    },
    {
        'name': 'Ebook Central',
        'url': 'https://ebookcentral.proquest.com/lib/kbcc-ebooks/search.action',
        'proxy': True,
    },
    {
        'name': 'EBSCO (all)',
        'url': 'https://search.ebscohost.com/login.aspx',
        'proxy': True,
    },
    {
        'name': 'Economist',
        'url': 'https://link.gale.com/apps/ECON',
        'proxy': True,
    },
    {
        'name': 'Encyclopedia Britannica Online',
        'url': 'https://academic.eb.com/levels/collegiate',
        'proxy': True,
    },
    {
        'name': 'Ethinc Newswatch',
        'url': 'https://search.proquest.com/ethnicnewswatch',
        'proxy': True,
    },
    {
        'name': 'Exercise and Sports Sciences Reviews',
        'url': 'http://journals.lww.com/acsm-essr/pages/issuelist.aspx',
        'proxy': False,
    },
    {
        'name': 'Financial Times Historical Archive, 1888-2010',
        'url': 'https://link.gale.com/apps/FTHA',
        'proxy': True,
    },
    {
        'name': 'Foreign Policy',
        'url': 'http://foreignpolicy.com',
        'proxy': True,
    },
    {
        'name': 'Gale Academic OneFile',
        'url': 'https://link.gale.com/apps/AONE',
        'proxy': True,
    },
    {
        'name': 'Gale eBooks',
        'url': 'https://link.gale.com/apps/GVRL',
        'proxy': True,
    },
    {
        'name': 'Gale General OneFile',
        'url': 'https://link.gale.com/apps/ITOF',
        'proxy': True,
    },
    {
        'name': 'Gale Interactive: Chemistry',
        'url': 'https://link.gale.com/apps/ICHEM',
        'proxy': True,
    },
    {
        'name': 'Gale Interactive: Human Anatomy',
        'url': 'http://cyber.galegroup.com/cyber/IANAT',
        'proxy': True,
    },
    {
        'name': 'Gale Literature',
        'url': 'https://link.gale.com/apps/GLS',
        'proxy': True,
    },
    {
        'name': 'Gale OneFile Diversity Studies',
        'url': 'https://link.gale.com/apps/PPDS',
        'proxy': True,
    },
    {
        'name': 'Gale OneFile: Science',
        'url': 'https://link.gale.com/apps/PPGS',
        'proxy': True,
    },
    {
        'name': 'Gale Primary Sources',
        'url': 'https://link.gale.com/apps/GDCS',
        'proxy': True,
    },
    {
        'name': 'Gale Small Business Builder',
        'url': 'https://app.dezinersoftware.com/library',
        'proxy': True,
    },
    {
        'name': 'Geoportal',
        'url': 'http://www.baruch.cuny.edu/geoportal/',
        'proxy': False,
    },
    {
        'name': 'Gerontologist',
        'url': 'https://academic.oup.com/gerontologist',
        'proxy': True,
    },
    {
        'name': 'Gerontology, The Journals of, Series A',
        'url': 'https://academic.oup.com/biomedgerontology',
        'proxy': True,
    },
    {
        'name': 'Global Issues in Context',
        'url': 'https://link.gale.com/apps/GIC',
        'proxy': True,
    },
    {
        'name': 'GrantForward Database',
        'url': 'https://www.grantforward.com/index',
        'proxy': True,
    },
    {
        'name': 'GREENR (Global Reference On The Environment/Energy/And Natural Resources)',
        'url': 'https://link.gale.com/apps/GRNR',
        'proxy': True,
    },
    {
        'name': 'Health & Wellness Resource Center',
        'url': 'https://link.gale.com/apps/HWRC',
        'proxy': True,
    },
    {
        'name': 'Health and Environmental Studies: Archives Unbound',
        'url': 'https://link.gale.com/apps/GDSC',
        'proxy': True,
    },
    {
        'name': 'Health Reference Center Academic',
        'url': 'https://link.gale.com/apps/HRCA',
        'proxy': True,
    },
    {
        'name': 'Highwire Press',
        'url': 'http://highwire.stanford.edu/',
        'proxy': False,
    },
    {
        'name': 'Historic American Newspapers',
        'url': 'http://chroniclingamerica.loc.gov/',
        'proxy': False,
    },
    {
        'name': 'Historical New York Times - 1851 to 2016',
        'url': 'https://search.proquest.com/hnpnewyorktimes',
        'proxy': True,
    },
    {
        'name': 'Holocaust Archives: Archives Unbound',
        'url': 'https://link.gale.com/apps/GDSC',
        'proxy': True,
    },
    {
        'name': 'ICPSR ( Inter-university Consortium for Political and Social Research)',
        'url': 'http://www.icpsr.umich.edu/icpsrweb/ICPSR/',
        'proxy': False,
    },
    {
        'name': 'IEEE Xplore Digital Library',
        'url': 'http://www.ieee.org/ieeexplore',
        'proxy': True,
    },
    {
        'name': 'Infoshare',
        'url': 'http://www.infoshare.org/',
        'proxy': True,
    },
    {
        'name': 'InfoTrac Newsstand',
        'url': 'https://link.gale.com/apps/STND',
        'proxy': True,
    },
    {
        'name': 'JAMA',
        'url': 'https://jamanetwork.com/journals/jama',
        'proxy': True,
    },
    {
        'name': 'JSTOR',
        'url': 'http://www.jstor.org/',
        'proxy': True,
    },
    {
        'name': 'Kanopy',
        'url': 'https://kbcccuny.kanopy.com/',
        'proxy': True,
    },
    {
        'name': 'KnightCite',
        'url': 'https://www.calvin.edu/library/knightcite/',
        'proxy': False,
    },
    {
        'name': 'LegalTrac',
        'url': 'https://link.gale.com/apps/LT',
        'proxy': True,
    },
    {
        'name': 'LexisNexis',
        'url': 'http://www.nexisuni.com',
        'proxy': True,
    },
    {
        'name': 'Literature Criticism Online',
        'url': 'https://link.gale.com/apps/LCO',
        'proxy': True,
    },
    {
        'name': 'Literature Resource Center',
        'url': 'https://link.gale.com/apps/LITRC',
        'proxy': True,
    },
    {
        'name': 'Litfinder',
        'url': 'https://link.gale.com/apps/LITF',
        'proxy': True,
    },
    {
        'name': 'Making of the Modern World',
        'url': 'https://link.gale.com/apps/MOME',
        'proxy': True,
    },
    {
        'name': 'MathSciNet',
        'url': 'https://mathscinet.ams.org/mathscinet',
        'proxy': True,
    },
    {
        'name': 'Medicine & Science in Sports & Exercise',
        'url': 'http://journals.lww.com/acsm-msse/pages/issuelist.aspx',
        'proxy': False,
    },
    {
        'name': 'MedlinePlus Consumer Health',
        'url': 'http://www.nlm.nih.gov/medlineplus/',
        'proxy': False,
    },
    {
        'name': 'MLA Style Guide at Purdue Online Writing Lab',
        'url': 'https://owl.english.purdue.edu/owl/section/2/11/',
        'proxy': False,
    },
    {
        'name': 'MoMA Learning',
        'url': 'https://www.moma.org/learn/moma_learning',
        'proxy': False,
    },
    {
        'name': 'Nature Journal',
        'url': 'http://www.nature.com/',
        'proxy': True,
    },
    {
        'name': 'New England Journal of Medicine',
        'url': 'http://www.nejm.org/',
        'proxy': True,
    },
    {
        'name': 'New York Public Library Digital Collections',
        'url': 'http://digitalcollections.nypl.org/',
        'proxy': False,
    },
    {
        'name': 'New York State Historic Newspapers',
        'url': 'http://nyshistoricnewspapers.org/newspapers/',
        'proxy': False,
    },
    {
        'name': 'New York State Newspapers',
        'url': 'https://link.gale.com/apps/SPJ.SP01',
        'proxy': True,
    },
    {
        'name': 'New York Times 1851-2016 (Historical Newspapers)',
        'url': 'https://search.proquest.com/hnpnewyorktimes/advanced',
        'proxy': True,
    },
    {
        'name': 'New York Times Academic Pass',
        'url': 'http://www.nytimes.com/passes',
        'proxy': False,
    },
    {
        'name': 'Nursing and Allied Health Collection',
        'url': 'https://link.gale.com/apps/PPNU',
        'proxy': True,
    },
    {
        'name': 'NYC Data',
        'url': 'http://www.baruch.cuny.edu/nycdata/',
        'proxy': False,
    },
    {
        'name': 'NYPD Crime Statistics',
        'url': 'https://www1.nyc.gov/site/nypd/stats/crime-statistics/crime-statistics-landing.page',
        'proxy': False,
    },
    {
        'name': 'O*Net Online',
        'url': 'http://www.onetonline.org/',
        'proxy': False,
    },
    {
        'name': 'Occupational Outlook Handbook',
        'url': 'http://www.bls.gov/ooh/',
        'proxy': False,
    },
    {
        'name': 'Open Library',
        'url': 'https://openlibrary.org/',
        'proxy': False,
    },
    {
        'name': 'Opposing Viewpoints in Context',
        'url': 'https://link.gale.com/apps/OVIC',
        'proxy': True,
    },
    {
        'name': 'OSHA: Occupational Safety & Health Administration',
        'url': 'https://www.osha.gov/SLTC/',
        'proxy': False,
    },
    {
        'name': 'Oxford Art Online',
        'url': 'http://www.oxfordartonline.com/groveart',
        'proxy': True,
    },
    {
        'name': 'Oxford English Dictionary',
        'url': 'http://www.oed.com/',
        'proxy': True,
    },
    {
        'name': 'Oxford Handbooks Online: Scholarly Research Reviews',
        'url': 'https://academic.oup.com/pages/oxford-handbooks',
        'proxy': True,
    },
    {
        'name': 'Oxford Music Online',
        'url': 'http://www.oxfordmusiconline.com/grovemusic',
        'proxy': True,
    },
    {
        'name': 'Pivot',
        'url': 'https://pivot.proquest.com',
        'proxy': True,
    },
    {
        'name': 'Primary Sources - Artemis Platform',
        'url': 'https://infotrac.gale.com/itweb/cuny_kingsboro',
        'proxy': True,
    },
    {
        'name': 'Project Muse',
        'url': 'http://muse.jhu.edu/',
        'proxy': True,
    },
    {
        'name': 'PsychiatryOnline (DSM-V-TR)',
        'url': 'http://psychiatryonline.org/index.aspx',
        'proxy': True,
    },
    {
        'name': 'PubMed',
        'url': 'http://www.ncbi.nlm.nih.gov/PubMed/',
        'proxy': False,
    },
    {
        'name': 'Purdue OWL',
        'url': 'https://owl.purdue.edu/',
        'proxy': False,
    },
    {
        'name': 'Refworks',
        'url': 'http://refworks.proquest.com',
        'proxy': True,
    },
    {
        'name': 'Science In Context',
        'url': 'https://link.gale.com/apps/SCIC',
        'proxy': True,
    },
    {
        'name': 'Science Magazine',
        'url': 'http://science.sciencemag.org/',
        'proxy': True,
    },
    {
        'name': 'Science.gov',
        'url': 'http://www.science.gov/',
        'proxy': False,
    },
    {
        'name': 'ScienceDirect',
        'url': 'http://www.sciencedirect.com/',
        'proxy': True,
    },
    {
        'name': 'Scribner Writers Online',
        'url': 'https://link.gale.com/apps/GVRL.xlit.scrb',
        'proxy': True,
    },
    {
        'name': 'Slavery and Anti-Slavery',
        'url': 'https://link.gale.com/apps/SAS',
        'proxy': True,
    },
    {
        'name': 'Slavery in America and the World: History, Culture & Law',
        'url': 'http://heinonline.org/HOL/FeedBack?action=slavery_new&collection=slavery',
        'proxy': True,
    },
    {
        'name': 'Smithsonian Magazines Archive 1970-Present',
        'url': 'https://link.gale.com/apps/SMIT',
        'proxy': True,
    },
    {
        'name': 'Social Explorer',
        'url': 'http://www.socialexplorer.com/',
        'proxy': True,
    },
    {
        'name': 'SpringerLink',
        'url': 'http://link.springer.com/',
        'proxy': True,
    },
    {
        'name': 'Swank',
        'url': 'https://digitalcampus.swankmp.net/kbcc386817',
        'proxy': True,
    },
    {
        'name': 'U.S. Census Bureau',
        'url': 'http://www.census.gov/',
        'proxy': False,
    },
    {
        'name': 'U.S. Department of Justice Statistics',
        'url': 'http://www.bjs.gov/',
        'proxy': False,
    },
    {
        'name': 'U.S. History in Context',
        'url': 'https://link.gale.com/apps/UHIC',
        'proxy': True,
    },
    {
        'name': 'U.S. Major Dailies',
        'url': 'https://search.proquest.com/usmajordailies/advanced/news/fromDatabasesLayer',
        'proxy': True,
    },
    {
        'name': 'USA.gov',
        'url': 'http://www.usa.gov/',
        'proxy': False,
    },
    {
        'name': 'Vault (Career Insider)',
        'url': 'https://access.vault.com/career-insider-login.aspx',
        'proxy': True,
    },
    {
        'name': 'Wall Street Journal',
        'url': 'http://search.proquest.com/wallstreetjournal',
        'proxy': True,
    },
    {
        'name': 'Wall Street Journal (Access to Digital App)',
        'url': 'https://partner.wsj.com/enter-redemption-code/CUNYnd5wtb6z',
        'proxy': False,
    },
    {
        'name': 'Wiley Online Library',
        'url': 'https://onlinelibrary.wiley.com/',
        'proxy': True,
    },
    {
        'name': 'Women and Social Movements in the U.S.',
        'url': 'http://wass.alexanderstreet.com',
        'proxy': True,
    },
    {
        'name': 'World History in Context',
        'url': 'https://link.gale.com/apps/WHIC',
        'proxy': True,
    },
    {
        'name': 'WorldCat',
        'url': 'http://newfirstsearch.oclc.org/dbname=WorldCat;done=referer;FSIP',
        'proxy': False,
    },
    {
        'name': 'Yearbook of Immigration Statistics',
        'url': 'https://www.dhs.gov/yearbook-immigration-statistics',
        'proxy': False,
    },
    {
        'name': 'Zotero',
        'url': 'https://www.zotero.org/',
        'proxy': False,
    },
    {
        'name': 'ZoteroBib',
        'url': 'https://zbib.org/',
        'proxy': False,
    },
]

async def run_func(client, service):
    try:
        response = await client.get(service['url'])
        service['status'] = response.status_code
    except:
        service['status'] = 500
    return service


@app.route('/')
async def index():
    headers = {'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
    async with httpx.AsyncClient(headers=headers) as client:
        output = []
        for service in services:
            output.append(asyncio.ensure_future(run_func(client, service)))
        gathered_data = await asyncio.gather(*output)

    return await render_template('index.html', services=gathered_data)

if __name__ == "__main__":
    app.run(port=8000, host="127.0.0.1")
