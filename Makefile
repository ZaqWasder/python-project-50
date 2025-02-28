install:
		uv sync

run:
		uv run gendiff

build:
		uv build

package-install:
		uv tool install dist/*.whl

package-uninstall:
		uv tool uninstall hexlet-code

package-reinstall: package-uninstall package-install

lint:
		uv run ruff check gendiff

.PHONY: install gendiff build package-install package-uninstall package-reinstall
