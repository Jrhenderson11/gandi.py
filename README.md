# Gandi.py

A python script to automate management of gandi DNS.  


## Usage

The API key must be specified in an environment variable `API_KEY`, this can be found in the gandi website under profile settings.

possible actions:  
 - list  
 - info  
 - clear  
 - add  
  
<pre>  
$ ./gandi.py list                             
Domains:
['example.com']

$<font color="#4E9A06">./gandi.py</font> info -d example.com

Info for <font color="#4E9A06"><b>example.com</b></font>:
+------------------+-------------+-------+-------------------------------------------+
|       Name       | Record Type |  TTL  |                 RR Values                 |
+------------------+-------------+-------+-------------------------------------------+
|        @         |      <font color="#CC0000"><b>A</b></font>      | 10800 |               XXX.XX.XXX.XX               |
|        @         |      <font color="#C4A000"><b>MX</b></font>     | 10800 |          10 spool.mail.gandi.net.         |
|                  |             |       |           50 fb.mail.gandi.net.           |
|        @         |     TXT     | 10800 | &quot;v=spf1 include:_mailcust.gandi.net ?all&quot; |
|  gm1._domainkey  |    <font color="#3465A4"><b>CNAME</b></font>    | 10800 |             gm1.gandimail.net.            |
|  gm2._domainkey  |    <font color="#3465A4"><b>CNAME</b></font>    | 10800 |             gm2.gandimail.net.            |
|  gm3._domainkey  |    <font color="#3465A4"><b>CNAME</b></font>    | 10800 |             gm3.gandimail.net.            |
|     webmail      |    <font color="#3465A4"><b>CNAME</b></font>    | 10800 |             webmail.gandi.net.            |
|       www        |    <font color="#3465A4"><b>CNAME</b></font>    | 10800 |          webredir.vip.gandi.net.          |
|    _imap._tcp    |     SRV     | 10800 |                 0 0 0   .                 |
|   _imaps._tcp    |     SRV     | 10800 |          0 1 993 mail.gandi.net.          |
|    _pop3._tcp    |     SRV     | 10800 |                 0 0 0   .                 |
|   _pop3s._tcp    |     SRV     | 10800 |          10 1 995 mail.gandi.net.         |
| _submission._tcp |     SRV     | 10800 |          0 1 465 mail.gandi.net.          |
+------------------+-------------+-------+-------------------------------------------+
</pre>