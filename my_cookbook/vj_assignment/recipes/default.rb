#
# Cookbook Name:: vj_assignment
# Recipe:: default
#
# Copyright 2017, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#

filename="simpleweb.py"

execute 'execute_file' do
	cwd '/etc/cookbooks/vj_assignment/recipes'
	command "python #{filename}"
end
