from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='69d3848d-e1e6-5534-afe4-69d1d8117bf0',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name',
    display_name='Oricorio',
    searchable_by=['Oricorio', 'Basic', 'Oricorio'],
    subtypes=['Basic'],
    collector_number=46,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=741,
    abilities=[
        Attack(
            title='Feather Dance',
            game_text="During your next turn, this Pokémon's Pom-Pom Punch attack's base damage is 100.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Pom-Pom Punch',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
    ],
)
