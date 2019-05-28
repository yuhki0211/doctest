readTemplate("/u01/app/oracle/Middleware/wlserver/common/templates/wls/wls.jar")

cd('/Security/base_domain/User/weblogic')
cmo.setPassword('password123456')

setOption('ServerStartMode', 'prod')

cd('/Servers/AdminServer')
set('ListenAddress','0.0.0.0')
set('ListenPort', 7001)


setOption('OverwriteDomain', 'true')
writeDomain('/home/userv/user_projects/domains/bramslm')

closeTemplate()
exit()
