from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2a158d14-7842-5d94-af59-30dc9fcc05b2',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name',
    display_name='Scyther',
    searchable_by=['Scyther', 'Basic', 'Scyther'],
    subtypes=['Basic'],
    collector_number=36,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=123,
    abilities=[
        Attack(
            title='Afterimage Strike',
            game_text="During your opponent's next turn, if Scyther would be damaged by an attack, flip a coin. If heads, prevent that attack's damage done to Scyther.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
