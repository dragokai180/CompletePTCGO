from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='63c2a4bb-83d5-567e-96af-ab797c754642',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpix.Name',
    display_name='Alolan Vulpix',
    searchable_by=['Alolan Vulpix', 'Basic', 'AlolanVulpix'],
    subtypes=['Basic'],
    collector_number=30,
    set_code='SM5',
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
            title='Roar',
            game_text='Your opponent switches their Active Pokémon with 1 of their Benched Pokémon.',
            cost={},
            effect=standard_attack,
        ),
        Attack(
            title='Icy Snow',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
