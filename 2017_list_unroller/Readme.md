# Loop Unroller

### Machine Setup
  This setup guide will install the deps of this project in virtualenvs, which will avoid polluting your global python namespace.

  * Install python & shellcheck if you don't have them already
        brew install python shellcheck

  * Install virtualenv globally
        sudo pip install virtualenv

  * Create a virtualenv to bootstrap from and start using it

        mkdir -p $HOME/venv
        virtualenv $HOME/venv/default
        source $HOME/venv/default/bin/activate

  * While inside the virtualenv, install pipenv

        pip install pipenv

  * Use pipenv to fetch the project deps & install them in a project-specific virtualenv
        cd <project>
        pipenv install

### Running Tests & Linter

  This project uses hypothesis generated tests.

       cd <project>
       pipenv shell
       ./dolint
       ./dotest
