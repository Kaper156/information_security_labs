from RGR.ciphers.cipher import Cipher


class FeistelCipher(Cipher):
    def set_up_parameters(self, params: dict):
        self.block_size = int(params['block_size'])
        self.empty_char = str(params.get('empty_char', ' '))
        self.rounds = int(params['rounds'])
        self.is_unsafe_ok = bool(params.get('is_unsafe_ok', False))

        # For key-gen
        self.A = params['A']
        self.B = params['B']
        self.M = params['M']
        self.init_key = params['key']

    def ciphering(self, text):
        return self.text_transformation(text, True)

    def deciphering(self, ciphered_text):
        res = self.text_transformation(ciphered_text, False)
        return self.strip_empty(res)

    def text_transformation(self, text: str, is_cipher: bool):
        result = ''
        keys = self.key_gen()
        if not is_cipher:
            keys = list(reversed(keys))
        for block in self.text_to_blocks(text):
            left, right = self.split_block(block)
            for i in range(self.rounds):
                swap = self.xor_parts(self.cipher_f(left, keys[i]), right)
                right = left
                left = swap
            result += left + right
        return result

    def key_gen(self):
        last_key = self.init_key
        keys = list()
        for i in range(self.rounds):
            last_key = (last_key * self.A + self.B) % self.M
            keys.append(last_key)
        return keys

    def cipher_f(self, data, key):
        res = ''
        for s in data:
            if self.is_unsafe_ok:
                res += chr(ord(s) + key)
            else:
                bl = ord(s).bit_length()
                mask = 2 ** (bl + 1) - 1
                res += chr(ord(s) ^ (key & mask))
        return res

    def text_to_blocks(self, text: str):
        a = len(text) - self.block_size * (len(text) // self.block_size)
        if a > 0:  # Check text-length and length of all blocks
            # Add whitespaces for last block which less than block-size
            text += self.empty_char * (self.block_size - a)
        blocks = [text[i: i + self.block_size] for i in range(0, len(text), self.block_size)]
        return blocks

    @staticmethod
    def split_block(block):
        half = len(block) // 2
        return block[half:], block[:half]

    @staticmethod
    def xor_parts(left, right):
        res = ''
        for i in range(len(left)):
            l = ord(left[i])
            r = ord(right[i])
            res += chr(l ^ r)
        return res

    def strip_empty(self, text: str):
        while text.endswith(self.empty_char):
            text = text[:-1]
        return text
