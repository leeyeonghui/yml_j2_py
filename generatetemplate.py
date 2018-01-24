#Author = Lee Yeong Hui
import yaml
import sys
import os 
from jinja2 import Template
from pprint import pprint as pp
from jnpr.junos import Device 
from jnpr.junos.utils.config import Config

#dev.bind (cfg=Config)

pp ("Starting configuration builder")
pp ("Reading YAML data file")
with open('datavars.yml') as dfh:
	yml = yaml.load (dfh.read())

pp(yml)

pp ("Reading Jinja2 templatefile")
with open ('ifacetemplate.j2') as tfh:
	j2 = tfh.read()

pp(j2)

pp ("Generating configuration")
template = Template (j2)
print (template.render (yml))
