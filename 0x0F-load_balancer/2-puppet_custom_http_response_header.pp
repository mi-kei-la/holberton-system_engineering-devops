# Ensure nginx is installed
  package {'nginx':
  ensure   => 'installed',
  provider => 'apt',
  name     => 'nginx',
}

# Add custom response header to server
file_line { 'header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'as directory, then fall back to displaying a 404.',
  line   => 'add_header X-Served-By $hostname;'
}

service {'nginx':
  ensure => 'running',
}
