"""place for storing all master templates"""

from datamaps.api import project_data_from_master

q1_1920 = project_data_from_master('C:\\Users\\Standalone\\general\\masters folder\\core_data\\master_1_2019.xlsx', 1, 2019)
q4_1819 = project_data_from_master('C:\\Users\\Standalone\\general\\masters folder\\core_data\\master_4_2018.xlsx', 4, 2018)
q3_1819 = project_data_from_master('C:\\Users\\Standalone\\general\\masters folder\\core_data\\master_3_2018.xlsx', 3, 2018)
q2_1819 = project_data_from_master('C:\\Users\\Standalone\\general\\masters folder\\core_data\\master_2_2018.xlsx', 2, 2018)
q1_1819 = project_data_from_master('C:\\Users\\Standalone\\general\\masters folder\\core_data\\master_1_2018.xlsx', 1, 2018)
q4_1718 = project_data_from_master('C:\\Users\\Standalone\\general\\masters folder\\core_data\\master_4_2017.xlsx', 4, 2017)
q3_1718 = project_data_from_master('C:\\Users\\Standalone\\general\\masters folder\\core_data\\master_3_2017.xlsx', 3, 2017)
q2_1718 = project_data_from_master('C:\\Users\\Standalone\\general\\masters folder\\core_data\\master_2_2017.xlsx', 2, 2017)
q1_1718 = project_data_from_master('C:\\Users\\Standalone\\general\\masters folder\\core_data\\master_1_2017.xlsx', 1, 2017)
q4_1617 = project_data_from_master('C:\\Users\\Standalone\\general\\masters folder\\core_data\\master_4_2016.xlsx', 4, 2016)
q3_1617 = project_data_from_master('C:\\Users\\Standalone\\general\\masters folder\\core_data\\master_3_2016.xlsx', 3, 2016)


"""list of dictionaries"""
one_quarter_master_list = [q1_1920]
bespoke_group_master_list = [q1_1920, q4_1819]
list_of_masters_all = [q1_1920, q4_1819, q3_1819, q2_1819, q1_1819, q4_1718, q3_1718, q2_1718, q1_1718, q4_1617, q3_1617]


