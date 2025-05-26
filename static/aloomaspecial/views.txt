
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

def index1(response):
    forms= CreateNewList()
    return render(response, "zeodigital/new-jersey/index.html", {
        
    })

def index2(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Trenton, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Trenton, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Trenton, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/trenton/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index3(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Newark, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Newark, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Newark, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/newark/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index4(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Jersey City, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Jersey City, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Jersey City, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/jersey-city/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index5(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Atlantic City, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Atlantic City, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Atlantic City, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/atlantic-city/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index6(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Paterson, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Paterson, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Paterson, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/paterson/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index7(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Elizabeth, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Elizabeth, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Elizabeth, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/elizabeth/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index8(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Vineland, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Vineland, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Vineland, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/vineland/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index9(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Clifton, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Clifton, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Clifton, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/clifton/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index10(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Camden, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Camden, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Camden, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/camden/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index11(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Bayonne, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Bayonne, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Bayonne, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/bayonne/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index12(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Passaic, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Passaic, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Passaic, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/passaic/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index13(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'East Orange, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'East Orange, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'East Orange, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/east-orange/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index14(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Union City, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Union City, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Union City, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/union-city/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index15(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Twin Rivers, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Twin Rivers, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Twin Rivers, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/twin-rivers/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index16(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Hoboken, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Hoboken, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Hoboken, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/hoboken/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index17(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'New Brunswick, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'New Brunswick, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'New Brunswick, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/new-brunswick/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index18(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Perth Amboy, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Perth Amboy, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Perth Amboy, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/perth-amboy/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index19(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Plainfield, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Plainfield, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Plainfield, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/plainfield/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index20(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'West New York, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'West New York, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'West New York, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/west-new-york/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index21(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Sicklerville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Sicklerville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Sicklerville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/sicklerville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index22(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Hackensack, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Hackensack, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Hackensack, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/hackensack/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index23(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Sayreville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Sayreville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Sayreville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/sayreville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index24(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Linden, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Linden, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Linden, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/linden/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index25(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Kearny, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Kearny, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Kearny, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/kearny/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index26(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Fort Lee, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Fort Lee, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Fort Lee, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/fort-lee/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index27(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Fair Lawn, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Fair Lawn, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Fair Lawn, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/fair-lawn/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index28(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Garfield, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Garfield, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Garfield, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/garfield/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index29(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Long Branch, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Long Branch, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Long Branch, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/long-branch/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index30(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Westfield, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Westfield, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Westfield, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/westfield/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index31(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Princeton, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Princeton, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Princeton, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/princeton/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index32(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Rahway, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Rahway, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Rahway, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/rahway/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index33(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Englewood, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Englewood, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Englewood, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/englewood/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index34(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Bergenfield, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Bergenfield, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Bergenfield, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/bergenfield/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index35(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Millville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Millville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Millville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/millville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index36(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Paramus, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Paramus, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Paramus, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/paramus/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index37(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ridgewood, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ridgewood, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ridgewood, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ridgewood/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index38(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Lodi, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Lodi, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Lodi, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/lodi/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index39(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Cliffside Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Cliffside Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Cliffside Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/cliffside-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index40(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Carteret, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Carteret, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Carteret, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/carteret/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index41(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Somerset, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Somerset, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Somerset, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/somerset/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index42(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'South Plainfield, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'South Plainfield, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'South Plainfield, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/south-plainfield/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index43(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'North Plainfield, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'North Plainfield, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'North Plainfield, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/north-plainfield/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index44(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Summit, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Summit, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Summit, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/summit/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index45(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Roselle, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Roselle, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Roselle, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/roselle/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index46(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Hillsborough, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Hillsborough, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Hillsborough, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/hillsborough/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index47(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Parsippany, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Parsippany, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Parsippany, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/parsippany/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index48(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Secaucus, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Secaucus, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Secaucus, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/secaucus/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index49(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Elmwood Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Elmwood Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Elmwood Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/elmwood-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index50(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Lindenwold, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Lindenwold, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Lindenwold, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/lindenwold/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index51(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Pleasantville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Pleasantville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Pleasantville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/pleasantville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index52(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Palisades Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Palisades Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Palisades Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/palisades-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index53(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Glassboro, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Glassboro, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Glassboro, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/glassboro/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index54(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Morristown, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Morristown, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Morristown, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/morristown/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index55(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Hawthorne, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Hawthorne, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Hawthorne, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/hawthorne/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index56(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Preakness, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Preakness, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Preakness, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/preakness/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index57(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Tinton Falls, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Tinton Falls, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Tinton Falls, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/tinton-falls/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index58(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Point Pleasant, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Point Pleasant, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Point Pleasant, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/point-pleasant/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index59(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Harrison, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Harrison, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Harrison, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/harrison/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index60(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Rutherford, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Rutherford, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Rutherford, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/rutherford/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index61(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Colonia, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Colonia, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Colonia, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/colonia/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index62(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Dover, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Dover, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Dover, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/dover/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index63(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Dumont, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Dumont, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Dumont, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/dumont/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index64(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ocean Acres, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ocean Acres, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ocean Acres, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ocean-acres/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index65(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Iselin, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Iselin, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Iselin, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/iselin/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index66(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Avenel, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Avenel, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Avenel, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/avenel/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index67(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'New Milford, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'New Milford, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'New Milford, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/new-milford/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index68(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Madison, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Madison, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Madison, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/madison/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index69(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'North Arlington, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'North Arlington, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'North Arlington, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/north-arlington/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index70(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'South River, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'South River, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'South River, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/south-river/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index71(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Princeton Meadows, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Princeton Meadows, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Princeton Meadows, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/princeton-meadows/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index72(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Springdale, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Springdale, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Springdale, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/springdale/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index73(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Tenafly, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Tenafly, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Tenafly, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/tenafly/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index74(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Asbury Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Asbury Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Asbury Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/asbury-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index75(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Phillipsburg, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Phillipsburg, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Phillipsburg, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/phillipsburg/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index76(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Highland Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Highland Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Highland Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/highland-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index77(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Williamstown, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Williamstown, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Williamstown, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/williamstown/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index78(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Fairview, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Fairview, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Fairview, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/fairview/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index79(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Metuchen, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Metuchen, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Metuchen, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/metuchen/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index80(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ramsey, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ramsey, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ramsey, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ramsey/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index81(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Bradley Gardens, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Bradley Gardens, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Bradley Gardens, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/bradley-gardens/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index82(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Hammonton, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Hammonton, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Hammonton, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/hammonton/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index83(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'West Freehold, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'West Freehold, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'West Freehold, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/west-freehold/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index84(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Middlesex, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Middlesex, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Middlesex, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/middlesex/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index85(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Short Hills, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Short Hills, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Short Hills, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/short-hills/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index86(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Hopatcong, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Hopatcong, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Hopatcong, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/hopatcong/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index87(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Moorestown-Lenola, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Moorestown-Lenola, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Moorestown-Lenola, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/moorestown-lenola/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index88(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Mercerville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Mercerville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Mercerville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/mercerville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index89(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Edgewater, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Edgewater, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Edgewater, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/edgewater/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index90(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Roselle Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Roselle Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Roselle Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/roselle-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index91(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Cherry Hill Mall, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Cherry Hill Mall, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Cherry Hill Mall, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/cherry-hill-mall/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index92(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Westmont, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Westmont, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Westmont, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/westmont/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index93(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Franklin Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Franklin Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Franklin Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/franklin-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index94(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Echelon, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Echelon, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Echelon, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/echelon/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index95(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'New Providence, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'New Providence, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'New Providence, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/new-providence/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index96(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Eatontown, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Eatontown, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Eatontown, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/eatontown/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index97(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ridgefield Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ridgefield Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ridgefield Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ridgefield-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index98(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Fords, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Fords, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Fords, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/fords/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index99(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Holiday City-Berkeley, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Holiday City-Berkeley, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Holiday City-Berkeley, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/holiday-city-berkeley/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index100(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Red Bank, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Red Bank, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Red Bank, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/red-bank/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index101(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Oakland, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Oakland, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Oakland, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/oakland/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index102(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Florham Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Florham Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Florham Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/florham-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index103(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Somerville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Somerville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Somerville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/somerville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index104(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Robertsville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Robertsville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Robertsville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/robertsville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index105(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Hamilton Square, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Hamilton Square, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Hamilton Square, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/hamilton-square/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index106(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Hasbrouck Heights, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Hasbrouck Heights, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Hasbrouck Heights, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/hasbrouck-heights/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index107(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Glen Rock, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Glen Rock, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Glen Rock, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/glen-rock/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index108(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Upper Montclair, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Upper Montclair, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Upper Montclair, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/upper-montclair/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index109(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'River Edge, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'River Edge, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'River Edge, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/river-edge/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index110(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Martinsville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Martinsville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Martinsville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/martinsville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index111(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Guttenberg, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Guttenberg, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Guttenberg, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/guttenberg/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index112(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Wallington, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Wallington, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Wallington, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/wallington/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index113(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Bound Brook, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Bound Brook, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Bound Brook, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/bound-brook/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index114(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ringwood, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ringwood, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ringwood, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ringwood/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index115(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Bellmawr, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Bellmawr, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Bellmawr, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/bellmawr/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index116(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ridgefield, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ridgefield, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ridgefield, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ridgefield/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index117(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Gloucester City, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Gloucester City, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Gloucester City, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/gloucester-city/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index118(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Wanaque, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Wanaque, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Wanaque, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/wanaque/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index119(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Westwood, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Westwood, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Westwood, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/westwood/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index120(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ocean City, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ocean City, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ocean City, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ocean-city/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index121(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Pompton Lakes, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Pompton Lakes, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Pompton Lakes, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/pompton-lakes/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index122(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Franklin Lakes, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Franklin Lakes, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Franklin Lakes, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/franklin-lakes/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index123(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'The Hills, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'The Hills, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'The Hills, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/the-hills/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index124(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Oak Ridge, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Oak Ridge, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Oak Ridge, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/oak-ridge/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index125(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Totowa, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Totowa, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Totowa, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/totowa/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index126(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Little Ferry, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Little Ferry, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Little Ferry, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/little-ferry/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index127(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Lincoln Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Lincoln Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Lincoln Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/lincoln-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index128(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Beachwood, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Beachwood, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Beachwood, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/beachwood/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index129(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Manville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Manville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Manville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/manville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index130(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Pompton Plains, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Pompton Plains, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Pompton Plains, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/pompton-plains/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index131(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Pine Hill, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Pine Hill, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Pine Hill, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/pine-hill/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index132(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Kendall Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Kendall Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Kendall Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/kendall-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index133(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Lake Hopatcong, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Lake Hopatcong, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Lake Hopatcong, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/lake-hopatcong/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index134(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Greentree, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Greentree, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Greentree, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/greentree/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index135(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Marlton, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Marlton, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Marlton, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/marlton/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index136(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Blackwells Mills, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Blackwells Mills, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Blackwells Mills, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/blackwells-mills/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index137(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Somers Point, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Somers Point, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Somers Point, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/somers-point/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index138(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Hackettstown, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Hackettstown, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Hackettstown, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/hackettstown/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index139(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Hillsdale, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Hillsdale, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Hillsdale, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/hillsdale/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index140(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Brookdale, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Brookdale, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Brookdale, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/brookdale/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index141(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Waldwick, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Waldwick, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Waldwick, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/waldwick/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index142(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Woodbury, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Woodbury, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Woodbury, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/woodbury/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index143(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Browns Mills, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Browns Mills, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Browns Mills, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/browns-mills/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index144(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Maywood, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Maywood, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Maywood, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/maywood/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index145(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Kinnelon, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Kinnelon, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Kinnelon, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/kinnelon/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index146(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Lake Hiawatha, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Lake Hiawatha, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Lake Hiawatha, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/lake-hiawatha/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index147(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Budd Lake, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Budd Lake, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Budd Lake, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/budd-lake/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index148(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'East Rutherford, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'East Rutherford, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'East Rutherford, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/east-rutherford/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index149(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Villas, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Villas, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Villas, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/villas/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index150(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Wood-Ridge, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Wood-Ridge, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Wood-Ridge, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/wood-ridge/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index151(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Keansburg, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Keansburg, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Keansburg, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/keansburg/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index152(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Monmouth Junction, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Monmouth Junction, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Monmouth Junction, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/monmouth-junction/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index153(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'White Horse, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'White Horse, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'White Horse, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/white-horse/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index154(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Succasunna, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Succasunna, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Succasunna, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/succasunna/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index155(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Lake Mohawk, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Lake Mohawk, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Lake Mohawk, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/lake-mohawk/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index156(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Matawan, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Matawan, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Matawan, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/matawan/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index157(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ventnor City, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ventnor City, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ventnor City, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ventnor-city/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index158(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'South Amboy, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'South Amboy, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'South Amboy, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/south-amboy/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index159(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Leonia, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Leonia, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Leonia, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/leonia/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index160(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ashland, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ashland, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ashland, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ashland/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index161(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Flanders, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Flanders, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Flanders, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/flanders/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index162(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Pine Lake Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Pine Lake Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Pine Lake Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/pine-lake-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index163(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Smithville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Smithville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Smithville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/smithville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index164(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Cresskill, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Cresskill, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Cresskill, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/cresskill/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index165(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'White Meadow Lake, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'White Meadow Lake, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'White Meadow Lake, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/white-meadow-lake/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index166(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Whippany, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Whippany, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Whippany, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/whippany/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index167(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Absecon, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Absecon, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Absecon, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/absecon/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index168(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Park Ridge, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Park Ridge, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Park Ridge, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/park-ridge/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index169(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Haledon, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Haledon, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Haledon, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/haledon/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index170(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'North Haledon, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'North Haledon, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'North Haledon, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/north-haledon/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index171(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Bogota, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Bogota, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Bogota, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/bogota/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index172(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Clayton, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Clayton, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Clayton, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/clayton/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index173(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Pitman, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Pitman, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Pitman, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/pitman/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index174(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Caldwell, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Caldwell, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Caldwell, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/caldwell/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index175(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Boonton, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Boonton, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Boonton, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/boonton/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index176(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Audubon, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Audubon, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Audubon, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/audubon/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index177(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Mckee City, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Mckee City, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Mckee City, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/mckee-city/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index178(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Closter, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Closter, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Closter, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/closter/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index179(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'West Long Branch, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'West Long Branch, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'West Long Branch, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/west-long-branch/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index180(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Newton, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Newton, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Newton, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/newton/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index181(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Northfield, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Northfield, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Northfield, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/northfield/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index182(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Crestwood Village, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Crestwood Village, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Crestwood Village, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/crestwood-village/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index183(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Montvale, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Montvale, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Montvale, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/montvale/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index184(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Kenilworth, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Kenilworth, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Kenilworth, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/kenilworth/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index185(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'East Franklin, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'East Franklin, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'East Franklin, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/east-franklin/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index186(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Upper Saddle River, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Upper Saddle River, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Upper Saddle River, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/upper-saddle-river/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index187(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Pomona, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Pomona, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Pomona, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/pomona/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index188(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Runnemede, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Runnemede, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Runnemede, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/runnemede/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index189(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Oradell, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Oradell, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Oradell, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/oradell/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index190(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Dayton, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Dayton, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Dayton, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/dayton/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index191(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Spotswood, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Spotswood, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Spotswood, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/spotswood/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index192(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Basking Ridge, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Basking Ridge, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Basking Ridge, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/basking-ridge/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index193(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Butler, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Butler, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Butler, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/butler/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index194(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Madison Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Madison Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Madison Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/madison-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index195(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Atco, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Atco, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Atco, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/atco/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index196(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Fort Dix, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Fort Dix, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Fort Dix, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/fort-dix/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index197(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Brigantine, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Brigantine, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Brigantine, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/brigantine/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index198(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Bernardsville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Bernardsville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Bernardsville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/bernardsville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index199(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Glen Ridge, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Glen Ridge, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Glen Ridge, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/glen-ridge/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index200(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Bloomingdale, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Bloomingdale, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Bloomingdale, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/bloomingdale/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index201(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Fanwood, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Fanwood, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Fanwood, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/fanwood/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index202(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Mystic Island, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Mystic Island, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Mystic Island, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/mystic-island/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index203(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Dunellen, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Dunellen, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Dunellen, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/dunellen/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index204(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Watsessing, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Watsessing, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Watsessing, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/watsessing/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index205(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Berlin, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Berlin, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Berlin, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/berlin/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index206(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Haddon Heights, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Haddon Heights, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Haddon Heights, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/haddon-heights/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index207(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Palmyra, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Palmyra, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Palmyra, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/palmyra/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index208(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Emerson, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Emerson, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Emerson, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/emerson/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index209(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Yorketown, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Yorketown, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Yorketown, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/yorketown/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index210(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Rumson, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Rumson, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Rumson, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/rumson/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index211(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Keyport, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Keyport, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Keyport, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/keyport/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index212(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Wharton, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Wharton, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Wharton, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/wharton/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index213(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Washington, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Washington, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Washington, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/washington/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index214(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Strathmore, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Strathmore, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Strathmore, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/strathmore/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index215(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Rutgers University-Busch Campus, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Rutgers University-Busch Campus, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Rutgers University-Busch Campus, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/rutgers-university-busch-campus/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index216(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Heathcote, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Heathcote, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Heathcote, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/heathcote/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index217(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Midland Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Midland Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Midland Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/midland-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index218(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Barrington, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Barrington, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Barrington, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/barrington/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index219(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Milltown, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Milltown, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Milltown, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/milltown/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index220(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Mountainside, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Mountainside, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Mountainside, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/mountainside/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index221(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Stratford, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Stratford, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Stratford, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/stratford/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index222(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Kingston Estates, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Kingston Estates, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Kingston Estates, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/kingston-estates/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index223(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Allendale, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Allendale, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Allendale, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/allendale/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index224(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Lincroft, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Lincroft, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Lincroft, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/lincroft/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index225(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'North Caldwell, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'North Caldwell, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'North Caldwell, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/north-caldwell/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index226(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Mays Landing, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Mays Landing, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Mays Landing, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/mays-landing/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index227(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ramtown, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ramtown, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ramtown, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ramtown/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index228(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Watchung, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Watchung, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Watchung, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/watchung/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index229(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Green Knoll, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Green Knoll, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Green Knoll, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/green-knoll/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index230(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Carlstadt, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Carlstadt, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Carlstadt, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/carlstadt/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index231(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ramblewood, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ramblewood, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ramblewood, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ramblewood/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index232(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Prospect Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Prospect Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Prospect Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/prospect-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index233(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Laurence Harbor, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Laurence Harbor, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Laurence Harbor, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/laurence-harbor/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index234(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Yardville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Yardville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Yardville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/yardville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index235(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Roseland, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Roseland, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Roseland, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/roseland/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index236(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Fair Haven, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Fair Haven, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Fair Haven, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/fair-haven/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index237(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Paulsboro, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Paulsboro, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Paulsboro, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/paulsboro/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index238(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Oceanport, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Oceanport, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Oceanport, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/oceanport/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index239(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Woodcliff Lake, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Woodcliff Lake, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Woodcliff Lake, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/woodcliff-lake/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index240(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Little Silver, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Little Silver, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Little Silver, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/little-silver/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index241(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Morris Plains, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Morris Plains, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Morris Plains, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/morris-plains/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index242(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Finderne, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Finderne, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Finderne, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/finderne/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index243(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Pine Brook, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Pine Brook, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Pine Brook, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/pine-brook/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index244(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Leisure Village, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Leisure Village, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Leisure Village, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/leisure-village/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index245(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Manasquan, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Manasquan, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Manasquan, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/manasquan/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index246(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Bridgewater Center, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Bridgewater Center, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Bridgewater Center, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/bridgewater-center/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index247(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Packanack Lake, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Packanack Lake, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Packanack Lake, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/packanack-lake/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index248(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Old Tappan, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Old Tappan, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Old Tappan, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/old-tappan/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index249(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Belmar, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Belmar, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Belmar, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/belmar/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index250(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Hightstown, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Hightstown, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Hightstown, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/hightstown/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index251(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Mount Arlington, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Mount Arlington, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Mount Arlington, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/mount-arlington/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index252(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Jamesburg, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Jamesburg, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Jamesburg, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/jamesburg/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index253(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Union Beach, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Union Beach, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Union Beach, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/union-beach/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index254(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Towaco, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Towaco, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Towaco, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/towaco/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index255(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Belle Mead, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Belle Mead, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Belle Mead, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/belle-mead/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index256(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Norwood, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Norwood, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Norwood, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/norwood/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index257(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Franklin Center, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Franklin Center, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Franklin Center, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/franklin-center/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index258(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Lyons, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Lyons, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Lyons, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/lyons/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index259(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Glendora, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Glendora, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Glendora, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/glendora/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index260(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Somerdale, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Somerdale, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Somerdale, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/somerdale/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index261(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Margate City, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Margate City, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Margate City, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/margate-city/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index262(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Vauxhall, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Vauxhall, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Vauxhall, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/vauxhall/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index263(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Beckett, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Beckett, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Beckett, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/beckett/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index264(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Bargaintown, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Bargaintown, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Bargaintown, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/bargaintown/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index265(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Englewood Cliffs, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Englewood Cliffs, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Englewood Cliffs, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/englewood-cliffs/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index266(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ledgewood, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ledgewood, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ledgewood, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ledgewood/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index267(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Clementon, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Clementon, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Clementon, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/clementon/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index268(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Neshanic Station, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Neshanic Station, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Neshanic Station, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/neshanic-station/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index269(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Salem, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Salem, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Salem, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/salem/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index270(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Mcguire Afb, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Mcguire Afb, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Mcguire Afb, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/mcguire-af/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index271(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Forked River, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Forked River, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Forked River, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/forked-river/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index272(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Troy Hills, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Troy Hills, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Troy Hills, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/troy-hills/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index273(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Cape May Court House, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Cape May Court House, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Cape May Court House, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/cape-may-court-house/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index274(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Wildwood, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Wildwood, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Wildwood, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/wildwood/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index275(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ellisburg, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ellisburg, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ellisburg, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ellisburg/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index276(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ampere North, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ampere North, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ampere North, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ampere-north/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index277(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Morganville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Morganville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Morganville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/morganville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index278(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Demarest, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Demarest, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Demarest, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/demarest/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index279(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Brielle, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Brielle, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Brielle, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/brielle/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index280(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Franklin, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Franklin, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Franklin, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/franklin/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index281(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Spring Lake Heights, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Spring Lake Heights, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Spring Lake Heights, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/spring-lake-heights/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index282(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'East Freehold, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'East Freehold, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'East Freehold, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/east-freehold/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index283(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Penns Grove, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Penns Grove, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Penns Grove, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/penns-grove/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index284(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Flemington, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Flemington, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Flemington, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/flemington/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index285(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'South Bound Brook, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'South Bound Brook, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'South Bound Brook, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/south-bound-brook/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index286(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Harrington Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Harrington Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Harrington Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/harrington-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index287(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Northvale, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Northvale, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Northvale, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/northvale/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index288(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Point Pleasant Beach, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Point Pleasant Beach, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Point Pleasant Beach, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/point-pleasant-beach/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index289(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Beach Haven West, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Beach Haven West, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Beach Haven West, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/beach-haven-west/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index290(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Golden Triangle, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Golden Triangle, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Golden Triangle, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/golden-triangle/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index291(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Landing, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Landing, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Landing, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/landing/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index292(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Highlands, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Highlands, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Highlands, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/highlands/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index293(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Neptune City, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Neptune City, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Neptune City, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/neptune-city/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index294(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Mount Ephraim, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Mount Ephraim, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Mount Ephraim, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/mount-ephraim/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index295(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Leisure Village East, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Leisure Village East, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Leisure Village East, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/leisure-village-east/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index296(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Wanamassa, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Wanamassa, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Wanamassa, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/wanamassa/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index297(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Highland Lakes, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Highland Lakes, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Highland Lakes, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/highland-lakes/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index298(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Buena, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Buena, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Buena, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/buena/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index299(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Beattystown, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Beattystown, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Beattystown, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/beattystown/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index300(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Blackwood, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Blackwood, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Blackwood, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/blackwood/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index301(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Mountain Lakes, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Mountain Lakes, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Mountain Lakes, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/mountain-lakes/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index302(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Garwood, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Garwood, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Garwood, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/garwood/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index303(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Atlantic Highlands, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Atlantic Highlands, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Atlantic Highlands, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/atlantic-highlands/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index304(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Barclay, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Barclay, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Barclay, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/barclay/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index305(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Panther Valley, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Panther Valley, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Panther Valley, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/panther-valley/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index306(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Magnolia, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Magnolia, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Magnolia, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/magnolia/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index307(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Oak Valley, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Oak Valley, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Oak Valley, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/oak-valley/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index308(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Westville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Westville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Westville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/westville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index309(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Cedar Knolls, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Cedar Knolls, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Cedar Knolls, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/cedar-knolls/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index310(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Bradley Beach, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Bradley Beach, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Bradley Beach, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/bradley-beach/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index311(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'The College Of New Jersey, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'The College Of New Jersey, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'The College Of New Jersey, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/the-college-of-new-jersey/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index312(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Country Lake Estates, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Country Lake Estates, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Country Lake Estates, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/country-lake-estates/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index313(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ho-Ho-Kus, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ho-Ho-Kus, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ho-Ho-Kus, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ho-ho-kus/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index314(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Medford Lakes, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Medford Lakes, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Medford Lakes, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/medford-lakes/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index315(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Silver Lake, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Silver Lake, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Silver Lake, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/silver-lake/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index316(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Singac, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Singac, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Singac, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/singac/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index317(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Mullica Hill, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Mullica Hill, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Mullica Hill, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/mullica-hill/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index318(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Shrewsbury, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Shrewsbury, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Shrewsbury, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/shrewsbury/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index319(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Roebling, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Roebling, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Roebling, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/roebling/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index320(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Lambertville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Lambertville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Lambertville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/lambertville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index321(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Holiday City South, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Holiday City South, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Holiday City South, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/holiday-city-south/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index322(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Great Notch, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Great Notch, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Great Notch, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/great-notch/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index323(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Riverdale, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Riverdale, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Riverdale, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/riverdale/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index324(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Leisure Village West, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Leisure Village West, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Leisure Village West, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/leisure-village-west/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index325(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'White House Station, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'White House Station, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'White House Station, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/white-house-station/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index326(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Port Reading, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Port Reading, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Port Reading, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/port-reading/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index327(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Oaklyn, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Oaklyn, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Oaklyn, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/oaklyn/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index328(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Richwood, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Richwood, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Richwood, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/richwood/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index329(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Port Monmouth, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Port Monmouth, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Port Monmouth, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/port-monmouth/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index330(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Oakhurst, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Oakhurst, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Oakhurst, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/oakhurst/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index331(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Merchantville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Merchantville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Merchantville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/merchantville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index332(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'North Cape May, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'North Cape May, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'North Cape May, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/north-cape-may/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index333(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Lawrenceville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Lawrenceville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Lawrenceville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/lawrenceville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index334(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'South Toms River, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'South Toms River, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'South Toms River, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/south-toms-river/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index335(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Woodstown, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Woodstown, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Woodstown, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/woodstown/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index336(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'North Wildwood, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'North Wildwood, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'North Wildwood, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/north-wildwood/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index337(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Tuckerton, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Tuckerton, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Tuckerton, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/tuckerton/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index338(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'High Bridge, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'High Bridge, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'High Bridge, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/high-bridge/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index339(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Sewell, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Sewell, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Sewell, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/sewell/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index340(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Rio Grande, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Rio Grande, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Rio Grande, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/rio-grande/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index341(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Stanhope, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Stanhope, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Stanhope, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/stanhope/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index342(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Gibbstown, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Gibbstown, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Gibbstown, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/gibbstown/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index343(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Netcong, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Netcong, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Netcong, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/netcong/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index344(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Upper Greenwood Lake, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Upper Greenwood Lake, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Upper Greenwood Lake, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/upper-greenwood-lake/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index345(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Saddle River, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Saddle River, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Saddle River, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/saddle-river/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index346(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Turnersville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Turnersville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Turnersville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/turnersville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index347(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Sewaren, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Sewaren, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Sewaren, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/sewaren/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index348(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Haworth, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Haworth, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Haworth, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/haworth/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index349(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Six Mile Run, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Six Mile Run, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Six Mile Run, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/six-mile-run/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index350(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Hamburg, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Hamburg, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Hamburg, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/hamburg/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index351(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Groveville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Groveville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Groveville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/groveville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index352(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Leisuretowne, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Leisuretowne, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Leisuretowne, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/leisuretowne/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index353(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Monmouth Beach, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Monmouth Beach, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Monmouth Beach, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/monmouth-beach/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index354(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Woodbury Heights, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Woodbury Heights, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Woodbury Heights, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/woodbury-heights/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index355(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Wildwood Crest, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Wildwood Crest, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Wildwood Crest, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/wildwood-crest/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index356(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Pines Lake, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Pines Lake, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Pines Lake, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/pines-lake/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index357(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Moonachie, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Moonachie, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Moonachie, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/moonachie/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index358(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'National Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'National Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'National Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/national-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index359(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Stirling, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Stirling, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Stirling, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/stirling/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index360(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Shark River Hills, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Shark River Hills, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Shark River Hills, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/shark-river-hills/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index361(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Cliffwood Beach, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Cliffwood Beach, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Cliffwood Beach, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/cliffwood-beach/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index362(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Mount Hope, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Mount Hope, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Mount Hope, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/mount-hope/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index363(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'East Newark, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'East Newark, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'East Newark, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/east-newark/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index364(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Lawnside, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Lawnside, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Lawnside, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/lawnside/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index365(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ocean Grove, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ocean Grove, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ocean Grove, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ocean-grove/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index366(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Millington, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Millington, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Millington, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/millington/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index367(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Keasbey, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Keasbey, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Keasbey, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/keasbey/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index368(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Cape May, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Cape May, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Cape May, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/cape-may/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index369(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Woodlynne, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Woodlynne, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Woodlynne, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/woodlynne/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index370(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Menlo Park Terrace, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Menlo Park Terrace, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Menlo Park Terrace, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/menlo-park-terrace/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index371(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'West Berlin, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'West Berlin, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'West Berlin, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/west-berlin/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index372(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Union, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Union, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Union, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/union/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index373(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Palermo, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Palermo, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Palermo, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/palermo/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index374(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Spring Lake, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Spring Lake, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Spring Lake, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/spring-lake/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index375(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Rossmoor, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Rossmoor, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Rossmoor, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/rossmoor/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index376(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Pennington, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Pennington, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Pennington, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/pennington/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index377(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Plainsboro Center, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Plainsboro Center, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Plainsboro Center, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/plainsboro-center/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index378(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Riverton, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Riverton, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Riverton, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/riverton/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index379(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Pemberton Heights, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Pemberton Heights, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Pemberton Heights, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/pemberton-heights/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index380(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Concordia, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Concordia, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Concordia, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/concordia/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index381(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Swedesboro, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Swedesboro, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Swedesboro, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/swedesboro/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index382(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Stockton University, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Stockton University, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Stockton University, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/stockton-university/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index383(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Leisure Knoll, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Leisure Knoll, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Leisure Knoll, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/leisure-knoll/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index384(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Gillette, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Gillette, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Gillette, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/gillette/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index385(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Pine Ridge At Crestwood, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Pine Ridge At Crestwood, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Pine Ridge At Crestwood, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/pine-ridge-at-crestwood/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index386(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Lakehurst, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Lakehurst, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Lakehurst, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/lakehurst/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index387(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Monroe Manor, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Monroe Manor, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Monroe Manor, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/monroe-manor/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index388(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'English Creek, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'English Creek, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'English Creek, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/english-creek/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index389(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Hewitt, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Hewitt, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Hewitt, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/hewitt/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index390(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Belvidere, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Belvidere, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Belvidere, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/belvidere/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index391(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Seaville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Seaville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Seaville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/seaville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index392(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Marmora, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Marmora, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Marmora, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/marmora/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index393(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Hopelawn, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Hopelawn, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Hopelawn, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/hopelawn/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index394(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Middlebush, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Middlebush, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Middlebush, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/middlebush/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index395(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'West Belmar, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'West Belmar, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'West Belmar, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/west-belmar/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index396(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Thorofare, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Thorofare, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Thorofare, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/thorofare/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index397(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'North Middletown, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'North Middletown, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'North Middletown, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/north-middletown/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index398(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Vista Center, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Vista Center, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Vista Center, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/vista-center/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index399(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Whittingham, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Whittingham, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Whittingham, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/whittingham/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index400(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Laurel Lake, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Laurel Lake, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Laurel Lake, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/laurel-lake/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index401(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Leonardo, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Leonardo, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Leonardo, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/leonardo/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index402(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Brownville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Brownville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Brownville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/brownville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index403(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Helmetta, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Helmetta, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Helmetta, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/helmetta/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index404(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Whitesboro, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Whitesboro, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Whitesboro, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/whitesboro/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index405(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Pine Beach, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Pine Beach, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Pine Beach, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/pine-beach/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index406(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Macopin, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Macopin, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Macopin, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/macopin/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index407(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Gibbsboro, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Gibbsboro, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Gibbsboro, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/gibbsboro/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index408(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Alpha, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Alpha, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Alpha, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/alpha/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index409(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Woodbine, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Woodbine, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Woodbine, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/woodbine/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index410(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Pleasantdale, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Pleasantdale, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Pleasantdale, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/pleasantdale/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index411(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ten Mile Run, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ten Mile Run, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ten Mile Run, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ten-mile-run/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index412(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'North Beach Haven, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'North Beach Haven, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'North Beach Haven, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/north-beach-haven/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index413(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Essex Fells, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Essex Fells, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Essex Fells, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/essex-fells/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index414(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Wenonah, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Wenonah, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Wenonah, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/wenonah/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index415(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ramapo College Of New Jersey, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ramapo College Of New Jersey, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ramapo College Of New Jersey, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ramapo-college-of-new-jersey/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index416(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Mickleton, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Mickleton, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Mickleton, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/mickleton/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index417(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Princeton Junction, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Princeton Junction, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Princeton Junction, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/princeton-junction/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index418(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ogdensburg, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ogdensburg, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ogdensburg, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ogdensburg/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index419(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Byram Center, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Byram Center, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Byram Center, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/byram-center/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index420(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Forsgate, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Forsgate, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Forsgate, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/forsgate/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index421(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Seaside Heights, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Seaside Heights, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Seaside Heights, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/seaside-heights/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index422(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Lavallette, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Lavallette, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Lavallette, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/lavallette/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index423(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Rutgers University-Livingston Campus, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Rutgers University-Livingston Campus, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Rutgers University-Livingston Campus, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/rutgers-university-livingston-campus/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index424(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Holiday Heights, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Holiday Heights, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Holiday Heights, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/holiday-heights/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index425(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Englishtown, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Englishtown, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Englishtown, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/englishtown/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index426(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Waretown, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Waretown, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Waretown, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/waretown/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index427(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Long Valley, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Long Valley, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Long Valley, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/long-valley/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index428(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Beverly, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Beverly, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Beverly, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/beverly/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index429(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Manahawkin, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Manahawkin, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Manahawkin, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/manahawkin/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index430(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Weston, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Weston, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Weston, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/weston/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index431(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Sea Isle City, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Sea Isle City, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Sea Isle City, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/sea-isle-city/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index432(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Belford, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Belford, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Belford, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/belford/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index433(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Regency At Monroe, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Regency At Monroe, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Regency At Monroe, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/regency-at-monroe/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index434(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Presidential Lakes Estates, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Presidential Lakes Estates, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Presidential Lakes Estates, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/presidential-lakes-estates/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index435(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Laurel Springs, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Laurel Springs, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Laurel Springs, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/laurel-springs/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index436(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Liberty Corner, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Liberty Corner, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Liberty Corner, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/liberty-corner/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index437(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Erma, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Erma, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Erma, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/erma/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index438(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Sea Girt, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Sea Girt, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Sea Girt, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/sea-girt/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index439(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Sussex, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Sussex, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Sussex, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/sussex/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index440(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Kenvil, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Kenvil, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Kenvil, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/kenvil/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index441(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Allentown, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Allentown, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Allentown, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/allentown/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index442(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Stonebridge, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Stonebridge, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Stonebridge, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/stonebridge/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index443(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Cranford, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Cranford, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Cranford, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/cranford/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index444(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Hopewell, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Hopewell, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Hopewell, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/hopewell/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index445(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Brooklawn, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Brooklawn, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Brooklawn, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/brooklawn/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index446(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Malaga, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Malaga, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Malaga, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/malaga/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index447(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Cedar Glen West, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Cedar Glen West, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Cedar Glen West, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/cedar-glen-west/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index448(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Dover Beaches North, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Dover Beaches North, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Dover Beaches North, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/dover-beaches-north/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index449(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Upper Pohatcong, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Upper Pohatcong, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Upper Pohatcong, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/upper-pohatcong/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index450(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'New Egypt, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'New Egypt, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'New Egypt, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/new-egypt/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index451(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Seaside Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Seaside Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Seaside Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/seaside-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index452(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Newfield, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Newfield, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Newfield, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/newfield/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index453(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Estell Manor, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Estell Manor, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Estell Manor, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/estell-manor/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index454(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Avon-By-The-Sea, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Avon-By-The-Sea, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Avon-By-The-Sea, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/avon-by-the-sea/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index455(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Lake Como, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Lake Como, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Lake Como, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/lake-como/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index456(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Annandale, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Annandale, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Annandale, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/annandale/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index457(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Folsom, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Folsom, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Folsom, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/folsom/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index458(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Port Norris, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Port Norris, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Port Norris, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/port-norris/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index459(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Frenchtown, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Frenchtown, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Frenchtown, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/frenchtown/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index460(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Victory Gardens, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Victory Gardens, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Victory Gardens, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/victory-gardens/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index461(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ocean Gate, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ocean Gate, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ocean Gate, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ocean-gate/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index462(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Glen Gardner, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Glen Gardner, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Glen Gardner, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/glen-gardner/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index463(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Brass Castle, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Brass Castle, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Brass Castle, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/brass-castle/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index464(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Gouldtown, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Gouldtown, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Gouldtown, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/gouldtown/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index465(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Franklinville, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Franklinville, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Franklinville, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/franklinville/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index466(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Rosenhayn, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Rosenhayn, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Rosenhayn, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/rosenhayn/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index467(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Collings Lakes, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Collings Lakes, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Collings Lakes, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/collings-lakes/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index468(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Cedar Glen Lakes, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Cedar Glen Lakes, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Cedar Glen Lakes, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/cedar-glen-lakes/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index469(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Sea Bright, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Sea Bright, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Sea Bright, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/sea-bright/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index470(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'West Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'West Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'West Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/west-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index471(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Island Heights, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Island Heights, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Island Heights, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/island-heights/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index472(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Victory Lakes, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Victory Lakes, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Victory Lakes, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/victory-lakes/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index473(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'South Dennis, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'South Dennis, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'South Dennis, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/south-dennis/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index474(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Springfield, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Springfield, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Springfield, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/springfield/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index475(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Vernon Center, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Vernon Center, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Vernon Center, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/vernon-center/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index476(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Absecon Highlands, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Absecon Highlands, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Absecon Highlands, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/absecon-highlands/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index477(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Cologne, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Cologne, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Cologne, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/cologne/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index478(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Olivet, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Olivet, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Olivet, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/olivet/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index479(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Chesilhurst, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Chesilhurst, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Chesilhurst, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/chesilhurst/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index480(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Avalon, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Avalon, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Avalon, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/avalon/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index481(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Crandon Lakes, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Crandon Lakes, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Crandon Lakes, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/crandon-lakes/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index482(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Brookside, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Brookside, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Brookside, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/brookside/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index483(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Dover Beaches South, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Dover Beaches South, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Dover Beaches South, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/dover-beaches-south/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index484(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Seabrook Farms, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Seabrook Farms, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Seabrook Farms, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/seabrook-farms/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index485(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'William Paterson University Of New Jersey, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'William Paterson University Of New Jersey, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'William Paterson University Of New Jersey, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/william-paterson-university-of-new-jersey/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index486(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Newfoundland, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Newfoundland, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Newfoundland, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/newfoundland/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index487(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Rainbow Lakes, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Rainbow Lakes, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Rainbow Lakes, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/rainbow-lakes/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index488(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Alpine, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Alpine, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Alpine, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/alpine/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index489(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Montclair State University, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Montclair State University, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Montclair State University, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/montclair-state-university/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index490(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Silver Lake, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Silver Lake, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Silver Lake, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/silver-lake/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index491(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Dorothy, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Dorothy, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Dorothy, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/dorothy/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index492(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Deans, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Deans, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Deans, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/deans/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index493(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Centre Grove, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Centre Grove, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Centre Grove, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/centre-grove/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index494(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Farmingdale, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Farmingdale, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Farmingdale, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/farmingdale/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index495(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Elmer, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Elmer, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Elmer, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/elmer/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index496(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Vernon Valley, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Vernon Valley, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Vernon Valley, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/vernon-valley/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index497(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Navesink, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Navesink, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Navesink, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/navesink/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index498(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Surf City, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Surf City, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Surf City, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/surf-city/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index499(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Green Village, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Green Village, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Green Village, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/green-village/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index500(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Milmay, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Milmay, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Milmay, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/milmay/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index501(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Lake Telemark, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Lake Telemark, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Lake Telemark, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/lake-telemark/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index502(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Beesleys Point, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Beesleys Point, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Beesleys Point, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/beesleys-point/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index503(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Bedminster, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Bedminster, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Bedminster, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/bedminster/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index504(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Kean University, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Kean University, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Kean University, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/kean-university/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index505(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'East Vineland, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'East Vineland, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'East Vineland, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/east-vineland/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index506(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Milford, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Milford, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Milford, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/milford/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index507(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Silver Ridge, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Silver Ridge, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Silver Ridge, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/silver-ridge/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index508(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Beach Haven, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Beach Haven, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Beach Haven, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/beach-haven/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index509(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Port Republic, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Port Republic, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Port Republic, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/port-republic/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index510(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Flagtown, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Flagtown, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Flagtown, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/flagtown/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index511(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Kingston, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Kingston, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Kingston, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/kingston/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index512(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Califon, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Califon, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Califon, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/califon/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index513(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Port Morris, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Port Morris, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Port Morris, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/port-morris/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index514(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Audubon Park, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Audubon Park, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Audubon Park, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/audubon-park/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index515(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Brookfield, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Brookfield, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Brookfield, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/brookfield/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index516(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'West Cape May, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'West Cape May, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'West Cape May, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/west-cape-may/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index517(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Roosevelt, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Roosevelt, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Roosevelt, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/roosevelt/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index518(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Far Hills, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Far Hills, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Far Hills, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/far-hills/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def index519(response):
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
    metatitle_citypage= split_metatitle_citypage[picker_metatitle_citypage].replace('#State', 'Ship Bottom, NJ')
    
    split_metadescription_citypage= read_root_file('City Page Meta Description').split('@@@')
    picker_metadescription_citypage= random.randint(0, len(split_metadescription_citypage)-1)
    metadescription_citypage= split_metadescription_citypage[picker_metadescription_citypage].replace('#State', 'Ship Bottom, NJ')

    randomize_data= generate_contents_body(phone_number, Long_formurl, shortformurl, randomize_image, citypage_contents, site_name).replace('#State', 'Ship Bottom, NJ').replace('"static/', '"../../static/')
    randomize_data = mark_safe(randomize_data)
    return render(response, "zeodigital/new-jersey/ship-bottom/index.html", {
        'aloomaidbody': randomize_data,
        'aloomaidtitle': metatitle_citypage,
        'aloomaiddescription': metadescription_citypage,
    })

def sitemaps(response):
    return render(response, "zeodigital/sitemaps/sitemaps.xml")
