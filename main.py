# This entrypoint file to be used in development. Start by reading README.md
import password_cracker
from unittest import main

# cracked_password1 = password_cracker.crack_sha1_hash(
#     "fbbe7e952d1050bfb09dfdb71d4c2ff2b3d845d2")
# print(cracked_password1)

# print(password_cracker.crack_sha1_hash("b305921a3723cd5d70a375cd21a61e60aabb84ec")) # sammy123
# print(password_cracker.crack_sha1_hash("c7ab388a5ebefbf4d550652f1eb4d833e5316e3e")) # abacab
# print(password_cracker.crack_sha1_hash("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8")) # password

# print(password_cracker.crack_sha1_hash("53d8b3dc9d39f0184144674e310185e41a87ffd5", True)) # superman
# print(password_cracker.crack_sha1_hash("da5a4e8cf89539e66097acd2f8af128acae2f8ae", True)) # q1w2e3r4t5
# print(password_cracker.crack_sha1_hash("ea3f62d498e3b98557f9f9cd0d905028b3b019e1", True)) # bubbles1

# cracked_password2 = password_cracker.crack_sha1_hash(
#     "dcc466796201f7232b22a03781110a8871fd038c", use_salts=True)
# print(cracked_password2)

# Run unit tests automatically
main(module='test_module', exit=False)
