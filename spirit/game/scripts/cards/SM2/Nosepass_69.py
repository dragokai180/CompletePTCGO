from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3b946ca6-796b-5390-aca6-95a59b6defe7',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name',
    display_name='Nosepass',
    searchable_by=['Nosepass', 'Basic', 'Nosepass'],
    subtypes=['Basic'],
    collector_number=69,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=299,
    abilities=[
        Attack(
            title='Ram',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title='Rising Lunge',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
