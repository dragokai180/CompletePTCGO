from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8970c1d7-d2f5-5cc7-8f56-511c1cd2d5e3',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name',
    display_name='Lapras',
    searchable_by=['Lapras', 'Basic', 'Lapras'],
    subtypes=['Basic'],
    collector_number=28,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=131,
    abilities=[
        Attack(
            title='Errand-Running',
            game_text='Search your deck for a Trainer card, reveal it, and put it into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Water Splash',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
