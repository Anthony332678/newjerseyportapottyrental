import os
import io, os
import chardet
import codecs
import html
import re
from bs4 import BeautifulSoup
import requests
import random
import shutil

#tool website operation

home_view_py='''
from django.shortcuts import render
from django.http import HttpResponse
from .operation import *
from .template import *
from .models import ToDoList, Item
from .forms import CreateNewList
import os
import random
from django.utils.safestring import mark_safe

# Create your views here.
def index(response):
    forms= CreateNewList()
    return render(response, "zeodigital/index.html", {
        
    })

def contact(response):
    forms= CreateNewList()
    return render(response, "zeodigital/contact-us.html", {
        
    })
'''
home_url_py= '''
from django.urls import path

from . import views

urlpatterns= [
    path("", views.index, name='index'),
    path("sitemap.xml/", views.sitemaps, name='sitemaps'),
    path("contact-us/", views.contact, name='contact'),
'''
state_views_py= '''
def index<num>(response):
    forms= CreateNewList()
    return render(response, "zeodigital/<STATE-PATH>/index.html", {
        
    })
'''
state_url_py= '''
    path("<STATE-URL>/", views.index<num>, name='index<num>'),
'''
city_views_py= '''
def index<num>(response):
    forms= CreateNewList()
    phone_number= read_root_file('Phone Number')
    site_name = read_root_file('Site Name')
    Long_formurl= read_root_file('Long Form')
    shortformurl= read_root_file('Short Form')
    randomize_image= read_root_file('Randomized image File root').split(',')
    randomize_image = list(filter(None, randomize_image))
    split_citypage_contents= read_root_file('City Page Contents').split('@@@')
    picker_citypage_contents= random.randint(0, len(split_citypage_contents)-1)
    citypage_contents= split_citypage_contents[picker_citypage_contents]

    split_metatitle_citypage= read_root_file('City Page Meta Title').split('@@@')
    picker_metatitle_citypage= random.randint(0, len(split_metatitle_citypage)-1)
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', '#city_land')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', '#city_land')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', '#city_land').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/<STATE-PATH>/<CITY-PATH>/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })
'''
city_url_py= '''
    path("<STATE-URL>/<CITY-URL>/", views.index<num>, name='index<num>'),
'''
county_views_py= '''
def index<num>(response):
    forms= CreateNewList()
    phone_number= read_root_file('Phone Number')
    site_name = read_root_file('Site Name')
    Long_formurl= read_root_file('Long Form')
    shortformurl= read_root_file('Short Form')
    randomize_image= read_root_file('Randomized image File root').split(',')
    randomize_image = list(filter(None, randomize_image))
    split_countypage_contents= read_root_file('County Page Contents').split('@@@')
    picker_countypage_contents= random.randint(0, len(split_countypage_contents)-1)
    countypage_contents= split_countypage_contents[picker_countypage_contents]

    split_metatitle_countypage= read_root_file('County Page Meta Title').split('@@@')
    picker_metatitle_countypage= random.randint(0, len(split_metatitle_countypage)-1)
    metatitle_countypage= split_metatitle_countypage[picker_metatitle_countypage].replace('#State', '#county_land')

    split_metadescription_countypage= read_root_file('County Page Meta Description').split('@@@')
    picker_metadescription_countypage= random.randint(0, len(split_metadescription_countypage)-1)
    metadescription_countypage= split_metadescription_countypage[picker_metadescription_countypage].replace('#State', '#county_land')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, countypage_contents, site_name).replace('#State', '#county_land').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/<STATE-PATH>/<COUNTY-PATH>/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_countypage,
        'aloomaiddescription': metadescription_countypage,
    })
'''
county_url_py= '''
    path("<STATE-URL>/<COUNTY-URL>/", views.index<num>, name='index<num>'),
'''
end_view_py='''
def sitemaps(response):
    return render(response, "zeodigital/sitemaps/sitemaps.xml")
'''
end_url_py='''
]
'''

home_page_template= '''
        <div class="col-m-2" id="aloomafotter1">
            <div id="aloomafotter2"><a href="aloomaidstaturl" id="aloomafotter">aloomaidstate</a></div>
        </div>
'''

home_page_template1= '''
        <div class="row">
            <div class="col-6 col-s-6 col-m-6 col-l-6" style="border: 2px solid black; text-align:center; background-color: white;"><a href="aloomaidcityurl"><strong>aloomaidcityname</strong></a></div>
            <div class="col-6 col-s-6 col-m-6 col-l-6" style="border: 2px solid black; text-align:center; background-color: white;"><strong>aloomaidzipcode</strong></div>
            
        </div>
'''

county_remove= '''    <br><br><br><br>
    <div class="containeralooma" style="background-color: transparent;">
        <section class="boxalooma" style="text-align: center;">
        <h2 class="heading-with-line template4 h2alooma">Counties In #State</h2>
        <div class="row">
            aloomaidstatecounty
        </div>
        </section>
    </div>
'''
def closing_ending():
    opp = open("static/aloomaspecial/views.txt", "r", encoding="utf-8").read()
    opp_pp = open("static/aloomaspecial/urls.txt", "r", encoding="utf-8").read()
    Good = open("views.py", "w", encoding='UTF-8')
    Good.write(opp)
    Good.close()
    Good1 = open("urls.py", "w", encoding='UTF-8')
    Good1.write(opp_pp)
    Good1.close()

def clean_text(cntents):
    soup = BeautifulSoup(cntents, 'html.parser')
    clean_text = soup.get_text()
    return clean_text


def replace_first_comma_from_behind(s):
    last_comma_index = s.rfind(',')
    if last_comma_index != -1:  # If a comma is found
        return s[:last_comma_index] + '' + s[last_comma_index+1:]
    else:
        return s
    


def short_code_state(state_repl):
    search_categories = open("static/aloomaspecial/content/uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
    for credentials in search_categories:
        credential= credentials.strip().split(',')
        short_code = credential[2].replace('ï»¿', '').upper()
        state_repl1= credential[3].replace('ï»¿', '').title()
        try:
            if state_repl.lower() == state_repl1.lower():
                break
        except:
            break
    return short_code

def random_homepage_webpage(confirm_home_pages):
    return open(confirm_home_pages, "r", encoding="utf-8-sig").read()


def create_home_page_url(confirm_home_pages, home_view_py, home_url_py, domain_site_name):
    home_page= random_homepage_webpage(confirm_home_pages).replace('#State', f'USA')
    fp = open('templates/zeodigital/index.html', "w", encoding='utf-8-sig')
    fp.writelines(home_page)
    fp.close()
    Good = open("static/aloomaspecial/views.txt", "a", encoding='utf-8-sig')
    Good.write(home_view_py)
    Good.close()
    Good1 = open("static/aloomaspecial/urls.txt", "a", encoding='utf-8-sig')
    Good1.write(home_url_py)
    Good1.close()
    return f'<url><loc>https://{domain_site_name}/</loc></url>'

def random_state_webpage(confirm_state_pages):
    return open(confirm_state_pages, "r", encoding="utf-8-sig").read()


def create_state_url(number, state_name, state_views_py, url_state_structure, state_url_py, confirm_state_pages, domain_site_name, state_abbr_short, all_table_dat1, all_table_dat2, rand_cty, rand_cunty):
    state_abbr_short= state_abbr_short.lower()
    state_name= state_name.replace("'", '')
    if all_table_dat2=='':
        state_page= random_state_webpage(confirm_state_pages).replace(county_remove, '').replace('aloomaidstatecity', all_table_dat1).replace('#State', f'{state_name}, {state_abbr_short.upper()}').replace('[listcountycity]', f'{rand_cty}, {rand_cunty}').replace('aloomaiddomainname', f'https://{domain_site_name}/{state_abbr_short}/')
    else:
        state_page= random_state_webpage(confirm_state_pages).replace('aloomaidstatecounty', all_table_dat2).replace('aloomaidstatecity', all_table_dat1).replace('#State', f'{state_name}, {state_abbr_short.upper()}').replace('[listcountycity]', f'{rand_cty}, {rand_cunty}').replace('aloomaiddomainname', f'https://{domain_site_name}/{state_abbr_short}/')
    try:
        os.makedirs(f'templates/zeodigital/{url_state_structure}') 
    except:
        pass
    fp = open(f'templates/zeodigital/{url_state_structure}/index.html', "w", encoding='utf-8-sig')
    fp.writelines(state_page)
    fp.close()
    save= state_views_py.replace('<num>', str(number)).replace('<STATE-PATH>', url_state_structure)
    save_path= state_url_py.replace('<num>', str(number)).replace('<STATE-URL>', state_abbr_short)
    Good = open("static/aloomaspecial/views.txt", "a", encoding='utf-8-sig')
    Good.write(save)
    Good.close()
    Good1 = open("static/aloomaspecial/urls.txt", "a", encoding='utf-8-sig')
    Good1.write(save_path)
    Good1.close()

    return state_name, f'<url><loc>https://{domain_site_name}/{state_abbr_short}/</loc></url>'

def random_city_webpage(confirm_city_pages):
    return open(confirm_city_pages, "r", encoding="utf-8-sig").read()

def create_city_page_url(number, state_name, url_state_structure, state_abbr_short, city_name, city_views_py, url_city_structure, city_url_py, confirm_city_pages, domain_site_name, county_web_contents1, all_table_data1, iframe, zip):
    state_abbr_short= state_abbr_short.lower()
    city_name= city_name.replace("'", '')
    city_page= random_city_webpage(confirm_city_pages).replace('aloomaidcontentscity', county_web_contents1).replace('aloomaidcitycloseto', all_table_data1).replace('aloomaidzip', zip).replace('aloomaidembeddedmap', iframe).replace('#State', f'{city_name}, {state_abbr_short.upper()}').replace('"../static/', '"../../static/').replace('aloomaiddomainname', f'https://{domain_site_name}/{state_abbr_short}/{url_city_structure}/')
    try:
        os.makedirs(f'templates/zeodigital/{url_state_structure}/{url_city_structure}') 
    except:
        pass
    fp = open(f'templates/zeodigital/{url_state_structure}/{url_city_structure}/index.html', "w", encoding='utf-8-sig')
    fp.writelines(city_page)
    fp.close()
    save= city_views_py.replace('<num>', str(number)).replace('<STATE-PATH>', url_state_structure).replace('<CITY-PATH>', url_city_structure).replace('#city_land', f'{city_name}, {state_abbr_short.upper()}')
    save_path= city_url_py.replace('<num>', str(number)).replace('<STATE-URL>', state_abbr_short).replace('<CITY-URL>', url_city_structure)
    Good = open("static/aloomaspecial/views.txt", "a", encoding='utf-8-sig')
    Good.write(save)
    Good.close()
    Good1 = open("static/aloomaspecial/urls.txt", "a", encoding='utf-8-sig')
    Good1.write(save_path)
    Good1.close()

    return f'<url><loc>https://{domain_site_name}/{state_abbr_short}/{url_city_structure}/</loc></url>'
   
def random_county_webpage(confirm_county_pages):
    return open(confirm_county_pages, "r", encoding="utf-8-sig").read()

def create_county_page_url(number, state_name, url_state_structure, state_abbr_short, county_name, county_views_py, url_county_structure, county_url_py, confirm_county_pages, domain_site_name, county_web_contents2, all_table_data2):
    state_abbr_short= state_abbr_short.lower()
    county_name= county_name.replace("'", '')
    county_page= random_county_webpage(confirm_county_pages).replace('aloomaidcountycontents', county_web_contents2).replace('aloomaidcountytable', all_table_data2).replace('#State',  f'{county_name}, {state_abbr_short.upper()}').replace('"../static/', '"../../static/').replace('aloomaiddomainname', f'https://{domain_site_name}/{state_abbr_short}/{url_county_structure}/')
    try:
        os.makedirs(f'templates/zeodigital/{url_state_structure}/{url_county_structure}') 
    except:
        pass
    fp = open(f'templates/zeodigital/{url_state_structure}/{url_county_structure}/index.html', "w", encoding='utf-8-sig')
    fp.writelines(county_page)
    fp.close()
    save= county_views_py.replace('<num>', str(number)).replace('<STATE-PATH>', url_state_structure).replace('<COUNTY-PATH>', url_county_structure).replace('#county_land', f'{county_name}, {state_abbr_short.upper()}')
    save_path= county_url_py.replace('<num>', str(number)).replace('<STATE-URL>', state_abbr_short).replace('<COUNTY-URL>', url_county_structure)
    Good = open("static/aloomaspecial/views.txt", "a", encoding='utf-8-sig')
    Good.write(save)
    Good.close()
    Good1 = open("static/aloomaspecial/urls.txt", "a", encoding='utf-8-sig')
    Good1.write(save_path)
    Good1.close()

    return f'<url><loc>https://{domain_site_name}/{state_abbr_short}/{url_county_structure}/</loc></url>'

def create_sitemape_page(sitemaps, end_view_py, end_url_py):
    try:
        os.makedirs('templates/zeodigital/sitemaps') 
        parent_dir5 = f"templates/zeodigital/sitemaps/sitemaps.xml"
        f = open(parent_dir5, "a", encoding='utf-8-sig', errors='replace')
        for site in sitemaps:
            f.write(site + '\n')
        f.close()
    except:
        pass
    Good = open("static/aloomaspecial/views.txt", "a", encoding='utf-8-sig')
    Good.write(end_view_py)
    Good.close()
    Good1 = open("static/aloomaspecial/urls.txt", "a", encoding='utf-8-sig')
    Good1.write(end_url_py)
    Good1.close()

def state_url_data(state_rep, state_abbr_short, radioselect, population_limit, Pages_created_options, Checkboxselected):
    def random_p(hrml_crens_one, picker_rand, col_nini):
        data= hrml_crens_one[picker_rand].replace('\n', '')
        if '$$' in data:
            return hrml_crens_one[picker_rand].replace('\n', '').split('$$')[col_nini].replace('ï»¿', '')
            
        else:
            return hrml_crens_one[picker_rand].replace('\n', '').split(',')[col_nini].replace('ï»¿', '')
    
    def all_state_url(state_rep, Checkboxselected):
        v= ''
        city_data= ''
        adeola=0
        selected_row=[]
        id1=0
        hrml_crens_one = open("static/aloomaspecial/content/uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
       
        for city in hrml_crens_one:
            if not city.strip():
                continue
            
            split_city= city.replace('\n', '').split(',')
            city_p= split_city[0].title().replace('ï»¿', '').replace('"', '')
            sub_ciy= split_city[0].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
            link_city= str(sub_ciy.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
            state_p= split_city[3].title().replace('ï»¿', '').replace('"', '')
            population= int(split_city[8])
            state_repl= split_city[3].title().replace('ï»¿', '').replace('"', '')
            if population < int(population_limit):
                continue

            if 'All Pages' == Pages_created_options:
                pass
            elif 'Selected State Pages' == Pages_created_options:
                if state_repl in Checkboxselected:
                    pass
                else:
                    continue
            elif 'Excluded State Pages' == Pages_created_options:
                if state_repl in Checkboxselected:
                    continue
                else:
                    pass
            
            if state_rep.lower() == state_p.lower() or state_rep.lower()[:5] == state_p.lower():
                
                v+= home_page_template.replace('aloomaidstaturl', f'/{state_abbr_short.lower()}/{link_city}/').replace('aloomaidstate', city_p)
                adeola += 1
                if adeola< 10:
                    while True:
                        picker_rand= random.randint(0,len(hrml_crens_one)-1)
                        if picker_rand in selected_row:
                            pass
                        else:
                            break
                    selected_row.append(picker_rand)
                    city_data+= f'{random_p(hrml_crens_one, picker_rand, 0)}, '
            
                id1+=1
                if id1==30:
                    break
                

        return v, city_data
    

    def all_county_url(state_rep):
        v= ''
        county_data= ''
        adeola=0
        selected_row=[]
        id1=0
        hrml_crens_one = open("static/aloomaspecial/content/county.txt", "r", encoding="windows-1254").readlines()
        for county in hrml_crens_one:
            if not county.strip():
                continue
            split_county= county.replace('\n', '').split('$$')
            county_p= split_county[0].replace('ï»¿', '').title()
            sub_county= county_p.replace(' ', '-').replace(',', '').replace('.', '').lower()
            sub_county= str(sub_county.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
            state_p= split_county[1].replace('ï»¿', '')

            
            if state_rep.lower() == state_p.lower() or state_rep.lower()[:5] == state_p.lower():
                v+= home_page_template.replace('aloomaidstaturl', f'/{state_abbr_short.lower()}/{sub_county}/').replace('aloomaidstate', county_p)
                adeola += 1
                if adeola< 10:
                    while True:
                        picker_rand= random.randint(0,len(hrml_crens_one)-1)
                        if picker_rand in selected_row:
                            pass
                        else:
                            break
                    selected_row.append(picker_rand)
                    county_data+= f'{random_p(hrml_crens_one, picker_rand, 0)}, '

                id1+=1
                if id1==30:
                    break
        return v, county_data
    
    all_table_data1, rand_city= all_state_url(state_rep, Checkboxselected)
    if 'Yes'== radioselect:
        all_table_data2, rand_county= all_county_url(state_rep)
    else:
        all_table_data2= ''
        rand_county= ''

    return all_table_data1, rand_city, all_table_data2, rand_county

def city_url_data(data_usage, data_usage1, state_abbr_short, population_limit, Pages_created_options, Checkboxselected):
    iframe= data_usage1.replace('"<iframe', '<iframe').replace('</iframe>"', '</iframe>')
    state_abbr_short= state_abbr_short.lower()
    split_usage= data_usage.replace('\n', '').replace('ï»¿', '').split('$$')
    county_web_contents= split_usage[1]
    all_table_data=''
    id=0
    hrml_crens_one = open("static/aloomaspecial/content/uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
    higest= len(hrml_crens_one)-1
       
    selected_row=[]
    for data_plus_plu1 in range(higest):
        while True:
            picker= random.randint(0,higest)
            if picker in selected_row:
                pass
            else:
                break
        selected_row.append(picker)
        split_city= hrml_crens_one[picker].replace('\n', '').split(',')

        city_p= split_city[0].title().replace('ï»¿', '').replace('"', '')
        sub_ciy= split_city[0].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
        link_city= str(sub_ciy.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
        state_repl= split_city[3].title().replace('ï»¿', '').replace('"', '')
        population= int(split_city[8])
        state_abbr_sho = split_city[2].replace('ï»¿', '')

        if state_abbr_sho.lower() == state_abbr_short:
            pass
        else:
            continue

        if population < int(population_limit):
            continue

        if 'All Pages' == Pages_created_options:
            pass
        elif 'Selected State Pages' == Pages_created_options:
            if state_repl in Checkboxselected:
                pass
            else:
                continue
        elif 'Excluded State Pages' == Pages_created_options:
            if state_repl in Checkboxselected:
                continue
            else:
                pass

        all_table_data += home_page_template.replace('aloomaidstaturl', f'/{state_abbr_short}/{link_city}/').replace('aloomaidstate', city_p)
        id+=1
        if id==50:
            break




 

    return county_web_contents, all_table_data, iframe

def county_url_data(data_usage, state_short_code_county):
    state_short_code_county= state_short_code_county.lower()
    split_usage= data_usage.replace('\n', '').replace('ï»¿', '').split('$$')
    county_web_contents= split_usage[1]
    county_zip_code_all= split_usage[2]
    all_table_data=''
    id1=0
    all_data= county_zip_code_all.split('</tr><tr>')
    for all_dat in all_data:
        if not all_dat.strip():
            continue
        
        county_name= all_dat.split('</a></td>')[0]
        county_name= clean_text(county_name)
        sub_ciy= county_name.replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
        sub_ciy= str(sub_ciy.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
        zip= all_dat.split('</a></td>')[1]
        zip= clean_text(zip)
        all_table_data+= home_page_template1.replace('aloomaidcityname', county_name).replace('aloomaidzipcode', zip).replace('aloomaidcityurl', f'/{state_short_code_county}/{sub_ciy}')
        id1+=1
        if id1==50:
            break
    return county_web_contents, all_table_data



def all_pages_protocol(population_limit, domain_site_name, radioselect):
    c=0
    duplicate_state=[]
    sitemaps = []
    sitemaps.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    confirm_state_pages= f'templates/zeodigital/allrequiredpages/state.html'
    confirm_city_pages= f'templates/zeodigital/allrequiredpages/city.html'
    confirm_county_pages= f'templates/zeodigital/allrequiredpages/county.html'
    confirm_home_pages= f'templates/zeodigital/index.html'

# -----------------------------------------------------------------------------------------------
    sitemaphomepageurl= create_home_page_url(confirm_home_pages, home_view_py, home_url_py, domain_site_name)
    sitemaps.append(sitemaphomepageurl)

# -----------------------------------------------------------------------------------------------
    naimah=0
    city_contents_data = open("static/aloomaspecial/content/content.csv", "r", encoding="utf-8-sig").readlines()
    city_embedded_data = open("static/aloomaspecial/content/mapembedded.txt", "r", encoding="utf-8-sig").readlines()
    search_categories = open("static/aloomaspecial/content/uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
    for credentials in search_categories:
        credential= credentials.strip().split(',')
        sub_ciy_repl= credential[0].title().replace('ï»¿', '').replace('"', '')
        sub_ciy= credential[0].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
        sub_ciy= str(sub_ciy.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
        state_abbr_short = credential[2].replace('ï»¿', '')
        state_repl= credential[3].title().replace('ï»¿', '').replace('"', '')
        state= credential[3].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
        state= str(state.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
        population= int(credential[8])
        zip_codes= credential[15]
        if 'Puerto Rico'.replace(' ', '-').lower() == state:
            continue
        elif 'Virgin Islands'.replace(' ', '-').lower() == state:
            continue
        elif 'Washington, D.C.'.replace(' ', '-').lower() == state:
            continue
        elif 'US Armed Forces Pacific'.replace(' ', '-').lower() == state:
            continue
        elif 'American Samoa'.replace(' ', '-').lower() == state:
            continue
        elif 'Guam'.replace(' ', '-').lower() == state:
            continue
        elif 'Palau'.replace(' ', '-').lower() == state:
            continue
        elif 'Federated States of Micronesia'.replace(' ', '-').lower() == state:
            continue
        elif 'Northern Mariana Islands'.replace(' ', '-').lower() == state:
            continue
        elif 'Marshall Islands'.replace(' ', '-').lower() == state:
            continue
        elif 'US Armed Forces Europe'.replace(' ', '-').lower() == state:
            continue
        else:
            pass
        
        if population < int(population_limit):
            continue
        
        if state_repl in duplicate_state:
            pass
        else:
            c +=1
            all_table_dat1, rand_cty, all_table_dat2, rand_cunty= state_url_data(state_repl, state_abbr_short, radioselect, population_limit, 'All Pages', [])
            check_state, sitemapstateurl= create_state_url(c, state_repl, state_views_py, state, state_url_py, confirm_state_pages, domain_site_name, state_abbr_short, all_table_dat1, all_table_dat2, rand_cty, rand_cunty)
            duplicate_state.append(check_state)
            sitemaps.append(sitemapstateurl)
        c +=1
        county_web_contents1, all_table_data1, iframe= city_url_data(city_contents_data[naimah], city_embedded_data[naimah], state_abbr_short, population_limit, 'All Pages', [])
        naimah+=1
        sitemapcityurl= create_city_page_url(c, state_repl, state, state_abbr_short, sub_ciy_repl, city_views_py, sub_ciy, city_url_py, confirm_city_pages, domain_site_name, county_web_contents1, all_table_data1, iframe, zip_codes)
        sitemaps.append(sitemapcityurl)
        


# -----------------------------------------------------------------------------------------------
    if 'Yes'== radioselect:
        nini=0
        county_embedded_data = open("static/aloomaspecial/content/content1.csv", "r", encoding="utf-8-sig").readlines()
        search_categories1 = open("static/aloomaspecial/content/county.txt", "r", encoding="utf-8").readlines()
        for credentials1 in search_categories1:
            if not credentials1.strip():
                continue
            
            credential1= credentials1.strip().split('$$')
            county_repl= credential1[0].title().replace('ï»¿', '').replace('"', '')
            county= credential1[0].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
            county= str(county.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
            
            state_repl= credential1[1].title().replace('ï»¿', '')
            state= credential1[1].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
            state= str(state.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
            state_short_code_county= short_code_state(state_repl)
            county_web_contents2, all_table_data2= county_url_data(county_embedded_data[nini], state_short_code_county)
            
            nini+=1
            c +=1
            sitemapcountyurl= create_county_page_url(c, state_repl, state, state_short_code_county, county_repl, county_views_py, county, county_url_py, confirm_county_pages, domain_site_name, county_web_contents2, all_table_data2)
            sitemaps.append(sitemapcountyurl)
    else:
        pass

    sitemaps.append('</urlset>')
    
#-------------------------------------------------------------------------------------------------
    create_sitemape_page(sitemaps, end_view_py, end_url_py)
    closing_ending()
    

def selected_state_pages(population_limit, domain_site_name, radioselect, Checkboxselected):
    c=0
    duplicate_state=[]
    sitemaps = []
    sitemaps.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    confirm_state_pages= f'templates/zeodigital/allrequiredpages/state.html'
    confirm_city_pages= f'templates/zeodigital/allrequiredpages/city.html'
    confirm_county_pages= f'templates/zeodigital/allrequiredpages/county.html'
    confirm_home_pages= f'templates/zeodigital/index.html'

# -----------------------------------------------------------------------------------------------
    sitemaphomepageurl= create_home_page_url(confirm_home_pages, home_view_py, home_url_py, domain_site_name)
    sitemaps.append(sitemaphomepageurl)

# -----------------------------------------------------------------------------------------------
    naimah=0
    city_contents_data = open("static/aloomaspecial/content/content.csv", "r", encoding="utf-8-sig").readlines()
    city_embedded_data = open("static/aloomaspecial/content/mapembedded.txt", "r", encoding="utf-8-sig").readlines()
    search_categories = open("static/aloomaspecial/content/uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
    for credentials in search_categories:
        credential= credentials.strip().split(',')
        sub_ciy_repl= credential[0].title().replace('ï»¿', '').replace('"', '')
        sub_ciy= credential[0].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
        sub_ciy= str(sub_ciy.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
        state_abbr_short = credential[2].replace('ï»¿', '')
        state_repl= credential[3].title().replace('ï»¿', '').replace('"', '')
        state= credential[3].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
        state= str(state.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
        population= int(credential[8])
        zip_codes= credential[15]
        if 'Puerto Rico'.replace(' ', '-').lower() == state:
            continue
        elif 'Virgin Islands'.replace(' ', '-').lower() == state:
            continue
        elif 'Washington, D.C.'.replace(' ', '-').lower() == state:
            continue
        elif 'US Armed Forces Pacific'.replace(' ', '-').lower() == state:
            continue
        elif 'American Samoa'.replace(' ', '-').lower() == state:
            continue
        elif 'Guam'.replace(' ', '-').lower() == state:
            continue
        elif 'Palau'.replace(' ', '-').lower() == state:
            continue
        elif 'Federated States of Micronesia'.replace(' ', '-').lower() == state:
            continue
        elif 'Northern Mariana Islands'.replace(' ', '-').lower() == state:
            continue
        elif 'Marshall Islands'.replace(' ', '-').lower() == state:
            continue
        elif 'US Armed Forces Europe'.replace(' ', '-').lower() == state:
            continue
        else:
            pass
        
        if population < int(population_limit):
            continue

        if state_repl in Checkboxselected:
            pass
        else:
            continue
        
        if state_repl in duplicate_state:
            pass
        else:
            c +=1
            all_table_dat1, rand_cty, all_table_dat2, rand_cunty= state_url_data(state_repl, state_abbr_short, radioselect, population_limit, 'Selected State Pages', Checkboxselected)
            check_state, sitemapstateurl= create_state_url(c, state_repl, state_views_py, state, state_url_py, confirm_state_pages, domain_site_name, state_abbr_short, all_table_dat1, all_table_dat2, rand_cty, rand_cunty)
            duplicate_state.append(check_state)
            sitemaps.append(sitemapstateurl)
        
        county_web_contents1, all_table_data1, iframe= city_url_data(city_contents_data[naimah], city_embedded_data[naimah], state_abbr_short, population_limit, 'Selected State Pages', Checkboxselected)
        naimah+=1
        c +=1
        sitemapcityurl= create_city_page_url(c, state_repl, state, state_abbr_short, sub_ciy_repl, city_views_py, sub_ciy, city_url_py, confirm_city_pages, domain_site_name, county_web_contents1, all_table_data1, iframe, zip_codes)
        sitemaps.append(sitemapcityurl)
        


# -----------------------------------------------------------------------------------------------
    if 'Yes'== radioselect:
        nini=0
        county_embedded_data = open("static/aloomaspecial/content/content1.csv", "r", encoding="utf-8-sig").readlines()
        search_categories1 = open("static/aloomaspecial/content/county.txt", "r", encoding="utf-8").readlines()
        for credentials1 in search_categories1:
            if not credentials1.strip():
                continue
            
            credential1= credentials1.strip().split('$$')
            county_repl= credential1[0].title().replace('ï»¿', '').replace('"', '')
            county= credential1[0].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
            county= str(county.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
            
            state_repl= credential1[1].title().replace('ï»¿', '')
            state= credential1[1].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
            state= str(state.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
            state_short_code_county= short_code_state(state_repl)
            if state_repl in Checkboxselected:
                pass
            else:
                continue
            county_web_contents2, all_table_data2= county_url_data(county_embedded_data[nini], state_short_code_county)
            
            nini+=1
            c +=1
            sitemapcountyurl= create_county_page_url(c, state_repl, state, state_short_code_county, county_repl, county_views_py, county, county_url_py, confirm_county_pages, domain_site_name, county_web_contents2, all_table_data2)
            sitemaps.append(sitemapcountyurl)
    else:
        pass

    sitemaps.append('</urlset>')
    
#-------------------------------------------------------------------------------------------------
    create_sitemape_page(sitemaps, end_view_py, end_url_py)
    closing_ending()

def excluded_state_pages(population_limit, domain_site_name, radioselect, Checkboxselected):
    c=0
    duplicate_state=[]
    sitemaps = []
    sitemaps.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    confirm_state_pages= f'templates/zeodigital/allrequiredpages/state.html'
    confirm_city_pages= f'templates/zeodigital/allrequiredpages/city.html'
    confirm_county_pages= f'templates/zeodigital/allrequiredpages/county.html'
    confirm_home_pages= f'templates/zeodigital/allrequiredpages/homepage.html'

# -----------------------------------------------------------------------------------------------
    sitemaphomepageurl= create_home_page_url(confirm_home_pages, home_view_py, home_url_py, domain_site_name)
    sitemaps.append(sitemaphomepageurl)

# -----------------------------------------------------------------------------------------------
    naimah=0
    city_contents_data = open("static/aloomaspecial/content/content.csv", "r", encoding="utf-8-sig").readlines()
    city_embedded_data = open("static/aloomaspecial/content/mapembedded.txt", "r", encoding="utf-8-sig").readlines()
    search_categories = open("static/aloomaspecial/content/uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
    for credentials in search_categories:
        credential= credentials.strip().split(',')
        sub_ciy_repl= credential[0].title().replace('ï»¿', '').replace('"', '')
        sub_ciy= credential[0].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
        sub_ciy= str(sub_ciy.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
        state_abbr_short = credential[2].replace('ï»¿', '')
        state_repl= credential[3].title().replace('ï»¿', '').replace('"', '')
        state= credential[3].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
        state= str(state.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
        population= int(credential[8])
        zip_codes= credential[15]
        if 'Puerto Rico'.replace(' ', '-').lower() == state:
            continue
        elif 'Virgin Islands'.replace(' ', '-').lower() == state:
            continue
        elif 'Washington, D.C.'.replace(' ', '-').lower() == state:
            continue
        elif 'US Armed Forces Pacific'.replace(' ', '-').lower() == state:
            continue
        elif 'American Samoa'.replace(' ', '-').lower() == state:
            continue
        elif 'Guam'.replace(' ', '-').lower() == state:
            continue
        elif 'Palau'.replace(' ', '-').lower() == state:
            continue
        elif 'Federated States of Micronesia'.replace(' ', '-').lower() == state:
            continue
        elif 'Northern Mariana Islands'.replace(' ', '-').lower() == state:
            continue
        elif 'Marshall Islands'.replace(' ', '-').lower() == state:
            continue
        elif 'US Armed Forces Europe'.replace(' ', '-').lower() == state:
            continue
        else:
            pass
        
        if population < int(population_limit):
            continue

        if state_repl in Checkboxselected:
            continue
        else:
            pass

        if state_repl in duplicate_state:
            pass
        else:
            c +=1
            all_table_dat1, rand_cty, all_table_dat2, rand_cunty= state_url_data(state_repl, state_abbr_short, radioselect, population_limit, 'Excluded State Pages', Checkboxselected)
            check_state, sitemapstateurl= create_state_url(c, state_repl, state_views_py, state, state_url_py, confirm_state_pages, domain_site_name, state_abbr_short, all_table_dat1, all_table_dat2, rand_cty, rand_cunty)
            duplicate_state.append(check_state)
            sitemaps.append(sitemapstateurl)
        
        county_web_contents1, all_table_data1, iframe= city_url_data(city_contents_data[naimah], city_embedded_data[naimah], state_abbr_short, population_limit, 'Excluded State Pages', Checkboxselected)
        naimah+=1
        c +=1
        sitemapcityurl= create_city_page_url(c, state_repl, state, state_abbr_short, sub_ciy_repl, city_views_py, sub_ciy, city_url_py, confirm_city_pages, domain_site_name, county_web_contents1, all_table_data1, iframe, zip_codes)
        sitemaps.append(sitemapcityurl)
        


# -----------------------------------------------------------------------------------------------
    if 'Yes'== radioselect:
        nini=0
        county_embedded_data = open("static/aloomaspecial/content/content1.csv", "r", encoding="utf-8-sig").readlines()
        search_categories1 = open("static/aloomaspecial/content/county.txt", "r", encoding="utf-8").readlines()
        for credentials1 in search_categories1:
            if not credentials1.strip():
                continue
            
            credential1= credentials1.strip().split('$$')
            county_repl= credential1[0].title().replace('ï»¿', '').replace('"', '')
            county= credential1[0].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
            county= str(county.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
            
            state_repl= credential1[1].title().replace('ï»¿', '')
            state= credential1[1].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
            state= str(state.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
            state_short_code_county= short_code_state(state_repl)
            if state_repl in Checkboxselected:
                continue
            else:
                pass
            county_web_contents2, all_table_data2= county_url_data(county_embedded_data[nini], state_short_code_county)
            nini+=1
            c +=1
            sitemapcountyurl= create_county_page_url(c, state_repl, state, state_short_code_county, county_repl, county_views_py, county, county_url_py, confirm_county_pages, domain_site_name, county_web_contents2, all_table_data2)
            sitemaps.append(sitemapcountyurl)
    else:
        pass

    sitemaps.append('</urlset>')
    
#-------------------------------------------------------------------------------------------------
    create_sitemape_page(sitemaps, end_view_py, end_url_py)
    closing_ending()


def read_root_file(file_name):
    save_file= file_name.replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
    save_file= str(save_file.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
    fp = open(f'static/aloomaspecial/records/{save_file}.txt', "r", encoding="utf-8-sig").read()
    return fp
domain_site_name= read_root_file('Domain Site')
population_limit= read_root_file('Population limit')
radioselect= read_root_file('Do you need County Page')
Checkboxselected= read_root_file('Selected and Excluded State')
selected_state_pages(population_limit, domain_site_name, radioselect, Checkboxselected)