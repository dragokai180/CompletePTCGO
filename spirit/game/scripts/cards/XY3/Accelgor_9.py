from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='49259a34-51ed-5a8b-b128-ec463f40b194',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Accelgor.Name',
    display_name='Accelgor',
    searchable_by=['Accelgor', 'Stage 1', 'Accelgor'],
    subtypes=['Stage 1'],
    collector_number=9,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name',
    family_id=616,
    abilities=[
        Attack(
            title='Raid',
            game_text='If this Pokémon evolved from Shelmet during this turn, this attack does 40 more damage.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Afterimage Strike',
            game_text="If any damage is done to this Pokémon by attacks during your opponent's next turn, flip a coin. If heads, prevent that damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
