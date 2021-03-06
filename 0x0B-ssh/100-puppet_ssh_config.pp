# Client SSH configuration file
include stdlib

file_line { 'PasswordAuthentication':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no'
}

file_line { 'IdentityFile':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school'
}
