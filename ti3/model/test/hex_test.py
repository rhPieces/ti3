import unittest

import ti3.model.hex as hex_model

class HexTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        hex = hex_model.Hex({'_id':1, 'type':'Planet', 'set':'Vanilla',
            'entities':[
                {'name':'test_ent1', 'type':'Wormhole'},
                {'name':'test_ent2', 'type':'Planet'}
            ]
        })

        self.assertEqual(1, hex._id)
        self.assertEqual('Planet', hex.type)
        self.assertEqual('Vanilla', hex.set)
        self.assertEqual(2, len(hex.entities))
        self.assertEqual(1, len(hex.planets))
        self.assertEqual('test_ent2', hex.planets[0]['name'])

if __name__ == '__main__':
    unittest.main()
