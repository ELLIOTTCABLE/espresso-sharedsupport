def _site_packages():
    import site, sys, os
    paths = []
    prefixes = [sys.prefix]
    if sys.exec_prefix != sys.prefix:
        prefixes.append(sys.exec_prefix)
    for prefix in prefixes:
	if prefix == sys.prefix:
	    paths.append(os.path.join("/Library/Python", sys.version[:3], "site-packages"))
	    paths.append(os.path.join(sys.prefix, "Extras", "lib", "python"))
	else:
	    paths.append(os.path.join(prefix, 'lib', 'python' + sys.version[:3],
		'site-packages'))
    if os.path.join('.framework', '') in os.path.join(sys.prefix, ''):
        home = os.environ.get('HOME')
        if home:
            paths.append(os.path.join(home, 'Library', 'Python',
                sys.version[:3], 'site-packages'))
    for path in paths:
        site.addsitedir(path)
_site_packages()


def _disable_linecache():
    import linecache
    def fake_getline(*args, **kwargs):
        return ''
    linecache.orig_getline = linecache.getline
    linecache.getline = fake_getline
_disable_linecache()


def _run(*scripts):
    global __file__
    import os, sys, site
    sys.frozen = 'macosx_plugin'
    base = os.environ['RESOURCEPATH']
    site.addsitedir(base)
    site.addsitedir(os.path.join(base, 'Python', 'site-packages'))
    for script in scripts:
        path = os.path.join(base, script)
        __file__ = path
        execfile(path, globals(), globals())


_run('TEAforEspresso.py')
