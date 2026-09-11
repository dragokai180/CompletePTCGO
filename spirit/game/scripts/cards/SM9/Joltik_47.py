from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f0da716a-f60c-5519-bce6-840340bd3285',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name',
    display_name='Joltik',
    searchable_by=['Joltik', 'Basic', 'Joltik'],
    subtypes=['Basic'],
    collector_number=47,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=595,
    abilities=[
        Attack(
            title='Leech Life',
            game_text="Heal from this Pokémon the same amount of damage you did to your opponent's Active Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
