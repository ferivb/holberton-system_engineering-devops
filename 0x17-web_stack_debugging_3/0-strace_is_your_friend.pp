#Puppet fix for typo bug
exec { 'correct typo':
    command => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
    path    => '/bin/',
}