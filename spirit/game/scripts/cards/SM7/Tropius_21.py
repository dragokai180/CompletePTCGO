from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7dde65ee-83b9-5a82-98b0-4107a5b32f8b',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name',
    display_name='Tropius',
    searchable_by=['Tropius', 'Basic', 'Tropius'],
    subtypes=['Basic'],
    collector_number=21,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=357,
    abilities=[
        Attack(
            title='Find a Friend',
            game_text='Search your deck for up to 2 Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Solar Beam',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
