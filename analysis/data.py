"""place for storing all master templates"""

from datamaps.api import project_data_from_master
from analysis.engine_functions import baseline_information_bc, baseline_index,get_project_income_profile, get_project_cost_profile
from openpyxl.styles import Font

q2_1920 = project_data_from_master('C:\\Users\\Standalone\\general\\core_data\\master_2_2019.xlsx', 2, 2019)
q1_1920 = project_data_from_master('C:\\Users\\Standalone\\general\\core_data\\master_1_2019.xlsx', 1, 2019)
q4_1819 = project_data_from_master('C:\\Users\\Standalone\\general\\core_data\\master_4_2018.xlsx', 4, 2018)
q3_1819 = project_data_from_master('C:\\Users\\Standalone\\general\\core_data\\master_3_2018.xlsx', 3, 2018)
q2_1819 = project_data_from_master('C:\\Users\\Standalone\\general\\core_data\\master_2_2018.xlsx', 2, 2018)
q1_1819 = project_data_from_master('C:\\Users\\Standalone\\general\\core_data\\master_1_2018.xlsx', 1, 2018)
q4_1718 = project_data_from_master('C:\\Users\\Standalone\\general\\core_data\\master_4_2017.xlsx', 4, 2017)
q3_1718 = project_data_from_master('C:\\Users\\Standalone\\general\\core_data\\master_3_2017.xlsx', 3, 2017)
q2_1718 = project_data_from_master('C:\\Users\\Standalone\\general\\core_data\\master_2_2017.xlsx', 2, 2017)
q1_1718 = project_data_from_master('C:\\Users\\Standalone\\general\\core_data\\master_1_2017.xlsx', 1, 2017)
q4_1617 = project_data_from_master('C:\\Users\\Standalone\\general\\core_data\\master_4_2016.xlsx', 4, 2016)
q3_1617 = project_data_from_master('C:\\Users\\Standalone\\general\\core_data\\master_3_2016.xlsx', 3, 2016)

"""list of dictionaries"""
one_quarter_master_list = [q1_1920]
bespoke_group_masters_list = [q2_1819, q1_1819]
financial_analysis_masters_list = [q2_1920, q1_1920, q4_1819, q3_1819, q2_1819, q1_1819]
list_of_masters_all = [q2_1920, q1_1920, q4_1819, q3_1819, q2_1819, q1_1819, q4_1718, q3_1718, q2_1718, q1_1718,
                       q4_1617, q3_1617]

'''list of project names. useful to have here and import into programme'''
latest_quarter_project_names = q2_1920.projects

'''baselining information'''
baseline_bcs = baseline_information_bc(latest_quarter_project_names, financial_analysis_masters_list)
bc_index = baseline_index(baseline_bcs)
#baseline_bc = bc_ref_stages(all_project_names, financial_analysis_masters_list)
#baseline_index = master_baseline_index(all_project_names, financial_analysis_masters_list, baseline_bc)

'''for highlight text'''
red_text = Font(color="FF0000")

'''lists and keys for running programmes'''
income_list = [' Forecast - Income both Revenue and Capital']
cost_list = [' RDEL Forecast Total', ' CDEL Forecast Total', ' Forecast Non-Gov']
year_list = ['19-20', '20-21', '21-22', '22-23', '23-24', '24-25', '25-26', '26-27', '27-28', '28-29', 'Unprofiled']
wlc_key = 'Total Forecast'

'''Financial information'''
latest_income_profiles = get_project_income_profile(latest_quarter_project_names, financial_analysis_masters_list,
                                                    income_list, year_list, bc_index, 0)
last_income_profiles = get_project_income_profile(latest_quarter_project_names, financial_analysis_masters_list,
                                                  income_list, year_list, bc_index, 1)
baseline_income_profiles = get_project_income_profile(latest_quarter_project_names, financial_analysis_masters_list,
                                                      income_list, year_list, bc_index, 2)

latest_cost_profiles = get_project_cost_profile(latest_quarter_project_names, financial_analysis_masters_list,
                                                      cost_list, year_list, bc_index, 0)
last_cost_profiles = get_project_cost_profile(latest_quarter_project_names, financial_analysis_masters_list,
                                                    cost_list, year_list, bc_index, 1)
baseline_cost_profiles = get_project_cost_profile(latest_quarter_project_names, financial_analysis_masters_list,
                                                        cost_list, year_list, bc_index, 2)


financial_narrative_keys = ['Project Costs Narrative',   # financial_dca_dashboard
                 'Cost comparison with last quarters cost narrative',
                 'Cost comparison within this quarters cost narrative']


'''specific project names. Useful to have them captured here so don't have to keep cutting and pasting string 
name from excel master'''
a12 = 'A12 Chelmsford to A120 widening'
a14 = 'A14 Cambridge to Huntingdon Improvement Scheme'
a303 = 'A303 Amesbury to Berwick Down'
a417 = 'A417 Air Balloon'
a428 = 'A428 Black Cat to Caxton Gibbet'
a66 = 'A66 Full Scheme'
cvs = 'Commercial Vehicle Services (CVS)'
east_coast_digital = 'East Coast Digital Programme'
east_coast_mainline = 'East Coast Mainline Programme'
em_franchise = 'East Midlands Franchise'
ewr_central = 'East West Rail Programme (Central Section)'
ewr_western = 'East West Rail Programme (Western Section)'
ftts = 'Future Theory Test Service (FTTS)'
heathrow_expansion = 'Heathrow Expansion'
hexagon = 'Hexagon'
hs2_programme = 'High Speed Rail Programme (HS2)'
hs2_2b = 'HS2 Phase 2b'
hs2_1 = 'HS2 Phase1'
hs2_2a = 'HS2 Phase2a'
ist = 'Integrated and Smart Ticketing - creating an account based back office'
lower_thames_crossing = 'Lower Thames Crossing'
m4 = 'M4 Junctions 3 to 12 Smart Motorway'
manchester_north_west_quad = 'Manchester North West Quadrant'
midland_mainline = 'Midland Main Line Programme'
north_of_england = 'North of England Programme'
northern_powerhouse = 'Northern Powerhouse Rail'
ox_cam_expressway = 'Oxford-Cambridge Expressway'
rail_franchising = 'Rail Franchising Programme'
west_coast_partnership = 'West Coast Partnership Franchise'
crossrail = 'Crossrail Programme'
gwrm = 'Great Western Route Modernisation (GWRM) including electrification'
iep = 'Intercity Express Programme'
south_west_route_capacity = 'South West Route Capacity'
thameslink = 'Thameslink Programme'
wrlth = 'Western Rail Link to Heathrow'

'''list of projects to exclude from counting of totals in portfolio financial profile'''
dont_double_count = [hs2_2b, hs2_2a, hs2_1, em_franchise, west_coast_partnership, northern_powerhouse,
                     east_coast_digital]

'''
keeping as colour coding is useful
s1 = chart.series[0]
s1.graphicalProperties.line.solidFill = "cfcfea" #light blue
s2 = chart.series[1]
s2.graphicalProperties.line.solidFill = "e2f1bb" #light green
s3 = chart.series[2]
s3.graphicalProperties.line.solidFill = "eaba9d" #light red
s4 = chart.series[3]
s4.graphicalProperties.line.solidFil = "5097a4" #medium blue
s5 = chart.series[4]
s5.graphicalProperties.line.solidFill = "a0db8e" #medium green
s6 = chart.series[5]
s6.graphicalProperties.line.solidFill = "b77575" #medium red
s7 = chart.series[6]
s7.graphicalProperties.line.solidFil = "0e2f44" #dark blue
s8 = chart.series[7]
s8.graphicalProperties.line.solidFill = "29ab87" #dark green
s9 = chart.series[8]
s9.graphicalProperties.line.solidFill = "691c1c" #dark red
'''