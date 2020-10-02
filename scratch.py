import json


def main():
    data = []
    with open('source_file_2.json') as f:
        data = json.load(f)
    managers = []
    watchers = []
    for d in data:
        for m in d['managers']:
            if m not in managers:
                managers.append(m)
        for w in d['watchers']:
            if w not in watchers:
                watchers.append(w)

    md = {}
    wd = {}
    for m in managers:
        md[m] = []
        for d in data:
            if m in d['managers']:
                md[m].append({'name': d['name'], 'priority': d['priority']})

    for w in watchers:
        wd[w] = []
        for d in data:
            if w in d['watchers']:
                wd[w].append({'name': d['name'], 'priority': d['priority']})

    managers_out = {}
    for k, v in md.items():
        row = sorted(v, key=lambda k: k['priority'])
        managers_out[k] = [v['name'] for v in row]

    watchers_out = {}
    for k, v in wd.items():
        row = sorted(v, key=lambda k: k['priority'])
        watchers_out[k] = [v['name'] for v in row]

    with open('managers.json', 'w') as mf:
        json.dump(managers_out, mf, indent=4)

    with open('watchers.json', 'w') as wf:
        json.dump(watchers_out, wf, indent=4)


if __name__ == '__main__':
    main()