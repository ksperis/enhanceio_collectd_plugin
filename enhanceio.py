import collectd

clist = []

def enhanceio_config(c):
    if c.values[0] != 'enhanceio':
        return

    for child in c.children:
        if child.key == 'Cache':
            for v in child.values:
                if v not in clist:
                    clist.append(v)

def enhanceio_read(data=None):
    if not len(clist):
        return

    values = collectd.Values(plugin='enhanceio')

    for cache in clist:
        d = {}
        procfile = '/proc/enhanceio/' + cache + '/stats'
        with open(procfile, 'r') as fd:
            d = dict(line.strip().split(None, 1) for line in fd)
            for key in d:
                values.dispatch(plugin_instance=cache, type='gauge', type_instance=key, values=[d[key]])
   
            values.dispatch(plugin_instance=cache, type='disk_ops', type_instance='enhanceio_ssd_rw', values=[d['ssd_reads'], d['ssd_writes']])
            values.dispatch(plugin_instance=cache, type='derive', type_instance='uncached_reads', values=[d['uncached_reads']])
            values.dispatch(plugin_instance=cache, type='derive', type_instance='uncached_writes', values=[d['uncached_writes']])

        fd.close()

collectd.register_read(enhanceio_read)
collectd.register_config(enhanceio_config)

