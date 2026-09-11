from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='616b4e6b-273f-517e-949b-f23995bedbb2',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Plusle.Name',
    display_name='Plusle',
    searchable_by=['Plusle', 'Basic', 'Plusle'],
    subtypes=['Basic'],
    collector_number=60,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=311,
    abilities=[
        Attack(
            title='Plus Damage',
            game_text="This attack does 10 more damage for each damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
