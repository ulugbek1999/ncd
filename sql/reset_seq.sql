select setval('auth_user_id_seq', (select max(id) from auth_user));

select setval('directory_city_id_seq', (select max(id) from directory_city));
select setval('directory_district_id_seq', (select max(id) from directory_district));
select setval('directory_country_id_seq', (select max(id) from directory_country));
select setval('directory_education_type_id_seq', (select max(id) from directory_education_type));
select setval('directory_language_id_seq', (select max(id) from directory_language));

select setval('employee_id_seq', (select max(id) from employee));
select setval('employee__army_id_seq', (select max(id) from employee__army));
select setval('employee__army__file_id_seq', (select max(id) from employee__army__file));
select setval('employee__army__changes_id_seq', (select max(id) from employee__army__changes));
select setval('employee__army__changes__file_id_seq', (select max(id) from employee__army__changes__file));

select setval('employee__countries_id_seq', (select max(id) from employee__countries));
select setval('employee__changes__countries_id_seq', (select max(id) from employee__changes__countries));
select setval('employee_changes_id_seq', (select max(id) from employee_changes));
select setval('employee_score_id_seq', (select max(id) from employee_score));
select setval('employee__changes__countries_id_seq', (select max(id) from employee__changes__countries));

select setval('employee__education_id_seq', (select max(id) from employee__education));
select setval('employee__education__file_id_seq', (select max(id) from employee__education__file));
select setval('employee__education__changes_id_seq', (select max(id) from employee__education__changes));
select setval('employee__education__changes__file_id_seq', (select max(id) from employee__education__changes__file));

select setval('employee__experience_id_seq', (select max(id) from employee__experience));
select setval('employee__experience__file_id_seq', (select max(id) from employee__experience__file));
select setval('employee__experience__changes_id_seq', (select max(id) from employee__experience__changes));
select setval('employee__experience__changes__file_id_seq', (select max(id) from employee__experience__changes__file));

select setval('employee__experience_id_seq', (select max(id) from employee__experience));
select setval('employee__experience__file_id_seq', (select max(id) from employee__experience__file));
select setval('employee__experience__changes_id_seq', (select max(id) from employee__experience__changes));
select setval('employee__experience__changes__file_id_seq', (select max(id) from employee__experience__changes__file));

select setval('employee__family_id_seq', (select max(id) from employee__family));
select setval('employee__family__file_id_seq', (select max(id) from employee__family__file));
select setval('employee__family__changes_id_seq', (select max(id) from employee__family__changes));
select setval('employee__family__changes__file_id_seq', (select max(id) from employee__family__changes__file));

select setval('employee__language_id_seq', (select max(id) from employee__language));
select setval('employee__language__file_id_seq', (select max(id) from employee__language__file));
select setval('employee__language__changes_id_seq', (select max(id) from employee__language__changes));
select setval('employee__language__changes__file_id_seq', (select max(id) from employee__language__changes__file));

select setval('employee__relative_id_seq', (select max(id) from employee__relative));
select setval('employee__relative__file_id_seq', (select max(id) from employee__relative__file));
select setval('employee__relative__changes_id_seq', (select max(id) from employee__relative__changes));
select setval('employee__relative__changes__file_id_seq', (select max(id) from employee__relative__changes__file));

select setval('employee__reward_id_seq', (select max(id) from employee__reward));
select setval('employee__reward__file_id_seq', (select max(id) from employee__reward__file));
select setval('employee__reward__changes_id_seq', (select max(id) from employee__reward__changes));
select setval('employee__reward__changes__file_id_seq', (select max(id) from employee__reward__changes__file));
--
select setval('operator_id_seq', (select max(id) from operator));
select setval('operator_group_id_seq', (select max(id) from operator_group));
select setval('partner_id_seq', (select max(id) from partner));
select setval('partner_employee_id_seq', (select max(id) from partner_employee));
select setval('partner_file_id_seq', (select max(id) from partner_file));
--
-- select setval('auth_user_id_seq', (select max(id) from auth_user));
-- select setval('auth_user_id_seq', (select max(id) from auth_user));
-- select setval('auth_user_id_seq', (select max(id) from auth_user));
-- select setval('auth_user_id_seq', (select max(id) from auth_user));
--
-- select setval('auth_user_id_seq', (select max(id) from auth_user));
-- select setval('auth_user_id_seq', (select max(id) from auth_user));
-- select setval('auth_user_id_seq', (select max(id) from auth_user));
-- select setval('auth_user_id_seq', (select max(id) from auth_user));
