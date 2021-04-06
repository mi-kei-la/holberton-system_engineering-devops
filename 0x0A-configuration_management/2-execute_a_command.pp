# This manifest kills a given process.
exec { 'pkill killmenow':
provider => 'shell',
}
