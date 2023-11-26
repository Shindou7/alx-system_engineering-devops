# Modify the configuration file ssh_config
# Changes SSH config file
include stdlib

file_line { 'Specify IdentityFile':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^#?\s*IdentityFile.*',
}

file_line { 'Remove other IdentityFile entries':
  path  => '/etc/ssh/ssh_config',
  line  => '# IdentityFile',
  match => '^IdentityFile.*',
  ensure => absent,
}
