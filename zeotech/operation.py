from .duplicate import *

def move_home_page():
    template_data_2 = open("zeotech/templates/zeodigital/index.html", "r", encoding="utf-8-sig").read()
    confirm_county_pages= f'zeotech/templates/zeodigital/allrequiredpages/homepage.html'
    fp = open(confirm_county_pages, "w", encoding='utf-8-sig')
    fp.writelines(template_data_2)
    fp.close()

def create_root_file(file_name, data_info):
    save_file= file_name.replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
    save_file= str(save_file.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
    if isinstance(data_info, list):
        all_list=''
        for data_inf in data_info:
            all_list+= f'{data_inf},'
        fp = open(f'zeotech/static/aloomaspecial/records/{save_file}.txt', "w", encoding='utf-8-sig')
        fp.writelines(all_list)
        fp.close()
    else:
        fp = open(f'zeotech/static/aloomaspecial/records/{save_file}.txt', "w", encoding='utf-8-sig')
        fp.writelines(data_info)
        fp.close()

def read_root_file(file_name):
    save_file= file_name.replace(' ', '-').replace(',', '').replace('.', '').replace('ï»¿', '').lower()
    save_file= str(save_file.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
    fp = open(f'zeotech/static/aloomaspecial/records/{save_file}.txt', "r", encoding="utf-8-sig").read()
    return fp

def save_image_to_root(image_file):
    image_file_name= str(image_file.name).replace(',', ' ')
    try:
        os.makedirs('zeotech/static/images') 
        with open('zeotech/static/images/' + image_file_name, 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)
    except:
        try:
            with open('zeotech/static/images/' + image_file_name, 'wb+') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)
        except:
            pass
    return f'static/images/{image_file_name}'

def rewrite_css(page_color, boxp_agecolor):
    editedcss = open(f'zeotech/static/aloomaspecial/css.txt', "r", encoding="utf-8-sig").read()
    fp = open(f'zeotech/static/aloomaspecial/alooma.css', "w", encoding='utf-8-sig')
    fp.writelines(editedcss.replace('aloomaidbackground', page_color).replace('aloomaidboxbackground', boxp_agecolor))
    fp.close()

    editedcss1 = open(f'zeotech/static/aloomaspecial/css1.txt', "r", encoding="utf-8-sig").read()
    fp1 = open(f'zeotech/static/aloomaspecial/alooma2.css', "w", encoding='utf-8-sig')
    fp1.writelines(editedcss1.replace('aloomaidbackground', page_color).replace('aloomaidboxbackground', boxp_agecolor))
    fp1.close()
    

def create_pages_directory(domain_site_name, population_limit, Pages_created_options, radioselect, Checkboxselected):
    if 'All Pages' == Pages_created_options:
        print('Processing All Pages Creation')
        all_pages_protocol(population_limit, domain_site_name, radioselect)
        print('Done All Pages Creation')
    elif 'Selected State Pages' == Pages_created_options:
        print('Processing Selected State Pages Creation')
        selected_state_pages(population_limit, domain_site_name, radioselect, Checkboxselected)
        print('Done Selected State Pages Creation')
    elif 'Excluded State Pages' == Pages_created_options:
        print('Processing Excluded State Pages Creation')
        excluded_state_pages(population_limit, domain_site_name, radioselect, Checkboxselected)
        print('Done Excluded State Pages Creation')


    