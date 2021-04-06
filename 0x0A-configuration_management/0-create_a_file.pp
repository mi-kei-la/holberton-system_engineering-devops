# This script creates a file with a puppet manifest.
file { '/tmp/holberton':
    ensure  => present,
    path    => '/tmp/holberton',
    content => 'I love Puppet',
    group   => 'www-data',
    owner   => 'www-data',
    mode    => '0744',
}
