from fanstatic import Library, Resource, Group
from js.jquery import jquery
from js.jqueryui import jqueryui

library = Library('jqgrid', 'resources')

jqgrid_js = Resource(library, 'js/jquery.jqGrid.src.js',
                     minified='js/jquery.jqGrid.min.js',
                     depends=[jquery, jqueryui])

jqgrid_i18n_ar = Resource(library, 'js/i18n/grid.locale-ar.js')
jqgrid_i18n_bg1251 = Resource(library, 'js/i18n/grid.locale-bg1251.js')
jqgrid_i18n_bg = Resource(library, 'js/i18n/grid.locale-bg.js')
jqgrid_i18n_cat = Resource(library, 'js/i18n/grid.locale-cat.js')
jqgrid_i18n_cn = Resource(library, 'js/i18n/grid.locale-cn.js')
jqgrid_i18n_cs = Resource(library, 'js/i18n/grid.locale-cs.js')
jqgrid_i18n_da = Resource(library, 'js/i18n/grid.locale-da.js')
jqgrid_i18n_de = Resource(library, 'js/i18n/grid.locale-de.js')
jqgrid_i18n_el = Resource(library, 'js/i18n/grid.locale-el.js')
jqgrid_i18n_en = Resource(library, 'js/i18n/grid.locale-en.js')
jqgrid_i18n_es = Resource(library, 'js/i18n/grid.locale-es.js')
jqgrid_i18n_fa = Resource(library, 'js/i18n/grid.locale-fa.js')
jqgrid_i18n_fi = Resource(library, 'js/i18n/grid.locale-fi.js')
jqgrid_i18n_fr = Resource(library, 'js/i18n/grid.locale-fr.js')
jqgrid_i18n_gl = Resource(library, 'js/i18n/grid.locale-gl.js')
jqgrid_i18n_he = Resource(library, 'js/i18n/grid.locale-he.js')
jqgrid_i18n_hu = Resource(library, 'js/i18n/grid.locale-hu.js')
jqgrid_i18n_is = Resource(library, 'js/i18n/grid.locale-is.js')
jqgrid_i18n_it = Resource(library, 'js/i18n/grid.locale-it.js')
jqgrid_i18n_ja = Resource(library, 'js/i18n/grid.locale-ja.js')
jqgrid_i18n_lt = Resource(library, 'js/i18n/grid.locale-lt.js')
jqgrid_i18n_mne = Resource(library, 'js/i18n/grid.locale-mne.js')
jqgrid_i18n_nl = Resource(library, 'js/i18n/grid.locale-nl.js')
jqgrid_i18n_no = Resource(library, 'js/i18n/grid.locale-no.js')
jqgrid_i18n_pl = Resource(library, 'js/i18n/grid.locale-pl.js')
jqgrid_i18n_pt_br = Resource(library, 'js/i18n/grid.locale-pt-br.js')
jqgrid_i18n_pt = Resource(library, 'js/i18n/grid.locale-pt.js')
jqgrid_i18n_ro = Resource(library, 'js/i18n/grid.locale-ro.js')
jqgrid_i18n_ru = Resource(library, 'js/i18n/grid.locale-ru.js')
jqgrid_i18n_sk = Resource(library, 'js/i18n/grid.locale-sk.js')
jqgrid_i18n_sr = Resource(library, 'js/i18n/grid.locale-sr.js')
jqgrid_i18n_sv = Resource(library, 'js/i18n/grid.locale-sv.js')
jqgrid_i18n_th = Resource(library, 'js/i18n/grid.locale-th.js')
jqgrid_i18n_tr = Resource(library, 'js/i18n/grid.locale-tr.js')
jqgrid_i18n_ua = Resource(library, 'js/i18n/grid.locale-ua.js')

jqgrid_css = Resource(library, 'css/ui.jqgrid.css')

jqgrid = Group([jqgrid_js, jqgrid_css])
