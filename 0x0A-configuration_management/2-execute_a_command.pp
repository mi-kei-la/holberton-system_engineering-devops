exec { 'kill_me_now':
command  => 'if pgrep -f killmenow; then pkill -f killmenow; fi',
path     => '/usr/local/bin/:/bin/',
provider => 'shell',
}
