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
		if key in ['read_hit_pct','write_hit_pct','dirty_write_hit_pct']:
                    values.dispatch(plugin_instance=cache, type='percent', type_instance=key, values=[d[key]])
	        elif key in ['nr_blocks', 'nr_dirty', 'nr_sets']:
                    values.dispatch(plugin_instance=cache, type='gauge', type_instance=key, values=[d[key]])
                else:
                    values.dispatch(plugin_instance=cache, type='derive', type_instance=key, values=[d[key]])
   
            values.dispatch(plugin_instance=cache, type='disk_ops', type_instance='enhanceio_ssd_rw', values=[d['ssd_reads'], d['ssd_writes']])
            values.dispatch(plugin_instance=cache, type='df', type_instance='df_cache', values=[d['cached_blocks'],str(int(d['nr_blocks'])-int(d['cached_blocks']))])

        fd.close()

collectd.register_read(enhanceio_read)
collectd.register_config(enhanceio_config)

