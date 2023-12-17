PC := python3
PY := *.py
EXEC := Main.py
FORMATTER := black

.PHONY: fmt launch

fmt: $(PY)
	$(PC) -m $(FORMATTER) $? 

launch: 
	$(PC) $(EXEC)
