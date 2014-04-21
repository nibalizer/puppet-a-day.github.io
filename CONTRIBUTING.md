# Contributing

You're free to contribute an article to this blog. You can write your post in
reStructuredText or Markdown, whichever suits you best.

Keep in mind, submitting a PR to this blog means you accept to license or
re-license your work under the CC Attribution-ShareAlike 4.0 International
license. If you are not the author of the work and the content isn't licensed
under a compatible license or no license is given you need to get written
consent from the author before the work can be reproduced here.

A PR for a new entry or corrections to an existing one must **always** be done
against the ``source`` branch, ``master`` only contains the generated content.

The posts can be found in the ``content/blog`` area. For information about how
to write a post, please see the [Pelican documentation](http://docs.getpelican.com/en/3.3.0/getting_started.html#writing-content-using-pelican).

## Required metadata

We expect every entry to contain the following metadata:

  * ``title``: title of this post;
  * ``date``: date this post was published, use [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601)
    format but omit time;
  * ``author``: your name or Github username, IRC handle, nickname;
  * ``email``: your e-mail, is used to pull an image from Gravatar;
  * ``category``:
    * blog: default category and may therefor be omitted;
    * release: used for release announcements of Puppet-related projects;
    * tutorial: identical in spirit to blog but intended for tutorial-style
      posts;
    * link: link to a post on a different blog;

## Optional metadata

We support a few additional things.

### Tags
The ``tags`` metadata entry, a comma-separated list of keywords relevant to this
article. Think carefully about them as they will end up in the ``<meta>`` of
the article which is important to search engines.

### Summary
The ``summary`` metadata entry may be used to provide a short, 50 words or less
summary of the article. This is used on the index page and for the feeds.

If you do not specify ``summary`` metadata the first 50 words of the article
will be used instead.

### Parts
We use the ``multi_part`` plugin to support posts in multiple instalments.
Simply add a ``parts`` metadata entry with an identical key, like
``FUTURE_PARSER_POSTS`` to every post.

At the top of every article a list will be generated linking to the other
posts in that same instalment.

### Twitter_handle
We generate Facebook OpenGraph and Twitter Cards ``<meta>`` tags. If a
``twitter_handle`` is found for a post it will cause a ``twitter:creator`` tag
to show up in the meta tags of that article.

Please don't forget to include the **@** in your ``twitter_handle``.

## Example article

Try to limit the line length to 80 characters. This is not always possible and
it's not a hard limit but it makes it easier for people on smaller or split-
screen setups to read and review the content.

A blog post will end up looking like this:

```markdown
title: Puppet Future parser - Lesson 1
author: Doge
twitter_handle: @doge
email: such@awesome.wow
date: 2014-04-20
category: tutorial
tags: future parser, puppet 4.x
summary: Introduction to the features in the upcoming future-parser.
parts: FUTURE_PARSER_POSTS

In this first lesson we'll take a look at the new features the future parser
provides. The next installements will dive deeper into a feature and show you
how to use it.

Here's a code sample:

    :::puppet
    package { 'Pelican':
      ensure   => latest,
      provider => 'pip',
    }
```

The equivalent of this post in reStructuredText:

```rst
:title: Puppet Future parser - Lesson 1
:author: Doge
:twitter_handle: @doge
:email: such@awesome.wow
:date: 2014-04-20
:category: tutorial
:tags: future parser, puppet 4
:summary: Introduction to the features in the upcoming future-parser.
:parts: FUTURE_PARSER_POSTS

In this first lesson we'll take a look at the new features the future parser
provides. The next installements will dive deeper into a feature and show you
how to use it.

.. code-block:: puppet

   package { 'Pelican':
     ensure   => latest,
     provider => 'pip',
   }
```
