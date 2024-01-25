# any error message.
# Fix problem of high amount files opened

exec {'Remove hard and soft file limit configs':
  command => 'sed -i "s/holberton/# holberton/g" /etc/security/limits.conf',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
