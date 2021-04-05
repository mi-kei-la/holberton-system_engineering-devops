$host = '35.231.30.18'
$path = '~/.ssh/holberton'
$config = "Host ${host}
IdentityFile ${path}"

file { '4-puppet_ssh_config.pp':
ensure  => 'present',
content => $config,
}

