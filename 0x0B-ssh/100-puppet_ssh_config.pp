# Client SSH configuration file

file_line { 'PasswordAuthentication':
    ensure => 'present',
    path   => '~/.ssh/ssh_config',
    line   => 'PasswordAuthentication no'
}

file_line { 'IdentityFile':
    ensure => 'present',
    path   => '~/.ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school'
}
