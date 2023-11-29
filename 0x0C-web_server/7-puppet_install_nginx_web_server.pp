$default_site_loc = '/etc/nginx/sites-available/default'
$site_available = 'https://github.com/Shindou7/alx-system_engineering-devops/blob/master/0x0C-web_server/site_available'

# Run apt-get update
exec { 'apt-update':
  command => '/usr/bin/apt-get update'
}

# Install nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-update'],
}

# Create a new index.html
file { 'Create index.html':
  require => Package['nginx'],
  path    => '/var/www/html/index.html',
  content => 'Hello World!\n'
}

# Create a new error page
file { 'Create 404.html':
  require => Package['nginx'],
  path    => '/var/www/html/404.html',
  content => 'Ceci n\'est pas une page\n'
}

# Replace site_available config
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  require => Package['nginx']
}-> exec { 'Replace config':
  command => "/usr/bin/curl ${site_available} > ${default_site_loc}"
}

# Start nginx service
service { 'nginx':
  ensure  => running,
  require => Exec['Replace config'],
}
