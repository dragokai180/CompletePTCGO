from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a5350e82-bf27-5c87-9f2e-5d4011070897',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name',
    display_name='Durant',
    searchable_by=['Durant', 'Basic', 'Durant'],
    subtypes=['Basic'],
    collector_number=129,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=632,
    abilities=[
        Attack(
            title='Swarming Rage',
            game_text='This attack does 20 damage for each damage counter on all of your Durant.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Hard Scissors',
            game_text="During your opponent's next turn, this Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
