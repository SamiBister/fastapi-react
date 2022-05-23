pyenv install --list | grep " 3\.[9]"
pyenv install -v 3.9.12
pyenv versions
pyenv which python
pyenv global 3.9.12

CFLAGS="-I$(brew --prefix openssl)/include -I$(brew --prefix bzip2)/include -I$(brew --prefix readline)/include -I$(xcrun --show-sdk-path)/usr/include" LDFLAGS="-L$(brew --prefix openssl)/lib -L$(brew --prefix readline)/lib -L$(brew --prefix zlib)/lib -L$(brew --prefix bzip2)/lib" pyenv install --patch 3.9.12 < <(curl -sSL https://github.com/python/cpython/commit/8ea6353.patch\?full_index\=1)


For compilers to find zlib you may need to set:
  export LDFLAGS="-L/Users/samibister/src/homebrew/homebrew/opt/zlib/lib"
  export CPPFLAGS="-I/Users/samibister/src/homebrew/homebrew/opt/zlib/include"

For pkg-config to find zlib you may need to set:
  export PKG_CONFIG_PATH="/Users/samibister/src/homebrew/homebrew/opt/zlib/lib/pkgconfig"

==> bzip2
bzip2 is keg-only, which means it was not symlinked into /Users/samibister/src/homebrew/homebrew,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

If you need to have bzip2 first in your PATH, run:
  echo 'export PATH="/Users/samibister/src/homebrew/homebrew/opt/bzip2/bin:$PATH"' >> ~/.zshrc

For compilers to find bzip2 you may need to set:
  export LDFLAGS="-L/Users/samibister/src/homebrew/homebrew/opt/bzip2/lib"
  export CPPFLAGS="-I/Users/samibister/src/homebrew/homebrew/opt/bzip2/include"


git remote add origin git@github-sbi:SamiBister/fastapi-react.git
