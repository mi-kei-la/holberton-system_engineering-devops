# This manifest kills a given process.
exec { 'kill_me_now':
command  => 'pkill -f killmenow',
path     => '/usr/local/bin/:/bin/',
provider => 'shell',
}
