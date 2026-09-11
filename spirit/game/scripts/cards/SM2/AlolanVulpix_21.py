from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d74b1f99-b5c4-59a8-9407-a8e3ca830246',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpix.Name',
    display_name='Alolan Vulpix',
    searchable_by=['Alolan Vulpix', 'Basic', 'AlolanVulpix'],
    subtypes=['Basic'],
    collector_number=21,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=37,
    abilities=[
        Attack(
            title='Beacon',
            game_text='Search your deck for up to 2 Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={},
            effect=standard_attack,
        ),
        Attack(
            title='Icy Snow',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
