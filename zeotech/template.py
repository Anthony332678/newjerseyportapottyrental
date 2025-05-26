import random

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

def state(response):
    forms= CreateNewList()
    return render(response, "zeodigital/allrequiredpages/state.html", {
        
    })

def contact(response):
    forms= CreateNewList()
    return render(response, "zeodigital/contact-us.html", {
        
    })

def city(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Miami FL')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Miami FL')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Miami FL').replace('"static/', '"../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/allrequiredpages/city.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def county(response):
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
    metatitle_countypage= split_metatitle_countypage[picker_metatitle_countypage].replace('#State', 'Barry County FL')

    split_metadescription_countypage= read_root_file('County Page Meta Description').split('@@@')
    picker_metadescription_countypage= random.randint(0, len(split_metadescription_countypage)-1)
    metadescription_countypage= split_metadescription_countypage[picker_metadescription_countypage].replace('#State', 'Barry County FL')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, countypage_contents, site_name).replace('#State', 'Barry County FL').replace('"static/', '"../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/allrequiredpages/county.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_countypage,
        'aloomaiddescription': metadescription_countypage,
    })

def softadmin(response):
    if response.method == "POST":
        try:
            os.makedirs(f'zeotech/static/aloomaspecial/records')
            domainsite_name = response.POST.get('domainsitename')
            create_root_file('Domain Site', domainsite_name)
            site_name = response.POST.get('sitename')
            create_root_file('Site Name', site_name)
            phone_number=  response.POST.get('phone_number')
            create_root_file('Phone Number', phone_number)
            page_color=  response.POST.get('pagecolor')
            create_root_file('Page Color', page_color)
            boxp_agecolor=  response.POST.get('boxpagecolor')
            create_root_file('Box Page Color', boxp_agecolor)
            site_root=  response.POST.get('siteroot')
            create_root_file('Site Root', site_root)
            popula_tions=  response.POST.get('populations')
            create_root_file('Population limit', popula_tions)
            selected_pages=  response.POST.get('selectedpages')
            create_root_file('Page Format', selected_pages)
            Long_formurl=  response.POST.get('Longformurl')
            create_root_file('Long Form', Long_formurl)
            shortformurl=  response.POST.get('shortformurl')
            create_root_file('Short Form', shortformurl)
            radioselect=  response.POST.get('Radio')
            create_root_file('Do you need County Page', radioselect)
            metatitle_homepage=  response.POST.get('metatitlehomepage')
            create_root_file('Home Page Meta title', metatitle_homepage)
            metadescription_homepage=  response.POST.get('metadescriptionhomepage')
            create_root_file('Home Page Meta Description', metadescription_homepage)
            metatitle_statepage=  response.POST.get('metatitlestatepage')
            create_root_file('State Page Meta Title', metatitle_statepage)
            metadescription_statepage=  response.POST.get('metadescriptionstatepage')
            create_root_file('State Page Meta Description', metadescription_statepage)
            Checkboxselected=  response.POST.getlist('Checkbox')
            create_root_file('Selected and Excluded State', Checkboxselected)
            metatitle_citypage=  response.POST.get('metatitlecitypage')
            create_root_file('City Page Meta Title', metatitle_citypage)
            metadescription_citypage=  response.POST.get('metadescriptioncitypage')
            create_root_file('City Page Meta Description', metadescription_citypage)
            metatitle_countypage=  response.POST.get('metatitlecountypage')
            create_root_file('County Page Meta Title', metatitle_countypage)
            metadescription_countypage=  response.POST.get('metadescriptioncountypage')
            create_root_file('County Page Meta Description', metadescription_countypage)
        
            image_list_root=[]
            for file in response.FILES.getlist('randomizeimage'):
                list_image_root= save_image_to_root(file)
                image_list_root.append(list_image_root)
            create_root_file('Randomized image File root', image_list_root)
            homepage_contents=  response.POST.get('homepagecontents')
            create_root_file('Home Page Contents', homepage_contents)
            statepage_contents=  response.POST.get('statepagecontents')
            create_root_file('State Page Contents', statepage_contents)
            countypage_contents=  response.POST.get('countypagecontents')
            create_root_file('County Page Contents', countypage_contents)
            citypage_contents=  response.POST.get('citypagecontents')
            create_root_file('City Page Contents', citypage_contents)
            run_script='No'
            
        except: 
            options_modify=  response.POST.get('optionsmodify')
            info_data=  response.POST.get('infodata')
            run_script=  response.POST.get('runscript')
            
            if options_modify== 'Domain Site':
                create_root_file('Domain Site', info_data)
            elif options_modify== 'Site Name':
                create_root_file('Site Name', info_data)
            elif options_modify== 'Phone Number':
                create_root_file('Phone Number', info_data)
            elif options_modify== 'Page Color':
                create_root_file('Page Color', info_data)
            elif options_modify== 'Box Page Color':
                create_root_file('Box Page Color', info_data)
            elif options_modify== 'Site Root':
                create_root_file('Site Root', info_data)
            elif options_modify== 'Population limit':
                create_root_file('Population limit', info_data)
            elif options_modify== 'Page Format':
                create_root_file('Page Format', info_data)
            elif options_modify== 'Long Form':
                create_root_file('Long Form', info_data)
            elif options_modify== 'Short Form':
                create_root_file('Short Form', info_data)
            elif options_modify== 'Do you need County Page':
                create_root_file('Do you need County Page', info_data)
            elif options_modify== 'Home Page Meta title':
                create_root_file('Home Page Meta title', info_data)
            elif options_modify== 'Home Page Meta Description':
                create_root_file('Home Page Meta Description', info_data)
            elif options_modify== 'State Page Meta Title':
                create_root_file('State Page Meta Title', info_data)
            elif options_modify== 'State Page Meta Description':
                create_root_file('State Page Meta Description', info_data)
            elif options_modify== 'Selected and Excluded State':
                create_root_file('Selected and Excluded State', info_data)
            elif options_modify== 'City Page Meta Title':
                create_root_file('City Page Meta Title', info_data)
            elif options_modify== 'City Page Meta Description':
                create_root_file('City Page Meta Description', info_data)
            elif options_modify== 'County Page Meta Title':
                create_root_file('County Page Meta Title', info_data)
            elif options_modify== 'County Page Meta Description':
                create_root_file('County Page Meta Description', info_data)
            elif options_modify== 'Home Page Contents':
                create_root_file('Home Page Contents', info_data)
            elif options_modify== 'State Page Contents':
                create_root_file('State Page Contents', info_data)
            elif options_modify== 'County Page Contents':
                create_root_file('County Page Contents', info_data)
            elif options_modify== 'City Page Contents':
                create_root_file('City Page Contents', info_data)


        domainsite_name= read_root_file('Domain Site')
        site_name = read_root_file('Site Name')
        phone_number= read_root_file('Phone Number')
        page_color= read_root_file('Page Color')
        boxp_agecolor= read_root_file('Box Page Color')
        site_root= read_root_file('Site Root')
        rewrite_css(page_color, boxp_agecolor)
        popula_tions= read_root_file('Population limit')
        selected_pages= read_root_file('Page Format')
        Long_formurl= read_root_file('Long Form')
        shortformurl= read_root_file('Short Form')
        radioselect= read_root_file('Do you need County Page')
        metatitle_homepage= read_root_file('Home Page Meta title')
        metadescription_homepage= read_root_file('Home Page Meta Description')
        metatitle_statepage= read_root_file('State Page Meta Title')
        metadescription_statepage= read_root_file('State Page Meta Description')
        Checkboxselected= read_root_file('Selected and Excluded State').split(',')
        Checkboxselected = list(filter(None, Checkboxselected))

        split_metatitle_citypage= read_root_file('City Page Meta Title').split('@@@')
        picker_metatitle_citypage= random.randint(0, len(split_metatitle_citypage)-1)
        metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage]
        
        split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
        picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
        metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage]

        split_metatitle_countypage= read_root_file('County Page Meta Title').split('@@@')
        picker_metatitle_countypage= random.randint(0, len(split_metatitle_countypage)-1)
        metatitle_countypage= split_metatitle_countypage[picker_metatitle_countypage]

        split_metadescription_countypage= read_root_file('County Page Meta Description').split('@@@')
        picker_metadescription_countypage= random.randint(0, len(split_metadescription_countypage)-1)
        metadescription_countypage= split_metadescription_countypage[picker_metadescription_countypage]

        randomize_image= read_root_file('Randomized image File root').split(',')
        randomize_image = list(filter(None, randomize_image))
        homepage_contents= read_root_file('Home Page Contents')
        statepage_contents= read_root_file('State Page Contents')

        split_countypage_contents= read_root_file('County Page Contents').split('@@@')
        picker_countypage_contents= random.randint(0, len(split_countypage_contents)-1)
        countypage_contents= split_countypage_contents[picker_countypage_contents]

        split_citypage_contents= read_root_file('City Page Contents').split('@@@')
        picker_citypage_contents= random.randint(0, len(split_citypage_contents)-1)
        citypage_contents= split_citypage_contents[picker_citypage_contents]
        
        if 'Yes'== radioselect:
            home_page(phone_number, Long_formurl, shortformurl, randomize_image, homepage_contents, metatitle_homepage, metadescription_homepage, domainsite_name, site_name, Checkboxselected, selected_pages, popula_tions)
            state_page(phone_number, Long_formurl, shortformurl, randomize_image, statepage_contents, metatitle_statepage, metadescription_statepage, domainsite_name, site_name, popula_tions)
            city_page(metatitle_citypage, metadescription_citypage, domainsite_name, site_name, popula_tions)
            county_page(metatitle_countypage, metadescription_countypage, domainsite_name, site_name, popula_tions)
            contact_us(metatitle_homepage, domainsite_name, site_name)
        else:
            home_page(phone_number, Long_formurl, shortformurl, randomize_image, homepage_contents, metatitle_homepage, metadescription_homepage, domainsite_name, site_name, Checkboxselected, selected_pages, popula_tions)
            state_page(phone_number, Long_formurl, shortformurl, randomize_image, statepage_contents, metatitle_statepage, metadescription_statepage, domainsite_name, site_name, popula_tions)
            city_page(metatitle_citypage, metadescription_citypage, domainsite_name, site_name, popula_tions)
            contact_us(metatitle_homepage, domainsite_name, site_name)
            
            
        
        if run_script== 'Yes':
            create_pages_directory(domainsite_name, popula_tions, selected_pages, radioselect, Checkboxselected)
        
        

   
    return render(response, "zeodigital/softadmin/index1.html", {
        
    })

'''
home_url_py= '''
from django.urls import path

from . import views

urlpatterns= [
    path("", views.index, name='index'),
    path("zeoadmin/", views.softadmin, name='softadmin'),
    path("state/", views.state, name='state'),
    path("city/", views.city, name='city'),
    path("county/", views.county, name='county'),
    path("contact-us/", views.contact, name='contact'),
    
]
'''

list_template='''
        <ul class="" style="list-style-type: disc !important;">
        aloomalistdata
        </ul>
'''

comments_template= '''
        <div class="col-m-4">
            <i class='fa-solid fa-star' style="color: gold; font-size: 20px;"></i><i class='fa-solid fa-star' style="color: gold; font-size: 20px;"></i><i class='fa-solid fa-star' style="color: gold; font-size: 20px;"></i><i class='fa-solid fa-star' style="color: gold; font-size: 20px;"></i><i class='fa-solid fa-star' style="color: gold; font-size: 20px;"></i>
            <p class="template4 palooma">aloomaidcomments</p>
            <label for="" style="float: right;">aloomaidcommenname</label>
        </div>
'''

home_page_template= '''
        <div class="col-m-2" id="aloomafotter1">
            <div id="aloomafotter2"><a href="aloomaidstaturl" id="aloomafotter">aloomaidstate</a></div>
        </div>
'''
replace_long_form= '''<div class="col-m-6 col-l-6">
                aloomalongform
            </div>
'''

replace_short_form= '''<div class="col-m-4 col-l-4">
                    aloomashortform
                </div>
'''

def short_code_state(state_repl):
    search_categories = open("zeotech/static/aloomaspecial/content/uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
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

def get_contents(selected_contents, split_info):
    header= selected_contents.split(f'{split_info}')[0].replace('<br>', '')
    paragraph= selected_contents.split(f'{split_info}')[1].replace('<br><br>', '<br>', 1)
    if '<list>' in paragraph:
        part_paragraph= paragraph.split('<list>')[0]
        list_paragraph= paragraph.split('<list>')[1].replace('<br>', '').split('^^')
        append_all_list= ''
        for list_paragrap in list_paragraph:
            append_all_list+= f'<li class="">{list_paragrap}</li>'
        second_part= list_template.replace('aloomalistdata', append_all_list)
        main_paragraph= f'{part_paragraph}'
    else:
        main_paragraph= paragraph
        second_part= ''
    return header, main_paragraph, second_part

def clean_text(hrml_cre):
    sss= hrml_cre
    start_index = sss.find("{")
    while start_index != -1:
        end_index = sss.find("}", start_index+1)
        if end_index != -1:
            occurence= sss[start_index+1:end_index]
            
            if '()' in occurence:
                start_index = sss.find("{", start_index+1)
                continue
            else:
                pass
            
            seen_replace= '{'+ occurence + '}'
            if '|' in str(occurence):
                randy= len(occurence.split('|')) -1
                new_data_spl= occurence.split('|')
                ran_chr= random.choice([0,randy])
                final_rela= new_data_spl[ran_chr]
            else:
                final_rela= occurence
            sss= sss.replace(seen_replace, final_rela)
                
        start_index = sss.find("{", start_index+1)
    return sss.replace('{', '').replace('}', '')

def handle_template(two_options1, two_options2):
    single_template_checker= random.choice([two_options1, two_options2])
    return single_template_checker

def generate_contents_body(phone_number, long_form, short_form, image_list, data, site_name):
    data= data.replace('&amp;', 'and').replace('\n', '<br>').replace('<br><br><br>', '<br>').strip()
    my_nini=0
    data= clean_text(data)
    used_image=[]

    all_refomated_body= ''
    all_stat= phone_number.replace(' ','').replace('(','').replace(')','').replace('-','')
    phone_number_url= f'tel:{all_stat}'
    all_data= data.split('$$')
    for all_dat in all_data:
        single_template_checker=''
        multiple_template_checker= ''
        selected_contents= all_dat.strip().replace('\n', '')
        if '%%' in selected_contents:
            multiple_checker= len(selected_contents.split('%%'))
            if '<review>' in selected_contents:
                multiple_template_checker= '<template9>'
            elif multiple_checker == 2:
                multiple_template_checker= '<template7>'
            elif multiple_checker == 3:
                multiple_template_checker= '<template5>'
            
        else:
            if '<contact>' in selected_contents:
                single_template_checker= '<template8>'
            else:
                if my_nini== 0:
                    single_template_checker= handle_template('<template1>', '<template4>')
                elif my_nini== 2:
                    single_template_checker= handle_template('<template2>', '<template3>')
                else:
                    single_template_checker= handle_template('<template6>', '<template6.1>')
                my_nini+=1

        if '<template1>' == single_template_checker:
            # template 1-- just one subtopic
            header, main_paragraph, second_part= get_contents(selected_contents, '<h2>')
            template_data_1 = open("zeotech/static/aloomaspecial/template1.txt", "r", encoding="utf-8-sig").read()
            if len(long_form) > 3:
                template_data_1= template_data_1.replace('aloomaidheader', header).replace('aloomaidparagraph', main_paragraph).replace('aloomalistdata', second_part).replace('aloomalongform', long_form).replace('aloomashortform', short_form).replace('aloomaidphonenumberful', phone_number).replace('aloomaidphonenumberurl', phone_number_url)
            else:
                template_data_1= template_data_1.replace('aloomaidheader', header).replace('aloomaidparagraph', main_paragraph).replace('aloomalistdata', second_part).replace(replace_long_form, '').replace('col-m-6 col-l-6', '').replace('aloomaidphonenumberful', phone_number).replace('aloomaidphonenumberurl', phone_number_url)
            all_refomated_body+= template_data_1
        elif '<template2>' == single_template_checker:
            # template 2 -- single subtopic with a list
            header, main_paragraph, second_part= get_contents(selected_contents, '<h2>')
            template_data_1 = open("zeotech/static/aloomaspecial/template2.txt", "r", encoding="utf-8-sig").read()
            if len(short_form) > 3:
                template_data_1= template_data_1.replace('aloomaidheader', header).replace('aloomaidparagraph', main_paragraph).replace('aloomalistdata', second_part).replace('aloomalongform', long_form).replace('aloomashortform', short_form).replace('aloomaidphonenumberful', phone_number).replace('aloomaidphonenumberurl', phone_number_url)
            else:
                template_data_1= template_data_1.replace('aloomaidheader', header).replace('aloomaidparagraph', main_paragraph).replace('aloomalistdata', second_part).replace(replace_short_form, '').replace('col-m-8 col-l-8', '').replace('aloomaidphonenumberful', phone_number).replace('aloomaidphonenumberurl', phone_number_url)
            all_refomated_body+= template_data_1
        elif '<template3>' == single_template_checker:
            # template 3 -- single subtopic with a list
            header, main_paragraph, second_part= get_contents(selected_contents, '<h2>')
            template_data_1 = open("zeotech/static/aloomaspecial/template3.txt", "r", encoding="utf-8-sig").read()
            if len(short_form) > 3:
                template_data_1= template_data_1.replace('aloomaidheader', header).replace('aloomaidparagraph', main_paragraph).replace('aloomalistdata', second_part).replace('aloomalongform', long_form).replace('aloomashortform', short_form).replace('aloomaidphonenumberful', phone_number).replace('aloomaidphonenumberurl', phone_number_url)
            else:
                template_data_1= template_data_1.replace('aloomaidheader', header).replace('aloomaidparagraph', main_paragraph).replace('aloomalistdata', second_part).replace(replace_short_form, '').replace('col-m-8 col-l-8', '').replace('aloomaidphonenumberful', phone_number).replace('aloomaidphonenumberurl', phone_number_url)
            all_refomated_body+= template_data_1
        elif '<template4>' == single_template_checker:
            # template 4-- just one subtopic
            header, main_paragraph, second_part= get_contents(selected_contents, '<h2>')
            template_data_1 = open("zeotech/static/aloomaspecial/template4.txt", "r", encoding="utf-8-sig").read()
            if len(long_form) > 3:
                template_data_1= template_data_1.replace('aloomaidheader', header).replace('aloomaidparagraph', main_paragraph).replace('aloomalistdata', second_part).replace('aloomalongform', long_form).replace('aloomashortform', short_form).replace('aloomaidphonenumberful', phone_number).replace('aloomaidphonenumberurl', phone_number_url)
            else:
                template_data_1= template_data_1.replace('aloomaidheader', header).replace('aloomaidparagraph', main_paragraph).replace('aloomalistdata', second_part).replace(replace_long_form, '').replace('col-m-6 col-l-6', '').replace('aloomaidphonenumberful', phone_number).replace('aloomaidphonenumberurl', phone_number_url)
            all_refomated_body+= template_data_1
        elif '<template5>' == multiple_template_checker:
            # About us template 5--- just 3 subtopic
            template_data_1 = open("zeotech/static/aloomaspecial/template5.txt", "r", encoding="utf-8-sig").read()
            all_data_split= selected_contents.split('%%')
            for all_data_spli in all_data_split:
                header, main_paragraph, second_part= get_contents(all_data_spli, '<h2>')
                template_data_1= template_data_1.replace('aloomaidheader', header, 1).replace('aloomaidparagraph', main_paragraph, 1).replace('aloomalistdata', second_part, 1).replace('aloomalongform', long_form, 1).replace('aloomashortform', short_form, 1).replace('aloomaidphonenumberful', phone_number).replace('aloomaidphonenumberurl', phone_number_url)
            all_refomated_body+= template_data_1
        elif '<template6>' == single_template_checker:
            # template 6--- just 1 subtopic and image
            counter=0
            while True:
                counter+=1
                pick_image= random.choice(image_list)
                if pick_image in used_image:
                    pass
                else:
                    break
                if counter ==20:
                    break
            
            alt_text= pick_image.split('/')[2].split('.')[0]
            header, main_paragraph, second_part= get_contents(selected_contents, '<h2>')
            template_data_1 = open("zeotech/static/aloomaspecial/template6.txt", "r", encoding="utf-8-sig").read()
            template_data_1= template_data_1.replace('aloomaidheader', header).replace('aloomaidparagraph', main_paragraph).replace('aloomalistdata', second_part).replace('aloomalongform', long_form).replace('aloomashortform', short_form).replace('aloomaidphonenumberful', phone_number).replace('aloomaidphonenumberurl', phone_number_url).replace('aloomaidpickimage', pick_image).replace('aloomaidalttitle', alt_text)
            all_refomated_body+= template_data_1
            used_image.append(pick_image)
        elif '<template6.1>' == single_template_checker:
            # template 6--- just 1 subtopic and image
            counter=0
            while True:
                counter+=1
                pick_image= random.choice(image_list)
                if pick_image in used_image:
                    pass
                else:
                    break
                if counter ==20:
                    break
            alt_text= pick_image.split('/')[2].split('.')[0]
            header, main_paragraph, second_part= get_contents(selected_contents, '<h2>')
            template_data_1 = open("zeotech/static/aloomaspecial/template6.txt", "r", encoding="utf-8-sig").read()
            template_data_1= template_data_1.replace('aloomaidheader', header).replace('aloomaidparagraph', main_paragraph).replace('aloomalistdata', second_part).replace('aloomalongform', long_form).replace('aloomashortform', short_form).replace('aloomaidphonenumberful', phone_number).replace('aloomaidphonenumberurl', phone_number_url).replace('aloomaidpickimage', pick_image).replace('aloomaidalttitle', alt_text)
            all_refomated_body+= template_data_1
            used_image.append(pick_image)
        elif '<template7>' == multiple_template_checker:
            # template 7 -- two subtopic with a list and image
            counter=0
            while True:
                counter+=1
                pick_image= random.choice(image_list)
                if pick_image in used_image:
                    pass
                else:
                    break
                if counter ==20:
                    break
            used_image.append(pick_image)
            counter1=0
            while True:
                counter1+=1
                pick_image1= random.choice(image_list)
                if pick_image1 in used_image:
                    pass
                else:
                    break
                if counter1 ==20:
                    break
            alt_text= pick_image.split('/')[2].split('.')[0]
            alt_text1= pick_image1.split('/')[2].split('.')[0]
            template_data_1 = open("zeotech/static/aloomaspecial/template7.txt", "r", encoding="utf-8-sig").read()
            all_data_split= selected_contents.split('%%')
            for all_data_spli in all_data_split:
                header, main_paragraph, second_part= get_contents(all_data_spli, '<h2>')
                template_data_1= template_data_1.replace('aloomaidheader', header, 1).replace('aloomaidparagraph', main_paragraph, 1).replace('aloomalistdata', second_part, 1).replace('aloomalongform', long_form, 1).replace('aloomashortform', short_form, 1).replace('aloomaidphonenumberful', phone_number).replace('aloomaidphonenumberurl', phone_number_url).replace('aloomaidpickimage', pick_image, 1).replace('aloomaidpickimage', pick_image1, 1).replace('aloomaidalttitle', alt_text, 1).replace('aloomaidalttitle', alt_text1, 1)
            all_refomated_body+= template_data_1
            used_image.append(pick_image1)
        elif '<template8>' == single_template_checker:
            # contact template 8-- just 1 subtopic
            header, main_paragraph, second_part= get_contents(selected_contents, '<h2>')
            template_data_1 = open("zeotech/static/aloomaspecial/template8.txt", "r", encoding="utf-8-sig").read()
            template_data_1= template_data_1.replace('aloomaidheader', header).replace('aloomaidparagraph', main_paragraph).replace('aloomalistdata', second_part).replace('aloomalongform', long_form).replace('aloomashortform', short_form).replace('aloomaidphonenumberful', phone_number).replace('aloomaidphonenumberurl', phone_number_url).replace('<contact>', '')
            all_refomated_body+= template_data_1
        elif '<template9>' == multiple_template_checker:
            # Reviews 
            all_cmments_data= ''
            all_data_split= selected_contents.split('%%')
            for all_data_spli in all_data_split:
                comments, costumername, second_part= get_contents(all_data_spli, '<h2>')
                all_cmments_data+= comments_template.replace('aloomaidcomments', comments).replace('aloomaidcommenname', costumername)
            template_data_1 = open("zeotech/static/aloomaspecial/template9.txt", "r", encoding="utf-8-sig").read()
            template_data_1= template_data_1.replace('aloomaidallcomments', all_cmments_data).replace('<review>', '')
            all_refomated_body+= template_data_1

    return all_refomated_body

def home_page_footer(population_limit):
    template_data_2 = open("zeotech/static/aloomaspecial/home_page.txt", "r", encoding="utf-8-sig").read()
    data_plus_plus= open("zeotech/static/aloomaspecial/content/state.txt", "r", encoding="utf-8-sig").readlines()
    data_plus_plus1= open("zeotech/static/aloomaspecial/content/uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
    higest= len(data_plus_plus1)-1

    all_foter_homepage= ''
    for data_plus_plu in data_plus_plus:
        state= data_plus_plu.strip()
        short_url= short_code_state(state).lower()
        replaced_data= home_page_template.replace('aloomaidstate', state).replace('aloomaidstaturl', f'/{short_url}')
        all_foter_homepage += replaced_data

    selected_row=[]
    id1=0
    all_foter_homepage1= ''
    for data_plus_plu1 in range(higest):
        while True:
            picker= random.randint(0,higest)
            if picker in selected_row:
                pass
            else:
                break
    
        
        selected_row.append(picker)
        split_city= data_plus_plus1[picker].replace('\n', '').split(',')

 
        city_p= split_city[0].title().replace('ï»¿', '').replace('"', '')
        sub_ciy= split_city[0].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
        link_city= str(sub_ciy.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
        state_p= split_city[3].title().replace('ï»¿', '').replace('"', '')
        population= int(split_city[8])
        if population < int(population_limit):
            continue

        
        short_url= short_code_state(state_p).lower()
        replaced_data1= home_page_template.replace('aloomaidstaturl', f'/{short_url}/{link_city}/').replace('aloomaidstate', city_p)
        all_foter_homepage1 += replaced_data1
        if data_plus_plu1==50:
            break
        id1+=1
        if id1==50:
            break
    final_fotter= template_data_2.replace('aloomaidallfotter', all_foter_homepage).replace('aloomaidallfottecity', all_foter_homepage1)
    return final_fotter

def selected_home_page_footer(Checkboxselected, population_limit):
    template_data_2 = open("zeotech/static/aloomaspecial/home_page.txt", "r", encoding="utf-8-sig").read()
    data_plus_plus= open("zeotech/static/aloomaspecial/content/state.txt", "r", encoding="utf-8-sig").readlines()
    data_plus_plus1= open("zeotech/static/aloomaspecial/content/uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
    higest= len(data_plus_plus1)-1
    id1=0
    all_foter_homepage= ''
    for data_plus_plu in data_plus_plus:
        state= data_plus_plu.strip()
        short_url= short_code_state(state).lower()
        if state in Checkboxselected:
            pass
        else:
            continue
        replaced_data= home_page_template.replace('aloomaidstate', state).replace('aloomaidstaturl', f'/{short_url}')
        all_foter_homepage += replaced_data

    selected_row=[]
    all_foter_homepage1= ''
    for data_plus_plu1 in range(higest):
        while True:
            picker= random.randint(0,higest)
            if picker in selected_row:
                pass
            else:
                break
        selected_row.append(picker)
        split_city= data_plus_plus1[picker].replace('\n', '').split(',')

        
        city_p= split_city[0].title().replace('ï»¿', '').replace('"', '')
        sub_ciy= split_city[0].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
        link_city= str(sub_ciy.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
        state_p= split_city[3].title().replace('ï»¿', '').replace('"', '')
        population= int(split_city[8])
        if population < int(population_limit):
            continue


        
        short_url= short_code_state(state_p).lower()
        if state_p in Checkboxselected:
            pass
        else:
            continue
        replaced_data1= home_page_template.replace('aloomaidstaturl', f'/{short_url}/{link_city}/').replace('aloomaidstate', city_p)
        all_foter_homepage1 += replaced_data1
        if data_plus_plu1==50:
            break
        id1+=1
        if id1==50:
            break
    final_fotter= template_data_2.replace('aloomaidallfotter', all_foter_homepage).replace('aloomaidallfottecity', all_foter_homepage1)
    return final_fotter

def excluded_home_page_footer(Checkboxselected, population_limit):
    template_data_2 = open("zeotech/static/aloomaspecial/home_page.txt", "r", encoding="utf-8-sig").read()
    data_plus_plus= open("zeotech/static/aloomaspecial/content/state.txt", "r", encoding="utf-8-sig").readlines()
    data_plus_plus1= open("zeotech/static/aloomaspecial/content/city.txt", "r", encoding="utf-8-sig").readlines()
    higest= len(data_plus_plus1)-1
    id1=0
    all_foter_homepage= ''
    for data_plus_plu in data_plus_plus:
        state= data_plus_plu.strip()
        short_url= short_code_state(state).lower()
        if state in Checkboxselected:
            continue
        else:
            pass
        replaced_data= home_page_template.replace('aloomaidstate', state).replace('aloomaidstaturl', f'/{short_url}')
        all_foter_homepage += replaced_data

    selected_row=[]
    all_foter_homepage1= ''
    for data_plus_plu1 in range(higest):
        while True:
            picker= random.randint(0,higest)
            if picker in selected_row:
                pass
            else:
                break
        selected_row.append(picker)
        split_city= data_plus_plus1[picker].replace('\n', '').split(',')

        city_p= split_city[0].title().replace('ï»¿', '').replace('"', '')
        sub_ciy= split_city[0].replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
        link_city= str(sub_ciy.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
        state_p= split_city[3].title().replace('ï»¿', '').replace('"', '')
        population= int(split_city[8])
        if population < int(population_limit):
            continue
        
        short_url= short_code_state(state_p).lower()
        if state_p in Checkboxselected:
            continue
        else:
            pass
        replaced_data1= home_page_template.replace('aloomaidstaturl', f'/{short_url}/{link_city}/').replace('aloomaidstate', city_p)
        all_foter_homepage1 += replaced_data1
        if data_plus_plu1==50:
            break
        id1+=1
        if id1==50:
            break
    final_fotter= template_data_2.replace('aloomaidallfotter', all_foter_homepage).replace('aloomaidallfottecity', all_foter_homepage1)
    return final_fotter


def home_page_html_data(metatitle_homepage, metadescription_homepage, domainsite_name, site_name, all_refomated_body):
    template_data_2 = open("zeotech/templates/zeodigital/allrequiredpages/homepage.html", "r", encoding="utf-8-sig").read().replace('</head>', '<link rel="stylesheet" href="static/aloomaspecial/alooma.css"><link rel="stylesheet" href="static/aloomaspecial/alooma2.css"></head>').replace('</body>', '<script src="https://kit.fontawesome.com/c4c9a6665b.js" crossorigin="anonymous"></script></body>', 1).replace('col-sm', 'col-s').replace('col-md', 'col-m').replace('col-lg', 'col-l')
    template_data_3 = open("zeotech/static/aloomaspecial/metatitledescription.txt", "r", encoding="utf-8-sig").read()
    complate_header= template_data_3.replace('aloomaidtitle', metatitle_homepage).replace('aloomaiddescription', metadescription_homepage).replace('aloomaiddomainname', f'https://{domainsite_name}/').replace('aloomaidsitename', site_name)
    
    return template_data_2.replace('<title></title>', complate_header).replace('aloomaidbody', all_refomated_body)

def home_page(phone_number, long_form, short_form, image_list, data, metatitle_homepage, metadescription_homepage, domainsite_name, site_name, Checkboxselected, selected_pages, population_limit):
    all_refomated_body = generate_contents_body(phone_number, long_form, short_form, image_list, data, site_name)
    if 'All Pages' == selected_pages:
        all_refomated_body += home_page_footer(population_limit)
    elif 'Selected State Pages' == selected_pages:
        all_refomated_body += selected_home_page_footer(Checkboxselected, population_limit)
    elif 'Excluded State Pages' == selected_pages:
        all_refomated_body += excluded_home_page_footer(Checkboxselected, population_limit)
    
    op2= home_page_html_data(metatitle_homepage, metadescription_homepage, domainsite_name, site_name, all_refomated_body)
    fp = open('zeotech/templates/zeodigital/index.html', "w", encoding='utf-8-sig')
    fp.writelines(op2)
    fp.close()

def state_page_html_data(metatitle_statepage, metadescription_statepage, domainsite_name, site_name, all_refomated_body):
    template_data_2 = open("zeotech/templates/zeodigital/state.html", "r", encoding="utf-8-sig").read().replace('</head>', '<link rel="stylesheet" href="../static/aloomaspecial/alooma.css"><link rel="stylesheet" href="../static/aloomaspecial/alooma2.css"></head>').replace('</body>', '<script src="https://kit.fontawesome.com/c4c9a6665b.js" crossorigin="anonymous"></script></body>', 1).replace('col-sm', 'col-s').replace('col-md', 'col-m').replace('col-lg', 'col-l')
    template_data_3 = open("zeotech/static/aloomaspecial/metatitledescription.txt", "r", encoding="utf-8-sig").read()
    
    complate_header= template_data_3.replace('aloomaidtitle', metatitle_statepage).replace('aloomaiddescription', metadescription_statepage).replace('aloomaidsitename', site_name)
    
    return template_data_2.replace('<title></title>', complate_header).replace('aloomaidbody', all_refomated_body)

def state_page(phone_number, long_form, short_form, image_list, data, metatitle_statepage, metadescription_statepage, domainsite_name, site_name, population_limit):
    if len(str(data).split('$$')) >= 2:
        all_refomated_body = generate_contents_body(phone_number, long_form, short_form, image_list, data, site_name)
    else:
        used_image=[]
        all_refomated_body= ''
        kaau= phone_number.replace(' ','').replace('(','').replace(')','').replace('-','')
        phone_number_url= f'tel:{kaau}'
        counter=0
        while True:
            counter+=1
            pick_image= random.choice(image_list)
            if pick_image in used_image:
                pass
            else:
                break
            if counter ==20:
                break
        header, main_paragraph, second_part= get_contents(data, '<h2>')
        template_data_1 = open("zeotech/static/aloomaspecial/template10.txt", "r", encoding="utf-8-sig").read()
        template_data_1= template_data_1.replace('aloomaidheader', header).replace('aloomaidparagraph', main_paragraph).replace('aloomalistdata', second_part).replace('aloomalongform', long_form).replace('aloomashortform', short_form).replace('aloomaidphonenumberful', phone_number).replace('aloomaidphonenumberurl', phone_number_url).replace('aloomaidpickimage', pick_image)
        all_refomated_body+= template_data_1
    template_data_5 = open("zeotech/static/aloomaspecial/state_footer.txt", "r", encoding="utf-8-sig").read()
    all_refomated_body+= template_data_5
    op2= state_page_html_data(metatitle_statepage, metadescription_statepage, domainsite_name, site_name, all_refomated_body).replace('"static/', '"../static/')
    fp = open('zeotech/templates/zeodigital/allrequiredpages/state.html', "w", encoding='utf-8-sig')
    fp.writelines(op2)
    fp.close()

def contact_us_html_data(metatitle_homepage, domainsite_name, site_name):
    template_data_2 = open("zeotech/templates/zeodigital/contact-us.html", "r", encoding="utf-8-sig").read().replace('</head>', '<link rel="stylesheet" href="static/aloomaspecial/alooma.css"><link rel="stylesheet" href="static/aloomaspecial/alooma2.css"></head>').replace('</body>', '<script src="https://kit.fontawesome.com/c4c9a6665b.js" crossorigin="anonymous"></script></body>', 1).replace('col-sm', 'col-s').replace('col-md', 'col-m').replace('col-lg', 'col-l')
    template_data_3 = open("zeotech/static/aloomaspecial/metatitledescription.txt", "r", encoding="utf-8-sig").read()
    complate_header= template_data_3.replace('aloomaidtitle', metatitle_homepage).replace('aloomaiddescription', '').replace('aloomaiddomainname', f'https://{domainsite_name}/contact-us/').replace('aloomaidsitename', site_name)
    
    return template_data_2.replace('<title></title>', complate_header)

def contact_us(metatitle_homepage, domainsite_name, site_name):
    op2= contact_us_html_data(metatitle_homepage, domainsite_name, site_name).replace('"static/', '"../static/')
    fp = open('zeotech/templates/zeodigital/contact-us.html', "w", encoding='utf-8-sig')
    fp.writelines(op2)
    fp.close()



def city_page_html_data(metatitle_citypage, metadescription_citypage, domainsite_name, site_name, all_refomated_body):
    template_data_2 = open("zeotech/templates/zeodigital/state.html", "r", encoding="utf-8-sig").read().replace('</head>', '<link rel="stylesheet" href="../static/aloomaspecial/alooma.css"><link rel="stylesheet" href="../static/aloomaspecial/alooma2.css"></head>').replace('</body>', '<script src="https://kit.fontawesome.com/c4c9a6665b.js" crossorigin="anonymous"></script></body>', 1).replace('col-sm', 'col-s').replace('col-md', 'col-m').replace('col-lg', 'col-l')
    template_data_3 = open("zeotech/static/aloomaspecial/metatitledescription.txt", "r", encoding="utf-8-sig").read()
    
    complate_header= template_data_3.replace('aloomaidtitle', '{{aloomaidtitle}}').replace('aloomaiddescription', '{{aloomaiddescription}}').replace('aloomaidsitename', site_name)
    
    return template_data_2.replace('<title></title>', complate_header).replace('aloomaidbody', all_refomated_body)


def city_page(metatitle_citypage, metadescription_citypage, domainsite_name, site_name, population_limit):
    all_refomated_body= '{{aloomaidbody}}\n'

    template_data_2 = open("zeotech/static/aloomaspecial/city_footer.txt", "r", encoding="utf-8-sig").read()
    all_refomated_body += template_data_2
    op2= city_page_html_data(metatitle_citypage, metadescription_citypage, domainsite_name, site_name, all_refomated_body)
    fp = open('zeotech/templates/zeodigital/allrequiredpages/city.html', "w", encoding='utf-8-sig')
    fp.writelines(op2)
    fp.close()


def county_page_html_data(metatitle_countypage, metadescription_countypage, domainsite_name, site_name, all_refomated_body):
    template_data_2 = open("zeotech/templates/zeodigital/state.html", "r", encoding="utf-8-sig").read().replace('</head>', '<link rel="stylesheet" href="../static/aloomaspecial/alooma.css"><link rel="stylesheet" href="../static/aloomaspecial/alooma2.css"></head>').replace('</body>', '<script src="https://kit.fontawesome.com/c4c9a6665b.js" crossorigin="anonymous"></script></body>', 1).replace('col-sm', 'col-s').replace('col-md', 'col-m').replace('col-lg', 'col-l')
    template_data_3 = open("zeotech/static/aloomaspecial/metatitledescription.txt", "r", encoding="utf-8-sig").read()
    
    complate_header= template_data_3.replace('aloomaidtitle', '{{aloomaidtitle}}').replace('aloomaiddescription', '{{aloomaiddescription}}').replace('aloomaidsitename', site_name)
    
    return template_data_2.replace('<title></title>', complate_header).replace('aloomaidbody', all_refomated_body)


def county_page(metatitle_countypage, metadescription_countypage, domainsite_name, site_name, population_limit):
    all_refomated_body= '{{aloomaidbody}}\n'

    template_data_2 = open("zeotech/static/aloomaspecial/county_footer.txt", "r", encoding="utf-8-sig").read()
    all_refomated_body += template_data_2
    op2= county_page_html_data(metatitle_countypage, metadescription_countypage, domainsite_name, site_name, all_refomated_body)
    fp = open('zeotech/templates/zeodigital/allrequiredpages/county.html', "w", encoding='utf-8-sig')
    fp.writelines(op2)
    fp.close()

def create_home_page_url(home_view_py, home_url_py):
    Good = open("zeotech/views.py", "w", encoding='utf-8-sig')
    Good.write(home_view_py + "\n")
    Good.close()
    Good1 = open("zeotech/urls.py", "w", encoding='utf-8-sig')
    Good1.write(home_url_py + "\n")
    Good1.close()

# home_page('(206) 647-6559', '<iframe src="//leads.polyares.com/?api_key=b45897227445c105815c9bfc451e92eb6357bedc&funnel=1&category=8&step=1&buttons=btn-danger" width="600" height="545" frameborder="0"></iframe>', '<div id="polyares_form_container"  ><div id="polyares_form" style="width: 244px; height: 377px;" class="mx-auto"><iframe src="//leads.polyares.com/?api_key=b45897227445c105815c9bfc451e92eb6357bedc&funnel=5&category=1&buttons=btn-danger" height="100%" width="100%" frameborder="no" scrolling="yes" noresize="true" vspace="0" hspace="0" style="border-radius: 10px; border: 1px solid #333;"></iframe></div></div>', 'static/images/neklesh-img.png,id')
