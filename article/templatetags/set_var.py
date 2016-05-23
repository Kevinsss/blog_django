from django import template  
import re  
register = template.Library()  
  
set_regex = re.compile(r'^\s*set\s+(\w+)\s*=\s*(.*)$')  
def do_set(parser, token):  
    m = re.match(set_regex, token.contents)  
    if m:  
        name, exp = m.group(1), m.group(2)  
        return SetNode(name, exp)  
    else:  
        raise template.TemplateSyntaxError('{% set varname = python_expression %}')  
      
class SetNode(template.Node):  
    def __init__(self, varname, expression):  
        self.varname = varname  
        self.expression = expression  
  
    def render(self, context):  
        context[self.varname] = eval(self.expression, {}, context)  
        return ''  
  
register.tag('set', do_set) 