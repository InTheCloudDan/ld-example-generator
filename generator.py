import launchdarkly_api
import jinja2

configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'CHANGE_ME'
api_instance = launchdarkly_api.FeatureFlagsApi(
    launchdarkly_api.ApiClient(configuration)
)


flags = api_instance.get_feature_flags('dano-test-project', env='production')
prefix = "ld_"
type_hints = True

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "template.j2"
template = templateEnv.get_template(TEMPLATE_FILE)
flag_template = flags.to_dict()
output = template.render(th = type_hints, flags=flag_template['items'], project='dano-test-project', environment='production', prefix=prefix)  # this is where to put args to the template renderer

with open('output.py', 'w') as f:
    f.write(output)
