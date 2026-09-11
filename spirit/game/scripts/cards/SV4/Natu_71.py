from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e6233763-2b83-53b4-90e0-6ea038b9c2e9',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name',
    display_name='Natu',
    searchable_by=['Natu', 'Basic', 'Natu'],
    subtypes=['Basic'],
    collector_number=71,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=177,
    abilities=[
        Attack(
            title='Triple Strike',
            game_text='Flip 3 coins. This attack does 10 damage for each heads.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
