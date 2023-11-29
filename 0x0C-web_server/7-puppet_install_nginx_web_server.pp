$default_site_loc = '/etc/nginx/sites-available/default'
$site_available = 'https://raw.githubusercontent.com/Shindou7/alx-system_engineering-devops/master/0x0C-web_server/site_available'

# Run apt-get update
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
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
  content => 'Hello World!\n',
}

# Create a new error page
file { 'Create 404.html':
  require => Package['nginx'],
  path    => '/var/www/html/404.html',
  content => 'Ceci n\'est pas une page\n',
}

# Replace site_available config
exec { 'Replace config':
  command => "/usr/bin/curl ${site_available} > ${default_site_loc}",
  require => File["/etc/nginx/sites-available/default"],
}

# Nginx site config
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('path/to/your/template.erb'),
  require => Exec['Replace config'],
}

# Create a symbolic link to sites-enabled
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File["/etc/nginx/sites-available/default"],
}

# Start nginx service
service { 'nginx':
  ensure  => running,
  require => Exec['Replace config'],
}

# Configure the redirect
nginx::resource::location { 'redirect_me':
  ensure       => present,
  location     => '/redirect_me',
  rewrite_rule => '^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent',
}
