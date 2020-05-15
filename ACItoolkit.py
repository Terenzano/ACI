from acitoolkit.acitoolkit import *

# see capabilities
# dir()

url = 'https://sandboxapicdc.cisco.com'
user = 'admin'
pw = 'ciscopsdt'

# create the session object

session = Session(url, user, pw)

# login

session.login()

# get tenants


tenants = Tenant.get(session)
for tenant in tenants:
    print(tenant.name)
    print(tenant.descr)
    print('*' * 30)
    print('')


# create a new tenant

new_tenant = Tenant("Tenant_Name_Here")
# new_tenant.get_url()
# new_tenant.get_json()

# create app profile and epg

anp = AppProfile('Terence_App', new_tenant)
epg = EPG('Terence_Epg', anp)


# create L3 namespace

context = Context('Terence_VRF', new_tenant)
bridge_domain = BridgeDomain('Terence_BD', new_tenant)


# associate the bd with the l3 namespace

bridge_domain.add_context(context)
epg.add_bd(bridge_domain)


# tenant creation is completed

print(new_tenant.get_url())
print(new_tenant.get_json())
response = session.push_to_apic(
    new_tenant.get_url(), data=new_tenant.get_json())
print(response)

tenants = Tenant.get(session)
for tenant in tenants:
    if tenant.name == 'Tenant_Name_Here':
        print(tenant.name)
    else:
        print(tenant.name)
        print(tenant.descr)
        print('*' * 30)
        print('')


# Delete new tenant

new_tenant.mark_as_deleted()
session.push_to_apic(new_tenant.get_url(), new_tenant.get_json())
