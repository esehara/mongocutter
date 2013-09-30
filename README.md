mongocutter
===========

 mongocutter generates test data,
 and check performance for mongodb.

Setting Python File
===================

```py
settings = "example.yaml"

def setup_hello():
    print "Hello, World."
```

And, command `python console.py foobar.py` (after create "example.yaml").

Setting Yaml
============

Connect Server
--------------

```yaml
server:
  address: 127.0.0.1
  port: 27071
  database: foobar
```

Document
----------

```yaml
scheme:
  user:
    user_id:
      type: RandomString
    screen_name:
      type: foobar
```

And Generate!!
----------------

```yaml
setup:
  - model:
     target: user
     generate: 10000
```

