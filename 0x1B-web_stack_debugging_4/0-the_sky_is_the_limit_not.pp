#Puppet fix for low amount of workers
exec { 'increase workers':
    command => 'sed -i "s/15/4096/" /etc/default/nginx; service nginx restart',
    path    => '/bin/:/usr/bin/',
}
