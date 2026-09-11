from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8cc27c2e-2be9-558d-bbda-d0bdd0aa2d41',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name',
    display_name='Manaphy',
    searchable_by=['Manaphy', 'Basic', 'Manaphy'],
    subtypes=['Basic'],
    collector_number=3,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=490,
    abilities=[
        Attack(
            title='Deep Sea Swirl',
            game_text='Shuffle your hand into your deck. Then, draw 5 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Wave Splash',
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
