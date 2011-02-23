#!/usr/bin/env python
# coding: utf-8

# tested with some 2500 emails:
# http://www.thefuture.dinfos.net/hugeemaillist.html

def emails_stat(raw_emails, limit=10):
    ''' Top `limit` domains of emails given in `raw_emails` '''
    emails = {}
    domains = (m.split('@')[-1].lower()
               for m in raw_emails if '@' in m)
    for d in domains:
        emails[d] = emails.get(d, 0) + 1
    stat = emails.items()
    stat.sort(key=lambda e: e[1], reverse=True)
    return stat[:limit]

def email_gen():
    while True:
        try:
            yield raw_input()
        except EOFError:
            raise StopIteration

def format_stat(stat):
    out = []
    for domain, count in stat:
        out.append('%s %s' % (domain, count))
    return '\n'.join(out)

if __name__ == '__main__':
    print format_stat(emails_stat(email_gen()))
else:
    print __name__
