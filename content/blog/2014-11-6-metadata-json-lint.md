title: Linting metadata.json
author: Spencer Krum
twitter_handle: @nibalizer
email: krum.spencer@gmail.com
date: 2014-11-06
summary: Use metadata-json-lint to check your metadata.json file

Summary:
--------

```shell
gem install metadata-json-lint
cd my_puppet_module/
metadata-json-lint metadata.json
```

In the recent past, the metadata.json file has replaced the Modulefile as the place where metadata about a Puppet module is kept. The Modulefile has a simple syntax and the Puppet module tool would generate the metadata.json from it.

Now, we must write our own metadata.json files. This leads to errors because json is a data format and humans suck at writing and reading it.

Tooling to work with this is in [flight](https://github.com/puppetlabs/forge-ruby). Currently geppetto has some tooling in it to do something with metadata.json, but that probably means some weird jar or something and ew. I've contributed the easy part, which is a linting tool to sanity-check your metadata.json. Metadata-json-lint will verify that your metadata.json is valid json and will ensure a number of required fields are there. It will also verify that the two fields that have been deprecated are no longer in your metadata.json file.


Install
-------


Command line:

```shell
gem install metadata-json-lint
```

Gemfile

```ruby
group :development, :test do
  gem 'rake', '10.1.1',         :require => false
#  ...
  gem 'metadata-json-lint',     :require => false
# ...
end
```


Usage
-----


Command line(success):

```shell
metadata-json-lint metadata.json
```

Command line(failure):

```shell
$: metadata-json-lint metadata.json 
Error: Unable to parse json. There is a syntax error somewhere.
$: echo $?
1
```

Command line(failure):

```shell
$: metadata-json-lint metadata.json 
Error: Required field 'summary' not found in metadata.json.
Errors found in metadata.json
$: echo $?
1
```


Rake:

```ruby
desc "Lint metadata.json file"
task :metadata do
  sh "metadata-json-lint metadata.json"
end
```


Adoption
--------


Meatadata-json-lint is currently being used in [puppet-module-puppetboard](https://github.com/puppet-community/puppet-module-puppetboard) and in [garethr's](https://twitter.com/garethr) [puppet-module-skeleton](https://github.com/garethr/puppet-module-skeleton). It has been [proposed](https://review.openstack.org/#/c/127608/) for inclusion in the openstack puppet modules.

