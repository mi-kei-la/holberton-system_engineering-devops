# Install NginX
package {'nginx':
	ensure => installed,
	provider => apt,
	name => 'nginx',
}

# Root file
file { '/var/www/html/index.html':
	ensure => present,
	content => 'Holberton School',
}

# Redirection string
file_line {'redirect_me':
	ensure => present,
	path => '/etc/nginx/sites-available/default',
	after => 'server_name _/;',
	line => 'rewrite ^/redirect_me/ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

# Restart service
service {'nginx':
	restart,
}
