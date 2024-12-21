<a href="https://github.com/ozneroL541/FunnyDH/blob/master/LICENSE.md"><img src="https://img.shields.io/github/license/ozneroL541/FunnyDH?color=2b9348" alt="License"/></a>

# Funny Diffie-Hellman
Funny Diffie-Hellman is an easy way to generate a common key between two entities.
> :warning: **Warning**
These modules are not safe. The algorithm implementation is purposely not secure. Must not be implemented in any program for security reasons.

## Dependences
This program requires **python3** and **pyCryptoDome** to work.

## How to use
Enter the folder.

    cd FunnyDH
Execute the main program (or one of the submodules if you already know which one you are going to use).

    python3 main.py
### Alice 1
To start a key exchange execute the Alice 1 module.
Give the prime number and the public key to Bob and memorize the private key.
### Bob
Start these module after receiving a pair of integers from Alice. You should have received a prime number and the Alice's public key. Insert them as asked. Give Alice the public key and use the human readable common key to communicate.
### Alice 2
Insert the prime number, the memorized private key and the Bob's public key. Use the human readable common key to communicate.

## Author
@ozneroL541 Lorenzo Radice

## License
**Funny Diffie-Hellman** is free software: you can redistribute it and/or modify
it under the terms of the **GNU General Public License** as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

**Funny Diffie-Hellman** is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with **Funny Diffie-Hellman**.  If not, see <http://www.gnu.org/licenses/>.
