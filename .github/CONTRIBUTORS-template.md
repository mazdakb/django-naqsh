# Contributors

## Django Naqsh Developers

These contributors have commit flags for this repository, and are able to
accept and merge pull requests here.

<table>
  <tr>
    <th>Name</th>
    <th>Github</th>
    <th>Twitter</th>
  </tr>
  {%- for contributor in core_contributors %}
  <tr>
    <td>{{ contributor.name }}</td>
    <td>
      <a href="https://github.com/{{ contributor.github_login }}">{{ contributor.github_login }}</a>
    </td>
    <td>{{ contributor.twitter_username }}</td>
  </tr>
  {%- endfor %}
</table>

## Cookiecutter Django Core Developers

These contributors have commit flags for the original repository, and are able to
accept and merge pull requests there.

<table>
  <tr>
    <th>Name</th>
    <th>Github</th>
    <th>Twitter</th>
  </tr>
  {%- for contributor in core_contributors %}
  <tr>
    <td>{{ contributor.name }}</td>
    <td>
      <a href="https://github.com/{{ contributor.github_login }}">{{ contributor.github_login }}</a>
    </td>
    <td>{{ contributor.twitter_username }}</td>
  </tr>
  {%- endfor %}
</table>

*Audrey is also the creator of Cookiecutter. Audrey and Daniel are on
the Cookiecutter core team.*

## Other Contributors

Listed in alphabetical order.

<table>
  <tr>
    <th>Name</th>
    <th>Github</th>
    <th>Twitter</th>
  </tr>
  {%- for contributor in other_contributors %}
  <tr>
    <td>{{ contributor.name }}</td>
    <td>
      <a href="https://github.com/{{ contributor.github_login }}">{{ contributor.github_login }}</a>
    </td>
    <td>{{ contributor.twitter_username }}</td>
  </tr>
  {%- endfor %}
</table>

### Special Thanks

The following haven't provided code directly, but have provided
guidance and advice.

-   Jannis Leidel
-   Nate Aune
-   Barry Morrison
