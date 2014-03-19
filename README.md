enhanceio collectd plugin
=========================

Install
------------

Add enhanceio.py in plugin directory, for exemple in /usr/lib/collectd/plugins

In collectd.conf :

        LoadPlugin python

        <Plugin python>
                ModulePath "/usr/lib/collectd/plugins"
                Import "enhanceio"
                <Module enhanceio>
                        Cache cache1
                        Cache cache2
                </Module>
        </Plugin>


Content
-----------

reads
writes
read_hits
read_hit_pct
write_hits
write_hit_pct
dirty_write_hits
dirty_write_hit_pct
cached_blocks
rd_replace
wr_replace
noroom
cleanings
md_write_dirty
md_write_clean
md_ssd_writes
do_clean
nr_blocks
nr_dirty
nr_sets
clean_index
uncached_reads
uncached_writes
uncached_map_size
uncached_map_uncacheable
disk_reads
disk_writes
ssd_reads
ssd_writes
ssd_readfills
ssd_readfill_unplugs
readdisk
writedisk
readcache
readfill
writecache
readcount
writecount
kb_reads
kb_writes
rdtime_ms
wrtime_ms
