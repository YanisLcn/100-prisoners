SUBDIRS := . 

TEX := *.tex
TEX_AUX_EXT := *.aux *.lof *.log *.lot *.fls *.out *.toc *.fmt *.fot *.cb *.cb2 .*.lb *.fdb_latexmk *.synctex *.synctex *.synctex.gz *.synctex.gz *.pdfsync

.PHONY: format_tex clean

format_tex: $(TEX)
	../tools/format_tex.sh $?

clean_tex_aux:
	rm -rfv $(TEX_AUX_EXT)

clean: clean_tex_aux

