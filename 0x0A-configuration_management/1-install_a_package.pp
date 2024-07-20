# Installs the flask framework for Python
package {'flask':
    ensure => '2.1.0',
    provider => 'pip3',
}
