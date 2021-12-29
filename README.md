# python-semrush-jp

主に以下の2点を修正

#### decode の変更

semurash api から出力される日本語はutf-8で変換されているが、それをunicode_escapeでdecodeしているため

`"ぎっとはぶ"` が

`'ã\x81\x8eã\x81£ã\x81¨ã\x81¯ã\x81¶'`

上記ような文字化けを起こす。

これをutf-8でdecodeするように修正。

- 12/29追記
export_decode ってのがあるから これを１にしてunicode_escape するのが本来の使い方っぽい？

#### requests の競合

メンテナンスされていないために requirements の requests が ==2.8になっており他のライブラリと衝突する。



---

python-semrush
---

Python-Semrush is a wrapper around the `SEMrush API`_ version 3.0.

Thanks to `tomlinton`_ and `storerjeremy`_ for the basis of this package.

- `SEMrush API`: http://www.semrush.com/api-documentation/
- `tomlinton`: https://github.com/tomlinton
- `storerjeremy`: https://github.com/storerjeremy

Installation
============

You can install python-semrush from github.

From github;


    $ pip install git+https://github.com/sishinami/python-semrush-jp.git

Usage
=====

    from python_semrush.semrush import SemrushClient
    client = SemrushClient(key='your_semrush_api_key')
    result = client.domain_ranks(domain='example.com')

Todo
====

- Implement projects API http://www.semrush.com/api-projects/
- Implement accounts API http://www.semrush.com/api-accounts/
- Implement specific errors

License
=======

This software is licensed under the `MIT License`. See the ``LICENSE``
file in the top distribution directory for the full license text.


Author
======

Jeremy Storer <storerjeremy@gmail.com>

@2021 sishinami <git@mail.hazime.net>
