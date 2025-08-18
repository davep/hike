# Hike ChangeLog

## Unreleased

**Released: WiP**

- Migrated from `rye` to `uv` for management of the development environment.
  ([#123](https://github.com/davep/hike/pull/123))

## v1.1.2

**Released: 2025-08-08**

- Fixed the `help` command in the command line widget not pulling up the
  help dialog. ([#117](https://github.com/davep/hike/pull/117))
- Pin Textual to >=5.3.0 now that `Markdown` stuff seems to have settled
  down again. ([#120](https://github.com/davep/hike/pull/120))

## v1.1.1

**Released: 2025-08-03**

- Pinned Textual to <5.0.0 due to breaking and broken changes to the
  `Markdown` widget.

## v1.1.0

**Released: 2025-07-09**

- By default the loading of a document now sets focus to the document
  viewer. ([#114](https://github.com/davep/hike/pull/114))

## v1.0.0

**Released: 2025-05-02**

- Added the ability to deduplicate the history.
  ([#105](https://github.com/davep/hike/pull/105))

## v0.12.0

**Released: 2025-04-30**

- Added some vi-friendly navigation to the navigation panel.
  ([#102](https://github.com/davep/hike/pull/102))

## v0.11.1

**Released: 2025-04-12**

- Work around
  [textual#5742](https://github.com/Textualize/textual/issues/5742).
  ([#99](https://github.com/davep/hike/pull/99))

## v0.11.0

**Released: 2025-04-06**

- Added an application command for searching history.
  ([#90](https://github.com/davep/hike/pull/90))

## v0.10.0

**Released: 2025-04-03**

- Added `--theme` as a command line switch; which lets the user configure
  the theme via the command line.
  ([#74](https://github.com/davep/hike/pull/74))
- Added `--navigation`/`--no-navigation` as command line switches; which
  lets the user control if he navigation panel is visible on startup.
  ([#75](https://github.com/davep/hike/pull/75))
- Fixed correct document not being shown when a command is given on the
  command line. ([#76](https://github.com/davep/hike/issues/76))
- Added an unattractive but better-than-nothing workaround for [yet another
  Textual `OptionList`
  borkage](https://github.com/Textualize/textual/issues/5701).
  ([#77](https://github.com/davep/hike/issues/77))
- Added some more movement key bindings (relating to going home and end) to
  the markdown document that might be familiar to users of things like `vim`
  and `less`. ([#82](https://github.com/davep/hike/pull/82))

## v0.9.0

**Released: 2025-04-01**

- Changed the alternative binding for jumping to the document to
  <kbd>ctrl</kbd>+<kbd>g</kbd> (<kbd>ctrl</kbd>+<kbd>r</kbd> was already
  used for reloading the document).
  ([#68](https://github.com/davep/hike/pull/68))
- Added support for changing the keyboard bindings of the main application
  commands. ([#69](https://github.com/davep/hike/pull/69))
- Added `--bindings` as a command line switch; which lists all the commands
  ([#69](https://github.com/davep/hike/pull/69))

## v0.8.0

**Released: 2025-03-31**

- Unpinned Textual. ([#50](https://github.com/davep/hike/pull/50))
- Added `local_start_location` to the configuration file.
  ([#59](https://github.com/davep/hike/pull/59))
- Added <kbd>ctrl</kbd>+<kbd>r</kbd> as an alternative binding for jumping
  to the document. ([#60](https://github.com/davep/hike/pull/60))
- Added support for scrolling the markdown up/down half a page.
  ([#62](https://github.com/davep/hike/pull/62))
- Added some movement key bindings to the markdown document that might be
  familiar to users of things like `vim` and `less`.
  ([#63](https://github.com/davep/hike/pull/63))

## v0.7.0

**Released: 2025-03-16**

- Pressing <kbd>Escape</kbd> in the command line input while there is
  existing input now clears the input and resets the location in the command
  history; pressing <kbd>Escape</kbd> while there is no input still exits
  the application. ([#47](https://github.com/davep/hike/pull/47))
- Fixed incompatibilities with older supported versions of Python.
  ([#48](https://github.com/davep/hike/pull/48))

## v0.6.0

**Released: 2025-03-03**

- Added `obsidian` as a command that the command line understands.
  ([#41](https://github.com/davep/hike/pull/41))

## v0.5.0

**Released: 2025-02-25**

- Added an application command for jumping to the markdown document viewer.
  ([#39](https://github.com/davep/hike/pull/39))
- Added `document` as a command that the command line understands.
  ([#39](https://github.com/davep/hike/pull/39))

## v0.4.0

**Released: 2025-02-19**

- Added `changelog` as a command that the command line understands.
  ([#33](https://github.com/davep/hike/pull/33))
- Added `readme` as a command that the command line understands.
  ([#33](https://github.com/davep/hike/pull/33))
- Fixed failing when opening a document-relative local non-markdown file
  from a click. ([#34](https://github.com/davep/hike/pull/34))

## v0.3.0

**Released: 2025-02-18**

- Added the ability to save a copy of the currently-viewed document.
  ([#15](https://github.com/davep/hike/pull/15))
- Made `chdir` a lot less fussy about the path given.
  ([#18](https://github.com/davep/hike/pull/18))
- Added `quit` as a command that the command line understands.
  ([#24](https://github.com/davep/hike/pull/24))
- Added `dir` and `ls` as aliases for `chdir`.
  ([#24](https://github.com/davep/hike/pull/24))
- Added `contents` as a command that the command line understands.
  ([#24](https://github.com/davep/hike/pull/24))
- Added `bookmarks` as a command that the command line understands.
  ([#24](https://github.com/davep/hike/pull/24))
- Added `history` as a command that the command line understands.
  ([#24](https://github.com/davep/hike/pull/24))
- Added `local` as a command that the command line understands.
  ([#24](https://github.com/davep/hike/pull/24))
- Added `help` as a command that the command line understands.
  ([#24](https://github.com/davep/hike/pull/24))
- Changed command line completion so that if history is empty, known
  commands are suggested. ([#29](https://github.com/davep/hike/pull/29))

## v0.2.0

**Released: 2025-02-16**

- The bookmark search command palette now sorts the bookmarks.
  ([#2](https://github.com/davep/hike/pull/2))
- The suggester for the command line now prefers newer history entries over
  older. ([#3](https://github.com/davep/hike/pull/3))
- Added the ability to move the command line to the top of the screen.
  ([#5](https://github.com/davep/hike/pull/5))
- Added the ability to copy the current location to the clipboard.
  ([#9](https://github.com/davep/hike/pull/9))
- Added the ability to copy the currently-viewed Markdown to the clipboard.
  ([#9](https://github.com/davep/hike/pull/9))
- Added the ability to edit a Markdown document if it's in the local
  filesystem. ([#10](https://github.com/davep/hike/pull/10))
- Pinned Textual to v1.0.0 for now as it broke `OptionList`.

## v0.1.0

**Released: 2025-02-14**

- Initial release.

## v0.0.1

**Released: 2025-02-07**

- Initial placeholder package to test that the name is available in PyPI.

[//]: # (ChangeLog.md ends here)
