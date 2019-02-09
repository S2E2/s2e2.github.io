import json
import sys


class AsciinemaFile(object):
    def __init__(self):
        self.header = {}
        self.entries = []

    @staticmethod
    def from_file(f):
        ret = AsciinemaFile()
        state = 0

        with open(f) as fp:
            for line in fp.readlines():
                j = json.loads(line)
                if state == 0:
                    if isinstance(j, dict):
                        ret.header = j
                        state = 1
                    else:
                        raise Exception("Invalid entry: %s" % j)
                elif state == 1:
                    if not isinstance(j, list):
                        raise Exception("Invalid entry: %s" % j)
                    ret.entries.append(j)

        return ret

    def shift(self, new_start_time):
        if not self.entries:
            return

        seq_start = self.entries[0][0]
        for entry in self.entries:
            entry[0] = entry[0] - seq_start + new_start_time

    def get_last_entry(self):
        return self.entries[len(self.entries)-1]

    def dump(self, fp):
        json.dump(self.header, fp)
        fp.write('\n')
        for e in self.entries:
            json.dump(e, fp)
            fp.write('\n')


def concat_files(files):
    ret = AsciinemaFile()
    start_time = 0

    for p in files:
        if not ret.header:
            ret.header = p.header
        elif ret.header['width'] != p.header['width'] or ret.header['height'] != p.header['height']:
            raise Exception("All files must have the same header")

        p.shift(start_time)
        start_time = p.get_last_entry()[0]
        ret.entries += p.entries

    return ret


def speedup(af):
    """
    This function speeds up the first part of the demo, where the image
    is downloaded and decompressed.
    """

    last_ts = 0
    state = 0

    offset = 0
    start = 0

    for j in af.entries:
        if state == 0:
            if 'Downloaded' in j[2]:
                state = 1
        elif state == 1:
            if 'Decompressing' in j[2]:
                state = 2
        elif state == 2:
            if 'new_project' in j[2]:
                state = 3
                print >> sys.stderr, last_ts
                offset = last_ts
                start = j[0]

        if state == 1:
            if j[0] - last_ts > 0.03:
                j[0] = last_ts + 0.03
        elif state == 2:
            if j[0] - last_ts > 1:
                j[0] = last_ts + 1
        elif state == 3:
            j[0] = j[0] - start + offset


        last_ts = j[0]


def get_tui_index(af):
    index = None
    for i, j in enumerate(af.entries):
        if "Starting TUI" in j[2]:
            index = i
            break

    return index


def cut_tui(af):
    """
    This function cuts the TUI part of the demo, it is useful to record
    it separately, because sometimes it is too slow.
    """

    index = get_tui_index(af)
    if index:
        af.entries = af.entries[:index]


def keep_tui(af):
    """
    This function cuts the first part of the demo, right before the TUI.
    """
    index = get_tui_index(af)
    if index:
        af.entries = af.entries[index:]


def main():
    af = AsciinemaFile.from_file('demo.cast')
    speedup(af)
    cut_tui(af)

    af_tui = AsciinemaFile.from_file('demo-tui.cast')
    keep_tui(af_tui)

    concated = concat_files([af, af_tui])
    concated.dump(sys.stdout)


if __name__ == "__main__":
    main()
