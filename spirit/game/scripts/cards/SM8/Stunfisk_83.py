from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a7648340-5102-513a-8715-05140df0d4d7',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Stunfisk.Name',
    display_name='Stunfisk',
    searchable_by=['Stunfisk', 'Basic', 'Stunfisk'],
    subtypes=['Basic'],
    collector_number=83,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=618,
    abilities=[
        Attack(
            title='Flail',
            game_text='This attack does 10 damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Thunder Blast',
            game_text='Discard a Lightning Energy from this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
