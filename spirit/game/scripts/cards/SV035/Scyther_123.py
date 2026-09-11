from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4951eb41-15f5-5f72-9387-496748d235e1',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name',
    display_name='Scyther',
    searchable_by=['Scyther', 'Basic', 'Scyther'],
    subtypes=['Basic'],
    collector_number=123,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=123,
    abilities=[
        Attack(
            title='Helpful Slash',
            game_text='Attach a Basic Grass Energy card from your discard pile to 1 of your Benched Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Slicing Blade',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
