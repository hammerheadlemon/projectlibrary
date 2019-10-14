'''

Store of common functions found in all analysis engine

This is also where the date of BICC is set. This is the date from which much of the analysis is set.
NOTE. Python date format is (YYYY,MM,DD)

'''

import random
import datetime

bicc_date = datetime.datetime(2019, 11, 4)

def all_milestone_data_bulk(project_list, master_data):
    '''
    function that filters all milestone data and returns it in dictionary format.

    dictionary is structured as {'project name': {'milestone name': datetime.date: 'notes'}}

    project list: list of project names of interest / in range
    master_data: quarter master data set
    '''

    upper_dictionary = {}

    for name in project_list:
        try:
            p_data = master_data.data[name]
            lower_dictionary = {}
            for i in range(1, 50):
                try:
                    try:
                        lower_dictionary[p_data['Approval MM' + str(i)]] = \
                            {p_data['Approval MM' + str(i) + ' Forecast / Actual']: p_data[
                                'Approval MM' + str(i) + ' Notes']}
                    except KeyError:
                        lower_dictionary[p_data['Approval MM' + str(i)]] = \
                            {p_data['Approval MM' + str(i) + ' Forecast - Actual']: p_data[
                                'Approval MM' + str(i) + ' Notes']}

                    lower_dictionary[p_data['Assurance MM' + str(i)]] = \
                        {p_data['Assurance MM' + str(i) + ' Forecast - Actual']: p_data[
                                'Assurance MM' + str(i) + ' Notes']}
                except KeyError:
                    pass

            for i in range(18, 67):
                try:
                    lower_dictionary[p_data['Project MM' + str(i)]] = \
                        {p_data['Project MM' + str(i) + ' Forecast - Actual']: p_data['Project MM' + str(i) + ' Notes']}
                except KeyError:
                    pass
        except KeyError:
            lower_dictionary = {}

        upper_dictionary[name] = lower_dictionary

    return upper_dictionary

def ap_p_milestone_data_bulk(project_list, master_data):
    '''
    function that filters  milestone data and returns it in dictionary format.

    dictionary is structured as {'project name': {'milestone name': datetime.date: 'notes'}}

    project list: list of project names of interest / in range
    master_data: quarter master data set
    '''

    upper_dictionary = {}

    for name in project_list:
        try:
            p_data = master_data.data[name]
            lower_dictionary = {}
            for i in range(1, 50):
                try:
                    try:
                        lower_dictionary[p_data['Approval MM' + str(i)]] = \
                            {p_data['Approval MM' + str(i) + ' Forecast / Actual'] : p_data['Approval MM' + str(i) + ' Notes']}
                    except KeyError:
                        lower_dictionary[p_data['Approval MM' + str(i)]] = \
                            {p_data['Approval MM' + str(i) + ' Forecast - Actual'] : p_data['Approval MM' + str(i) + ' Notes']}

                except KeyError:
                    pass

            for i in range(18, 67):
                try:
                    lower_dictionary[p_data['Project MM' + str(i)]] = \
                        {p_data['Project MM' + str(i) + ' Forecast - Actual'] : p_data['Project MM' + str(i) + ' Notes']}
                except KeyError:
                    pass
        except KeyError:
            lower_dictionary = {}

        upper_dictionary[name] = lower_dictionary

    return upper_dictionary

def assurance_milestone_data_bulk(project_list, master_data):
    """Function to filter out assurance milestone data"""
    upper_dictionary = {}

    for name in project_list:
        try:
            p_data = master_data.data[name]
            lower_dictionary = {}
            for i in range(1, 50):
                lower_dictionary[p_data['Assurance MM' + str(i)]] = \
                    {p_data['Assurance MM' + str(i) + ' Forecast - Actual']: p_data['Assurance MM' + str(i) + ' Notes']}

            upper_dictionary[name] = lower_dictionary
        except KeyError:
            upper_dictionary[name] = {}

    return upper_dictionary

def project_time_difference(proj_m_data_1, proj_m_data_2):
    """Function that calculates time different between milestone dates"""
    upper_dictionary = {}

    for proj_name in proj_m_data_1:
        td_dict = {}
        for milestone in proj_m_data_1[proj_name]:
            if milestone is not None:
                milestone_date = tuple(proj_m_data_1[proj_name][milestone])[0]
                try:
                    if bicc_date <= milestone_date:
                        try:
                            old_milestone_date = tuple(proj_m_data_2[proj_name][milestone])[0]
                            time_delta = (milestone_date - old_milestone_date).days  # time_delta calculated here
                            if time_delta == 0:
                                td_dict[milestone] = 0
                            else:
                                td_dict[milestone] = time_delta
                        except (KeyError, TypeError):
                            td_dict[milestone] = 'Not reported' # not reported that quarter
                except (KeyError, TypeError):
                    td_dict[milestone] = 'No date provided' # date has now been removed

        upper_dictionary[proj_name] = td_dict

    return upper_dictionary

def filter_gmpp(master):
    project_list = []
    for project_name in master.projects:
        if master.data[project_name]['GMPP - IPA ID Number'] is not None:
            project_list.append(project_name)

    return project_list

def bc_ref_stages(project_list, masters_list):
    """One of key functions used for calculating which quarter to baseline data from.

    Function returns a dictionary structured in the following way project name[('latest quarter info', 'latest bc'),
    ('last quarter info', 'last bc'), ('last baseline quarter info', 'last baseline bc'), ('oldest quarter info',
    'oldest bc')] depending on the amount information available in the data. Only the first three key values are returned,
    to ensure consistency (which is helpful later).

    project_list: list of project names
    masters_list = list of master dictionaries

    """
    output = {}

    for project_name in project_list:
        #print(name)
        all_list = []      # format [('quarter info': 'bc')] across all masters including project
        bl_list = []        # format ['bc', 'bc'] across all masters. bl_list_2 removes duplicates
        ref_list = []       # format as for all list but only contains the three tuples of interest
        for master in masters_list:
            try:
                bc_stage = master.data[project_name]['BICC approval point']
                quarter = master.data[project_name]['Reporting period (GMPP - Snapshot Date)']
                tuple = (quarter, bc_stage)
                all_list.append(tuple)
            except KeyError:
                pass

        for i in range(0, len(all_list)):
            bl_list.append(all_list[i][1])

        '''below lines of text from stackoverflow. Question, remove duplicates in python list while
        preserving order'''
        seen = set()
        seen_add = seen.add
        bl_list_2 = [x for x in bl_list if not (x in seen or seen_add(x))]

        ref_list.insert(0, all_list[0])     # puts the latest info into the list first

        try:
            ref_list.insert(1, all_list[1])    # puts that last info into the list
        except IndexError:
            ref_list.insert(1, all_list[0])

        if len(bl_list_2) == 1:                     # puts oldest info into list (as basline if no baseline)
            ref_list.insert(2, all_list[-1])
        else:
            for i in range(0, len(all_list)):      # puts in baseline
                if all_list[i][1] == bl_list[0]:
                    ref_list.insert(2, all_list[i])

        '''there is a hack here i.e. returning only first three in ref_list. There's a bug which I don't fully
        understand, but this solution is hopefully good enough for now'''
        output[project_name] = ref_list[0:3]

    return output

def master_baseline_index(project_list, masters_list, baselines_list):
    """
    Another key function to calculate which quarter to baseline data from.

    Function returns a dictionary structured as {'project name': [n,n,n]}.
    The n (number) values denote where the relevant baseline master dictionaries are list of master dictionaries.
    The first n in the latest master, second n is last master, third n is baseline master.

    project_list: list of projects
    masters_list: list of masters
    baseline_list: list of project baseline information in the structure {'project name': [('quarter stamp', 'bc stage),
    (), ()] as created by bc_ref_stage function.

    """
    output = {}

    for project_name in project_list:
        master_q_list = []
        for key in baselines_list[project_name]:
            for x, master in enumerate(masters_list):
                try:
                    quarter = master.data[project_name]['Reporting period (GMPP - Snapshot Date)']
                    if quarter == key[0]:
                        master_q_list.append(x)
                except KeyError:
                    pass

        output[project_name] = master_q_list

    return output

def convert_rag_text(dca_rating):

    if dca_rating == 'Green':
        return 'G'
    elif dca_rating == 'Amber/Green':
        return 'A/G'
    elif dca_rating == 'Amber':
        return 'A'
    elif dca_rating == 'Amber/Red':
        return 'A/R'
    elif dca_rating == 'Red':
        return 'R'
    else:
        return 'None'

def filter_project_group(master_data, group):
    '''
    function for return a list of projects according to their group
    :param master_data: one quarters master data
    :param group: group name of interest. this is a string.
    options are 'Rail Group', 'HSMRPG', 'International Security and Environment', 'Roads Devolution & Motoring'.
    Note this list should be kept up to date as group names change.
    :return: list of projects in specified group
    '''

    project_name_list = master_data.projects

    output_list = []

    for project_name in project_name_list:
        if master_data.data[project_name]['DfT Group'] == group:
            output_list.append(project_name)
        else:
            pass

    return output_list

def get_all_project_names(masters_list):
    '''
    function returns list of all projects across multiple dictionaries

    useful if you need project names across multiple quarters

    masters_list: list of masters containing quarter information
    '''

    output_list = []
    for master in masters_list:
        for name in master.projects:
            if name not in output_list:
                output_list.append(name)

    return output_list

def get_quarter_stamp(masters_list):
    '''
    Function used to specify the quarter being reported.

    masters_list: list of masters containing quarter information
    '''

    output_list = []
    for master in masters_list:
        project_name = random.choice(master.projects)
        quarter_stamp = master.data[project_name]['Reporting period (GMPP - Snapshot Date)']
        output_list.append(quarter_stamp)

    return output_list

def concatenate_dates(date):
    '''
    function for converting dates into concatenated written time periods
    :param date:
    :return:
    '''
    today = bicc_date
    if date != None:
        a = (date - today.date()).days
        year = 365
        month = 30
        fortnight = 14
        week = 7
        if a >= 365:
            yrs = int(a / year)
            holding_days_years = a % year
            months = int(holding_days_years / month)
            holding_days_months = a % month
            fortnights = int(holding_days_months / fortnight)
            weeks = int(holding_days_months / week)
        elif 0 <= a <= 365:
            yrs = 0
            months = int(a / month)
            holding_days_months = a % month
            fortnights = int(holding_days_months / fortnight)
            weeks = int(holding_days_months / week)
            # if 0 <= a <=60:
        elif a <= -365:
            yrs = int(a / year)
            holding_days = a % -year
            months = int(holding_days / month)
            holding_days_months = a % -month
            fortnights = int(holding_days_months / fortnight)
            weeks = int(holding_days_months / week)
        elif -365 <= a <= 0:
            yrs = 0
            months = int(a / month)
            holding_days_months = a % -month
            fortnights = int(holding_days_months / fortnight)
            weeks = int(holding_days_months / week)
            # if -60 <= a <= 0:
        else:
            print('something is wrong and needs checking')

        if yrs == 1:
            if months == 1:
                return ('{} yr, {} mth'.format(yrs, months))
            if months > 1:
                return ('{} yr, {} mths'.format(yrs, months))
            else:
                return ('{} yr'.format(yrs))
        elif yrs > 1:
            if months == 1:
                return ('{} yrs, {} mth'.format(yrs, months))
            if months > 1:
                return ('{} yrs, {} mths'.format(yrs, months))
            else:
                return ('{} yrs'.format(yrs))
        elif yrs == 0:
            if a == 0:
                return ('Today')
            elif 1 <= a <= 6:
                return ('This week')
            elif 7 <= a <= 13:
                return ('Next week')
            elif -7 <= a <= -1:
                return ('Last week')
            elif -14 <= a <= -8:
                return ('-2 weeks')
            elif 14 <= a <= 20:
                return ('2 weeks')
            elif 20 <= a <= 60:
                if today.month == date.month:
                    return ('Later this mth')
                elif (date.month - today.month) == 1:
                    return ('Next mth')
                else:
                    return ('2 mths')
            elif -60 <= a <= -15:
                if today.month == date.month:
                    return ('Earlier this mth')
                elif (date.month - today.month) == -1:
                    return ('Last mth')
                else:
                    return ('-2 mths')
            elif months == 12:
                return ('1 yr')
            else:
                return ('{} mths'.format(months))

        elif yrs == -1:
            if months == -1:
                return ('{} yr, {} mth'.format(yrs, -(months)))
            if months < -1:
                return ('{} yr, {} mths'.format(yrs, -(months)))
            else:
                return ('{} yr'.format(yrs))
        elif yrs < -1:
            if months == -1:
                return ('{} yrs, {} mth'.format(yrs, -(months)))
            if months < -1:
                return ('{} yrs, {} mths'.format(yrs, -(months)))
            else:
                return ('{} yrs'.format(yrs))
    else:
        return ('None')

def up_or_down(latest_dca, last_dca):
    '''
    function that calculates if confidence has increased or decreased
    :param latest_dca:
    :param last_dca:
    :return:
    '''

    if latest_dca == last_dca:
        return (int(0))
    elif latest_dca != last_dca:
        if last_dca == 'Green':
            if latest_dca != 'Amber/Green':
                return (int(-1))
        elif last_dca == 'Amber/Green':
            if latest_dca == 'Green':
                return (int(1))
            else:
                return (int(-1))
        elif last_dca == 'Amber':
            if latest_dca == 'Green':
                return (int(1))
            elif latest_dca == 'Amber/Green':
                return (int(1))
            else:
                return (int(-1))
        elif last_dca == 'Amber/Red':
            if latest_dca == 'Red':
                return (int(-1))
            else:
                return (int(1))
        else:
            return (int(1))

def convert_bc_stage_text(bc_stage):
    '''
    function that converts bc stage.
    :param bc_stage:
    :return:
    '''

    if bc_stage == 'Strategic Outline Case':
        return 'SOBC'
    elif bc_stage == 'Outline Business Case':
        return 'OBC'
    elif bc_stage == 'Full Business Case':
        return 'FBC'
    elif bc_stage == 'pre-Strategic Outline Case':
        return 'pre-SOBC'
    else:
        return bc_stage
