# 1-install_a_package.pp

# Ensure that the package 'flask' is installed using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

# Ensure that the package 'werkzeug' is installed using pip3 and specify version 2.1.1
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3'
}
