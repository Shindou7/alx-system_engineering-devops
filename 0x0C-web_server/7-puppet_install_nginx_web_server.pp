$default_site_loc = '/etc/nginx/sites-available/default'
$default_site = 'https://raw.githubusercontent.com/Shindou7/alx-system_engineering-devops/master/0x0C-web_server/site_available'

# Run apt-get update
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
}

# Install nginx
class { 'nginx':
  manage_repo => true,
  require     => Exec['apt-update'],
}

# Create a new index.html
file { 'Create index.html':
  require => Class['nginx'],
  path    => '/var/www/html/index.html',
  content => 'Hello World!\n',
}

# Create a new error page
file { 'Create 404.html':
  require => Class['nginx'],
  path    => '/var/www/html/404.html',
  content => 'Ceci n\'est pas une page\n',
}

# Replace default site config
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  source  => $default_site,
  require => Class['nginx'],
}

# Start and enable nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File["/etc/nginx/sites-available/default"],
}

# Add a resource for the redirect
nginx::resource::location { 'redirect_me':
  ensure   => present,
  location => '/redirect_me',
  rewrite  => '^/redirect_me$',
  options  => {
    'return' => '301 https://www.example.com/',
  },
  require  => File["/etc/nginx/sites-available/default"],
}
