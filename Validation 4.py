from schema import Schema, And, Use, Optional, SchemaError

def validateData(conf_schema, conf):
    try:
        conf_schema.validate(conf)
        return True
    except SchemaError: 
        return False
    
conf_schema = Schema({
    'version': And(Use(int)),
    'info': {
        'conf_one':And(Use(float)),
        'conf_two':And(Use(str)),
        'conf_three': And(Use(bool)),
        Optional('optional_conf'):And(Use(str))
        }
    })

conf = {
    'version':500,
    'info': {
        'conf_one':3.14,
        'conf_two':'Ronald',
        'conf_three':False,
        'optional_conf':'Ngwashi'
    }
}
print(check(conf_schema, conf))
                     
